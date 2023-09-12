from django import template
from userauth.models import Batch, UserDetail
from routine.models import Routine, RoutineDetail
from django.shortcuts import get_object_or_404

register = template.Library()


@register.filter(name="dayfilter")
def dayfilter(value,rid):
    routine = get_object_or_404(Routine, id=rid)
    if not routine:
        return None
    detail = RoutineDetail.objects.filter(routine=routine,day=value)
    return detail