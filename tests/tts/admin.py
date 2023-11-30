from django.contrib import admin
from .models import Prepod, JobHistory

class JobHistoryInline(admin.TabularInline):
    model = JobHistory
    extra = 0

class PrepodAdmin(admin.ModelAdmin):
    inlines = [JobHistoryInline]

admin.site.register(Prepod, PrepodAdmin)