from django.conf import settings
import importlib

celery_module = getattr(settings, 'CELERY_INIT_MODULE', 'mailster.celery')
celery_app = importlib.import_module(celery_module).app