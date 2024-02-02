from django.urls import path
from . import views
from .views import match_partners

urlpatterns = [
    path('',views.index, name="index"),
    path('match_partners/', match_partners, name='match_partners'),
]