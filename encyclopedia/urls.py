from django.urls import path

from . import views

app_name = 'encyclopedia'

urlpatterns = [
    path("", views.index, name="index"),
    # get entry path
    path("search/", views.searchBar, name="search"),
    path("search_result/", views.searchBar, name="search_result"),
    path("new_page/", views.new_page, name="newpage"),
    path("<str:name>/", views.getPage, name="get"),
    path("search/<str:name>/", views.getPage, name="result"),
    path("<str:name>/edit", views.edit_page, name="edit"),
    path("search/<str:name>/edit", views.edit_page, name="search_edit")
]
