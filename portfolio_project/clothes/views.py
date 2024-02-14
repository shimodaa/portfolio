from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Outer,Inner,Pants,Shoes,Coordinate,Favorite
from django.views.generic.edit import (
    CreateView, UpdateView, DeleteView,
    FormView,
)
import os
from . import forms
from django.db import models 
from .forms import OuterForm,InnerForm,PantsForm,ShoesForm,CoordinateForm,CoordinateUpdateForm
from datetime import datetime
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from random import choice
from django.db import transaction
from django.http import Http404
from django.core.files.base import ContentFile


class RegisterOuterView(FormView):
    template_name = 'clothes/register_outer.html'
    form_class = OuterForm 
    success_url = reverse_lazy('clothes:register_outer')
    
    def post(self, request, *args, **kwargs):
        outer_form = OuterForm(request.POST or None, request.FILES or None)
        
        if outer_form.is_valid() and outer_form.files:
            outer_instance = outer_form.save(commit=False)
            outer_instance.create_at = datetime.now()
            outer_instance.update_at = datetime.now()
            outer_instance.user = self.request.user
            outer_instance.save()

            return self.form_valid(outer_form)

        return super().post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['outer_form'] = OuterForm()
        return context
    
    def form_valid(self, form):
        form.instance.create_at = datetime.now()
        form.instance.update_at = datetime.now()
        form.instance.user = self.request.user
        return super().form_valid(form) 

class RegisterInnerView(FormView):
    template_name = 'clothes/register_inner.html'
    form_class = InnerForm 
    success_url = reverse_lazy('clothes:register_inner')
    
    def post(self, request, *args, **kwargs):
        inner_form = InnerForm(request.POST or None, request.FILES or None)
        
        if inner_form.is_valid() and inner_form.files:
            inner_instance = inner_form.save(commit=False)
            inner_instance.create_at = datetime.now()
            inner_instance.update_at = datetime.now()
            inner_instance.user = self.request.user
            inner_instance.save()

            return self.form_valid(inner_form)

        return super().post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['inner_form'] = InnerForm()
        return context
    
    def form_valid(self, form):
        form.instance.create_at = datetime.now()
        form.instance.update_at = datetime.now()
        form.instance.user = self.request.user
        return super().form_valid(form) 
    
class RegisterPantsView(FormView):
    template_name = 'clothes/register_pants.html'
    form_class = PantsForm 
    success_url = reverse_lazy('clothes:register_outer')
    
    def post(self, request, *args, **kwargs):
        pants_form = PantsForm(request.POST or None, request.FILES or None)
        
        if pants_form.is_valid() and pants_form.files:
            pants_instance = pants_form.save(commit=False)
            pants_instance.user = self.request.user
            pants_instance.save()

            return self.form_valid(pants_form)

        return super().post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pants_form'] = PantsForm()
        return context
    
    def form_valid(self, form):
        form.instance.create_at = datetime.now()
        form.instance.update_at = datetime.now()
        form.instance.user = self.request.user
        return super().form_valid(form) 
    
class RegisterShoesView(FormView):
    template_name = 'clothes/register_shoes.html'
    form_class = ShoesForm 
    success_url = reverse_lazy('clothes:register_shoes')
    
    def post(self, request, *args, **kwargs):
        shoes_form = ShoesForm(request.POST or None, request.FILES or None)
        
        if shoes_form.is_valid() and shoes_form.files:
            shoes_instance = shoes_form.save(commit=False)
            shoes_instance.user = self.request.user
            shoes_instance.save()

            return self.form_valid(shoes_form)

        return super().post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shoes_form'] = ShoesForm()
        return context
    
    def form_valid(self, form):
        form.instance.create_at = datetime.now()
        form.instance.update_at = datetime.now()
        form.instance.user = self.request.user
        return super().form_valid(form) 

    
class OuterListView(ListView):
    model = Outer
    model = Coordinate
    model = Favorite
    template_name = 'clothes/outer_list.html'
   
    context_object_name1 = 'outers'
    context_object_name2 = 'coordinates'
    context_object_name3 = 'favorites'

    
    def get_queryset(self):
       if self.request.user.is_authenticated:
         outer_queryset = Outer.objects.filter(user=self.request.user)
         coordinate_queryset = Coordinate.objects.filter(user=self.request.user)
         favorite_queryset = Favorite.objects.filter(user=self.request.user)
        #  return Outer.objects.filter(user=self.request.user)
         return outer_queryset, coordinate_queryset, favorite_queryset
       else:
        # return Outer.objects.none()
        return Outer.objects.none(), Coordinate.objects.none(), Favorite.objects.none()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        outer_queryset, coordinate_queryset, favorite_queryset = self.get_queryset()
        context[self.context_object_name1] = outer_queryset
        context[self.context_object_name2] = coordinate_queryset
        context[self.context_object_name3] = favorite_queryset        
        return context
    
class InnerListView(ListView):
    model = Inner
    model = Coordinate
    model = Favorite
    template_name = 'clothes/inner_list.html'
    context_object_name1 = 'inners'
    context_object_name2 = 'coordinates'
    context_object_name3 = 'favorites'
    
    def get_queryset(self):          
       if self.request.user.is_authenticated:
         inner_queryset = Inner.objects.filter(user=self.request.user)
         coordinate_queryset = Coordinate.objects.filter(user=self.request.user)
         favorite_queryset = Favorite.objects.filter(user=self.request.user)
         return inner_queryset, coordinate_queryset, favorite_queryset
       else:
        # ユーザーが認証されてない場合
        return Inner.objects.none(), Coordinate.objects.none(),Favorite.objects.none()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        inner_queryset, coordinate_queryset, favorite_queryset = self.get_queryset()
        context[self.context_object_name1] = inner_queryset
        context[self.context_object_name2] = coordinate_queryset
        context[self.context_object_name3] = favorite_queryset
        return context
    
class PantsListView(ListView):
    model = Pants
    model = Coordinate
    model = Favorite
    template_name = 'clothes/pants_list.html'
   
    context_object_name1 = 'pants'
    context_object_name2 = 'coordinates'
    context_object_name3 = 'favorites'

    
    def get_queryset(self):
       if self.request.user.is_authenticated:
         pants_queryset = Pants.objects.filter(user=self.request.user)
         coordinate_queryset = Coordinate.objects.filter(user=self.request.user)
         favorite_queryset = Favorite.objects.filter(user=self.request.user)
        #  return Outer.objects.filter(user=self.request.user)
         return pants_queryset, coordinate_queryset, favorite_queryset
       else:
        # return Outer.objects.none()
        return Pants.objects.none(), Coordinate.objects.none(), Favorite.objects.none()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        pants_queryset, coordinate_queryset, favorite_queryset = self.get_queryset()
        context[self.context_object_name1] = pants_queryset
        context[self.context_object_name2] = coordinate_queryset
        context[self.context_object_name3] = favorite_queryset        
        return context
    
class CoordinateListView(ListView):
    model = Coordinate
    template_name = 'coordinate_list.html'
    context_object_name = 'coordinates'
    
    def get_queryset(self):
       if self.request.user.is_authenticated:
         coordinate_queryset = Coordinate.objects.filter(user=self.request.user)
        #  return Outer.objects.filter(user=self.request.user)
         return  coordinate_queryset
       else:
        return Coordinate.objects.none()   
    
class CoordinateUpdateView(SuccessMessageMixin,UpdateView):          
    template_name = 'clothes/coordinate_form.html'
    model = Coordinate
    # form_class = forms.CoordinateUpdateForm
    fields = ['name', 'description']
    success_message = '更新に成功しました'
    success_url = reverse_lazy('clothes:coordinate_list')   
    
def coordinate_delete(request, pk):
    coordinate = get_object_or_404(Coordinate, pk=pk)
           
    coordinate.delete()
    messages.success(request, 'コーディネイトを削除しました')
    return redirect('clothes:coordinate_list')        

def delete_picture(request, pk):

    outer = get_object_or_404(Outer, pk=pk)    
      
    if outer.outer:     
     import os 
     if os.path.isfile(outer.outer.path):
         os.remove(outer.outer.path)  
         
     outer.outer.delete()  
    
    with transaction.atomic():
     outer.delete()

    messages.success(request, 'アウターを削除しました')

    return redirect('clothes:outer_list')

def favorite_outer_delete_picture(request, pk):

    favorite = get_object_or_404(Favorite, pk=pk)    
      
    if favorite.outer:     
     import os 
     if os.path.isfile(favorite.outer.path):
         os.remove(favorite.outer.path)  
         
     favorite.outer.delete()  
    
    with transaction.atomic():
     favorite.delete()

    messages.success(request, 'お気に入りを削除しました')

    return redirect('clothes:outer_list')


def add_favorite_outer_view(request,pk):
    
    try:
        
        outer = Outer.objects.get(pk=pk)
        user_id = request.user.id
        favorite = Favorite.objects.create(user_id=user_id, outer=outer.outer)
        favorite.save()
        
        messages.success(request, '画像をお気に入りに登録したよ')
        return redirect('clothes:outer_list')
    except Outer.DoesNotExist:
        return render(request, 'home.html')

def add_outer_coordinate_view(request, outer_id, coordinate_id):
    
    try:
        
        outer = Outer.objects.get(pk=outer_id)
        
        coordinate_instance = Coordinate.objects.get(pk=coordinate_id)
       
        if outer.outer:
            # Outerモデルの画像データを読み込み、Coordinateモデルに保存
            coordinate_instance.outer.save(outer.outer.name, ContentFile(outer.outer.read()), save=True)

        
        messages.success(request, '画像をコーディネイトに登録したよ')
        return redirect('clothes:outer_list')
    
    except Outer.DoesNotExist:
        return render(request, 'home.html')

def create_outer_coordinate(request,pk):
    
    try:
        
        outer = Outer.objects.get(pk=pk)
        user_id = request.user.id
        outer = Coordinate.objects.create(user_id=user_id, outer=outer.outer)
        outer.save()
        
        messages.success(request, 'コーディネイトを作成しました')
        return redirect('clothes:outer_list')
    except Outer.DoesNotExist:
        return render(request, 'home.html')
    

def create_favorite_outer_coordinate(request,pk):
    
    try:
        
        favorite = Favorite.objects.get(pk=pk)
        user_id = request.user.id
        outer = Coordinate.objects.create(user_id=user_id, outer=favorite.outer)
        outer.save()
        
        messages.success(request, 'コーディネイトを作成しました')
        return redirect('clothes:outer_list')
    except Outer.DoesNotExist:
        return render(request, 'home.html')


def add_favorite_outer_coordinate(request, outer_id, coordinate_id):
    
    try:
        
         favorite = Favorite.objects.get(pk=outer_id)
        
         coordinate = Coordinate.objects.get(pk=coordinate_id)
       
         if favorite.outer:
            # Outerモデルの画像データを読み込み、Coordinateモデルに保存
            coordinate.outer.save(favorite.outer.name, ContentFile(favorite.outer.read()), save=True)

        
         messages.success(request, 'コーディネイトを作成しました')
         return redirect('clothes:outer_list')
    except Favorite.DoesNotExist:
        return render(request, 'home.html')
        

    
def inner_delete_picture(request, pk):
    inner = get_object_or_404(Inner, pk=pk)     
    if inner.inner:     
     import os 
     if os.path.isfile(inner.inner.path):
         os.remove(inner.inner.path)  
     inner.inner.delete()  
    with transaction.atomic():
     inner.delete()
    messages.success(request, 'インナーを削除しました')
    return redirect('clothes:inner_list')

def create_inner_coordinate_view(request,pk):
    
    try:
        inner = Inner.objects.get(pk=pk)
        user_id = request.user.id
        inner = Coordinate.objects.create(user_id=user_id, inner=inner.inner)
        inner.save()
        
        
        messages.success(request, '画像をコーディネイトに登録したよ')
        return redirect('clothes:inner_list')
    
    except Inner.DoesNotExist:
        return render(request, 'home.html')
    
def add_inner_coordinate(request, inner_id, coordinate_id):
    
    try:
        
        inner = Inner.objects.get(pk=inner_id)
        
        coordinate_instance = Coordinate.objects.get(pk=coordinate_id)
       
        if inner.inner:
            # Outerモデルの画像データを読み込み、Coordinateモデルに保存
            coordinate_instance.inner.save(inner.inner.name, ContentFile(inner.inner.read()), save=True)

        
        messages.success(request, '画像をコーディネイトに登録したよ')
        return redirect('clothes:inner_list')
    
    except Inner.DoesNotExist:
        return render(request, 'home.html')
    
def add_favorite_inner(request,pk):
    
    try:
        
        inner = Inner.objects.get(pk=pk)
        user_id = request.user.id
        inner = Favorite.objects.create(user_id=user_id, inner=inner.inner)
        inner.save()
        
        messages.success(request, '画像をお気に入りに登録したよ')
        return redirect('clothes:inner_list')
    except Inner.DoesNotExist:
        return render(request, 'home.html')

def create_favorite_inner_coordinate(request,pk):
    
    try:
        
        favorite = Favorite.objects.get(pk=pk)
        user_id = request.user.id
        inner = Coordinate.objects.create(user_id=user_id, inner=favorite.inner)
        inner.save()
        
        messages.success(request, 'コーディネイトを作成しました')
        return redirect('clothes:inner_list')
    except Inner.DoesNotExist:
        return render(request, 'home.html')    

def add_favorite_inner_coordinate(request, inner_id, coordinate_id):
    
    try:
        
         favorite = Favorite.objects.get(pk=inner_id)
        
         coordinate = Coordinate.objects.get(pk=coordinate_id)
       
         if favorite.inner:
            # Outerモデルの画像データを読み込み、Coordinateモデルに保存
            coordinate.inner.save(favorite.inner.name, ContentFile(favorite.inner.read()), save=True)

        
         messages.success(request, 'コーディネイトを作成しました')
         return redirect('clothes:inner_list')
    except Favorite.DoesNotExist:
        return render(request, 'home.html')    
    
def favorite_inner_delete_picture(request, pk):

    favorite = get_object_or_404(Favorite, pk=pk)    
      
    if favorite.inner:     
     import os 
     if os.path.isfile(favorite.inner.path):
         os.remove(favorite.inner.path)  
         
     favorite.inner.delete()  
    
    with transaction.atomic():
     favorite.delete()

    messages.success(request, 'お気に入りを削除しました')

    return redirect('clothes:inner_list')
    
    
def pants_delete_picture(request, pk):
    pants = get_object_or_404(Pants, pk=pk)     
    if pants.pants:     
     import os 
     if os.path.isfile(pants.pants.path):
         os.remove(pants.pants.path)  
     pants.pants.delete()  
    with transaction.atomic():
     pants.delete()
    messages.success(request, 'パンツを削除しました')
    return redirect('clothes:pants_list')
    
def create_pants_coordinate(request,pk):
    
    try:
        
        pants = Pants.objects.get(pk=pk)
        user_id = request.user.id
        pants = Coordinate.objects.create(user_id=user_id, pants=pants.pants)
        pants.save()
        
        messages.success(request, 'コーディネイトを作成しました')
        return redirect('clothes:pants_list')
    except Pants.DoesNotExist:
        return render(request, 'home.html')  

def add_pants_coordinate(request, pants_id, coordinate_id):
    
    try:
        
        pants = Pants.objects.get(pk=pants_id)
        
        coordinate_instance = Coordinate.objects.get(pk=coordinate_id)
       
        if pants.pants:
            # Outerモデルの画像データを読み込み、Coordinateモデルに保存
            coordinate_instance.pants.save(pants.pants.name, ContentFile(pants.pants.read()), save=True)

        
        messages.success(request, '画像をコーディネイトに登録したよ')
        return redirect('clothes:pants_list')
    
    except Pants.DoesNotExist:
        return render(request, 'home.html')

def add_favorite_pants(request,pk):
    
    try:
        
        pants = Pants.objects.get(pk=pk)
        user_id = request.user.id
        pants = Favorite.objects.create(user_id=user_id, pants=pants.pants)
        pants.save()
        
        messages.success(request, '画像をお気に入りに登録したよ')
        return redirect('clothes:pants_list')
    except Pants.DoesNotExist:
        return render(request, 'home.html')
    
def create_favorite_pants_coordinate(request,pk):
    
    try:
        
        favorite = Favorite.objects.get(pk=pk)
        user_id = request.user.id
        pants = Coordinate.objects.create(user_id=user_id, pants=favorite.pants)
        pants.save()
        
        messages.success(request, 'コーディネイトを作成しました')
        return redirect('clothes:pants_list')
    except Pants.DoesNotExist:
        return render(request, 'home.html')


def add_favorite_pants_coordinate(request, pants_id, coordinate_id):
    
    try:
        
         favorite = Favorite.objects.get(pk=pants_id)
        
         coordinate = Coordinate.objects.get(pk=coordinate_id)
       
         if favorite.pants:
            # Outerモデルの画像データを読み込み、Coordinateモデルに保存
            coordinate.pants.save(favorite.pants.name, ContentFile(favorite.pants.read()), save=True)

        
         messages.success(request, 'コーディネイトに追加しました。')
         return redirect('clothes:pants_list')
    except Pants.DoesNotExist:
        return render(request, 'home.html')

def favorite_pants_delete_picture(request, pk):

    favorite = get_object_or_404(Favorite, pk=pk)    
      
    if favorite.pants:     
     import os 
     if os.path.isfile(favorite.pants.path):
         os.remove(favorite.pants.path)  
         
     favorite.pants.delete()  
    
    with transaction.atomic():
     favorite.delete()

    messages.success(request, 'お気に入りを削除しました')

    return redirect('clothes:pants_list')   

class ShoesListView(ListView):
    model = Shoes
    model = Coordinate
    model = Favorite
    template_name = 'clothes/shoes_list.html'
   
    context_object_name1 = 'shoess'
    context_object_name2 = 'coordinates'
    context_object_name3 = 'favorites'

    
    def get_queryset(self):
       if self.request.user.is_authenticated:
         shoes_queryset = Shoes.objects.filter(user=self.request.user)
         coordinate_queryset = Coordinate.objects.filter(user=self.request.user)
         favorite_queryset = Favorite.objects.filter(user=self.request.user)
        #  return Outer.objects.filter(user=self.request.user)
         return shoes_queryset, coordinate_queryset, favorite_queryset
       else:
        # return Outer.objects.none()
        return Shoes.objects.none(), Coordinate.objects.none(), Favorite.objects.none()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) 
        shoes_queryset, coordinate_queryset, favorite_queryset = self.get_queryset()
        context[self.context_object_name1] = shoes_queryset
        context[self.context_object_name2] = coordinate_queryset
        context[self.context_object_name3] = favorite_queryset        
        return context
    
def shoes_delete_picture(request, pk):

    shoes = get_object_or_404(Shoes, pk=pk)    
      
    if shoes.shoes:     
     import os 
     if os.path.isfile(shoes.shoes.path):
         os.remove(shoes.shoes.path)  
         
     shoes.shoes.delete()  
    
    with transaction.atomic():
     shoes.delete()

    messages.success(request, 'シューズを削除しました')

    return redirect('clothes:shoes_list')

def favorite_shoes_delete_picture(request, pk):

    favorite = get_object_or_404(Favorite, pk=pk)    
      
    if favorite.shoes:     
     import os 
     if os.path.isfile(favorite.shoes.path):
         os.remove(favorite.shoes.path)  
         
     favorite.shoes.delete()  
    
    with transaction.atomic():
     favorite.delete()

    messages.success(request, 'お気に入りを削除しました')

    return redirect('clothes:shoes_list')


    
def create_shoes_coordinate(request,pk):
    
    try:
        
        shoes = Shoes.objects.get(pk=pk)
        user_id = request.user.id
        shoes = Coordinate.objects.create(user_id=user_id, shoes=shoes.shoes)
        shoes.save()
        
        messages.success(request, 'コーディネイトを作成しました')
        return redirect('clothes:shoes_list')
    except Shoes.DoesNotExist:
        return render(request, 'home.html')

def add_shoes_coordinate(request, shoes_id, coordinate_id):
    
    try:
        
        shoes = Shoes.objects.get(pk=shoes_id)
        
        coordinate_instance = Coordinate.objects.get(pk=coordinate_id)
       
        if shoes.shoes:
            # Outerモデルの画像データを読み込み、Coordinateモデルに保存
            coordinate_instance.shoes.save(shoes.shoes.name, ContentFile(shoes.shoes.read()), save=True)

        
        messages.success(request, '画像をコーディネイトに登録したよ')
        return redirect('clothes:shoes_list')
    
    except Shoes.DoesNotExist:
        return render(request, 'home.html')
    
def add_favorite_shoes_view(request,pk):
    
    try:
        
        shoes = Shoes.objects.get(pk=pk)
        user_id = request.user.id
        shoes = Favorite.objects.create(user_id=user_id, shoes=shoes.shoes)
        shoes.save()
        
        messages.success(request, '画像をお気に入りに登録したよ')
        return redirect('clothes:shoes_list')
    except Shoes.DoesNotExist:
        return render(request, 'home.html')



def create_favorite_shoes_coordinate(request,pk):
    
    try:
        
        favorite = Favorite.objects.get(pk=pk)
        user_id = request.user.id
        shoes = Coordinate.objects.create(user_id=user_id, shoes=favorite.outer)
        shoes.save()
        
        messages.success(request, 'コーディネイトを作成しました')
        return redirect('clothes:shoes_list')
    except Shoes.DoesNotExist:
        return render(request, 'home.html')


def add_favorite_shoes_coordinate(request, shoes_id, coordinate_id):
    
    try:
        
         favorite = Favorite.objects.get(pk=shoes_id)
        
         coordinate = Coordinate.objects.get(pk=coordinate_id)
       
         if favorite.shoes:
            # Outerモデルの画像データを読み込み、Coordinateモデルに保存
            coordinate.shoes.save(favorite.shoes.name, ContentFile(favorite.shoes.read()), save=True)

        
         messages.success(request, 'コーディネイトを作成しました')
         return redirect('clothes:shoes_list')
    except Favorite.DoesNotExist:
        return render(request, 'home.html')
        