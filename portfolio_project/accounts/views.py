from django.shortcuts import render, redirect

from django.views.generic.edit import CreateView, FormView
from django.views.generic.base import TemplateView, View
from .forms import RegistForm, UserLoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Users
from django.views.generic import DeleteView


# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'


class RegistUserView(CreateView):
    template_name = 'regist.html'
    form_class = RegistForm

class UserLoginView(LoginView):
    template_name = 'user_login.html'
    authentication_form = UserLoginForm

    def form_valid(self, form):
        remember=form.cleaned_data['remember']
        if remember:
            self.request.session.set_expiry(1200000)
        return super().form_valid(form)


class UserLogoutView(LogoutView):
    template_name = 'logout.html'
    http_method_names = ['post']
   

# @method_decorator(login_required, name='dispatch')    
class UserView(LoginRequiredMixin, TemplateView):
    template_name = 'user.html'

    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


@login_required
def user_information(request):
    user_data = request.user 
    return render(request, 'user_information.html', {'user_data': user_data})

@login_required
def delete_user_view(request):
    if request.method == 'POST':
        user = request.user
        user.delete_user()
        return HttpResponseRedirect(reverse_lazy('accounts:home'))  
    else:
        return render(request, 'delete_user.html')
    