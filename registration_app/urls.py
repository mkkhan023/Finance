from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('login/', views.login, name='login'),
    path('webpg/',views.webpg, name='webpg'),
    path('forms/',views.formView, name='form')
]