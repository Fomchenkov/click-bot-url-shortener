from django.urls import path

from . import views

urlpatterns = [
    path('', views.indexView, name='indexView'),
    path('<str:url_token>', views.redirectView, name='redirectView'),
    path('stat/<str:url_token>', views.statView, name='statView'),
]
