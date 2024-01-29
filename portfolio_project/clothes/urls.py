from django.urls import path
from .views import (ItemCreateView,ItemListView,
    delete_picture,coordinate_view,
    CoordinateListView,coordinate_delete,CoordinateUpdateView,inner_delete_picture,
    
)
from django.conf import settings
from django.conf.urls.static import static
# from django.views.generic.base import TemplateView


app_name = 'clothes'

urlpatterns = [
    path('register_item/', ItemCreateView.as_view(), name='register_item'),
    path('item_list/', ItemListView.as_view(), name='item_list'),
    path('delete_picture/<int:pk>', delete_picture, name='delete_picture'),
    path('coordinate/<int:pk>', coordinate_view, name='coordinate_view'),
    path('coordinate_list/',CoordinateListView.as_view() , name='coordinate_list'),
    path('coordinate/<int:pk>/delete/',coordinate_delete , name='coordinate_delete'),
    path('coordinate_form/<int:pk>',CoordinateUpdateView.as_view() , name='coordinate_form'),
    # path('inner_list/', InnerListView.as_view(), name='inner_list'),
    path('inner_delete_picture/<int:pk>',inner_delete_picture , name='inner_delete_picture'),
   

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)