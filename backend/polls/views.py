from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework import views, serializers, status, viewsets
from rest_framework.response import Response

from .models import Poll

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


@api_view()
def poll_get(request):
    return Response({
        "message": "HELLO WORLD"
    })


class PollSerializer(serializers.Serializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()


class PollViewSet(viewsets.ViewSet):
    def list(self, request):
        polls = Poll.objects.all()
        serializer = PollSerializer(polls, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        polls = Poll.objects.all().filter(first_name="pk")
        serializer = PollSerializer(polls)
        serializer.is_valid(raise_exception=True)
        return Response({"aaa": "bbb"})

    def create(self, request):
        return Response({"aaa": "cccc"})
