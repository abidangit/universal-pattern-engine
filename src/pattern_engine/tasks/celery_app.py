from celery import Celery

celery_app = Celery('upe', broker='redis://localhost:6379/0')

@celery_app.task
def add(x, y):
    return x + y
