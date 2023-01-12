from django.urls import path
from . import views



urlpatterns = [
    path('',views.package,name="packagepage"),
    path('cmt/',views.cmt,name="commentpage"),
    path("search/",views.search,name="searchpage"),
    path("auto/",views.autosearch,name="autopage")
]