from django.conf.urls import url, include
from . import views


urlpatterns = [

    url(r"^$", views.home, name="home"),
    url(r"^category/$", views.category, name="category"),
    url(r"^detail/$", views.detail, name="detail"),

]