from django import forms
from .models import Item, Coordinate
from datetime import datetime


class PictureUploadForm(forms.ModelForm):
    outer = forms.FileField(required=False)
    inner = forms.FileField(required=False)
    pants = forms.FileField(required=False)
    shoes = forms.FileField(required=False)
    
    class Meta:
        model = Item
        fields = ['outer', 'inner', 'pants', 'shoes']

    def save(self, *args, **kwargs):
        obj = super(PictureUploadForm, self).save(commit=False)
        obj.create_at = datetime.now()
        obj.update_at = datetime.now()
        
        outer_file = self.cleaned_data.get('outer', None)
        inner_file = self.cleaned_data.get('inner', None)
        pants_file = self.cleaned_data.get('pants', None)
        shoes_file = self.cleaned_data.get('shoes', None)
        
        obj.outer = outer_file
        obj.inner = inner_file
        obj.pants = pants_file
        obj.shoes = shoes_file
        
        obj.save()
        return obj
    
class CoordinateForm(forms.ModelForm):
    class Meta:
        model = Coordinate
        fields = ['name','description', 'outer','inner','pants','shoes']
   
    def save(self, *args, **kwargs):
        obj = super(CoordinateForm, self).save(commit=False)
        obj.create_at = datetime.now()
        obj.update_at = datetime.now()
        # obj.book = kwargs['book']
        obj.save()
        return obj
    
class CoordinateUpdateForm(forms.ModelForm):
    class Meta:
        model = Coordinate
        fields = ['name','description','outer','inner','pants','shoes']
   
    def save(self, *args, **kwargs):
        obj = super(CoordinateUpdateForm, self).save(commit=False)      
        obj.update_at = datetime.now()
        # obj.book = kwargs['book']
        obj.save()
        return obj