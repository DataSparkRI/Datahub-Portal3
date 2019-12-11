web: gunicorn Datahub_Portal.wsgi
worker: celery -A Datahub_Portal worker --loglevel=INFO
camera: celery -A Datahub_Portal events -l info --camera django_celery_monitor.camera.Camera --frequency=2.0
