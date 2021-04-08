from rest_framework.viewsets import ModelViewSet

from .models import Poll, Question
from .serializers import PollModelSerializer, QuestionModelSerializer
from .permissions import PollPermission, QuestionPermission


class PollModelViewSet(ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollModelSerializer
    permission_classes = (PollPermission, )


class QuestionModelViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionModelSerializer
    permission_classes = (QuestionPermission, )