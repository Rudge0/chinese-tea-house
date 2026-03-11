from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.template.context_processors import request
from django.urls import reverse_lazy
from django.views import generic

from catalog.froms import TeaSearchForm, SupplierSearchForm, TeaForm
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


class TeaListView(generic.ListView):
    model = Tea
    paginate_by = 10

    def get_context_data(
        self, *, object_list = ..., **kwargs
    ):
        context = super(TeaListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["name"] = name
        context["search_form"] = TeaSearchForm(
            initial={"name": name}
        )
        return context

    def get_queryset(self):
        queryset = Tea.objects.select_related("category", "province")
        form = TeaSearchForm(self.request.GET)
        if form.is_valid():
           return queryset.filter(name__icontains=form.cleaned_data["name"])
        return queryset


class TeaDetailView(generic.DetailView):
    model = Tea
    queryset = Tea.objects.select_related("category", "province").prefetch_related("supplier")


class TeaCreateView(generic.CreateView):
    model = Tea
    form_class = TeaForm


class TeaUpdateView(generic.UpdateView):
    model = Tea
    fields = "__all__"

class TeaDeleteView(generic.DeleteView):
    model = Tea
    success_url = reverse_lazy("catalog:tea-list")


class SupplierListView(generic.ListView):
    model = Supplier
    paginate_by = 10

    def get_context_data(
        self, *, object_list = ..., **kwargs
    ):
        context = super(SupplierListView, self).get_context_data(**kwargs)
        last_name = self.request.GET.get("last_name", "")
        context["last_name"] = last_name
        context["search_form"] = SupplierSearchForm(
            initial={"last_name": last_name}
        )
        return context

    def get_queryset(self):
        queryset = Supplier.objects.all()
        form = SupplierSearchForm(self.request.GET)
        if form.is_valid():
           return queryset.filter(last_name__icontains=form.cleaned_data["last_name"])
        return queryset


class SupplierDetailView(generic.DetailView):
    model = Supplier


class SupplierCreateView(generic.CreateView):
    model = Supplier
    fields = "__all__"
    success_url = reverse_lazy("catalog:supplier-list")


class SupplierUpdateView(generic.UpdateView):
    model = Supplier
    fields = "__all__"

class SupplierDeleteView(generic.DeleteView):
    model = Supplier
    success_url = reverse_lazy("catalog:supplier-list")
