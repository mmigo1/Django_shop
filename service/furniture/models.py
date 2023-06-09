from django.db import models
from django.urls import reverse


class Furniture(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    price = models.FloatField(default=10, verbose_name='Цена')
    date_create = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    date_update = models.DateTimeField(auto_now=True, null=True, verbose_name='Дата обновления')
    photo = models.ImageField(upload_to='image/',blank=True, null=True, verbose_name='Фотография')
    exist = models.BooleanField(default=True, verbose_name='Есть в наличии?')

    supplier = models.ForeignKey('Supplier', on_delete=models.PROTECT, null=True, verbose_name='Поставщик')

    def __str(self):
        return self.name

    def get_absolute_url(self):
        return reverse('furn_info', args=[self.pk])

    class Meta:
        verbose_name = 'Мебель'
        verbose_name_plural = 'Мебель'
        ordering = 'name',


class Supplier(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название поставщика')
    agent_name = models.CharField(max_length=100, verbose_name='Имя агента поставщика')
    agent_firstname = models.CharField(max_length=100, verbose_name='Фамилия агента поставщика')
    agent_patronymic = models.CharField(max_length=100, verbose_name='Отчество агента поставщика')
    exist = models.BooleanField(default=True, verbose_name='Сотрудничаем?')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'
        ordering = ['title']


class Order(models.Model):
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заказа')
    date_finish = models.DateTimeField(null=True, blank=True, verbose_name='Дата завершения заказа')
    price = models.FloatField(null=True, verbose_name='Стоимость заказа')
    address_delivery = models.CharField(max_length=150, verbose_name='Адрес доставки')
    status = models.CharField(max_length=150, verbose_name='Статус',
                              choices=[
                                  ('1', 'Создан'),
                                  ('2', 'Отменён'),
                                  ('3', 'Согласован'),
                                  ('4', 'В пути'),
                                  ('5', 'Завершён')
                              ]
                              )

    furniture = models.ManyToManyField(Furniture)
    # furniture = models.ManyToManyField(Furniture, verbose_name='Мебель') # обычное создание связи М к М, через техническую таблицу Fruit_order
    employee = models.ForeignKey('Employee', on_delete=models.PROTECT, null=True, verbose_name='Сотрудник')

    def __str__(self):
        return f"{self.date_create} {self.status} {self.price}"

    class Meta:  #
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'  #
        ordering = ['date_create']


class Employee(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя сотрудника')
    firstname = models.CharField(max_length=100, verbose_name='Фамилия сотрудника')
    patronymic = models.CharField(max_length=100, verbose_name='Отчество сотрудника')
    date_hired = models.DateTimeField(auto_now_add=True, verbose_name='Дата заключения договора')
    position = models.CharField(max_length=100,verbose_name='Должность сотрудника')
    exist = models.BooleanField(default=True, verbose_name='Числится в штате?')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'
        ordering = ['name']



