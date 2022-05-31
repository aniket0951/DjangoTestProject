import logging

logger = logging.getLogger("django")

from django_crontab import crontab

def my_scheduled_job():
    print("scheduler run")
    logger.debug("Logger called from scheduler")

def TestFunction():
    print("logger get called from test function")
    logger.debug("logger get called from test function")