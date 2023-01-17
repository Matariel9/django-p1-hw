from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import DetailView
from django.http import HttpResponse, JsonResponse
import json
import pandas as pd
import os
from .models import ad, category
# Create your views here.

@method_decorator(csrf_exempt, name = "dispatch")
class AppView(View):
    def get(self, request):
        return JsonResponse({"status":"ok"})

@method_decorator(csrf_exempt, name = "dispatch")
class CategoryView(View):
    def get(self, request):
        categories = category.objects.all()
        return JsonResponse([{"id":i.id,"name":i.category}for i in categories], safe = False)

    def post(self, request):
        category_data = json.loads(request.body)
        _category = category()
        _category.category = category_data["name"]
        _category.save()
        return JsonResponse({"id": _category.id, "name": _category.category})

@method_decorator(csrf_exempt, name = "dispatch")
class CategoryDetailView(DetailView):
    model = category

    def get(self, request, *args, **kwargs):
        cat = self.get_object()
        return JsonResponse({"id":cat.id, "name":cat.category})

class AdView(View):
    def get(self, request):
        ads = ad.objects.all()
        return JsonResponse([{"id":i.id,"name":i.name,"author":i.author,"price":i.price,"description":i.description,"address":i.address,"is_published":i.is_published}for i in ads], safe = False)
    def post(self, request):
        ad_data = json.loads(request.body)
        _ad = ad()
        _ad.name = ad_data["name"]
        _ad.author = ad_data["author"]
        _ad.price = ad_data["price"]
        _ad.description = ad_data["description"]
        _ad.address = ad_data["address"]
        _ad.is_published = ad_data["is_published"]
        _ad.save()
        return JsonResponse({"id":_ad.id,"name":_ad.name,"author":_ad.author,"price":_ad.price,"description":_ad.description,"address":_ad.address,"is_published":_ad.is_published})

class AdDetailView(DetailView):
    model = ad

    def get(self, request, *args, **kwargs):
        _ad = self.get_object()
        return JsonResponse({"id":_ad.id,"name":_ad.name,"author":_ad.author,"price":_ad.price,"description":_ad.description,"address":_ad.address,"is_published":_ad.is_published})