import datetime

from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Poll, Question
from .serializers import PollModelSerializer, QuestionModelSerializer
from .permissions import PollPermission, QuestionPermission


class PollModelViewSet(ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollModelSerializer
    permission_classes = (PollPermission, )

    def list(self, request, *args, **kwargs):
        if request.user.is_staff:
            queryset = self.filter_queryset(self.get_queryset())
        else:
            queryset = Poll.objects.filter(end_date__gte=datetime.date.today())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class QuestionModelViewSet(ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionModelSerializer
    permission_classes = (QuestionPermission, )