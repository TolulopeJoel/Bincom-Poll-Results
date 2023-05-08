from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from .forms import LGAForm, PollingUnitResultForm
from .models import PollingUnit, AnnouncedPollingUnitResult, Lga


class PollingUnitResultListView(generic.ListView):
    model = PollingUnit
    context_object_name = 'polling_units'
    template_name = 'ElectionResults/polling_unit_result_list.html'

    def get_queryset(self):
        polling_unit_ids = AnnouncedPollingUnitResult.objects.filter(
            party_score__isnull=False
        ).values_list('polling_unit__uniqueid', flat=True).distinct()

        return PollingUnit.objects.filter(uniqueid__in=polling_unit_ids)


def lga_total_results_view(request):
    form = LGAForm(request.POST)
    if form.is_valid():
        lga_name = form.cleaned_data['lga']
        polling_units = PollingUnit.objects.filter(lga=lga_name)
        all_polling_units_result = {}
        all_unit_scores = []

        for polling_unit in polling_units:
            polling_unit_result = []
            results = polling_unit.results.all()

            for result in results:
                party_result = {
                    'party': result.party.name,
                    'score': result.party_score,
                }
                polling_unit_result.append(party_result)

            all_polling_units_result[polling_unit.name] = polling_unit_result
            all_unit_scores.extend(result.party_score for result in results)

        lga_total_score = sum(all_unit_scores)

        context = {
            'form': form,
            'lga': lga_name,
            'lga_total_score': lga_total_score,
            'unit_scores': all_polling_units_result,
        }

        return render(request, 'ElectionResults/lga_result.html', context)

    return render(request, 'ElectionResults/lga_result.html', {'form': form})


class AddPollingUnitResultView(generic.CreateView):
    model = AnnouncedPollingUnitResult
    form_class = PollingUnitResultForm
    template_name = 'ElectionResults/add_polling_unit_result.html'
    success_url = reverse_lazy('polling_unit_results')
