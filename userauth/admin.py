from django.contrib import admin
from .models import UserDetail, Batch


admin.site.register(Batch)



class UserDetailAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'is_teacher','is_student')  # Customize the fields displayed in the list view
    list_filter = ('is_teacher', 'is_student')  # Add filters to the admin list view
    list_per_page = 20  # Set the number of items per page in the admin list view

admin.site.register(UserDetail, UserDetailAdmin)
