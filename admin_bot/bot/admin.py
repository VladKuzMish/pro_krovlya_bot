from django.contrib import admin
from .models import User, WorkDay, Object


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'chat_id', 'rate')


@admin.register(WorkDay)
class WorkDayAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'start_work', 'end_work', 'lunch', 'work_time', 'salary_per_day')


@admin.register(Object)
class ObjectAdmin(admin.ModelAdmin):
    list_display = ('name', )
