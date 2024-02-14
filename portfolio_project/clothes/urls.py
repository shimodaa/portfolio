from django.urls import path
from .views import (RegisterOuterView,RegisterInnerView,RegisterPantsView,RegisterShoesView,
                    OuterListView,InnerListView,PantsListView,ShoesListView,CoordinateListView,CoordinateUpdateView,
     create_outer_coordinate,add_outer_coordinate_view,delete_picture,add_favorite_outer_view,create_favorite_outer_coordinate,
     add_favorite_outer_coordinate,favorite_outer_delete_picture,
     inner_delete_picture,create_inner_coordinate_view,add_inner_coordinate,add_favorite_inner,create_favorite_inner_coordinate,
     add_favorite_inner_coordinate,favorite_inner_delete_picture,
     pants_delete_picture,create_pants_coordinate,add_pants_coordinate,
     add_favorite_pants_coordinate,create_favorite_pants_coordinate,add_favorite_pants,favorite_pants_delete_picture,
     coordinate_delete,
     shoes_delete_picture,favorite_shoes_delete_picture,create_shoes_coordinate,add_shoes_coordinate,add_favorite_shoes_view,
     create_favorite_shoes_coordinate,add_favorite_shoes_coordinate,
    
    
 )
from django.conf import settings
from django.conf.urls.static import static
# from django.views.generic.base import TemplateView


app_name = 'clothes'

urlpatterns = [
    path('register_outer/', RegisterOuterView.as_view(), name='register_outer'),
    path('register_inner/', RegisterInnerView.as_view(), name='register_inner'),
    path('register_pants/', RegisterPantsView.as_view(), name='register_pants'),
    path('register_shoes/', RegisterShoesView.as_view(), name='register_shoes'),
    path('outer_list/', OuterListView.as_view(), name='outer_list'), 
    path('create_outer_coordinate<int:pk>/',create_outer_coordinate, name='create_outer_coordinate'), 
    path('add_outer_coordinate/<int:outer_id>/<int:coordinate_id>/', add_outer_coordinate_view, name='add_outer_coordinate_view'),        
    path('delete_picture/<int:pk>', delete_picture, name='delete_picture'),    
    path('add_favorite_outer<int:pk>/',add_favorite_outer_view , name='add_favorite_outer_view'),    
    path('create_favorite_outer_coordinate<int:pk>/',create_favorite_outer_coordinate, name='create_favorite_outer_coordinate'),         
    path('add_favorite_outer_coordinate<int:outer_id>/<int:coordinate_id>/',add_favorite_outer_coordinate, name='add_favorite_outer_coordinate'),     
    path('favorite_outer_delete_picture/<int:pk>', favorite_outer_delete_picture, name='favorite_outer_delete_picture'),   
    path('inner_list/', InnerListView.as_view(), name='inner_list'), 
    path('inner_delete_picture/<int:pk>', inner_delete_picture, name='inner_delete_picture'),
    path('add_inner_coordinate/<int:inner_id>/<int:coordinate_id>/',add_inner_coordinate, name='add_inner_coordinate'),
    path('add_favorite_inner<int:pk>/',add_favorite_inner, name='add_favorite_inner'),
    path('create_favorite_inner_coordinate<int:pk>/',create_favorite_inner_coordinate, name='create_favorite_inner_coordinate'),
    path('add_favorite_inner_coordinate/<int:inner_id>/<int:coordinate_id>',add_favorite_inner_coordinate, name='add_favorite_inner_coordinate'),
    path('favorite_inner_delete_picture/<int:pk>',favorite_inner_delete_picture, name='favorite_inner_delete_picture'),
    path('pants_list/',PantsListView.as_view(), name='pants_list'),
    path('pants_delete_picture/<int:pk>', pants_delete_picture, name='pants_delete_picture'),    
    path('create_inner_coordinate/<int:pk>',create_inner_coordinate_view , name='create_inner_coordinate_view'),    
    path('create_pants_coordinate/<int:pk>',create_pants_coordinate, name='create_pants_coordinate'), 
    path('add_pants_coordinate/<int:pants_id>/<int:coordinate_id>',add_pants_coordinate, name='add_pants_coordinate'),     
    path('add_favorite_pants<int:pk>/',add_favorite_pants, name='add_favorite_pants'),
    path('create_favorite_pants_coordinate<int:pk>/',create_favorite_pants_coordinate, name='create_favorite_pants_coordinate'),    
    path('add_favorite_pants_coordinate/<int:pants_id>/<int:coordinate_id>',add_favorite_pants_coordinate, name='add_favorite_pants_coordinate'),         
    path('favorite_pants_delete_picture/<int:pk>',favorite_pants_delete_picture, name='favorite_pants_delete_picture'),       
    path('shoes_list/',ShoesListView.as_view(), name='shoes_list'),
    path('shoes_delete_picture/<int:pk>',shoes_delete_picture, name='shoes_delete_picture'),
    path('favorite_shoes_delete_picture/<int:pk>',favorite_shoes_delete_picture, name='favorite_shoes_delete_picture'), 
    path('create_shoes_coordinate/<int:pk>',create_shoes_coordinate, name='create_shoes_coordinate'),      
    path('add_favorite_shoes<int:pk>/',add_favorite_shoes_view, name='add_favorite_shoes'),
    path('add_shoes_coordinate/<int:shoes_id>/<int:coordinate_id>',add_shoes_coordinate, name='add_shoes_coordinate'),         
    path('create_favorite_shoes_coordinate/<int:pk>',create_favorite_shoes_coordinate, name='create_favorite_shoes_coordinate'), 
    path('add_favorite_shoes_coordinate/<int:shoes_id>/<int:coordinate_id>',add_favorite_shoes_coordinate, name='add_favorite_shoes_coordinate'),         
    path('coordinate_list/',CoordinateListView.as_view() , name='coordinate_list'),
    path('coordinate/<int:pk>/delete/',coordinate_delete , name='coordinate_delete'),
    path('coordinate_form/<int:pk>',CoordinateUpdateView.as_view() , name='coordinate_form'),
   
    # # path('inner_list/', InnerListView.as_view(), name='inner_list'),
    # path('inner_delete_picture/<int:pk>',inner_delete_picture , name='inner_delete_picture'),
   

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)