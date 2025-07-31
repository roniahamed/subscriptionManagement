from rest_framework import serializers
from .models import Plan, Subscription, ExchangeRateLog
from django.contrib.auth.models import User

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'
