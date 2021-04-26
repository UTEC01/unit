from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    p_no = models.CharField(max_length=40)
    o_no = models.CharField(max_length=40)
    c_name = models.CharField(max_length=200, null=True)
    text = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    c_date = models.DateField(blank=True, null=True)
    購入納期 = models.DateField(blank=True, null=True)
    出荷日 = models.DateField(blank=True, null=True)
    手配残 = models.IntegerField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.p_no

class Minyuka(models.Model):
    発注番号 = models.CharField(max_length=40)
    発注先 = models.CharField(max_length=40)
    納期 = models.DateField(blank=True, null=True)
    個数 = models.IntegerField(blank=True, null=True)
    読込日 = models.DateField(blank=True, null=True)
    品名 = models.CharField(blank=True, max_length=40)
    mmm = models.IntegerField(blank=True, null=True)
    備考 = models.CharField(blank=True, max_length=40)
    入荷FLG = models.IntegerField(blank=True, null=True)
    def __str__(self):
        return self.発注番号
