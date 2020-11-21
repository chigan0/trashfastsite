from django.db import models
from uuid import uuid4
from datetime import datetime as d

# Create your models here.

class ConsoleName(models.Model):
	name = models.CharField('console name',max_length=16,null=False)
	datetime = models.CharField(
		max_length=40,
		default=f'{d.utcnow().day}/{d.utcnow().month}/{d.utcnow().year}'
		)

	def __str__(self):
		return f"console {self.name}"

class Category(models.Model):
	cate_name = models.CharField(
		'Category name',
		max_length=86,
		null=False,
		)
	datetime = models.CharField(
		max_length=40,
		default=f'{d.utcnow().day}/{d.utcnow().month}/{d.utcnow().year}')
	console = models.ForeignKey(ConsoleName,default=None,on_delete=models.CASCADE)
	
	def __str__(self):
		return f"category {self.cate_name} for {self.console}"

class Games(models.Model):
	game = models.CharField('Games Name',max_length=180)
	game_img = models.ImageField(default=None,null=False)
	datetime = models.CharField(
		max_length=40,
		default=f'{d.utcnow().day}.{d.utcnow().month}.{d.utcnow().year}')
	cate_id = models.ForeignKey(Category,default=None,on_delete=models.CASCADE)
	console = models.ForeignKey(ConsoleName,default=None,on_delete=models.CASCADE)

	def __str__(self):
		return 'Games %r' % self.game

class Visits(models.Model):
	ip = models.CharField('ip',max_length=256)
	views = models.IntegerField('views')

	def __str__(self):
		return f"ip {self.ip} views {self.views}"