from django.contrib import admin
from .models import Plan, Subscription, ExchangeRateLog

@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'duration_days')
    search_fields = ('name',)

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('user', 'plan', 'start_date', 'end_date', 'status')
    list_filter = ('status', 'plan')
    search_fields = ('user__username',)
    autocomplete_fields = ('user', 'plan')

@admin.register(ExchangeRateLog)
class ExchangeRateLogAdmin(admin.ModelAdmin):
    list_display = ('base_currency', 'target_currency', 'rate', 'fetched_at')
    list_filter = ('base_currency', 'target_currency')
    ordering = ('-fetched_at',)