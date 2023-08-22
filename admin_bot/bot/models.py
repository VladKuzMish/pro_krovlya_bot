from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100, verbose_name="telegramm name работника")
    chat_id = models.IntegerField(unique=True, verbose_name="chat id telegram")
    rate = models.FloatField(verbose_name="Зарплата работника в час (в рублях)")

    def __str__(self):
        return self.name


class Object(models.Model):
    name = models.CharField(max_length=255, verbose_name="Наименование объекта", blank=True, null=True)

    def __str__(self):
        return self.name


class WorkDay(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Поьзователь")
    object = models.ForeignKey(Object, on_delete=models.CASCADE, null=True, verbose_name="Объект")
    created_at = models.DateField(verbose_name="Год - Месяц - Число", help_text="Пример ввода данных - 2022-01-01")
    start_work = models.TimeField(verbose_name="Время начала рабочего дня", help_text="Пример ввода данных -  09:00")
    end_work = models.TimeField(verbose_name="Время окончания рабочего дня", help_text="Пример ввода данных -  19:00")
    lunch = models.TimeField(verbose_name="Время обеда", help_text="Пример ввода данных -  01:00")
    work_time = models.FloatField(verbose_name="Чисто время работы (за вычетом обеда)")
    salary_per_day = models.FloatField(verbose_name="Зарплата за текущую дату")

    def __str__(self):
        return f"WorkDay for {self.user.name} on {self.created_at}"