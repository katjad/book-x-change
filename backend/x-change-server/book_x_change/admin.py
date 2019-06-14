from django.contrib import admin
from .models import Book, BookAdmin

# Register your models here.
admin.site.register(Book, BookAdmin)
