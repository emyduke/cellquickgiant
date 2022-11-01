from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import resolve

import requests, json, jwt, hashlib, base64

def contact_us(request):
    return render(request, "homepage/contact.html", {})
