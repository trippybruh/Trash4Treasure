from django.template import loader
from django.urls import reverse
from django.http import *
from django.views.decorators.csrf import csrf_exempt, requires_csrf_token, csrf_protect
from django.db.models import Q
from django.contrib.auth import *