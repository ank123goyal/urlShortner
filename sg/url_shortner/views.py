# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.http import JsonResponse
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from models import URLMapping

# Import custom libs
from url_shortner_service import urlShortnerService

# Create your views here.



HOST_DOMAIN = "localhost:8000/"

@csrf_exempt
def create_short_url(request):

	original_url =  request.body

	# Call UrlShortnerService for generatering url
	short_url_key = urlShortnerService.get_short_url(original_url)

	return JsonResponse({"url" : HOST_DOMAIN + short_url_key})


def get_original_url(request):
	short_url =  request.GET.get('short_url', None)

	short_url_key = short_url.split("/")[1].strip()
	original_url = urlShortnerService.get_original_url(short_url_key)

	return JsonResponse({"url" : original_url})


def handle_redirect(request):
	short_url_key = request.META['PATH_INFO'].strip("/")
	redirect_url = urlShortnerService.get_original_url(short_url_key)

  	return redirect(redirect_url)