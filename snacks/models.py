from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
class Snack(models.Model):
    title=models.CharField(max_length=265)
    purchaser=models.TextField()
    description=models.TextField()
    Register_model=models.ForeignKey(get_user_model())
    
    def __str__(self):
        return self.name