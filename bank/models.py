from django.db import models




class banks(models.Model):
	name 		= models.CharField(max_length=49)
	_id 		= models.BigIntegerField(null=False, default=0)


	def __str__(self):
		return self.name
		



class branches(models.Model):
	ifsc 		= models.CharField(max_length=11)
	branch 		= models.CharField(max_length=74)
	address 	= models.CharField(max_length=195)
	city 		= models.CharField(max_length=50)
	district 	= models.CharField(max_length=50)
	state 		= models.CharField(max_length=26)
	bank 		= models.ForeignKey(banks, on_delete=models.SET_NULL, blank=True, null=True)


	def __str__(self):
		return self.branch
