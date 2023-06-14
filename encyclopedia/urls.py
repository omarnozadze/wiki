from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("new_page.html", views.new_page, name="new_page"),
    path("search", views.search, name="search"),
    path("editor/<str:title>", views.editor, name="editor"),
    path("wiki/<str:page>", views.page, name="page"),
    
]
