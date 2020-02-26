from django.urls import path
from . import views

urlpatterns = [
    path('reg', views.regUser, name='reg'),
    path('login', views.logUser, name='login'),
]