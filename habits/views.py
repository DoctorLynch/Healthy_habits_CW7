from rest_framework import generics

from habits.models import Habit
from habits.paginators import ListPagination
from habits.serializers import HabitSerializers


class HabitCreateAPIView(generics.CreateAPIView):
    """Создание привычки"""
    serializer_class = HabitSerializers


class HabitListAPIView(generics.ListAPIView):
    """Просмотр всех привычек, но не более 5 на странице."""
    serializer_class = HabitSerializers
    pagination_class = ListPagination

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class HabitPublicListAPIView(generics.ListAPIView):
    """Просмотр всех привычек."""
    serializer_class = HabitSerializers

    def get_queryset(self):
        return Habit.objects.filter(is_public=True)


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    """Просмотр привычки по ID"""
    serializer_class = HabitSerializers

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class HabitUpdateAPIView(generics.UpdateAPIView):
    """Редактирование привычки"""
    serializer_class = HabitSerializers

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


class HabitDestroyAPIView(generics.DestroyAPIView):
    """Удаление привычки"""

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)