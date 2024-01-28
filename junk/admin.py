from django.contrib import admin

from .models import Course, Group, Loop, Person, Day

admin.site.register(Course)
admin.site.register(Group)
admin.site.register(Person)
admin.site.register(Loop)

class DayLoopAdminInline(admin.TabularInline):
    model = Loop
    extra = 1

@admin.register(Day)
class DayAdmin(admin.ModelAdmin):
    inlines = (DayLoopAdminInline,)
