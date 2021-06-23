from django.contrib import admin
from .models import Report, TextReport, Follow

# Register your models here.

admin.site.register(Report)
admin.site.register(TextReport)
admin.site.register(Follow)
