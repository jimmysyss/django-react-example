from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework import views, serializers, status, viewsets
from rest_framework.response import Response

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


@api_view()
def poll_get(request):
    return Response({
        "message": "HELLO WORLD"
    })


class PollViewSet(viewsets.ViewSet):
    def list(self, request):
        return Response([1, 2, 3, 4, 5])

    def retrieve(self, request, pk=None):
        return Response({"aaa": "bbb"})

    def create(self, request):
        return Response({"aaa": "cccc"})
