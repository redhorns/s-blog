from django.conf.urls import url, include
from miscellaneous import views


urlpatterns = [

    url(r"^panel/home_top_slider/$", views.home_top_slider, name="home_top_slider"),
    url(r"^panel/home_top_slider_add/$", views.home_top_slider_add, name="home_top_slider_add"),
    url(r"^panel/home_top_slider_delete/(?P<top_slider_pk>\d+)/$", views.home_top_slider_delete, name="home_top_slider_delete"),

]
