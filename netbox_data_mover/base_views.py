from netbox.views import generic
from django.urls import reverse
from utilities.views import ViewTab
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from . import tables 
import re

class BaseChangeLogView(generic.ObjectChangeLogView):
    base_template = 'netbox_servicemgmt/default-detail.html'
    
class BaseObjectView(generic.ObjectView):
    template_name = 'netbox_servicemgmt/default-detail.html'
    