from rest_framework import serializers
from .models import Poll, Question


class PollModelSerializer(serializers.ModelSerializer):
   class Meta:
       model = Poll
       fields = '__all__'


class QuestionModelSerializer(serializers.ModelSerializer):
   class Meta:
       model = Question
       fields = '__all__'