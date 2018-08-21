from django.db import models

# Create your models here.

class Visitor(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Department(models.Model):
    question = models.ForeignKey(Visitor, on_delete=models.PROTECT)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
