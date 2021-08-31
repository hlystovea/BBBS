from django.core.mail import send_mail
from django.forms import EmailField
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AdminPasswordChangeForm
from django.conf import settings

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    email = EmailField(required=True)  # TODO blank=False в модели CustomUser

    def save(self, commit=True):
        """Save the new user and send mail to user with login and password"""
        user = super().save(commit=False)
        password = self.cleaned_data['password1']
        email = self.cleaned_data['email']
        login = self.cleaned_data['username']
        user.set_password(password)
        send_mail(
            subject='Логин для BBBS',
            message=(f'Используйте этот логин {login} и '
                     'пароль {password} для входа на сайт'),
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[email]
        )
        if commit:
            user.save()
        return user


class CustomAdminPasswordChangeForm(AdminPasswordChangeForm):

    def save(self, commit=True):
        """Save the new password and send mail to user with the new password"""
        password = self.cleaned_data['password1']
        self.user.set_password(password)
        send_mail(
            subject='Изменение пароля для BBBS',
            message=('Ваш пароль для BBBS был изменён. Используйте новый '
                     f'пароль {password} для входа на сайт'),
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.user.email]
        )
        if commit:
            self.user.save()
        return self.user
