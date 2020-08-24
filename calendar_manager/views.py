from django.shortcuts import render
from .forms import EventForm


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
            return render(request,
                          'calendar/calendar.html',
                            {'form': event_form})
    else:
        return 'test'