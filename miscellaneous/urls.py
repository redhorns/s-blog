from django.conf.urls import url, include
from miscellaneous import views


urlpatterns = [

    url(r"^panel/home_top_slider/$", views.home_top_slider, name="home_top_slider"),
    url(r"^panel/home_top_slider_add/$", views.home_top_slider_add, name="home_top_slider_add"),
    url(r"^panel/home_top_slider_delete/(?P<top_slider_pk>\d+)/$", views.home_top_slider_delete, name="home_top_slider_delete"),

    url(r"^panel/home_most_popular/$", views.home_most_popular, name="home_most_popular"),
    url(r"^panel/home_most_popular_add/$", views.home_most_popular_add, name="home_most_popular_add"),
    url(r"^panel/home_most_popular_delete/(?P<most_popular_pk>\d+)/$", views.home_most_popular_delete, name="home_most_popular_delete"),


    # 1
    url(r"^panel/home_intro_1/$", views.home_intro_1, name="home_intro_1"),
    url(r"^panel/home_intro_1_add/$", views.home_intro_1_add, name="home_intro_1_add"),
    url(r"^panel/home_intro_1_delete/(?P<intro_1_pk>\d+)/$", views.home_intro_1_delete, name="home_intro_1_delete"),
    # 2
    url(r"^panel/home_intro_2/$", views.home_intro_2, name="home_intro_2"),
    url(r"^panel/home_intro_2_add/$", views.home_intro_2_add, name="home_intro_2_add"),
    url(r"^panel/home_intro_2_delete/(?P<intro_2_pk>\d+)/$", views.home_intro_2_delete, name="home_intro_2_delete"),
    # 3
    url(r"^panel/home_intro_3/$", views.home_intro_3, name="home_intro_3"),
    url(r"^panel/home_intro_3_add/$", views.home_intro_3_add, name="home_intro_3_add"),
    url(r"^panel/home_intro_3_delete/(?P<intro_3_pk>\d+)/$", views.home_intro_3_delete, name="home_intro_3_delete"),
    # 4
    url(r"^panel/home_intro_4/$", views.home_intro_4, name="home_intro_4"),
    url(r"^panel/home_intro_4_add/$", views.home_intro_4_add, name="home_intro_4_add"),
    url(r"^panel/home_intro_4_delete/(?P<intro_4_pk>\d+)/$", views.home_intro_4_delete, name="home_intro_4_delete"),
    # 5
    url(r"^panel/home_intro_5/$", views.home_intro_5, name="home_intro_5"),
    url(r"^panel/home_intro_5_add/$", views.home_intro_5_add, name="home_intro_5_add"),
    url(r"^panel/home_intro_5_delete/(?P<intro_5_pk>\d+)/$", views.home_intro_5_delete, name="home_intro_5_delete"),


    url(r"^panel/home_boss/$", views.home_boss, name="home_boss"),
    url(r"^panel/home_boss_add/$", views.home_boss_add, name="home_boss_add"),
    url(r"^panel/home_boss_delete/(?P<boss_pk>\d+)/$", views.home_boss_delete, name="home_boss_delete"),



]
