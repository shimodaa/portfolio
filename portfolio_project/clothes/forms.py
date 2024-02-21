from django import forms
from .models import Outer,Inner,Pants,Shoes, Coordinate
from datetime import datetime

class OuterForm(forms.ModelForm):
    class Meta:
        model = Outer
        fields = ['outer']
          
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['outer'].required = False

        
class InnerForm(forms.ModelForm):
    class Meta:
        model = Inner
        fields = ['inner']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['inner'].required = False


class PantsForm(forms.ModelForm):
    class Meta:
        model = Pants
        fields = ['pants']

class ShoesForm(forms.ModelForm):
    class Meta:
        model = Shoes
        fields = ['shoes']

    
class CoordinateForm(forms.ModelForm):
    class Meta:
        model = Coordinate
        fields = ['name','description', 'outer','inner','pants','shoes']
   
        labels = {
            'description': 'Description', 
        }
   
    description = forms.CharField(
        required=False, )
   
    def save(self, *args, **kwargs):
        obj = super(CoordinateForm, self).save(commit=False)
        obj.create_at = datetime.now()
        obj.update_at = datetime.now()
        obj.save()
        return obj
    
class CoordinateUpdateForm(forms.ModelForm):
    class Meta:
        model = Coordinate
        fields = ['name','description','outer','inner','pants','shoes']
   
        labels = {
            'description': 'Description', 
        }
   
    description = forms.CharField(
        required=False, )
   
    def save(self, *args, **kwargs):
        obj = super(CoordinateUpdateForm, self).save(commit=False)      
        obj.update_at = datetime.now()
        obj.save()
        return obj