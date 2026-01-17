from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from textblob import TextBlob
from .models import SentimentRecord
from .serializers import SentimentSerializer

class SentimentAPIView(APIView):

    def post(self, request):
        text = request.data.get("text")

        if not text:
            return Response({"error": "Text is required"}, status=status.HTTP_400_BAD_REQUEST)

        blob = TextBlob(text)
        polarity = blob.sentiment.polarity

        if polarity > 0:
            sentiment = "Positive"
        elif polarity < 0:
            sentiment = "Negative"
        else:
            sentiment = "Neutral"

        record = SentimentRecord.objects.create(
            text=text,
            polarity=polarity,
            sentiment=sentiment
        )

        serializer = SentimentSerializer(record)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SentimentHistoryAPIView(APIView):

    def get(self, request):
        records = SentimentRecord.objects.all().order_by("-created_at")
        serializer = SentimentSerializer(records, many=True)
        return Response(serializer.data)
