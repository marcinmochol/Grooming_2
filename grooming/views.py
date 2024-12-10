from django.shortcuts import render
from grooming.models import DogReservation, DogService
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.views import View


class Base(View):
    def get(self, request):
        return render(request, 'base.html')
    
