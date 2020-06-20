from django.db import models

# Create your models here.

class Spam(models.Model):
	spam_id = models.IntegerField(primary_key=True)
	spam_mobno = models.IntegerField()
	spam_count = models.IntegerField()

	class Meta:
		managed = True
		db_table = 'spam'