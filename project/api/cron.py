import time

from django.core.mail import send_mail, mail_admins
from django.utils.timezone import now
from django_cron import CronJobBase, Schedule

from .models import Event, Participant


class EventCanceled(CronJobBase):
    RUN_EVERY_MINS = 10
    ALLOW_PARALLEL_RUNS = True
    MIN_NUM_FAILURES = 3
    FAILED_RUNS_CRONJOB_EMAIL_PREFIX = '[BBBS ошибка отправки]:'

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'api.event_canceled'

    def do(self):
        events = Event.objects.filter(canceled=True, end_at__gt=now())
        for event in events:
            mail_admins(
                subject=f'Событие {event.title} отменено.',
                message=f'Событие: {event.title}, запланированное на '
                        f'{event.start_at.strftime("%d.%m.%Y")}, '
                        f'было отменено.\n'
                        f'Контакт: {event.contact} {event.phone_number}',
                fail_silently=True
            )
            participants = Participant.objects.filter(event=event)
            for participant in participants:
                send_mail(
                    subject=f'Событие {event.title} отменено.',
                    message=f'Событие: {event.title}, запланированное на '
                            f'{event.start_at.strftime("%d.%m.%Y")}, '
                            'было отменено.',
                    from_email=None,
                    recipient_list=[participant.participant.email],
                )
                time.sleep(30)
