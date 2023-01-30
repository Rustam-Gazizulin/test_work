from django.db import models


class Contact(models.Model):
    email = models.EmailField(max_length=255, unique=True, error_messages={'unique': 'This email is already in use.'},
                              verbose_name='Электронная почта', null=True)
    country = models.CharField(max_length=50, verbose_name='Страна')
    city = models.CharField(max_length=50, verbose_name='Город')
    street = models.CharField(max_length=50, verbose_name='Улица')
    house_number = models.CharField(max_length=5, verbose_name='Номер дома')

    class Meta:
        verbose_name = 'Контактная информация'
        verbose_name_plural = 'Контактные данные'

    def __str__(self):
        return self.country


class Products(models.Model):
    title = models.CharField(max_length=30, verbose_name='Название')
    model = models.CharField(max_length=30, verbose_name='Модель')
    release = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.title


class Provider(models.Model):

    FACTORY = 'Завод'
    RETAIL_NETWORK = 'Розничная сеть'
    BUSINESSMAN = 'Предприниматель'

    STATUS = [(FACTORY, 'Завод'), (RETAIL_NETWORK, 'Розничная сеть'), (BUSINESSMAN, 'Предприниматель')]

    name = models.CharField(max_length=20, verbose_name='Название компании')
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='cont', blank=True, null=True)
    products = models.ForeignKey(Products, on_delete=models.CASCADE, related_name='prod', blank=True, null=True)
    level_in_hierarchy = models.CharField(max_length=20, choices=STATUS)
    credit = models.DecimalField(max_digits=15, decimal_places=2, default=0, verbose_name='Кредиторская задолженность')
    creation_time = models.DateTimeField(auto_now_add=True, verbose_name='Дата регистрации в сети')

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'

    def __str__(self):
        return self.name
