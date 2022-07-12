from django.shortcuts import render
from django.core.paginator import Paginator
from .models import (
    Clients,
    Durations,
    Equipment,
    Modes,
)
from django.db.models import Q, Model
from .forms import DurationsForm


def index(request):
    context = {}
    form = DurationsForm()
    durations = Durations.objects.all().order_by('client')

    if request.POST:
        form = DurationsForm(request.POST)
        if form.is_valid():
            q_expr = Q()
            form_data = form.cleaned_data
            for k, v in form_data.items():
                if isinstance(v, Model):
                    q_expr &= Q((k, v))
                elif k == 'hour_stop' and v is not None:
                    q_expr &= Q(("stop__hour", v))
                elif k == 'hour_start' and v is not None:
                    q_expr &= Q(("start__hour", v))
                elif k =='start' and v is not None:
                    q_expr &= Q(("start__date", v))
                elif k == 'stop' and v is not None:
                    q_expr &= Q(("stop__date", v))
                elif k == 'minutes' and v is not None:
                    q_expr &= Q((k, v))
            if q_expr:
                durations = durations.filter(q_expr)
    paginator = Paginator(durations, 25)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context['page_obj'] = page_obj
    context['form'] = form
    return render(
        request,
        'index.html',
        context,
    )