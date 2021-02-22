from django.conf.urls import url, include
from panel import views


urlpatterns = [

    url(r"^panel/$", views.panel, name="panel"),

    url(r"^panel/blog/list/$", views.blog_list, name="blog_list"),
    url(r"^panel/blog/add/$", views.blog_add, name="blog_add"),
    url(r"^panel/blog/edit/(?P<blog_pk>\d+)/$", views.blog_edit, name="blog_edit"),
    url(r"^panel/blog/delete/(?P<blog_pk>\d+)/$", views.blog_delete, name="blog_delete"),
    url(r"^panel/blog/remove_image/(?P<blog_pk>\d+)/$", views.remove_blog_image, name="remove_blog_image"),
    
    url(r"^panel/filter_og/(?P<sec_pk>\d+)/$", views.blog_filter_og, name="blog_filter_og"),
    url(r"^panel/filter/$", views.blog_filter, name="blog_filter"),

    # blog section
    url(r"^panel/blog_section/$", views.blog_section, name="blog_section"),
    url(r"^panel/blog_section/edit/(?P<blog_sec_pk>\d+)/$", views.blog_section_edit, name="blog_section_edit"),

    # newsletter back
    url(r"^panel/newsletter/list/$", views.newsletter_back, name="newsletter_back"),
    url(r"^panel/newsletter/delete/(?P<news_pk>\d+)/$", views.newsletter_delete, name="newsletter_delete"),

    # instagram
    url(r"^panel/instagram/list/$", views.instagram_list, name="instagram_list"),
    url(r"^panel/instagram/add/$", views.instagram_add, name="instagram_add"),
    url(r"^panel/instagram/delete/(?P<ig_pk>\d+)/$", views.instagram_delete, name="instagram_delete"),

    # author
    url(r"^panel/author-profile/list/$", views.author_list, name="author_list"),
    url(r"^panel/author-profile/add/$", views.author_add, name="author_add"),
    url(r"^panel/author-profile/edit/(?P<auth_pk>\d+)/$", views.author_edit, name="author_edit"),
    url(r"^panel/author-profile/delete/(?P<auth_pk>\d+)/$", views.author_delete, name="author_delete"),


]
