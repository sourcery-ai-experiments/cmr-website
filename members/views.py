from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from members.models import Member


def member(request, memberID):
    member = get_object_or_404(Member, id=memberID)

    data = {
        'member': member,
    }

    return render(request, 'member.html', data)


def members(request):
    members = Member.objects.all().order_by('lastName', 'firstName')
    paginator = Paginator(members, settings.DEFAULT_LIST_LEN)

    pageNum = int(request.GET.get('page', 1))
    page = paginator.page(max(min(pageNum, paginator.num_pages), 1))

    data = {
        'members': page.object_list,
        'page': page,
    }

    return render(request, 'members.html', data)
