from django.db import models

class TodoItem(models.Model):
    content = models.TextField()
    # date_created
    # author