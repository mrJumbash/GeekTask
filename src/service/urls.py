from django.urls import path
from service import views

urlpatterns = [
    path("books/", view=views.BookAPIView.as_view()),
    path("books/<uuid:id>/", view=views.BookDetailAPIView.as_view()),
]
