from django.contrib import admin
from .models import Post, Category, User, Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'title_id')
    list_filter = ('author', 'category')
    ordering = ('title_id',)



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('__str__',)


@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email','first_name', 'last_name')
    search_fields = ('username', 'email')
    ordering = ('username',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'content')
   # list_filter = ('author',)
    #search_fields = ('content',)
    ordering = ('author',)