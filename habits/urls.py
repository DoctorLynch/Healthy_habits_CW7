from django.urls import path

from habits.apps import HabitsConfig
from habits.views import HabitPublicListAPIView, HabitListAPIView, HabitCreateAPIView, HabitRetrieveAPIView, \
    HabitUpdateAPIView, HabitDestroyAPIView

app_name = HabitsConfig.name

urlpatterns = [
    path('', HabitPublicListAPIView.as_view(), name='habits_is_public'),
    path('habits/', HabitListAPIView.as_view(), name='habits'),
    path('create/', HabitCreateAPIView.as_view(), name='habit_create'),
    path('<int:pk>/', HabitRetrieveAPIView.as_view(), name='habit'),
    path('update/<int:pk>/', HabitUpdateAPIView.as_view(),
         name='habit_update'),
    path('delete/<int:pk>/', HabitDestroyAPIView.as_view(),
         name='habit_delete'),
]