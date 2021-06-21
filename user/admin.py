from django.contrib import admin
from . import models
# Register your models here.

# class RateUserAdmin(admin.TabularInline):
#     model = models.RateUser
#     fields = ['user', 'stars',]

class RateUserAdmin(admin.ModelAdmin):
    # fields = ['user', 'user',]
    list_display = ("user_from", "user_to",)


class ViewUser(admin.ModelAdmin):
    empty_value_display = 'Trống'
    list_display = ("username", "get_full_name", "email", "phone")
    # inlines = [RateUserAdmin,]

admin.site.register(models.MyUser, ViewUser)
admin.site.register(models.RateUser, RateUserAdmin)