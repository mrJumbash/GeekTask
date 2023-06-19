from django.core.validators import MaxValueValidator
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from service.models import Book, Genre, Writer
from service.settings import TODAY_YEAR

"""Validation Serializers for Books"""


class BookListSerializer(serializers.ModelSerializer):
    """Serializer for get request"""

    writer = serializers.PrimaryKeyRelatedField(
        queryset=Writer.objects.filter(is_deleted=False),
        required=True,
        allow_null=False,
    )
    genre = serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.filter(is_deleted=False), required=True, allow_null=False
    )

    class Meta:
        model = Book
        fields = [
            "id",
            "image",
            "title",
            "description",
            "price",
            "promotion",
            "genre",
            "writer",
            "published",
        ]


class BookDetailSerializer(serializers.ModelSerializer):
    """Serializer for retrieve/patch/del requests"""

    writer = serializers.PrimaryKeyRelatedField(
        queryset=Writer.objects.filter(is_deleted=False),
        required=True,
        allow_null=False,
    )
    genre = serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.filter(is_deleted=False), required=True, allow_null=False
    )

    class Meta:
        model = Book
        fields = [
            "id",
            "image",
            "title",
            "description",
            "price",
            "promotion",
            "genre",
            "writer",
            "published",
        ]
        read_only = ["id", "genre", "writer"]


class BookCreateSerializer(serializers.ModelSerializer):
    """Serializer for post request"""

    image = serializers.ImageField(
        allow_null=True, allow_empty_file=True, required=False
    )
    title = serializers.CharField(allow_null=False, required=True, max_length=255)
    description = serializers.CharField(allow_null=True, required=False, max_length=255)
    price = serializers.IntegerField(allow_null=False, required=True, min_value=0)
    promotion = serializers.BooleanField(
        allow_null=False, required=False, default=False
    )
    published = serializers.IntegerField(validators=[MaxValueValidator(TODAY_YEAR)])
    writer = serializers.CharField(max_length=255, allow_null=False, required=True)
    genre = serializers.CharField(max_length=255, allow_null=False, required=True)

    def validate(self, attrs):
        writer = attrs["writer"]
        try:
            Writer.objects.get(id=writer)
        except Writer.objects.DoesNotExist:
            raise ValidationError(f"Error! {writer} does not exists")
        genre = attrs["genre"]
        try:
            Genre.objects.get(id=genre)

        except Genre.objects.DoesNotExist:
            raise ValidationError(f"Error! {genre} does not exists")
        return attrs

    class Meta:
        model = Book
        fields = [
            "id",
            "image",
            "title",
            "description",
            "price",
            "promotion",
            "genre",
            "writer",
            "published",
        ]


"""VAlidation Serializers for Genres & Writers"""


class GenreSerializer(serializers.ModelSerializer):
    """Serializer for all requests"""

    class Meta:
        model = Genre
        fields = ["id", "name"]
        read_only = ["id"]


class WriterSerializer(serializers.ModelSerializer):
    """Serializer for all requests"""

    class Meta:
        model = Writer
        fields = ["id", "full_name"]
        read_only = ["id"]
