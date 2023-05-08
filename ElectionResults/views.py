from django.views import generic

from .models import PollingUnit, AnnouncedPollingUnitResult


class PollingUnitResultList(generic.ListView):
    model = PollingUnit
    context_object_name = 'polling_units'
    template_name = 'ElectionResults/polling_unit_result_list.html'

    def get_queryset(self):
        polling_unit_ids = AnnouncedPollingUnitResult.objects.filter(
            party_score__isnull=False
        ).values_list('polling_unit__uniqueid', flat=True).distinct()

        return PollingUnit.objects.filter(uniqueid__in=polling_unit_ids)

