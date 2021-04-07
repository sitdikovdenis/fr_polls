from rest_framework.viewsets import ModelViewSet

from .models import Poll, Question
from .serializers import PollModelSerializer, QuestionModelSerializer


class PollModelViewSet(ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollModelSerializer


class QuestionModelViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionModelSerializer
