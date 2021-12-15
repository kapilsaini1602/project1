from django.forms import ModelForm
from django import forms
from homepg.models import Insert
from django.core.exceptions import ValidationError

# define the class of a form
class PostForm(ModelForm):
    name = forms.CharField(max_length=30)
    contact = forms.IntegerField()

    class Meta:
        model = Insert
        fields = '__all__'

    def clean(self):
        cleaned_data = super(PostForm,self).clean()
        contact = cleaned_data.get('contact')
        if len(str(contact)) < 10:
            raise ValidationError("Invalid Contact Number")




