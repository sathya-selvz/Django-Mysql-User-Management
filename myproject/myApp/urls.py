from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_user_details, name='home'),
    path('enter_details/', views.get_user_details, name='enter_user_details'),
    path('display_data/', views.display_user_data, name='display_user_data'),
    path('edit/<int:user_id>/', views.edit_user, name='edit_user'),
    path('delete/<int:user_id>/', views.delete_user, name='delete_user'),

]