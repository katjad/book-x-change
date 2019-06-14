from django.db import models
from django.contrib import admin
from django.contrib.auth import get_user_model
from .utils import ChoiceEnum

class LoanStatus(ChoiceEnum):
    AV = "available"
    OL = "on loan"
    RQ = "requested"
    NA = "not available"

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    cover = models.ImageField(upload_to="covers/", blank=True)
    thumb = models.ImageField(upload_to="covers/", blank=True)
    published_date = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(auto_now_add=True, null=True)
    isbn = models.CharField("ISBN", max_length=17, null=True)
    description = models.TextField(
        max_length=1000,
        help_text="Enter \
        a brief description of the book",
        null=True,
    )
    status = models.CharField(
        max_length=50,
        choices=[(tag.name, tag.value) for tag in LoanStatus],
        default=(LoanStatus.AV.name),
    )
    objects = models.Manager()

class BookLoan(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    holder = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    status = models.CharField(max_length=2, default="RQ")
    date_requested = models.DateTimeField(blank=True, null=True)
    date_borrowed = models.DateTimeField(blank=True, null=True)
    date_returned = models.DateTimeField(blank=True, null=True)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
