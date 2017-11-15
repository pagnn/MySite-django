from django.conf.urls import url,include
from .views import user_login,register
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'login/$',user_login,name='user_login'),
    url(r'logout/$',auth_views.logout,{'template_name':'account/logout.html'},name='user_logout'),
    url(r'register/$',register,name='register'),
]
