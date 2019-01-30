# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import datetime

class Team(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name


class Game(models.Model):
    favorite = models.ForeignKey(Team, related_name="favorite_team", on_delete=models.CASCADE)
    dog = models.ForeignKey(Team, related_name="underdog_team", on_delete=models.CASCADE)
    line = models.FloatField(default=0)
    ou = models.FloatField(default=0)
    winner = models.ForeignKey(Team, related_name="winner", on_delete=models.CASCADE, blank=True) #Always starts as nothing until we come back and edit
    def __str__(self):
        return "{fav} - {dog}".format(fav=self.favorite, dog=self.dog)


class Week(models.Model):
    date = models.DateField()
    games = models.ManyToManyField(Game)
    cutoffTime = models.DateTimeField()
    def __str__(self):
        return str(self.date)


class Pick(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    selection = models.ForeignKey(Team, on_delete=models.CASCADE)
    correct = models.IntegerField(default=0)
    def __str__(self):
        return str(self.selection)


class PlayerSubmission(models.Model):
    email = models.EmailField()
    week = models.ForeignKey(Week, on_delete=models.CASCADE)
    picks = models.ManyToManyField(Pick)
    winners = models.IntegerField(default=0)
    def __str__(self):
        return "{date} - {email}".format(date=self.week, email=self.email)


class Result(models.Model):
    weekof = models.DateField()
    email = models.EmailField()
    correct = models.IntegerField(default=0)
    def __str__(self):
        return "{week} - {email}: {correct}".format(week=self.weekof, email=self.email, correct=self.correct)