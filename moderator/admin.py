from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from moderator.models import User, Moderator
from pages.models import Eslatma, Icon, IjtimoiyTarmoqlar, Manzili, MaqolaJoylash, Narxlar


@admin.register(User)
class MainUserAdmin(UserAdmin):
    fieldsets = (
        ("Avtorizatsiya", {"fields": ("username", "password")}),
        (_("Shaxsiy ma'lumotlar"), {"fields": ("first_name", "last_name", "email", "image")}),
        (_("Huquqlar"),{"fields": ("is_active","is_staff","is_superuser","groups",),},),
        (_("Muhim vaqtlar"), {"fields": ("last_login", "date_joined")}),
        (_("Qo'shimcha"), {"fields": ("dark_mode",)})
    )
    list_display = ['username', 'last_name', 'first_name', 'email', 'is_active', 'is_staff', 'is_superuser']

@admin.register(Moderator)
class ModeratorAdmin(admin.ModelAdmin):
    list_display = ['user', 'pk', 'role', 'is_created']


@admin.register(Eslatma)
class EslatmaAdmin(admin.ModelAdmin):
    list_display = ['name', 'pk']

@admin.register(Icon)
class IconAdmin(admin.ModelAdmin):
    list_display = ['image', 'pk']

@admin.register(IjtimoiyTarmoqlar)
class IjtimoiyTarmoqlarAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon', 'pk']

@admin.register(Manzili)
class ManziliAdmin(admin.ModelAdmin):
    list_display = ['manzil', 'pk']

@admin.register(MaqolaJoylash)
class MaqolaJoylashAdmin(admin.ModelAdmin):
    list_display = ['name', 'short_name', 'image', 'pk']

@admin.register(Narxlar)
class NarxlarAdmin(admin.ModelAdmin):
    list_display = ['name', 'short_name', 'image', 'pk']