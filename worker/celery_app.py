import os
from celery import Celery
from dotenv import load_dotenv

load_dotenv()

# Create Celery instance
celery_app = Celery(
    'memory_palace_worker',
    broker=os.environ.get('CELERY_BROKER_URL', 'redis://redis:6379/0'),
    backend=os.environ.get('CELERY_RESULT_BACKEND', 'redis://redis:6379/0'),
    include=['tasks.ai_tasks', 'tasks.notification_tasks']
)

# Celery configuration
celery_app.conf.update(
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
    task_track_started=True,
    task_time_limit=30 * 60,  # 30 minutes
    task_soft_time_limit=25 * 60,  # 25 minutes
    worker_prefetch_multiplier=1,
    worker_max_tasks_per_child=1000,
)

# Task routing
celery_app.conf.task_routes = {
    'tasks.ai_tasks.*': {'queue': 'ai_queue'},
    'tasks.notification_tasks.*': {'queue': 'notification_queue'},
}

if __name__ == '__main__':
    celery_app.start()