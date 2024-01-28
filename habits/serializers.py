from rest_framework import serializers

from habits.models import Habit
from habits.validators import RelatedAndAwardValidator, HabitTimeCompleteValidator, \
    HabitRelatedHabitIsPleasantValidator, HabitPleasantValidator, HabitFrequencyValidator


class HabitSerializers(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [
            RelatedAndAwardValidator(),
            HabitTimeCompleteValidator(),
            HabitRelatedHabitIsPleasantValidator(),
            HabitPleasantValidator(),
            HabitFrequencyValidator(),
        ]
