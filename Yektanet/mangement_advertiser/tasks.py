from celery import shared_task 
from .models import Ad, Click, View, HourlyClickReport, HourlyViewReport, DailyClickReport, DailyViewReport;
from datetime import datetime, timedelta
import pytz
from django.db.models import Count, Sum
from celery.utils.log import get_task_logger

UTC = pytz.utc
logger = get_task_logger(__name__)

@shared_task(name='hourly')
def last_hour_report():
    
    time = datetime.now(UTC) - timedelta(hours=1)

    click = Click.objects.filter(time__gte=time).values('ad').annotate(count = Count('ad'))
    for i in click:
        ad = Ad.objects.get(id = i['ad'])
        clickReport = HourlyClickReport(ad = ad, count = i['count'])
        clickReport.save()

    view = View.objects.filter(time__gte=time).values('ad').annotate(count = Count('ad'))
    for i in view:
        ad = Ad.objects.get(id = i['ad'])
        viewReport = HourlyViewReport(ad = ad, count = i['count'])
        viewReport.save()

    logger.info("hourly finished.")

    
@shared_task(name='daily')
def last_day_report():
    time = datetime.now(UTC) - timedelta(days=1)

    click = HourlyClickReport.objects.filter(keyTime__gte=time).values('ad').annotate(sum = Sum('count'))
    for i in click:
        ad = Ad.objects.get(id = i['ad'])
        clickReport = DailyClickReport(ad = ad, count = i['sum'])
        clickReport.save()

    view = HourlyViewReport.objects.filter(keyTime__gte=time).values('ad').annotate(sum = Sum('count'))
    for i in view:
        ad = Ad.objects.get(id = i['ad'])
        viewReport = DailyViewReport(ad = ad, count = i['sum'])
        viewReport.save()

    logger.info("daily finished.")