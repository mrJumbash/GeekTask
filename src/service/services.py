from rest_framework.exceptions import ValidationError

from service import models
from django.db.models import QuerySet


class BookService:
    __book_model = models.Book
    __genre_model = models.Genre
    __writer_model = models.Writer

    @classmethod
    def get_list(cls, **filters) -> QuerySet[models.Book]:
        return (
            cls.__book_model.objects.filter(**filters)
            .order_by("-published")
            .only(
                "id",
                "title",
                "description",
                "promotion",
                "price",
                "genre",
                "writer",
                "published",
            )
            .select_related("writer", "genre")
        )

    @classmethod
    def create_book(
        cls,
        image,
        title: str,
        description: str,
        promotion: bool,
        price: float,
        genre: str,
        writer: str,
        published: int,
    ):
        return cls.__book_model.objects.create(
            image=image,
            title=title,
            description=description,
            promotion=promotion,
            price=price,
            genre_id=genre,
            writer_id=writer,
            published=published,
        )
