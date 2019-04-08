from django.db import models

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=500)
	body = models.TextField()

class Category_Link(models.Model):
	category1 = models.ForeignKey(
	Category,
	related_name = "cat1",
	on_delete=models.CASCADE,
	)
	category2 = models.ForeignKey(
	Category,
	related_name = "cat2",
	on_delete=models.CASCADE,
	)

class Item(models.Model):
	name = models.CharField(max_length=500)
	body = models.TextField()
	category = models.ForeignKey(
	Category,
	models.SET_NULL,
	blank=True,
	null=True,
	)

class Tag(models.Model):
	name = models.CharField(max_length=500)
	item = models.ForeignKey(
	Item,
	models.SET_NULL,
	blank=True,
	null=True,
	)