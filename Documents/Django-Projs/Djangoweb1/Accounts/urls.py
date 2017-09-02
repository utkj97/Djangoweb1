from django.contrib.auth import views as auth_views
from django.conf.urls import url
from . import views
app_name='Accounts'

urlpatterns = [
        url(r'^login/$',auth_views.login,{'template_name':'registration/login.html'},name = 'login'),
        url(r'^register/$',views.UserFormView.as_view(),name = 'register')
]

