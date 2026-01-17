from django.urls import path
from .views import SentimentAPIView, SentimentHistoryAPIView

urlpatterns = [
    path("analyze/", SentimentAPIView.as_view()),
    path("history/", SentimentHistoryAPIView.as_view()),
]
