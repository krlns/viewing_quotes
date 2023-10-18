from django.db import models


class CoinList(models.Model):
    name = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    coin_type = models.CharField(max_length=50)
    tx_fee = models.FloatField()
    img = models.CharField(max_length=300)
    price = models.FloatField()
