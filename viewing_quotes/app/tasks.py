import viewing_quotes
from django.db import DataError, connection
from .models import CompanyList


@viewing_quotes.celery_app.task()
def update_data(data: dict):
    table_names = connection.introspection.table_names()

    for category in data:
        if "app_companylist" in table_names and len(CompanyList.objects.values()) == 0:
            CompanyList.objects.bulk_create([CompanyList(
                name=el,
                last_deal=el['last_deal'],
                opening_prices=el['opening_prices'],
                max=el['max'],
                min=el['min'],
                category=category
            ) for el in category])
        else:
            for el in category:
                CompanyList.objects.filter(name=el).update(
                    last_deal=el['last_deal'],
                    opening_prices=el['opening_prices'],
                    max=el['max'],
                    min=el['min'],
                    category=category
                )
