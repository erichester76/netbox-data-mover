
from django import forms
from netbox.forms import NetBoxModelForm
from .models import DataMoverConfig, DataMoverDataSource
from utilities.forms.fields import DynamicModelChoiceField


class DataMoverConfigForm(NetBoxModelForm):
    
    
    source = DynamicModelChoiceField(
            queryset=DataMoverDataSource.objects.all(),
            required=True,
            label="Source",
            help_text="Select the data source."
    )
    
    destination = DynamicModelChoiceField(
        queryset=DataMoverDataSource.objects.all(),
        required=True,
        label="Destination",
        help_text="Select the data destination."
    )
    
    source_endpoint = DynamicModelChoiceField(
        queryset=DataMoverDataSource.objects.none(),
        required=True,
        label="Source Endpoint",
        query_params={'endpoint_id': '$source', 'type': 'endpoints'},
        help_text="Select an endpoint for the chosen source."
    )

    destination_endpoint = DynamicModelChoiceField(
        queryset=DataMoverDataSource.objects.none(),
        required=True,
        label="Destination Endpoint",
        query_params={'endpoint_id': '$destination', 'type': 'endpoints'},
        help_text="Select an endpoint for the chosen destination."
    )

To add a DynamicModelChoiceField that isn't part of the model but acts as a dynamic, form-only field, you can absolutely achieve this by defining the field directly on the form, just like the previous fields (source, destination, etc.). Since you want this field to pull additional data from the DataMoverDataSource API without being tied to the model itself, you don't need it to be in the Meta class or defined as a model field.

Here's how to approach it:

Define the Dynamic Field Directly on the Form:

You will define the source_mapping_fields as a DynamicModelChoiceField in the form's main body, similar to how source or destination were defined.
You will use query_params to control how this field dynamically loads its options.
Use Django's get_extra_context:

If you need additional context for the rendering of the template or specific logic to handle this field, you can utilize Django's get_extra_context method.
You can even override the form's __init__() method to modify or update the field behavior as needed.
Here's a complete implementation of how you could add the source_mapping_fields:

python
Copy code
from django import forms
from netbox.forms import NetBoxModelForm
from utilities.forms.fields import DynamicModelChoiceField
from .models import DataMoverConfig, DataMoverDataSource

class DataMoverConfigForm(NetBoxModelForm):
    source = DynamicModelChoiceField(
        queryset=DataMoverDataSource.objects.all(),
        required=True,
        label="Source",
        help_text="Select the data source."
    )
    
    destination = DynamicModelChoiceField(
        queryset=DataMoverDataSource.objects.all(),
        required=True,
        label="Destination",
        help_text="Select the data destination."
    )
    
    source_endpoint = DynamicModelChoiceField(
        queryset=DataMoverDataSource.objects.none(),
        required=True,
        label="Source Endpoint",
        query_params={'endpoint_id': '$source', 'type': 'endpoints'},
        help_text="Select an endpoint for the chosen source."
    )

    destination_endpoint = DynamicModelChoiceField(
        queryset=DataMoverDataSource.objects.none(),
        required=True,
        label="Destination Endpoint",
        query_params={'endpoint_id': '$destination', 'type': 'endpoints'},
        help_text="Select an endpoint for the chosen destination."
    )

    # New field that is not a part of the model
    source_mapping_fields = DynamicModelChoiceField(
        queryset=DataMoverDataSource.objects.none(),  # Start with none, will be updated dynamically
        required=False,
        label="Source Mapping Fields",
        query_params={'mapping_id': '$source_endpoint', 'type': 'mapping_fields'},
        help_text="Select the fields for mapping from the source endpoint."
    )
    
    
To add a DynamicModelChoiceField that isn't part of the model but acts as a dynamic, form-only field, you can absolutely achieve this by defining the field directly on the form, just like the previous fields (source, destination, etc.). Since you want this field to pull additional data from the DataMoverDataSource API without being tied to the model itself, you don't need it to be in the Meta class or defined as a model field.

Here's how to approach it:

Define the Dynamic Field Directly on the Form:

You will define the source_mapping_fields as a DynamicModelChoiceField in the form's main body, similar to how source or destination were defined.
You will use query_params to control how this field dynamically loads its options.
Use Django's get_extra_context:

If you need additional context for the rendering of the template or specific logic to handle this field, you can utilize Django's get_extra_context method.
You can even override the form's __init__() method to modify or update the field behavior as needed.
Here's a complete implementation of how you could add the source_mapping_fields:

python
Copy code
from django import forms
from netbox.forms import NetBoxModelForm
from utilities.forms.fields import DynamicModelChoiceField
from .models import DataMoverConfig, DataMoverDataSource

class DataMoverConfigForm(NetBoxModelForm):
    source = DynamicModelChoiceField(
        queryset=DataMoverDataSource.objects.all(),
        required=True,
        label="Source",
        help_text="Select the data source."
    )
    
    destination = DynamicModelChoiceField(
        queryset=DataMoverDataSource.objects.all(),
        required=True,
        label="Destination",
        help_text="Select the data destination."
    )
    
    source_endpoint = DynamicModelChoiceField(
        queryset=DataMoverDataSource.objects.none(),
        required=True,
        label="Source Endpoint",
        query_params={'endpoint_id': '$source', 'type': 'endpoints'},
        help_text="Select an endpoint for the chosen source."
    )

    destination_endpoint = DynamicModelChoiceField(
        queryset=DataMoverDataSource.objects.none(),
        required=True,
        label="Destination Endpoint",
        query_params={'endpoint_id': '$destination', 'type': 'endpoints'},
        help_text="Select an endpoint for the chosen destination."
    )
    source_mapping_fields = DynamicModelChoiceField(
        queryset=DataMoverDataSource.objects.none(),  # Start with none, will be updated dynamically
        required=False,
        label="Source Mapping Field",
        query_params={'mapping_id': '$source_endpoint', 'type': 'mapping_fields'},
        help_text="Select the field for mapping from the source endpoint."
    )
    destination_mapping_fields = DynamicModelChoiceField(
        queryset=DataMoverDataSource.objects.none(),  # Start with none, will be updated dynamically
        required=False,
        label="Destination Mapping Field",
        query_params={'mapping_id': '$destination_endpoint', 'type': 'mapping_fields'},
        help_text="Select the field for mapping to the destination endpoint."
    )
    
    class Meta:
        SCHEDULE_CHOICES = [
            ('', 'None - Manual Only'),
            ('0 * * * *', 'Hourly'),
            ('0 0 * * *', 'Daily'),
            ('0 0 * * 0', 'Weekly'),
            ('0 0 1 * *', 'Monthly'),
        ]
        
        model = DataMoverConfig
        fields = ['source', 'source_endpoint', 'source_mapping_fields',
                  'destination', 'destination_endpoint', 'destination_mapping_fields',
                  'name', 'schedule', 'description']
        
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class DataMoverDataSourceForm(NetBoxModelForm):
    class Meta:
        model = DataMoverDataSource
        fields = [
            'name', 'type', 'module', 'endpoints', 'auth_method', 'auth_function', 
            'find_function', 'create_function', 'update_function', 'fetch_function', 
            'auth_args', 'base_urls'
        ]
