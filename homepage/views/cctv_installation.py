from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import resolve

import requests, json, jwt, hashlib, base64

def cctv_installations(request):
    return render(request, "homepage/cctv-installations.html", {})
