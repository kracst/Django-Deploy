from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json

from .models import *

class HomeView(ListView):
    context_object_name = 'project_list'
    model = Project
    template_name = "azure_content/home.html"

class AboutView(TemplateView):
    template_name = "azure_content/about.html"

class ProjectCreateView(CreateView):
    model = Project
    fields = ['name', 'description']
    template_name = "azure_content/create.html"
    success_url ="/"

class ProjectEditView(UpdateView):
    model = Project
    fields = ['name','description']
    template_name = "azure_content/create.html"
    success_url ="/"

class ProjectDeleteView(DeleteView):
    model = Project
    template_name = "azure_content/delete.html"
    fields = ['name']
    success_url ="/"

@api_view(["POST"])
def receive_sensor_data(request):
    try:
        temperature = request.data.get("temperature")
        humidity = request.data.get("humidity")

        if temperature is not None and humidity is not None:
            SensorData.objects.create(temperature=temperature, humidity=humidity)
            return Response({"message": "Data saved successfully"}, status=201)

        return Response({"error": "Invalid data"}, status=400)

    except Exception as e:
        return Response({"error": str(e)}, status=500)