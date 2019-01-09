from django.db import models

# Create your models here.
class todo_item(models.Model):
    item_text = models.CharField(max_length=1000)
