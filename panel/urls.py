from django.conf.urls import url, include
from panel import views


urlpatterns = [

    url(r"^panel/$", views.panel, name="panel"),

    url(r"^panel/blog/list/$", views.blog_list, name="blog_list"),
    url(r"^panel/blog/add/$", views.blog_add, name="blog_add"),
    url(r"^panel/blog/edit/(?P<blog_pk>\d+)/$", views.blog_edit, name="blog_edit"),
    url(r"^panel/blog/delete/(?P<blog_pk>\d+)/$", views.blog_delete, name="blog_delete"),
    url(r"^panel/blog/remove_image/(?P<blog_pk>\d+)/$", views.remove_blog_image, name="remove_blog_image"),
    
    url(r"^panel/filter/$", views.blog_filter, name="blog_filter"),


    url(r"^panel/blog_section/$", views.blog_section, name="blog_section"),
    url(r"^panel/blog_section/edit/(?P<blog_sec_pk>\d+)/$", views.blog_section_edit, name="blog_section_edit"),

]
