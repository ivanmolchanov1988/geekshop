from django.urls import path

#from adminapp.views import index, admin_users_read
from adminapp import views
app_name = 'adminapp'

urlpatterns = [
    path('', views.index, name='index'),
    #path('admin-users-read/', views.admin_users_read, name='admin_users_read'),
    path('admin-users-read/', views.UserListView.as_view(), name='admin_users_read'),
    # path('admin-users-create/', views.admin_users_create, name='admin_users_create'),
    path('admin-users-create/', views.UserCreateView.as_view(), name='admin_users_create'),
    #path('admin-users-update/<int:id>/', views.admin_users_update, name='admin_users_update'),
    path('admin-users-update/<int:pk>/', views.UserUpdateView.as_view(), name='admin_users_update'),
    #path('admin-users-delete/<int:id>/', views.admin_users_delete, name='admin_users_delete'),
    path('admin-users-delete/<int:pk>/', views.UserDeleteView.as_view(), name='admin_users_delete'),

]