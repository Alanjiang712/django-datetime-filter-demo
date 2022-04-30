from django.db import models
from django.contrib.auth.models import User
import datetime


class Todo(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


#选择今日和今周的记录
daynow = int(datetime.datetime.now().strftime('%d'))
weeknow = int(datetime.datetime.now().strftime('%W'))
yearnow = int(datetime.datetime.now().strftime('%Y'))

Todo.objects.filter(datecompleted__year=yearnow, datecompleted__week=weeknow)
Todo.objects.filter(datecompleted__year=yearnow, datecompleted__week=weeknow, datecompleted__day=daynow)


#选择未来7天内的记录
startTime = datetime.datetime.now()+datetime.timedelta(days=1)
endTime = datetime.datetime.now()+datetime.timedelta(days=7)

Todo.objects.filter(datecompleted__range=(startTime, endTime))