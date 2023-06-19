from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from service.settings import TODAY_YEAR
from common.models import BaseModel


class Writer(BaseModel):
    """Writer field for books"""

    full_name = models.CharField(
        verbose_name="Имя - Фамилия", max_length=255, unique=True
    )

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = "service_writer"
        verbose_name = "Писатель"
        verbose_name_plural = "Писатели"
        ordering = ("-created_at",)


class Genre(BaseModel):
    """Genre field for books"""

    name = models.CharField(verbose_name="Название Жанра", max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "service_genre"
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"
        ordering = ("-created_at",)


class Book(BaseModel):
    """Model for books with own fields"""

    image = models.ImageField(blank=True, null=True)
    title = models.CharField(verbose_name="Заголовок", max_length=255, unique=True)
    description = models.TextField(verbose_name="Описание")
    price = models.FloatField(verbose_name="Цена", validators=[MinValueValidator(0)])
    promotion = models.BooleanField(verbose_name="Акция", default=False)
    genre = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE,
        verbose_name="Жанры",
        related_name="books_genres",
    )
    writer = models.ForeignKey(
        Writer, on_delete=models.CASCADE, related_name="books_writers"
    )
    published = models.PositiveIntegerField(
        verbose_name="Дата Публикации", validators=[MaxValueValidator(TODAY_YEAR)]
    )

    def __str__(self):
        return self.title

    class Meta:
        db_table = "service_book"
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
        ordering = ("-published",)
