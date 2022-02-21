import factory


class ProductFactory(factory.django.DjangoModelFactory):
    title = "Combining Pytest and FactoryBoy for simplified tests in Django"
    status = "draft"

    class Meta:
        model = "app.Product"