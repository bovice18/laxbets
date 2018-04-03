from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^make-picks$', views.makePicks, name='make-picks'),
    url(r'^results$', views.results, name='results'),
    url(r'^submitPicks/week-(?P<week_id>[0-9]+)$', views.submitPicks, name='submitPicks'),
]