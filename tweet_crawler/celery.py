import os
#from celery import Celery
#from celery.schedules import crontab
#from tweet_crawler import tweet_functions

# set the default Django settings module for the 'celery' program.
#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cappers_collective.settings')

#app = Celery('cappers_collective', broker='amqp://localhost')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
#app.config_from_object('django.conf:settings')

# Load task modules from all registered Django app configs.
#app.autodiscover_tasks('settings.INSTALLED_APPS')
#app.conf.timezone = 'EST'

#@app.task(bind=True, name="periodic_task_crawl")
#def run(self):
#    tweet_functions.start_crawl()
    
