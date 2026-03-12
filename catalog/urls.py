from django.urls import path
from catalog.views import ( \
    index,

    TeaListView,
    TeaDetailView,
    TeaCreateView,
    TeaUpdateView,
    TeaDeleteView,


    SupplierListView,
    SupplierDetailView,
    SupplierCreateView,
    SupplierUpdateView,
    SupplierDeleteView,

    ProvinceListView,
    ProvinceDetailView,
    ProvinceCreateView,
    ProvinceUpdateView,
    ProvinceDeleteView,

    TeaCategoryListView,
    TeaCategoryDetailView,
    TeaCategoryCreateView,
    TeaCategoryUpdateView,
    TeaCategoryDeleteView,

)

urlpatterns = [
    path("", index, name="index"),

####### Tea
    path("teas/", TeaListView.as_view(), name="tea-list"),
    path("teas/create/", TeaCreateView.as_view(), name="tea-create"),
    path("teas/<int:pk>/", TeaDetailView.as_view(), name="tea-detail"),
    path("teas/<int:pk>/update/", TeaUpdateView.as_view(), name="tea-update"),
    path("teas/<int:pk>/delete", TeaDeleteView.as_view(), name="tea-delete"),
####### Tea

####### Supplier
    path("suppliers/", SupplierListView.as_view(), name="supplier-list"),
    path("suppliers/create/", SupplierCreateView.as_view(), name="supplier-create"),
    path("suppliers/<int:pk>/", SupplierDetailView.as_view(), name="supplier-detail"),
    path("suppliers/<int:pk>/update/", SupplierUpdateView.as_view(), name="supplier-update"),
    path("suppliers/<int:pk>/delete", SupplierDeleteView.as_view(), name="supplier-delete"),
####### Supplier

####### Province
    path("provinces/", ProvinceListView.as_view(), name="province-list"),
    path("provinces/create/", ProvinceCreateView.as_view(), name="province-create"),
    path("provinces/<int:pk>/", ProvinceDetailView.as_view(), name="province-detail"),
    path("provinces/<int:pk>/update/", ProvinceUpdateView.as_view(), name="province-update"),
    path("provinces/<int:pk>/delete", ProvinceDeleteView.as_view(), name="province-delete"),
####### Province

####### Tea Category
    path("tea-categories/", TeaCategoryListView.as_view(), name="tea-category-list"),
    path("tea-categories/create/", TeaCategoryCreateView.as_view(), name="tea-category-create"),
    path("tea-categories/<int:pk>/", TeaCategoryDetailView.as_view(), name="tea-category-detail"),
    path("tea-categories/<int:pk>/update/", TeaCategoryUpdateView.as_view(), name="tea-category-update"),
    path("tea-categories/<int:pk>/delete", TeaCategoryDeleteView.as_view(), name="tea-category-delete"),
####### Tea Category
]


app_name = "catalog"
