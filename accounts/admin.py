from django.contrib import admin
from .models import User, UserProfile
from django.contrib.auth.admin import UserAdmin




class CustomUserAdmin(UserAdmin):
    # what all you want to display in the admin
    list_display = ('email', 'first_name', 'last_name', 'username', 'role', 'is_active')
    ordering = ('-date_joined',) # - means descending order, it is a tuple so a ,
    
    # To make password in admin page non editable
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    

# Register your models here.
admin.site.register(User)
admin.site.register(UserProfile)
