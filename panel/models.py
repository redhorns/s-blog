from __future__ import unicode_literals
from django.db import models
from ckeditor.fields import RichTextField

# for deletion of the attachments after deletion of object
from django.db.models.signals import post_delete
from django.dispatch import receiver

# auto populate the slug-field
from django.utils.text import slugify


class Blog_Section(models.Model) :

    index = models.IntegerField(default=0, null=True, blank=True)
    section_name = models.CharField(max_length=100, null=True, blank=True)
    section_slug = models.CharField(max_length=100, null=True, blank=True)
    section_info = models.TextField(null=True, blank=True)

    # section banner-icons
    image_1 = models.ImageField(upload_to="blog_section", null=True, blank=True)
    image_2 = models.ImageField(upload_to="blog_section", null=True, blank=True)

    # meta
    meta_title = models.CharField(max_length=250, null=True, blank=True)
    meta_description = models.TextField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.section_slug = slugify(self.section_name)
        super(Blog_Section, self).save(*args, **kwargs)

    def __str__(self) : 

        return str(self.index) + " | " + self.section_name + '(' + str(self.pk ) + ')'   


@receiver(post_delete, sender=Blog_Section)
def submission_delete(sender, instance, **kwargs) :
    instance.image_1.delete(False)
    instance.image_2.delete(False)




class Blog(models.Model) :

    index = models.IntegerField(null=True, blank=True)
    section = models.ForeignKey(Blog_Section, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=300, null=True, blank=True)
    intro = models.TextField(null=True, blank=True)
    detail = RichTextField(null=True, blank=True)
    image_1 = models.ImageField(upload_to="blog_images", null=True, blank=True)
    image_credit = models.TextField(null=True, blank=True)
    special_blog = models.BooleanField(default=False, null=True, blank=True)
    special_image = models.ImageField(upload_to="blog_images", null=True, blank=True)
    date = models.CharField(max_length=100, null=True, blank=True)
    read_duration = models.IntegerField(null=True, blank=True)
    tags = models.TextField(null=True, blank=True)

    # meta
    meta_title = models.CharField(max_length=300, null=True, blank=True)
    meta_description = models.TextField(null=True, blank=True)


    def __str__(self) :
        if self.section :
            return str(self.index) + " | " + self.title + " ( " + self.section.section_name + " )"
        else :
            return str(self.index) + " | " + self.title + " ( None )"


@receiver(post_delete, sender=Blog)
def submission_delete1(sender, instance, **kwargs) :
    instance.image_1.delete(False)
    instance.special_image.delete(False)




class Newsletter(models.Model) :

    name = models.TextField(null=True, blank=True)
    email = models.TextField(null=True, blank=True)
    date = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self) :
        return self.email



class Instagram_Pic(models.Model) :

    image1 = models.ImageField(upload_to="instagram", null=True, blank=True)

    def __str__(self) :
        return self.pk
    
@receiver(post_delete, sender=Instagram_Pic)
def submission_delete2(sender, instance, **kwargs) :
    instance.image1.delete(False)



class Author(models.Model) :

    name = models.TextField(null=True, blank=True)
    intro = models.TextField(null=True, blank=True)
    detail = models.TextField(null=True, blank=True)
    image1 = models.ImageField(upload_to='author', null=True, blank=True)
    image2 = models.ImageField(upload_to='author', null=True, blank=True)

    def __str__(self) :
        return "Author Profile " + str(self.pk)

@receiver(post_delete, sender=Author)
def submission_delete3(sender, instance, **kwargs) :
    instance.image1.delete(False)
    instance.image2.delete(False)


class Author_SM(models.Model) :

    fk = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, blank=True)
    sm_name = models.CharField(max_length=150, null=True, blank=True)
    sm_icon = models.CharField(max_length=150, null=True, blank=True)
    sm_url  = models.TextField(null=True, blank=True)

    def __str__(self) :
        return self.sm_name


