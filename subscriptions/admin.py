from django.contrib import admin
from .models import Plan, Subscription, ExchangeRateLog

@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'duration_days')
    search_fields = ('name',)