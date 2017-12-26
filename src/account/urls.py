from django.conf.urls import url,include
from .views import user_login,register
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'login/$',user_login,name='user_login'),
    url(r'logout/$',auth_views.logout,{'template_name':'account/logout.html'},name='user_logout'),
    url(r'register/$',register,name='register'),
    url(r'password-change/$',auth_views.password_change,{'template_name':'account/password_change.html'},name='password_change'),
    url(r'password-change-done/$',auth_views.password_change_done,{'template_name':'account/password_change_done.html'},name='password_change_done')
]
