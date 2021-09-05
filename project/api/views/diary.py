from django.conf import settings
from django.core.mail import send_mail
from django.utils.translation import gettext_lazy as _
from requests.exceptions import RequestException
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

from ..models import Diary
from ..permissions import IsOwner
from ..serializers import DiarySerializer, EmailSerializer


class DiaryViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    serializer_class = DiarySerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        return Diary.objects.filter(mentor=self.request.user).order_by('-date')

    def perform_create(self, serializer):
        serializer.save(mentor=self.request.user)

    @action(methods=['post'], detail=True)
    def send(self, request, pk=None):
        mentor = request.user
        diary = get_object_or_404(Diary, pk=pk, mentor=mentor)
        if not diary.sent_to_curator:
            email = mentor.curator.email
            serializer = EmailSerializer(data={'email': email})
            if serializer.is_valid(raise_exception=True):
                try:
                    send_mail(
                        subject=settings.SEND_DIARY_TO_CURATOR_SUBJECT % (
                            mentor,
                            diary.date.isoformat()
                        ),
                        message=diary.description,
                        from_email=None,
                        recipient_list=[email],
                    )
                except RequestException:
                    message = {
                        'diary': _('Проблемы с отправкой, попробуйте позднее.')
                    }
                    return Response(
                        message,
                        status=status.HTTP_504_GATEWAY_TIMEOUT
                    )
                diary.sent_to_curator = True
                diary.save()
                message = {'diary': _('Запись дневника отправлена куратору.')}
                return Response(message, status=status.HTTP_200_OK)
        message = {
            'diary': _('Запись дневника уже была отправлена куратору ранее.')
        }
        return Response(message, status=status.HTTP_200_OK)
