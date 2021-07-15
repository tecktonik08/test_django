from django.db import models

# Create your models here.
class Question(models.Model):   # Table
    question_text = models.CharField(max_length=100)    # column, datatype
    public_date = models.CharField(max_length=100)  # models.DateTimeField()
    votes = models.DecimalField(max_digits=20, decimal_places=10)   # models.BigIntegerField()

class Economics(models.Model):
    title = models.CharField(max_length=100)
    href = models.CharField(max_length=100)
    create_date = models.CharField(max_length=100)

