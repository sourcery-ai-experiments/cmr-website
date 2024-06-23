from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from roadnames.models import RoadName


def roadname(request, roadnameID):
    roadname = get_object_or_404(RoadName, id=roadnameID)

    data = {
        'roadname': roadname,
    }

    return render(request, 'roadname.html', data)


def roadnames(request):
    roadnames = RoadName.objects.all().order_by('name')
    paginator = Paginator(roadnames, settings.DEFAULT_LIST_LEN)

    pageNum = int(request.GET.get('page', 1))
    page = paginator.page(max(min(pageNum, paginator.num_pages), 1))

    data = {
        'roadnames': page.object_list,
        'page': page,
    }

    return render(request, 'roadnames.html', data)
