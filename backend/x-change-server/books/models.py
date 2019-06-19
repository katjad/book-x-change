from django.db import models
from django.contrib import admin
from django.contrib.auth import get_user_model
from django_fsm import FSMField, transition
from django.utils import timezone
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
    status = FSMField(
        max_length=50,
        default=(LoanStatus.AV),
        choices=[(tag.name, tag.value) for tag in LoanStatus]
    )

    objects = models.Manager()

    @transition(field=status, source=[LoanStatus.AV], target=LoanStatus.OL)
    def loan_item(self, book, borrower):
        self.log_loan_event(book, borrower, LoanStatus.OL)

    @transition(field=status, source=[LoanStatus.AV], target=LoanStatus.RQ)
    def request_item(self, book, borrower):
        self.log_loan_event(book, borrower, LoanStatus.RQ)

    @transition(field=status, source=[LoanStatus.OL], target=LoanStatus.AV)
    def return_item(self, book, borrower):
        self.log_loan_event(book, borrower, LoanStatus.AV)

    def log_loan_event(self, book, borrower, status):
        BookLoanEvent.objects.create(
            book=book,
            holder=borrower,
            date=timezone.now(),
            status=status,
        )

    def get_loan(self, status):
        try:
            loan = BookLoanEvent.objects.filter(status=status, book=self).latest('date')
        except BookLoanEvent.DoesNotExist:
            loan = None
        return loan

    def get_holder_for_status(self, status):
        loan = self.get_loan(status)
        return loan.holder if loan else None

class BookLoanEvent(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    holder = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    status = models.CharField(max_length=2, default=LoanStatus.RQ)
    date = models.DateTimeField(blank=True, null=True)

class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author")
    list_filter = ["published_date"]
    search_fields = ["title", "author"]
