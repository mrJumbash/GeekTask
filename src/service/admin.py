from django.contrib import admin
from service import models
from django.db.models import QuerySet


"""Registration of all Models into admin panel"""


@admin.register(models.Writer)
class WriterAdmin(admin.ModelAdmin):
    list_display = ["id", "full_name"]
    readonly_fields = ["id", "created_at"]
    fields = ["full_name"]


@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]
    readonly_fields = ["id", "created_at"]
    fields = ["name"]


@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = [
        "image",
        "title",
        "description",
        "price",
        "promotion",
        "writer",
        "genre",
        "published",
    ]
    readonly_fields = ["id", "created_at"]
    fields = [
        "image",
        "title",
        "description",
        "price",
        "promotion",
        "genre",
        "writer",
        "published",
    ]

    raw_id_fields = ["writer", "genre"]

    """Getting queryset for ForeingKey relations"""

    def get_queryset(self, request) -> QuerySet[models.Book]:
        queryset = super().get_queryset(request)
        queryset = queryset.select_related("writer", "genre")
        return queryset
