# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import datetime
import pytz
from django.template import loader
from .models import Week, Game, Pick, PlayerSubmission, Result, Team


def makePicks(request):
    latest_week = Week.objects.order_by('-date').first()
    now = datetime.datetime.now(tz=pytz.timezone("America/New_York"))
    if latest_week:
        displayPicks = now <= latest_week.cutoffTime
    else:
        displayPicks = False
    context = {
        'games': latest_week.games.all(),
        'date': latest_week.date,
        'week_id': latest_week.id,
        'cutoffTime': latest_week.cutoffTime,
        'display': displayPicks
    }
    return render(request, 'laxbets/pick.html', context)

def index(request):
    return render(request, 'laxbets/index.html')


def submitPicks(request, week_id):
    week = Week.objects.get(pk=week_id)
    weeks_submissions = PlayerSubmission.objects.filter(week=week)

    emails = [x.email for x in weeks_submissions.all()]
    if request.POST.get("email") in emails:
        print "DUPE!"
        return render(request, 'laxbets/picksMade.html', {'emailDupe': True,
                                                          'date': week.date,
                                                          'email': request.POST.get("email")})

    output = ""
    for game in week.games.all():
        output += "{}: Choice = {} <br>".format(game, request.POST.get(str(game.id)))

    picks = []
    for game in week.games.all():
        teamPicked = Team.objects.get(pk=request.POST.get(str(game.id)))
        p = Pick(game=game, selection=teamPicked)
        p.save()
        picks.append(p)

    submission = PlayerSubmission.objects.create(email=request.POST.get("email"), week=week)
    for p in picks:
        submission.picks.add(p)
    print picks
    context = {
        "games": week.games.all(),
        "picks": submission.picks.all(),
        "email": request.POST.get("email"),
        "date": week.date
    }

    return render(request, 'laxbets/picksMade.html', context)
    pass


def results(request):
    latest_week = Week.objects.order_by('-date')
    latest_week = latest_week[0]
    weeks_submissions = PlayerSubmission.objects.filter(week=latest_week)
    now = datetime.datetime.now(tz=pytz.timezone("America/New_York"))
    displayPicks = now >= latest_week.cutoffTime

    for submission in weeks_submissions.all():
        updateWins(submission)

    context = {
        'submissions': weeks_submissions.all(),
        'games': latest_week.games.all(),
        'date': latest_week.date,
        'cutoffTime': latest_week.cutoffTime,
        'display': displayPicks
    }
    return render(request, 'laxbets/results.html', context)

def updateWins(submission):
    wins = 0
    for p in submission.picks.all():
        try:
            if p.selection == p.game.winner:
                wins += 1
                p.correct = 1
                p.save()
            elif p.game.winner.name != "PLACEHOLDER":
                p.correct = 2
                p.save()
            else:
                p.correct = 0
                p.save()
        except ValueError:
            continue
    submission.winners = wins
    submission.save()
