from django.urls import path
from . import views

urlpatterns = [
    path('landingpage', views.home_page_view, name='landingpage'),
    path('add', views.add_user_view, name='add'),
    path('save', views.save_user_view, name='save'),
    path('all',views.get_all_users,name='all'),
    path('delete/<int:user_id>/',views.delete_user_view,name='deleteuser'),
    path('update/<int:user_id>/',views.get_user_info,name ='getuser'),
    path('update_user/<int:user_id>/',views.update_user,name ='updateuser'),
]