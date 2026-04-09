from django.db import models
from django.conf import settings
from django.db.models import Q
from django.utils import timezone

User = settings.AUTH_USER_MODEL


class Record(models.Model):
    TYPE_CHOICES = (
        ('income', 'Income'),
        ('expense', 'Expense'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    category = models.CharField(max_length=100)
    date = models.DateField(default=timezone.now)
    notes = models.TextField(blank=True, null=True)

    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.type} - {self.amount}"

    class Meta:
        ordering = ['-date']

        constraints = [
            models.CheckConstraint(
                condition=Q(amount__gt=0),
                name="amount_positive"
            )
        ]

        indexes = [
            models.Index(fields=['user']),
            models.Index(fields=['category']),
            models.Index(fields=['type']),
            models.Index(fields=['date']),
        ]