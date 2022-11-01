from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import resolve


def sales(request):
    return render(request, "homepage/sales.html", {})
