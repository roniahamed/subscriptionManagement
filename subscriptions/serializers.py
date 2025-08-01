from rest_framework import serializers
from .models import Plan, Subscription, ExchangeRateLog
from django.contrib.auth.models import User

class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class SubscriptionSerializer(serializers.ModelSerializer):
    plan = PlanSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Subscription
        fields = ('id', 'user', 'plan', 'start_date', 'end_date', 'status')

class SubscribeSerializer(serializers.ModelSerializer):
    plan_id = serializers.IntegerField()

    def validate_plan_id(self, value):
        if not Plan.objects.filter(pk=value).exists():
            raise serializers.ValidationError('Plan with this ID does not exist.')
        return value
