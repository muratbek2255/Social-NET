from asgiref.sync import sync_to_async
from django.contrib.auth import get_user_model
from django.shortcuts import render, reverse, get_object_or_404
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from .models import Room, Message

User = get_user_model()


def test(request):
    return render(request, 'test.html')
