from django.contrib import admin
from base.models import User, Post

class AllUsersAdmin(admin.ModelAdmin):
    list_display = ('pk', 'first_name', 'last_name', 'username', 'password', 'email', 'is_active', 'date_joined', 'adress')
    # list_editable = ("pa",)

class AllPostsAdmin(admin.ModelAdmin):
    list_display = ('content', 'title', 'image', 'author', 'date_created')

admin.site.register(User, AllUsersAdmin)
admin.site.register(Post, AllPostsAdmin)
