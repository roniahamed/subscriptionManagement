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
