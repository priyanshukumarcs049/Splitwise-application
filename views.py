from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context 
from django.views.generic.base import TemplateView 
from SPLITWISE.models import ACTIVITY, PEOPLE, CALCULATION
from django.core import serializers
import os, re, math
import json
from django import forms

def index(request):
    return HttpResponse("<h1> WELCOME TO SPLITWISE APPLICATION")


def Total_amount_spend(total_amount_spend_by_one_person, no_of_people_in_group):
    return int(total_amount_spend_by_one_person / no_of_people_in_group)

    