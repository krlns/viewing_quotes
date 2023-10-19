import viewing_quotes
from django.db import DataError, connection
from .models import CoinList
from typing import List


@viewing_quotes.celery_app.task()
def update_data(list_data: List[dict]):
    table_names = connection.introspection.table_names()

    if "app_coinlist" in table_names and len(CoinList.objects.values()) == 0:
        CoinList.objects.bulk_create([CoinList(
            name=el['name'],
            status=el['status'],
            coin_type=el['coin_type'],
            tx_fee=el['tx_fee'],
            img=el['img'],
            price=el['price']
        ) for el in list_data])
    else:
        for el in list_data:
            CoinList.objects.filter(name=el['name']).update(
                price=el['price']
            )
