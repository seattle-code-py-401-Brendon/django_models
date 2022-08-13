from django.db import models
from django.contrib.auth import get_user_model


class Snack(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField(default=" ")
    purchaser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f'Name: {self.name}, Description: {self.description}, Purchaser: {self.purchaser}'
