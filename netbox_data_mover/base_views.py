from netbox.views import generic
from django.urls import reverse
from utilities.views import ViewTab
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from . import tables 
import re

class BaseChangeLogView(generic.ObjectChangeLogView):
    base_template = 'netbox_data_mover/default-detail.html'
    
class BaseObjectView(generic.ObjectView):
    template_name = 'netbox_data_mover/default-detail.html'
    
    def get_extra_context(self, request, instance):
    # Extract fields and their values for the object, including relationships
        field_data = []
        object_name = instance._meta.verbose_name
        # Define fields to exclude
        excluded_extras = {
            'id', 
            'custom_field_data', 
            'tags', 
            'bookmarks', 
            'journal_entries', 
            'subscriptions', 
            'tagged_items', 
            'created',
            'last_updated',
            'object_id',
            'object_type'
        }

        # Extract fields and their values for the object, including relationships
        field_data = []
        for field in instance._meta.get_fields():      
            # Skip excluded fields listed above
            if field.name in excluded_extras:
                continue      
            
            value = None
            url = None
            
            try:
                
                # display only forward relations, not reverse. reverse should be tables below
                if field.is_relation and not field.auto_created:
                    related_object = getattr(instance, field.name)
                    value = str(related_object)  
                    # if hasattr(related_object, 'get_absolute_url'):
                    #     url = related_object.get_absolute_url()
                #handle normal fields
                elif not field.is_relation:
                    value = getattr(instance, field.name)
                else:
                    continue
                    
            except AttributeError:
                value = None  

            field_data.append({
                'name': field.verbose_name if hasattr(field, 'verbose_name') else field.name,
                'value': value,
                'url': url, 
            })

        # Find reverse relations dynamically and add them to related_tables
        related_tables = []
        # for rel in instance._meta.get_fields():
        #     if rel.is_relation and rel.auto_created and not rel.concrete:
        #         related_model = rel.related_model
        #         related_objects = getattr(instance, rel.get_accessor_name()).all()
            
        #         # Create the URL for adding a new related object
        #         add_url = None
        #         if hasattr(related_model, 'get_absolute_url'):
        #             model_name = related_model._meta.model_name.lower()
        #             add_url = reverse(
        #                 f'plugins:netbox_servicemgmt:{model_name}_add'
        #             )   
        #             # Pre-fill the linking field with the current object's ID, if possible
        #             add_url += f'?{instance._meta.model_name.lower()}={instance.pk}'
        #             content_type = ContentType.objects.get_for_model(instance)
        #             attach_url = reverse('plugins:netbox_servicemgmt:generic_attach', kwargs={
        #                 'app_label': content_type.app_label,
        #                 'model_name': content_type.model,
        #                 'pk': instance.pk
        #             })

        #         # Create a table dynamically if a suitable one exists
        #         table_class_name = f"{related_model.__name__}Table"
        #         if hasattr(tables, table_class_name):
        #             table_class = getattr(tables, table_class_name)
        #             # Always create the table, even if related_objects is empty
        #             related_table = table_class(related_objects)
        #         else:
        #             related_table = None

        #         # Append the table to related_tables even if there are no related objects
        #         related_tables.append({
        #             'name': related_model._meta.verbose_name_plural,
        #             'objects': related_objects,
        #             'table': related_table,
        #             'add_url': add_url,
        #             'attach_url': attach_url,
        #         })

                    
        return {
            'object_name': object_name,
            'field_data': field_data,
            'related_tables': related_tables,
        }
    