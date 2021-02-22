from django.shortcuts import render, redirect, HttpResponse
from panel.models import Blog, Blog_Section
from miscellaneous.models import Home_Top_Slider, Home_Most_Popular, Home_Intro_1,Home_Intro_2, Home_Intro_3, Home_Intro_4, Home_Intro_5, Home_Boss
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



def home_most_popular(request) :

    most_popular = Home_Most_Popular.objects.all()

    blog = Blog.objects.all().order_by('-index')

    send = {
        'most_popular': most_popular,
        'blog': blog,
    }

    return render(request, 'back/miscellaneous/home_most_popular.html', send)



def home_most_popular_add(request) :

    if request.method == 'POST' :

        blog_pk = request.POST.get('blog_pk', '')

        try :
            blog = Blog.objects.get(pk=blog_pk)
        except :
            blog = None

        if not blog :

            msg = "Something went wrong, refresh the page and try again!"
            messages.success(request, msg)

            return redirect('home_most_popular')


        most_popular = Home_Most_Popular(blog=blog)

        most_popular.save()


        # remove prev on addition of 4th post
        most_popular_all = Home_Most_Popular.objects.all()

        if most_popular_all.count() > 4 :
            first = most_popular_all.first()
            first.delete()

        msg = "Success, New Most Popular post has been added successfully !"
        messages.success(request, msg)

        return redirect('home_most_popular')



def home_most_popular_delete(request, most_popular_pk) :

    try :
        most_popular = Home_Most_Popular.objects.get(pk=most_popular_pk)
    except :
        most_popular = None

    if not most_popular :

        msg = "Failure, Something went wrong. refresh the page and try again."
        messages.success(request, msg)

        return redirect('home_most_popular')

    most_popular.delete()

    msg = "Success,New Most Popular post has been removed successfully !"
    messages.success(request, msg)

    return redirect('home_most_popular')


# < -------------------------------   1111   ----------------------------- >

def home_intro_1(request) :

    intro_1 = Home_Intro_1.objects.all()

    blog = Blog.objects.all().order_by('-index')

    send = {
        'intro_1': intro_1,
        'blog': blog,
    }

    return render(request, 'back/miscellaneous/home_intro_1.html', send)


def home_intro_1_add(request) :
    
    if request.method == 'POST' :

        blog_pk = request.POST.get('blog_pk', '')

        try :
            blog = Blog.objects.get(pk=blog_pk)
        except :
            blog = None

        if not blog :

            msg = "Something went wrong, refresh the page and try again!"
            messages.success(request, msg)

            return redirect('home_intro_1')


        intro_1 = Home_Intro_1(blog=blog)

        intro_1.save()


        # remove prev on addition of 3rd post
        intro_1_all = Home_Intro_1.objects.all()

        if intro_1_all.count() > 1 :
            first = intro_1_all.first()
            first.delete()

        msg = "Success, New post has been added to Main Container successfully !"
        messages.success(request, msg)


    return redirect('home_intro_1')


def home_intro_1_delete(request, intro_1_pk) :

    try :
        intro_1 = Home_Intro_1.objects.get(pk=intro_1_pk)
    except :
        intro_1 = None

    if not intro_1 :

        msg = "Failure, Something went wrong. refresh the page and try again."
        messages.success(request, msg)

        return redirect('home_intro')

    intro_1.delete()

    msg = "Success,New post has been removed from Main Container successfully !"
    messages.success(request, msg)

    return redirect('home_intro_1')


# < -------------------------------   2222   ----------------------------- >

def home_intro_2(request) :

    intro_2 = Home_Intro_2.objects.all()

    blog = Blog.objects.all().order_by('-index')

    send = {
        'intro_2': intro_2,
        'blog': blog,
    }

    return render(request, 'back/miscellaneous/home_intro_2.html', send)


def home_intro_2_add(request) :
    
    if request.method == 'POST' :

        blog_pk = request.POST.get('blog_pk', '')

        try :
            blog = Blog.objects.get(pk=blog_pk)
        except :
            blog = None

        if not blog :

            msg = "Something went wrong, refresh the page and try again!"
            messages.success(request, msg)

            return redirect('home_intro_2')


        intro_2 = Home_Intro_2(blog=blog)

        intro_2.save()


        # remove prev on addition of 4th post
        intro_2_all = Home_Intro_2.objects.all()

        if intro_2_all.count() > 2 :
            first = intro_2_all.first()
            first.delete()

        msg = "Success, New post has been added to Top Left Container successfully !"
        messages.success(request, msg)


    return redirect('home_intro_2')


def home_intro_2_delete(request, intro_2_pk) :

    try :
        intro_2 = Home_Intro_2.objects.get(pk=intro_2_pk)
    except :
        intro_2 = None

    if not intro_2 :

        msg = "Failure, Something went wrong. refresh the page and try again."
        messages.success(request, msg)

        return redirect('home_intro_2')

    intro_2.delete()

    msg = "Success,New post has been removed from Top Left Container successfully !"
    messages.success(request, msg)

    return redirect('home_intro_2')


# < -------------------------------   3333   ----------------------------- >

def home_intro_3(request) :

    intro_3 = Home_Intro_3.objects.all()

    blog = Blog.objects.all().order_by('-index')

    send = {
        'intro_3': intro_3,
        'blog': blog,
    }

    return render(request, 'back/miscellaneous/home_intro_3.html', send)


def home_intro_3_add(request) :
    
    if request.method == 'POST' :

        blog_pk = request.POST.get('blog_pk', '')

        try :
            blog = Blog.objects.get(pk=blog_pk)
        except :
            blog = None

        if not blog :

            msg = "Something went wrong, refresh the page and try again!"
            messages.success(request, msg)

            return redirect('home_intro_3')


        intro_3 = Home_Intro_3(blog=blog)

        intro_3.save()


        # remove prev on addition of 3rd post
        intro_3_all = Home_Intro_3.objects.all()

        if intro_3_all.count() > 2 :
            first = intro_3_all.first()
            first.delete()

        msg = "Success, New post has been added to Top Right Container successfully !"
        messages.success(request, msg)


    return redirect('home_intro_3')


def home_intro_3_delete(request, intro_3_pk) :

    try :
        intro_3 = Home_Intro_3.objects.get(pk=intro_3_pk)
    except :
        intro_3 = None

    if not intro_3 :

        msg = "Failure, Something went wrong. refresh the page and try again."
        messages.success(request, msg)

        return redirect('home_intro_3')

    intro_3.delete()

    msg = "Success,New post has been removed from Top Right Container successfully !"
    messages.success(request, msg)

    return redirect('home_intro_3')


# < -------------------------------   4444   ----------------------------- >

def home_intro_4(request) :

    intro_4 = Home_Intro_4.objects.all()

    blog = Blog.objects.all().order_by('-index')

    send = {
        'intro_4': intro_4,
        'blog': blog,
    }

    return render(request, 'back/miscellaneous/home_intro_4.html', send)


def home_intro_4_add(request) :
    
    if request.method == 'POST' :

        blog_pk = request.POST.get('blog_pk', '')

        try :
            blog = Blog.objects.get(pk=blog_pk)
        except :
            blog = None

        if not blog :

            msg = "Something went wrong, refresh the page and try again!"
            messages.success(request, msg)

            return redirect('home_intro_4')


        intro_4 = Home_Intro_4(blog=blog)

        intro_4.save()


        # remove prev on addition of 3rd post
        intro_4_all = Home_Intro_4.objects.all()

        if intro_4_all.count() > 2 :
            first = intro_4_all.first()
            first.delete()

        msg = "Success, New post has been added to Bottom Left Container successfully !"
        messages.success(request, msg)


    return redirect('home_intro_4')


def home_intro_4_delete(request, intro_4_pk) :

    try :
        intro_4 = Home_Intro_4.objects.get(pk=intro_4_pk)
    except :
        intro_4 = None

    if not intro_4 :

        msg = "Failure, Something went wrong. refresh the page and try again."
        messages.success(request, msg)

        return redirect('home_intro_4')

    intro_4.delete()

    msg = "Success,New post has been removed from Bottom Left Container successfully !"
    messages.success(request, msg)

    return redirect('home_intro_4')


# < -------------------------------   5555   ----------------------------- >

def home_intro_5(request) :

    intro_5 = Home_Intro_5.objects.all()

    blog = Blog.objects.all().order_by('-index')

    send = {
        'intro_5': intro_5,
        'blog': blog,
    }

    return render(request, 'back/miscellaneous/home_intro_5.html', send)


def home_intro_5_add(request) :
    
    if request.method == 'POST' :

        blog_pk = request.POST.get('blog_pk', '')

        try :
            blog = Blog.objects.get(pk=blog_pk)
        except :
            blog = None

        if not blog :

            msg = "Something went wrong, refresh the page and try again!"
            messages.success(request, msg)

            return redirect('home_intro_5')


        intro_5 = Home_Intro_5(blog=blog)

        intro_5.save()


        # remove prev on addition of 3rd post
        intro_5_all = Home_Intro_5.objects.all()

        if intro_5_all.count() > 2 :
            first = intro_5_all.first()
            first.delete()

        msg = "Success, New post has been added to Bottom Right Container successfully !"
        messages.success(request, msg)


    return redirect('home_intro_5')


def home_intro_5_delete(request, intro_5_pk) :

    try :
        intro_5 = Home_Intro_5.objects.get(pk=intro_5_pk)
    except :
        intro_5 = None

    if not intro_5 :

        msg = "Failure, Something went wrong. refresh the page and try again."
        messages.success(request, msg)

        return redirect('home_intro_5')

    intro_5.delete()

    msg = "Success,New post has been removed from Bottom Right Container successfully !"
    messages.success(request, msg)

    return redirect('home_intro_5')






def home_boss(request) :

    boss = Home_Boss.objects.all()

    for i in boss :
        print("======")

    blog = Blog.objects.all().order_by('-index')

    send = {
        'boss': boss,
        'blog': blog,
    }

    return render(request, 'back/miscellaneous/home_boss.html', send)



def home_boss_add(request) :

    if request.method == 'POST' :

        blog_pk = request.POST.get('blog_pk', '')

        try :
            blog = Blog.objects.get(pk=blog_pk)
        except :
            blog = None

        if not blog :

            msg = "Something went wrong, refresh the page and try again!"
            messages.success(request, msg)

            return redirect('home_boss')


        home_boss = Home_Boss(blog=blog)

        home_boss.save()


        # remove prev on addition of 3rd post
        home_boss_all = Home_Boss.objects.all()

        if home_boss_all.count() > 1 :
            first = home_boss_all.first()
            first.delete()

        msg = "Success, Boss Post has been updated successfully !"
        messages.success(request, msg)


    return redirect('home_boss')



def home_boss_delete(request, boss_pk) :

    try :
        home_boss = Home_Boss.objects.get(pk=boss_pk)
    except :
        home_boss = None

    if not home_boss :

        msg = "Failure, Something went wrong. refresh the page and try again."
        messages.success(request, msg)

        return redirect('home_boss')

    home_boss.delete()

    msg = "Success, Boss Post has been deleted successfully !"
    messages.success(request, msg)

    return redirect('home_boss')




