from django.contrib import admin
from apps.users.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'tel')
    search_fields = ('username', 'email')
    ordering = ('username',)
    list_per_page = 1

admin.site.register(User, UserAdmin)


