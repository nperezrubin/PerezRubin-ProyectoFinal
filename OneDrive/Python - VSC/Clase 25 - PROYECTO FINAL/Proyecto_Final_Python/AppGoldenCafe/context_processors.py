from django.utils import timezone
from datetime import datetime, date

def current_datetime(request):
  return {'current_datetime': timezone.now()}