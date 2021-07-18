from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

User = get_user_model()


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'email', 'first_name',
                    'last_name', 'city', 'region', 'is_staff', 'is_mentor')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    list_filter = ('city', 'region', 'is_mentor',
                   'is_staff', 'is_active', 'is_superuser')
    autocomplete_fields = ('city', 'region', 'curator')
    readonly_fields = ('date_joined', 'last_login')

    fieldsets = (
        (_('Логин/пароль'), {
            'fields': ('username', 'password')
        }),
        (_('Персональная информация'), {
            'fields': (('first_name', 'last_name'), 'email',
                       ('city', 'region'), 'is_mentor', 'curator')
        }),
        (_('Права доступа'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups'),
        }),
        (_('Даты последнего входа/регистрации'), {
            'fields': ('last_login', 'date_joined')
        }),
    )

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        disabled_fields = set()
        if not is_superuser:
            disabled_fields |= {
                'is_superuser',
                'user_permissions',
            }
        if (
            not is_superuser
            and obj is not None
            and (obj.is_superuser or obj == request.user)
        ):
            disabled_fields |= {
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
            }
        for f in disabled_fields:
            if f in form.base_fields:
                form.base_fields[f].disabled = True
        return form
