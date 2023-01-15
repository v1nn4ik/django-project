from django.db import models


# Create your models here.

class HomeInfo(models.Model):
    title = models.CharField("Заголовок", max_length=100)
    text = models.TextField("Текст", default=None)


class DemandInfo(models.Model):
    title = models.CharField("Заголовок", max_length=100)
    img = models.ImageField("Картинка", upload_to='img/')
    text = models.TextField("Текст", default=None)
