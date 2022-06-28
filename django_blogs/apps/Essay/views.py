import json

import django.db.utils
from django.shortcuts import render
from django.views import View
from django import http

from Essay.models import ClassifyModel, LabelModel

from django_blogs.data.EssayCode import *

