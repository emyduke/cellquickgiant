from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import resolve

import requests, json, jwt, hashlib, base64

def sales(request):
    return render(request, "homepage/sales.html", {})
