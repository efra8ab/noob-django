from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('results/', views.results, name='results'),
    path('<int:question_id>/', views.detail, name='details'),
    path('<int:question_id>/vote', views.vote , name="vote")
]
