from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    # ex: /polls/
    # path("", views.index, name="index"),
    # ex: /polls/5/
    path("ourtravels", views.ourtravels, name="ourtravels"),
    # ex: /polls/5/results/
    path("countries/", views.countries, name="countries"),

    path('login/', views.custom_login, name='custom_login'),
    path('register/', views.register, name='register'),  # Optional for registration
    #path('admin/', admin.site.urls),  # Django admin URL
    # ex: /polls/5/vote/
    # path("<int:question_id>/vote/", views.vote, name="vote"),
]