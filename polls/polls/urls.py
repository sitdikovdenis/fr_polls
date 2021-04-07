from django.contrib import admin
from django.urls import path, include
from polls_app.views import PollModelViewSet, QuestionModelViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('polls', PollModelViewSet)
router.register('questions', QuestionModelViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
]
