from django.conf.urls import url, include
from authenticate import views


urlpatterns = [

    url(r"^authentication/register/$", views.myregister, name="myregister"),
    url(r"^authentication/login/$", views.mylogin, name="mylogin"),
    url(r"^authentication/logout/$", views.mylogout, name="mylogout"),

    url(r"^authentication/admin/login/$", views.admin_login, name="admin_login"),
    url(r"^authentication/admin/logout/$", views.admin_logout, name="admin_logout"),


]
