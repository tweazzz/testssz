from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PrepodViewSet, JobHistoryViewSet


router = DefaultRouter()
router.register(r'prepod', PrepodViewSet)
router.register(r'jobhistory', JobHistoryViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]