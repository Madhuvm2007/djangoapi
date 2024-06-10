from django.shortcuts import render
from rest_framework import viewsets
from .models import course
from .serializers import courseserializers

class courseView(viewsets.ModelViewSet):
	queryset=course.objects.all()
	serializer_class=courseserializers