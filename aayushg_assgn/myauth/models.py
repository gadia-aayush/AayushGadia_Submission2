from django.db import models

# Create your models here.

class UserContacts(models.Model):
	uc_id = models.IntegerField(primary_key=True)
	contact_regid = models.IntegerField()
	uc_name = models.CharField(max_length=255)
	uc_mobno = models.IntegerField()

	class Meta:
		managed = True
		db_table = 'usercontacts'