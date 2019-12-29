from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.
class Product(models.Model):
	name = models.CharField(max_length=64, unique=True)
	price = models.FloatField()
	cost = models.FloatField()
	description = models.CharField(max_length=128)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ["name"]

class Branch(models.Model):
	location = models.CharField(max_length=64, unique=True)
	def __str__(self):
		return self.location


class Entry(models.Model):
	product_number = models.PositiveIntegerField()
	date = models.DateField()
	product = models.ForeignKey(Product, related_name="entries", on_delete=models.CASCADE)
	branch = models.ForeignKey(Branch, related_name="entries", on_delete=models.CASCADE)
	
	def __str__(self):
		return str(self.date) + " " + str(self.branch) + " " + str(self.product) + " " + str(self.product_number)

	class Meta:
		ordering = ["-date"]
		unique_together = ["date", "product", "branch"]

class DailyCash(models.Model):
	branch = models.ForeignKey(Branch, related_name="dailyincome", on_delete=models.CASCADE)
	date = models.DateField()
	actual_income = models.DecimalField(decimal_places=2, max_digits=12, validators=[MinValueValidator(0)])
	theoretical_income = models.FloatField()
	difference_value = models.FloatField()
	difference_percent = models.FloatField()
	def __str__(self):
		return str(self.date) + " " + str(self.branch) + " " + str(self.actual_income)
	class Meta:
		ordering = ["-date"]
		unique_together = ["branch", "date"]