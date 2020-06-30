from django import forms
from Avadell.models import Cotizacion
from localflavor.us.forms import USZipCodeField


class CotizacionCreateForm(forms.ModelForm):
    postal_code = USZipCodeField()
    class Meta:
        model = Cotizacion
        fields = ['project_name', 'report_code', 'email', 'address']