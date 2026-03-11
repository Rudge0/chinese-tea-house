from django.urls import path
from catalog.views import ( \
    index,

    TeaListView,
    TeaDetailView,
    TeaCreateView,
    TeaUpdateView,
    TeaDeleteView,



)

urlpatterns = [
    path("", index, name="index"),

    path("teas/", TeaListView.as_view(), name="tea-list"),
    path("teas/create/", TeaCreateView.as_view(), name="tea-create"),
    path("teas/<int:pk>/", TeaDetailView.as_view(), name="tea-detail"),
    path("teas/<int:pk>/update/", TeaUpdateView.as_view(), name="tea-update"),
    path("teas/<int:pk>/delete", TeaDeleteView.as_view(), name="tea-delete"),
]


app_name = "catalog"
