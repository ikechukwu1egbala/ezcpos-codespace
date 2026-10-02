from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User,Business,Branch
admin.site.register(User,UserAdmin); admin.site.register(Business); admin.site.register(Branch)
