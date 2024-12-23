from django.shortcuts import render, redirect
from .chat import get_response
from django.http import JsonResponse
from django.views import View
import json

def home(request):
    return render(request, "home.html")

def predict(request):
    if request.method == "POST":
        data = json.loads(request.body)
        message = data.get("message")
        response = get_response(message)
        return JsonResponse({"answer": response})