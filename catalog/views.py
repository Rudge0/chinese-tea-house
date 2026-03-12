from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from catalog.froms import (
    TeaSearchForm,
    SupplierSearchForm,
    TeaForm,
    SupplierCreationForm,
    ProvinceForm,
    TeaCategoryForm
)
from catalog.models import (
    Tea,
    Supplier,
    Province,
    TeaCategory,
)


@login_required
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


class TeaListView(LoginRequiredMixin, generic.ListView):
    model = Tea
    paginate_by = 10

    def get_context_data(
            self, *, object_list=..., **kwargs
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


class TeaDetailView(LoginRequiredMixin, generic.DetailView):
    model = Tea
    queryset = Tea.objects.select_related("category", "province").prefetch_related("supplier")


class TeaCreateView(LoginRequiredMixin, generic.CreateView):
    model = Tea
    form_class = TeaForm


class TeaUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Tea
    fields = TeaForm


class TeaDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Tea
    success_url = reverse_lazy("catalog:tea-list")


class SupplierListView(LoginRequiredMixin, generic.ListView):
    model = Supplier
    paginate_by = 10

    def get_context_data(
            self, *, object_list=..., **kwargs
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


class SupplierDetailView(LoginRequiredMixin, generic.DetailView):
    model = Supplier


class SupplierCreateView(LoginRequiredMixin, generic.CreateView):
    model = Supplier
    form_class = SupplierCreationForm
    success_url = reverse_lazy("catalog:supplier-list")


class SupplierUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Supplier
    form_class = SupplierCreationForm


class SupplierDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Supplier
    success_url = reverse_lazy("catalog:supplier-list")


class ProvinceListView(LoginRequiredMixin, generic.ListView):
    model = Province
    paginate_by = 10


class ProvinceDetailView(LoginRequiredMixin, generic.DetailView):
    model = Province


class ProvinceCreateView(LoginRequiredMixin, generic.CreateView):
    model = Province
    form_class = ProvinceForm
    success_url = reverse_lazy("catalog:province-list")


class ProvinceUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Province
    form_class = ProvinceForm


class ProvinceDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Province
    success_url = reverse_lazy("catalog:province-list")


class TeaCategoryListView(LoginRequiredMixin, generic.ListView):
    model = TeaCategory
    paginate_by = 10
    template_name = "catalog/tea_category_list.html"
    context_object_name = "tea_categories_list"


class TeaCategoryDetailView(LoginRequiredMixin, generic.DetailView):
    model = TeaCategory
    template_name = "catalog/tea_category_detail.html"
    context_object_name = "tea_category"

class TeaCategoryCreateView(LoginRequiredMixin, generic.CreateView):
    model = TeaCategory
    form_class = TeaCategoryForm
    success_url = reverse_lazy("catalog:province-list")
    template_name = "catalog/tea_category_form.html"

class TeaCategoryUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = TeaCategory
    form_class = TeaCategoryForm
    template_name = "catalog/tea_category_form.html"

class TeaCategoryDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = TeaCategory
    success_url = reverse_lazy("catalog:tea-category-list")
    template_name = "catalog/tea_category_confirm_delete.html"
