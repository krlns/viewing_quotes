from django.db import models


class CompanyList(models.Model):
    CHOICES_CATEGORY = [
        ("fr", "foreign"),
        ("ru", "russian")
    ]
    name = models.CharField(max_length=70)
    last_deal = models.FloatField()
    opening_prices = models.FloatField()
    max = models.FloatField()
    min = models.FloatField()
    category = models.CharField(max_length=10, choices=CHOICES_CATEGORY)
