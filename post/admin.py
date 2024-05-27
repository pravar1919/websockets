from django.contrib import admin

from .models import Post, LikedPost
# Register your models here.


class LikeInlineAdmin(admin.TabularInline):
    model = Post.like.through


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    fields = ["user", "message"]

    inlines = (LikeInlineAdmin,)


admin.site.register(LikedPost)
