from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from locations.models import Location


def location(request, locationID):
    location = get_object_or_404(Location, id=locationID)

    data = {
        'location': location,
    }

    return render(request, 'location.html', data)


def locations(request):
    locations = Location.objects.all().order_by('name')
    paginator = Paginator(locations, settings.DEFAULT_LIST_LEN)

    pageNum = int(request.GET.get('page', 1))
    page = paginator.page(max(min(pageNum, paginator.num_pages), 1))

    data = {
        'locations': page.object_list,
        'page': page,
    }

    return render(request, 'locations.html', data)
