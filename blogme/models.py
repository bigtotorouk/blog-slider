from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=30)
    
    def __unicode__(self):
        # show when you post a post in admin-html
        return unicode(self.name)

class Post(models.Model):
    # Article and Comment
    creator = models.ForeignKey(User)
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True, auto_now=True, blank=True, null=True)

    def get_absolute_url(self):
        return "/blog/post/%i/" % self.id
    def __unicode__(self):
        return unicode(self.title)

class UserProfile(models.Model):
    """docstring"""
    avatar = models.ImageField("Profile Pic",upload_to="images/",blank=True,null=True)
    signature = models.CharField(blank=True,max_length=200)
    user = models.OneToOneField(User)


    def __unicode__(self):
        return unicode(self.user)

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=User)
