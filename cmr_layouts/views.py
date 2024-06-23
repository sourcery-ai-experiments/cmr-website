from django.conf import settings
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from cmr_layouts.models import Customer, Location, Locomotive, RollingStock


def location(request, locationID):
    location = get_object_or_404(Location, id=locationID)

    data = {
        'location': location,
    }

    return render(request, 'cmr_location.html', data)


def locations(request):
    locations = Location.objects.all().order_by('name')
    paginator = Paginator(locations, settings.DEFAULT_LIST_LEN)

    pageNum = int(request.GET.get('page', 1))
    page = paginator.page(max(min(pageNum, paginator.num_pages), 1))

    data = {
        'locations': page.object_list,
        'page': page,
    }

    return render(request, 'cmr_locations.html', data)


def customer(request, customerID):
    customer = get_object_or_404(Customer, id=customerID)

    data = {
        'customer': customer,
    }

    return render(request, 'cmr_customer.html', data)


def customers(request):
    customers = Customer.objects.all().order_by('name')
    paginator = Paginator(customers, settings.DEFAULT_LIST_LEN)

    pageNum = int(request.GET.get('page', 1))
    page = paginator.page(max(min(pageNum, paginator.num_pages), 1))

    data = {
        'customers': page.object_list,
        'page': page,
    }

    return render(request, 'cmr_customers.html', data)


def locomotive(request, locomotiveID):
    locomotive = get_object_or_404(Locomotive, id=locomotiveID)

    data = {
        'locomotive': locomotive,
    }

    return render(request, 'cmr_locomotive.html', data)


def locomotives(request):
    locomotives = Locomotive.objects.all().order_by('roadName', 'model', 'number')
    paginator = Paginator(locomotives, settings.DEFAULT_LIST_LEN)

    pageNum = int(request.GET.get('page', 1))
    page = paginator.page(max(min(pageNum, paginator.num_pages), 1))

    data = {
        'locomotives': page.object_list,
        'page': page,
    }

    return render(request, 'cmr_locomotives.html', data)


def rollingstock(request, rollingstockID):
    rollingstock = get_object_or_404(RollingStock, id=rollingstockID)

    data = {
        'rollingstock': rollingstock,
    }

    return render(request, 'cmr_rollingstock.html', data)


def rollingstock_list(request):
    rollingstock = RollingStock.objects.all().order_by('roadName', 'model', 'number')
    paginator = Paginator(rollingstock, settings.DEFAULT_LIST_LEN)

    pageNum = int(request.GET.get('page', 1))
    page = paginator.page(max(min(pageNum, paginator.num_pages), 1))

    data = {
        'rollingstock': page.object_list,
        'page': page,
    }

    return render(request, 'cmr_rollingstock_list.html', data)
