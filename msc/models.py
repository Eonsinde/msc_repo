from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=1000)
    mail = models.EmailField(max_length=1000)
    subject = models.CharField(max_length=2000)
    message = models.TextField(max_length=10000)

    def __str__(self):
        return f'{self.name}: {self.subject}'


class NutritionTips(models.Model):
    tip = models.TextField(max_length=10000)
    pub_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'Tip: {self.id}'

    class Meta:
        ordering = ['-pub_date']
    

class Review(models.Model):
    topic = models.CharField(max_length=1000)
    briefing = models.TextField(max_length=5000)
    image = models.ImageField(upload_to='treated/')
    pub_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.topic}'

    class Meta:
        ordering = ['-pub_date']

