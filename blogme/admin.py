from django.contrib import admin
from blogme.models import Category,Post,UserProfile

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','created']
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user']

admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(Post,PostAdmin)
admin.site.register(Category,CategoryAdmin)
