from celery import shared_task 
from .models import Click, View, HourlyReport, DailyReport;
from datetime import datetime, timedelta
import pytz
from django.db.models import Count
from celery.utils.log import get_task_logger

UTC = pytz.utc
logger = get_task_logger(__name__)

@shared_task(name='hourly')
def last_hour_report():
    logger.info("hourly run")
    time = datetime.now(UTC) - timedelta(hours=1)
    clickCount = (View.objects.filter(time__gte=time).aggregate(Count('id'))['id__count'])
    clickReport = HourlyReport(type = "click", count = clickCount)
    clickReport.save()
    viewCount = (Click.objects.filter(time__gte=time).aggregate(Count('id'))['id__count'])
    viewReport = HourlyReport(type = "view", count = viewCount)
    viewReport.save()

    
@shared_task(name='daily')
def last_day_report():
    logger.info("daily run")
    time = datetime.now(UTC) - timedelta(days=1)
    clickCount = HourlyReport.objects.filter(timeKey__gte=time, type = "click").aggregate(Count('id'))['id__count']
    clickReport = HourlyReport(type = "click", count = clickCount)
    clickReport.save()
    viewCount = HourlyReport.objects.filter(timeKey__gte=time, type = "view").aggregate(Count('id'))['id__count']
    viewReport = HourlyReport(type = "view", count = viewCount)
    viewReport.save()