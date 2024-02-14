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


# class PictureUploadForm(forms.ModelForm):
#     outer = forms.FileField(required=False)
#     inner = forms.FileField(required=False)
#     pants = forms.FileField(required=False)
#     shoes = forms.FileField(required=False)
    
#     # class Meta:
#     #     model =
#     #     fields = ['outer', 'inner', 'pants', 'shoes']

#     def save(self, *args, **kwargs):
#         obj = super(PictureUploadForm, self).save(commit=False)
#         obj.create_at = datetime.now()
#         obj.update_at = datetime.now()
        
#         outer_file = self.cleaned_data.get('outer', None)
#         inner_file = self.cleaned_data.get('inner', None)
#         pants_file = self.cleaned_data.get('pants', None)
#         shoes_file = self.cleaned_data.get('shoes', None)
        
#         obj.outer = outer_file
#         obj.inner = inner_file
#         obj.pants = pants_file
#         obj.shoes = shoes_file
        
#         obj.save()
#         return obj
    
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