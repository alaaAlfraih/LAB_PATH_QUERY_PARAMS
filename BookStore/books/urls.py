from django.urls import path
from . import views

app_name="books"

urlpatterns=[
    path("books/list",views.views_all_book,name="books"),
    path("books/view/<int:book_id>",views.view_book,name="books")
]