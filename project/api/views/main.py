from django.db.models import Count, Exists, F, OuterRef
from django.utils.timezone import now
from rest_framework.generics import RetrieveAPIView, get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from ..models import City, Event, Main
from ..serializers.main import MainSerializer


def get_events(request):
    user = request.user
    if user.is_authenticated:
        city = user.city
    else:
        city = get_object_or_404(City, id=request.GET.get('city'))
    queryset = Event.objects.filter(end_at__gt=now(), city=city) \
                    .annotate(remain_seats=F('seats') - Count('participants'))
    if user.is_authenticated:
        booked = Event.objects.filter(pk=OuterRef('pk'), participants=user)
        queryset = queryset.annotate(booked=Exists(booked))
    return queryset


class MainViewSet(RetrieveAPIView):
    queryset = Main.objects.all()
    serializer_class = MainSerializer
    permission_classes = [AllowAny]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_queryset().last()
        if instance:
            instance.events = get_events(request)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
