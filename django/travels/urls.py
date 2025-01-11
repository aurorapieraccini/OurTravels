from django.urls import path

from . import views

urlpatterns = [
    # ex: /polls/
    # path("", views.index, name="index"),
    # ex: /polls/5/
    path("ourtravels", views.ourtravels, name="ourtravels"),
    # ex: /polls/5/results/
    path("countries/", views.countries, name="countries"),
    # ex: /polls/5/vote/
    # path("<int:question_id>/vote/", views.vote, name="vote"),
]