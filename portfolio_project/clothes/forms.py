from django import forms
from .models import Outer,Inner,Pants,Shoes, Coordinate
from datetime import datetime
from django.core.exceptions import ValidationError

class OuterForm(forms.ModelForm):
     
    outer = forms.FileField()
     
    class Meta:
        model = Outer
        fields = ['outer']
          
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['outer'].required = False
        
    def clean_outer(self):
        outer = self.cleaned_data.get('outer')
        
        if outer:
            if not outer.name.lower().endswith(('.jpg', '.jpeg', '.png')):
                verbose_name = self.fields['outer'].label or 'image'
                raise ValidationError(f'Please upload a valid {verbose_name.lower()} image')

        return outer

        
class InnerForm(forms.ModelForm):
    
    inner = forms.FileField()
    
    class Meta:
        model = Inner
        fields = ['inner']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['inner'].required = False
        
    def clean_inner(self):
        inner = self.cleaned_data.get('inner')
        
        if inner:
            if not inner.name.lower().endswith(('.jpg', '.jpeg', '.png')):
                raise ValidationError('画像ファイルはJPG または PNG にしてください')

        return inner


class PantsForm(forms.ModelForm):
    
    pants = forms.FileField()
    
    class Meta:
        model = Pants
        fields = ['pants']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['pants'].required = False
        
    def clean_pants(self):
        pants = self.cleaned_data.get('pants')
        
        if pants:
            if not pants.name.lower().endswith(('.jpg', '.jpeg', '.png')):
                raise ValidationError('画像ファイルはJPG または PNG にしてください')

        return pants

class ShoesForm(forms.ModelForm):
    
    shoes = forms.FileField()
    
    class Meta:
        model = Shoes
        fields = ['shoes']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['shoes'].required = False
        
    def clean_shoes(self):
        shoes = self.cleaned_data.get('shoes')
        
        if shoes:
            if not shoes.name.lower().endswith(('.jpg', '.jpeg', '.png')):
                raise ValidationError('画像ファイルはJPG または PNG にしてください')

        return shoes

    
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