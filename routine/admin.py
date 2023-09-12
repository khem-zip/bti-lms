from django.contrib import admin
from .models import Routine, RoutineDetail

class RoutineDetailInline(admin.TabularInline):  # or admin.StackedInline for a different display style
    model = RoutineDetail
    extra = 1  # Number of empty forms to display for adding new RoutineDetail objects
    
class RoutineAdmin(admin.ModelAdmin):
    inlines = [RoutineDetailInline]

admin.site.register(Routine, RoutineAdmin)
