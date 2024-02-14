from django.urls import path
from .views import (
    RegistUserView, HomeView, UserLoginView,
    UserLogoutView, UserView,delete_user_view,user_information
)


app_name = 'accounts'
urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    # path('user_information/', UserInformationView.as_view(), name='user_information'),
    path('regist/', RegistUserView.as_view(), name='regist'),
    path('user_login/', UserLoginView.as_view(), name='user_login'),
    # path('user_logout/', UserLogoutView.as_view(), name='user_logout'),
    path('user/', UserView.as_view(), name='user'),
    path('logout/', UserLogoutView.as_view(), name='logout'),    
    path('delete_user/', delete_user_view , name='delete_user'),
    path('user_information/', user_information, name='user_information'),
]