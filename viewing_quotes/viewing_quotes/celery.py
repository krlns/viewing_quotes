import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'viewing_quotes.settings')

app = Celery('viewing_quotes')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
