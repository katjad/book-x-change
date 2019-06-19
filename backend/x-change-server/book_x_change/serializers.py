from rest_framework import serializers
from.models import Book

# Serializers define the API representation.
class BookSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Book
        fields = (
            'title',
            'author',
            'cover',
            'thumb',
            'published_date',
            'last_updated',
            'isbn',
            'description',
            'status',
        )
