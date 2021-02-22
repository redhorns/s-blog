import os
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.core.files.storage import default_storage
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from panel.models import Blog, Blog_Section
from django.contrib import messages
from datetime import datetime  
from django.utils.text import slugify
import json
from django.views.decorators.csrf import csrf_exempt



############################## Panel #############################

def panel(request) :
    # if not request.user.is_authenticated :
    #     return redirect('mylogin')

    return render(request, 'back/panel.html')



def blog_list(request) :

    blog = Blog.objects.all()

    section = Blog_Section.objects.all()

    return render(request, 'back/blog/blog_list.html', {
        'blog': blog,
        'section': section,
    })



def blog_add(request) :

    if request.method == 'POST' :

        index = request.POST.get('index', '')
        section = request.POST.get('section', '')
        title = request.POST.get('title', '')
        intro = request.GET.get('intro', '')
        detail = request.POST.get('detail', '')
        image_1 = request.FILES.get('image_1', None)
        image_credit = request.POST.get('image_credit', '')

        # special blog
        special_blog = request.POST.get('special_blog', 'False')
        special_image = request.FILES.get('special_image', None)

        read_duration = request.POST.get('read_duration')
        tags = request.POST.get('tags', '')

        # meta
        meta_title = request.POST.get('meta_title', '')
        meta_description = request.POST.get('meta_description', '')


        try:
            section_ = Blog_Section.objects.get(pk=section)
        except Blog_Section.DoesNotExist:
            section_ = None

        if section_ != None :
            
            if special_blog == True  :
                if special_image != None :
                    pass
                elif special_image == None :
                    return HttpResponse("You have to select Affermative and image both if you want to list this blog as special blog under Section Page !")
            elif special_blog == False :
                if special_image != None :
                    return HttpResponse("You have to select Affermative and image both if you want to list this blog as special blog under Section Page !")
                elif special_image == None :
                    pass


            if image_1 != None :
                if str(image_1.content_type).startswith('image'):
                    # in bytes, 350KB
                    if image_1.size < 360000:
                        pass
                    else:
                        return HttpResponse("image size must be under 350KB, i know reader would love HD images but he also will get frustrated on slow page speed. Let's give reader a balanced diet !")
                else :
                    return HttpResponse("file type is not supported, only images are allowed here !")
            
            if special_image != None :
                if str(special_image.content_type).startswith('image'):
                    # in bytes, 350KB
                    if special_image.size < 210000:
                        pass
                    else:
                        return HttpResponse("image size must be under 200KB, i know reader would love HD images but he also will get frustrated on slow page speed. Let's give reader a balanced diet !")
                else :
                    return HttpResponse("file type is not supported, only images are allowed here !")


            today = datetime.now()
            day = today.day
            month = today.strftime('%B')
            year = today.year
            date = month + " " + str(day) + ", " + str(year)

            if read_duration :
                read_duration = read_duration
            elif not read_duration :
                read_duration = None


            blog = Blog(
                index = index,
                section = section_,
                title = title,
                intro = intro,
                detail = detail,
                image_1 = image_1,
                image_credit = image_credit,
                date = date,

                # special blog
                special_blog = special_blog,
                special_image = special_image,

                read_duration = read_duration,
                tags = tags,

                # meta
                meta_title = meta_title,
                meta_description = meta_description,
            )

            blog.save()

            return redirect('blog_list')

        else :

            return HttpResponse("Can not identify the section !")



    section = Blog_Section.objects.all()
    blog_index = Blog.objects.all().count() + 1

    return render(request, 'back/blog/blog_add.html', {
        'section': section,
        'blog_index': blog_index,
    })



def blog_edit(request, blog_pk) :

    if request.method == 'POST' :

        index = request.POST.get('index' '')
        section = request.POST.get('section', '')
        title = request.POST.get('title', '')
        intro = request.POST.get('intro', '')
        detail = request.POST.get('detail', '')
        image_1 = request.FILES.get('image_1', None)

        image_credit = request.POST.get('image_credit')

        # special blog
        special_blog = request.POST.get('special_blog', 'False')
        special_image = request.FILES.get('special_image', None)

        read_duration = request.POST.get('read_duration', None)
        tags = request.POST.get('tags', '')

        # meta
        meta_title = request.POST.get('meta_title', '')
        meta_description = request.POST.get('meta_description', '')

        # date 
        date = request.POST.get('date', '')


        try:
            blog = Blog.objects.get(pk=blog_pk)
        except Blog.DoesNotExist:
            blog = None

        if blog != None :

            try:
                section_ = Blog_Section.objects.get(pk=section)
            except Blog_Section.DoesNotExist:
                section_ = None

            if section != None :

                if special_blog == 'True' and not special_image and not blog.special_image :
                    return HttpResponse("You have to select Affermative and image both if you want to list this blog as special blog under Section Page !")
                elif special_blog == 'True' and not special_image and blog.special_image :
                    pass 
                elif special_blog == 'True' and special_image and not blog.special_image :
                    if str(special_image.content_type).startswith('image'):
                        # in bytes, 200KB
                        if special_image.size < 210000:
                            blog.special_image = special_image
                        else:
                            return HttpResponse("image size must be under 200KB, i know reader would love HD images but he also will get frustrated on slow page speed. Let's give reader a balanced diet !")
                    else :
                        return HttpResponse("file type is not supported, only images are allowed here !")
                elif special_blog == 'True' and special_image and blog.special_image :
                    if str(special_image.content_type).startswith('image'):
                        # in bytes, 200KB
                        if special_image.size < 210000:
                            default_storage.delete(blog.special_image.path)
                            blog.special_image = special_image
                        else:
                            return HttpResponse("image size must be under 200KB, i know reader would love HD images but he also will get frustrated on slow page speed. Let's give reader a balanced diet !")
                    else :
                        return HttpResponse("file type is not supported, only images are allowed here !")

                elif special_blog == 'False' and not special_image and not blog.special_image :
                    pass
                elif special_blog == 'False' and not special_image and blog.special_image :
                    default_storage.delete(blog.special_image.path)
                    blog.special_image = None
                    blog.save()
                elif special_blog == 'False' and special_image and not blog.special_image :
                    pass
                elif special_blog == 'False' and special_image and blog.special_image :
                    default_storage.delete(blog.special_image.path)
                    blog.special_image = None
                    blog.save()
                    

                if image_1 != None :
                    if str(image_1.content_type).startswith('image'):
                        # in bytes, 350KB
                        if image_1.size < 360000:
                            if blog.image_1 :
                                default_storage.delete(blog.image_1.path)
                            blog.image_1 = image_1
                        else:
                            return HttpResponse("image size must be under 350KB, i know reader would love HD images but he also will get frustrated on slow page speed. Let's give reader a balanced diet !")
                    else :
                        return HttpResponse("file type is not supported, only images are allowed here !")


                blog.index = index
                blog.section = section_
                blog.title = title
                blog.intro = intro
                blog.detail = detail
                blog.image_credit = image_credit

                # special blog
                blog.special_blog = special_blog

                if read_duration :
                    blog.read_duration = read_duration
                elif not read_duration:
                    blog.read_duration = None

                blog.tags = tags
                blog.date = date

                # meta
                blog.meta_title = meta_title
                blog.meta_description = meta_description

                blog.save()

                msg = "All the changes made to blog #" + str(slugify(blog.title)) + " has been commited successfully !" 
                messages.success(request, msg)

                return redirect('blog_list')

            else :

                return HttpResponse("Section object not found !")

        else :

            return HttpResponse("Blog object not found !")




    try:
        blog = Blog.objects.get(pk=blog_pk)
    except Blog.DoesNotExist:
        blog = None

    if blog != None :

        section = Blog_Section.objects.all().exclude(pk=blog.section.pk)

        return render(request, 'back/blog/blog_edit.html', {
            'section': section,
            'blog': blog,
        })

    else :

        return HttpResponse('Blog object not found while editing ! ')



def blog_delete(request, blog_pk) :

    try:
        blog = Blog.objects.get(pk=blog_pk)
    except Blog.DoesNotExist:
        blog = None

    if blog != None :

        blog.delete()

        msg = "Article #" + slugify(blog.title) + " has been deleted !" 
        messages.success(request, msg)

        return redirect('blog_list')

    else :
        return HttpResponse("Blog object not found ! ")



def remove_blog_image(request, blog_pk) :

    try:
        blog = Blog.objects.get(pk=blog_pk)
    except Blog.DoesNotExist:
        blog = None

    if blog != None :

        if blog.special_image :

            default_storage.delete(blog.special_image.path)
            blog.special_image = None
            blog.save()

            return redirect('blog_edit', blog_pk)

        else :
            return HttpResponse("Blog has no special image associated with it !")

    else :
        return HttpResponse("Blog object not found !")



@csrf_exempt 
def blog_filter(request):
    # request.is_ajax() also can be used with post checking to confirm its ajax req
    if request.method == 'POST' : 
        if request.method == 'POST':
            name = request.POST.get('data')

            print("====success=====", name)

            return render(request, 'back/panel.html')

            # return JsonResponse({
            #     'name': 'success baby!!!'
            # })

            # return HttpResponse(json.dumps(name), content_type="application/json")
        else :
            return render('ajax_test.html', locals())


    return render(request, 'back/temp.html')

    # # blog_section = Blog_Section.objects.get(pk=section_pk)

    # # blog = Blog.objects.filter(section=blog_section)

    # # section = Blog_Section.objects.all()

    # return render(request, 'back/blog_filter.html', {
    #     # 'blog': blog,
    #     # 'section': section,
    # })



def blog_section(request) :

    if request.method == 'POST' :

        index = request.POST.get('index', None)
        section_name = request.POST.get('section_name', '')
        section_info = request.POST.get('section_info', '')
        # image
        image_1 = request.FILES.get('image_1', None)
        image_2 = request.FILES.get('image_2', None)
        # meta
        meta_title = request.POST.get('meta_title', '')
        meta_description = request.POST.get('meta_description', '')


        section = Blog_Section.objects.all()

        for sc in section :
            if sc.section_name == section_name :
                return HttpResponse('Two section can not have same name, it will create confusion in long run. If you still want to keep it same then use numarator to uniquely identify each ! ')

        if image_1 != None :
            if str(image_1.content_type).startswith('image'):
                # in bytes, 350KB
                if image_1.size < 360000:
                    pass
                else:
                    return HttpResponse("image size must be under 350KB, i know user would love HD images but he also will get frustrated on slow page speed. Let's give user a balanced diet !")
            else :
                return HttpResponse("file type is not supported, only images are allowed here !")

        if image_2 != None :
            if str(image_2.content_type).startswith('image'):
                # in bytes, 350KB
                if image_2.size < 360000:
                    pass
                else:
                    return HttpResponse("image size must be under 350KB, i know user would love HD images but he also will get frustrated on slow page speed. Let's give user a balanced diet !")
            else :
                return HttpResponse("file type is not supported, only images are allowed here !")


        obj = Blog_Section(

            index=index, 
            section_name=section_name, 
            section_info=section_info, 
            image_1=image_1,
            image_2=image_2,
            meta_title=meta_title, 
            meta_description=meta_description,

        )

        obj.save()

        msg = "New section has been added successfully !"
        messages.success(request, msg)

        return redirect('blog_section')



    section = Blog_Section.objects.all()

    section_index = section.count() + 1



    return render(request, 'back/blog/blog_section.html', {
        'section': section,
        'section_index': section_index,
    })



def blog_section_edit(request, blog_sec_pk) :

    if request.method == 'POST' :
        
        try :
            obj = Blog_Section.objects.get(pk=blog_sec_pk)
        except :
            obj = None
         
        if obj :

            index = request.POST.get('index', None)
            section_name = request.POST.get('section_name', '')
            section_info = request.POST.get('section_info', '')
            # image
            image_1 = request.FILES.get('image_1', None)
            image_2 = request.FILES.get('image_2', None)
            # meta
            meta_title = request.POST.get('meta_title', '')
            meta_description = request.POST.get('meta_description', '')

            section = Blog_Section.objects.all().exclude(pk=blog_sec_pk)

            for sc in section :
                if sc :
                    if sc.section_name == section_name :
                        return HttpResponse('Two section can not have same name, it will create confusion in long run. If you still want to keep it same then use numarator to uniquely identify each ! ')

            if image_1 != None :
                if str(image_1.content_type).startswith('image'):
                    # in bytes, 350KB
                    if image_1.size < 360000:
                        if obj.image_1 :
                            default_storage.delete(obj.image_1.path)
                        obj.image_1 = image_1
                    else:
                        return HttpResponse("image size must be under 350KB, i know user would love HD images but he also will get frustrated on slow page speed. Let's give user a balanced diet !")
                else :
                    return HttpResponse("file type is not supported, only images are allowed here !")
                            
            if image_2 != None :                
                if str(image_2.content_type).startswith('image'):
                    # in bytes, 350KB
                    if image_2.size < 360000:
                        if obj.image_2 :
                            default_storage.delete(obj.image_2.path)
                        obj.image_2 = image_2
                    else:
                        return HttpResponse("image size must be under 350KB, i know user would love HD images but he also will get frustrated on slow page speed. Let's give user a balanced diet !")
                else :
                    return HttpResponse("file type is not supported, only images are allowed here !")

            obj.index = index
            obj.section_name = section_name
            obj.section_info = section_info
            obj.meta_title = meta_title
            obj.meta_description = meta_description

            obj.save()

            msg = "Updated made to section object are commited successfully !"
            messages.success(request, msg)

            return redirect('blog_section')

        else :
            return HttpResponse("Section object not found, try going back and refreshing the page again !")

    try :
        section = Blog_Section.objects.get(pk=blog_sec_pk)
    except :
        section = None

    if section :

        return render(request, 'back/blog/blog_section_edit.html', {
            'section': section,
        })
    
    else :
        return HttpResponse("Section Object not found, try going back and refreshing the feed again !")



# def blog_section_delete(request, page_name_w) :

#     # Controlling User Access to Control Panel
#     if not request.user.is_authenticated :
#         return redirect('mylogin')

#     obj = Page_Handler.objects.get(page_name=page_name_w)
#     obj.delete()

#     return redirect('page_handler')



