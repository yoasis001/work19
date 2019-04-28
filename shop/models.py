from django.conf import settings
from django.db import models
from django.urls import reverse
from pytz import timezone


def local_time(input_time):
    fmt = '%Y-%m-%d %H:%M'
    my_zone = timezone(settings.TIME_ZONE)
    my_local_time = input_time.astimezone(my_zone)
    return my_local_time.strftime(fmt)

class Item(models.Model):
    name = models.CharField(max_length=20)
    desc = models.TextField(blank=True)
    price = models.PositiveIntegerField(default=0)
    photo = models.ImageField()  # blank=True 지정하지 않은 경우
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:item_detail', kwargs={'pk': self.pk})

class Review(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE,
                             related_name='reviews', verbose_name='아이템')
    message = models.TextField('리뷰')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-item__id', '-id']  # '-item__id', '-id'

    def __str__(self):
        return self.message

    def updated(self):
        return local_time(self.updated_at)
    updated.short_description = '수정 일시'