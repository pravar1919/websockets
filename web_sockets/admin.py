from django.contrib import admin

from django.contrib.auth.models import User
# Register your models here.

# admin.site.unregister(User)

from .models import User, Friends
admin.site.register(User)
admin.site.register(Friends)
