from django.shortcuts import render, redirect, HttpResponse
from panel.models import Blog, Blog_Section
from miscellaneous.models import Home_Top_Slider
from django.contrib import messages





def home_top_slider(request) :

    top_slider = Home_Top_Slider.objects.all()

    blog = Blog.objects.all().order_by('-index')

    next_index = top_slider.count() + 1


    send = {
        'top_slider': top_slider,
        'blog': blog,
        'next_index': next_index,
    }

    return render(request, 'back/miscellaneous/home_top_slider.html', send)



def home_top_slider_add(request) :

    if request.method == 'POST' :

        index = request.POST.get('index', '')
        blog_pk = request.POST.get('blog_pk', '')

        try :
            blog = Blog.objects.get(pk=blog_pk)
        except :
            blog = None

        if not blog :

            msg = "Something went wrong, refresh the page and try again!"
            messages.success(request, msg)

            return redirect('home_top_slider')


        top_slider = Home_Top_Slider(index=index, blog=blog)

        top_slider.save()

        msg = "Success, New Top Slider has been added successfully !"
        messages.success(request, msg)

        return redirect('home_top_slider')


def home_top_slider_delete(request, top_slider_pk) :

    try :
        top_slider = Home_Top_Slider.objects.get(pk=top_slider_pk)
    except :
        top_slider = None

    if not top_slider :

        msg = "Failure, Something went wrong. refresh the page and try again."
        messages.success(request, msg)

        return redirect('home_top_slider')

    top_slider.delete()

    msg = "Success, Top Slider has been removed successfully !"
    messages.success(request, msg)

    return redirect('home_top_slider')





