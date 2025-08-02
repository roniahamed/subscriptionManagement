import requests
from django.conf import settings
from django.db import transaction
from django.shortcuts import render
from django.views import View
from rest_framework import generics, views, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Plan, Subscription, ExchangeRateLog
from .serializers import CancelSubscriptionSerializer, SubscribeSerializer, SubscriptionSerializer

class SubscribeView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = SubscribeSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        plan_id = serializer.validated_data['plan_id']
        user = request.user

        try:
            plan = Plan.objects.get(pk=plan_id)

            with transaction.atomic():
                if Subscription.objects.filter(user=user, status='active').exists():
                    return Response(
                        {'error':'User already has an active Subscription'}, status = status.HTTP_400_BAD_REQUEST
                    )
                subscription = Subscription.objects.create(user=user, plan = plan)
            response_serializer = SubscribeSerializer(subscription)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        except Plan.DoesNotExist:
            return Response({'error':'Plan not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error':str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


