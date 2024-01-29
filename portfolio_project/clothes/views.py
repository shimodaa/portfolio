from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Item,Coordinate
from django.views.generic.edit import (
    CreateView, UpdateView, DeleteView,
    FormView,
)
import os
from . import forms
from .forms import PictureUploadForm,CoordinateForm,CoordinateUpdateForm
from datetime import datetime
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from random import choice



class ItemCreateView(LoginRequiredMixin,CreateView): 
    model = Item
    form_class = PictureUploadForm
    # fields = ['outer','inner','pants','shoes']
    template_name = 'clothes/register_item.html'
    success_url = reverse_lazy('clothes:register_item')
    

    def get_context_data(self, **kwargs): 
        context = super().get_context_data(**kwargs)
        form_to_use = forms.PictureUploadForm()
        context['form_to_use'] = form_to_use
        context['item'] = Item.objects.all() 
        return context
    
    def form_valid(self, form):
        form.instance.create_at = datetime.now()
        form.instance.update_at = datetime.now()
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    # def post(self, request, *args, **kwargs):
    #     form_to_use = forms.PictureUploadForm(request.POST or None, request.FILES or None)     
    #     if form_to_use.is_valid() and request.FILES:
    #        form_to_use.save() 
    #     return super(ItemCreateView, self).post(request, *args, **kwargs)
    
# class ItemCreateView(LoginRequiredMixin, CreateView): 
#     model = Item
#     fields = ['outer', 'inner', 'pants', 'shoes']
#     template_name = os.path.join('clothes', 'register_item.html')
#     success_url = reverse_lazy('clothes:register_item')
#     context_object_name = 'items' 
    
    
#     def form_valid(self, form):
#         # フォームのデータを保存する前に Item インスタンスを作成
#         item_instance = form.save(commit=False)
#         item_instance.outer = form.cleaned_data['outer']
#         item_instance.inner = form.cleaned_data['inner']
#         item_instance.pants = form.cleaned_data['pants']
#         item_instance.shoes = form.cleaned_data['shoes']
#         item_instance.save()

#         # フォームのデータを使いたい場合、form_to_use にデータをセット
#         form_to_use = forms.PictureUploadForm(self.request.POST, self.request.FILES)
#         if form_to_use.is_valid():
#             form_to_use.save()

#         return super().form_valid(form)

#     def get_context_data(self, **kwargs): 
#         context = super().get_context_data(**kwargs)
#         # フォームをテンプレートに追加
#         context['form_to_use'] = forms.PictureUploadForm()
#         context['items'] = Item.objects.all()
#         return context    


    
    
class ItemListView(ListView):
    model = Item
    template_name = 'item_list.html'
    context_object_name = 'items'
    
    # def get_queryset(self):
    #    return Item.objects.all()
   
# class InnerListView(ListView):
#     model = Item
#     template_name = 'inner_list.html'
#     context_object_name = 'items'
    
    # def get_queryset(self):
    #    return Item.objects.all()
    
def delete_picture(request, pk):
    item = get_object_or_404(Item, pk=pk)    
    item.outer.delete()
    import os # 画像をデータから削除する処理
    if os.path.isfile(item.outer.path):
        os.remove(item.outer.path)
    messages.success(request, '画像を削除しました')
    return redirect('clothes:item_list')
    
def inner_delete_picture(request, pk):
    item = get_object_or_404(Item, pk=pk)    
    item.inner.delete()
    import os 
    if os.path.isfile(item.inner.path):
        os.remove(item.inner.path)
    messages.success(request, 'インナーを削除したよ')
    return redirect('clothes:inner_list')
        

def coordinate_view(request,pk):
    
    try:
        outer = Item.objects.get(pk=pk)
        
        coordinate = Coordinate()
        coordinate.outer = outer.outer
        
        coordinate.save()
        
        messages.success(request, '画像をコーディネイトに登録したよ')
        return redirect('clothes:item_list')
    
    except Item.DoesNotExist:
        return render(request, 'home.html')

class CoordinateListView(ListView):
    model = Coordinate
    template_name = 'coordinate_list.html'
    context_object_name = 'coordinates'    

def coordinate_delete(request, pk):
    coordinate = get_object_or_404(Coordinate, pk=pk)
           
    coordinate.delete()
    messages.success(request, 'コーディネイトを削除しました')
    return redirect('clothes:coordinate_list')


class CoordinateUpdateView(SuccessMessageMixin,UpdateView):          
    template_name = 'clothes/coordinate_form.html'
    model = Coordinate
    # form_class = forms.CoordinateUpdateForm
    fields = ['name', 'description']
    success_message = '更新に成功しました'
    success_url = reverse_lazy('clothes:coordinate_list')   
   