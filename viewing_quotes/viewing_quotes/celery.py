import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'viewing_quotes.settings')

app = Celery('viewing_quotes')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'every-10-second': {
        'task': 'app.tasks.update_data',
        'schedule': 10.0,
    },
}
app.conf.timezone = 'UTC'