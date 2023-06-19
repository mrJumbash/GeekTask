from rest_framework import generics, response, status
from service import services, serializers


"""Views For Books"""


class BookAPIView(generics.GenericAPIView):
    serializer_class = serializers.BookListSerializer

    def get(self, request, *args, **kwargs):
        books = services.BookService.get_list(is_deleted=False)
        serializer = self.get_serializer(books, many=True)
        return response.Response(
            data={"data": serializer.data},
            status=status.HTTP_200_OK,
        )

    def post(self, request, *args, **kwargs) -> response.Response:
        serializer = serializers.BookCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = services.BookService.create_book(
            image=serializer.validated_data.get("image"),
            title=serializer.validated_data.get("title"),
            description=serializer.validated_data.get("description"),
            price=serializer.validated_data.get("price"),
            promotion=serializer.validated_data.get("promotion"),
            genre=serializer.validated_data.get("genre"),
            writer=serializer.validated_data.get("writer"),
            published=serializer.validated_data.get("published"),
        )
        return response.Response(
            data={
                "message": "Book was succesfully created",
                "data": serializers.BookCreateSerializer(data).data,
                "status": "Created",
            },
            status=status.HTTP_201_CREATED,
        )


class BookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = services.BookService.get_list(is_deleted=False)
    serializer_class = serializers.BookDetailSerializer
    lookup_field = "id"

    def get(self, request, *args, **kwargs) -> response.Response:
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return response.Response(data=serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return response.Response(
            data={
                "message": "Book data successfully updated",
                "data": serializers.BookDetailSerializer(instance).data,
                "status": "Updated",
            }
        )
