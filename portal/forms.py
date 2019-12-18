from django import forms
from portal.models import Template

class TemplateForm(forms.ModelForm):
    file_name = forms.CharField(label='Name', max_length=200, required=True)
    content = forms.CharField(label='HTML', widget=forms.Textarea, required=False)
    
    file_name.widget.attrs.update({'class': 'form-control form-control-lg'})
    content.widget.attrs.update({'class': 'form-control form-control-lg', 'style':'display:none;'})

    class Meta:
        model = Template
        fields = ('file_name', 'content')
