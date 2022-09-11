from django.db import models
from django.forms import CharField, DateField

# Create your models here.

class article_ids(models.Model):
    verge_ids = models.IntegerField(("verge_ids"), max_length=20)

class Verge_data(models.Model):

    verge_ids = models.ForeignKey(article_ids, on_delete=models.CASCADE, primary_key=True)

    https_links = models.CharField(("https_links"), max_length=510)

    verge_articles = models.CharField(("verge_articles"), max_length=510)
 
    verge_authors = models.CharField(("verge_authors"), max_length=100)

    article_dates = models.DateField(("article_dates"), max_length=20)
