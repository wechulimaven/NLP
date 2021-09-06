from django.db import models
from django.contrib.auth.models import Permission, User
# Create your models here.


# class textlang(models.Model):
# 	CHOICES = (
# 			('ar', 'Arabic'),
# 			('bn', 'Bengali'),
# 			('en', 'English'),
# 			('fr', 'French'),
# 			('de', 'German'),
# 			('hi', 'Hindi'),
# 			('it', 'Italian'),
# 			('ja', 'Japanese'),
# 			('mr', 'Marathi'),
# 			('pt', 'Portuguese'),
# 			('pa', 'Punjabi'),
# 			('ru', 'Russian'),
# 			('es', 'Spanish'),
# 			('ta', 'Tamil'),
# 			('te', 'Telugu')
# 		)
# 	text = models.CharField(max_length=150)
# 	lang1 = models.CharField(max_length=15,choices=CHOICES)
# 	lang2 = models.CharField(max_length=15,choices=CHOICES)

# 	def __self__(self):
# 		return self.text,self.lang

class translator(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    english = models.CharField(max_length=50)
    luo = models.CharField(max_length=50)
    def __str__(self):
        return f'{self.english}'

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'translator'
        verbose_name_plural = 'translators'