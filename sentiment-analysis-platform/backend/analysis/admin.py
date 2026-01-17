from django.contrib import admin
from .models import SentimentRecord

@admin.register(SentimentRecord)
class SentimentAdmin(admin.ModelAdmin):
    list_display = ("sentiment", "polarity", "created_at")
