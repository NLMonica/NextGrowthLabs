from django.urls import path

from . import views


urlpatterns = [
    #path("", views.index, name="index"),
    path('administrator/admin_login/', views.admin_login, name='admin_login'),
    path('administrator/push_data/', views.push_data, name='push_data'),
    path('administrator/',views.admin_home, name='admin_home'),
    path('administrator/admin_signup/', views.admin_signup, name='admin_signup'),
    path('administrator/admin_logout/', views.admin_logout, name='admin_logout'),
    path('user/user_login/', views.user_login, name='user_login'),
    path('user/user_signup/', views.user_signup, name='user_signup'),
    path('user/user_logout/', views.user_logout, name='user_logout'),
    path("user/", views.render_data,name='user_home'),
]