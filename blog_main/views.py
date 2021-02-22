from django.shortcuts import render, redirect
from django.http import HttpResponse
from panel.models import Newsletter
from django.contrib import messages
from datetime import datetime  



def home(request) :

    # for key, value in request.session.items(): 
    #     print('{} => {}'.format(key, value))
    
    # path = request.get_full_path()
    # host = request.get_host()

    # return redirect('/')

    return render(request, 'front/index.html')

def category(request) :

    return render(request, 'front/category.html')



def detail(request) :

    return render(request, 'front/detail.html')



def newsletter(request) :

    if request.method == 'POST' :

        path = request.POST.get('path', '')

        name = request.POST.get('name', '')
        email = request.POST.get('email', '')

        newsletter_all = Newsletter.objects.all()

        # Checking : Email already exists
        for i in newsletter_all :
            if i.email == email :
                msg = "This email is already associated with us !"
                messages.success(request, msg)
                return redirect(path)

        today = datetime.now()
        day = today.day
        month = today.strftime('%B')
        year = today.year
        date = month + " " + str(day) + ", " + str(year)

        newsletter = Newsletter(
            name = name,
            email = email,
            date = date,
        )

        newsletter.save()

        msg = "Great, You have successfully subscribed to our newsletter"
        messages.success(request, msg)

        return redirect(path)

    return redirect('home')












