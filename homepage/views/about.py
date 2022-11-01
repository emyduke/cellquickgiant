from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import resolve


def about(request):
    return render(request, "homepage/about.html", {})
    


def tnc(request):
    return render(request, "homepage/tnc.html", {})


def privacy_policy(request):
    return render(request, "homepage/privacy-policy.html", {})
    