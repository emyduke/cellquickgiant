from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import resolve

def index(request):
    return render(request, "homepage/index.html", {})
