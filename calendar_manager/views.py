from django.shortcuts import render, redirect
from .forms import EventForm
from .models import Event
from django.http import JsonResponse
from django.utils.dateparse import parse_datetime
from django.db.models import Q

# Create your views here.


def calendar(request):
    form = EventForm
    return render(request,
                  'calendar/calendar.html',
                  {'form': form
                   })


def add_event(request):
    if request.method == 'POST':
        event_form = EventForm(request.POST)
        if event_form.is_valid():
            new_doc = event_form.save(commit=False)
            new_doc.save()
            return redirect('calendar_main')
    else:
        return 'test'


def events(request):

    object_list = Event.objects.get_queryset()
    start = request.GET.get('start', '')
    end = request.GET.get('end', '')
    start_dt = parse_datetime(start)
    end_dt = parse_datetime(end)

    object_list = object_list.filter(Q(start__gte=start_dt) & Q(start__lt=end_dt))

    data = list(object_list.values())  # wrap in list(), because QuerySet is not JSON serializable
    # data = data.replace('all_day', 'allDay')
    return JsonResponse(data, safe=False)
