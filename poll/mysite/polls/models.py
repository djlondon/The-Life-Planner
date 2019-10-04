import datetime

from django.db import models
from django.utils import timezone

# Each model is represented by a class that subclasses
# django.db.models.Model 
#
# Each field is represented by an instance of a Field class
# The name of each Field instance is the field’s name
class Question(models.Model):
    # field_name = FieldClass()
    question_text = models.CharField(max_length=200)
    # 'date published' is the human-friendly name
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text