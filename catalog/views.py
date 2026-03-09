from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from catalog.models import (
    Tea,
    Supplier,
    Province,
    TeaCategory,
)


def index(request: HttpRequest) -> HttpResponse:

    num_teas = Tea.objects.count()
    num_supplier = Supplier.objects.count()
    num_provinces = Province.objects.count()
    num_tea_category = TeaCategory.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_visits": num_visits,
        "num_teas": num_teas,
        "num_supplier": num_supplier,
        "num_provinces": num_provinces,
        "num_tea_category": num_tea_category,
    }

    return render(request, "catalog/index.html", context=context)


