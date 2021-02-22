from django.db import models
from panel.models import Blog



class Home_Top_Slider(models.Model) :

    index = models.IntegerField(null=True, blank=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        if self.blog :
            return str(self.index) + self.blog.title
        else :
            return self.index

class Home_Most_Popular(models.Model) :

    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        if self.blog :
            return self.blog.title
        else :
            return None


# Home Intro

class Home_Intro_1(models.Model) :

    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        if self.blog :
            return self.blog.title
        else :
            return None

class Home_Intro_2(models.Model) :

    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        if self.blog :
            return self.blog.title
        else :
            return None


class Home_Intro_3(models.Model) :

    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        if self.blog :
            return self.blog.title
        else :
            return None


class Home_Intro_4(models.Model) :

    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        if self.blog :
            return self.blog.title
        else :
            return None


class Home_Intro_5(models.Model) :

    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        if self.blog :
            return self.blog.title
        else :
            return None


# Boss Post

class Home_Boss(models.Model) :

    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        if self.blog :
            return self.blog.title
        else :
            return None


