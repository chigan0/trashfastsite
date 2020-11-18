from django.contrib import admin
from django.utils.html import mark_safe
from .models import *

# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	exclude=['datetime']
	list_display = ('cate_name','datetime')

@admin.register(Games)
class GamesAdmin(admin.ModelAdmin):
	exclude=['datetime']
	list_display = ('game','cate_id','datetime','get_img')
	list_filter = ('cate_id', 'game')

	def get_img(self,obj):
		return mark_safe(f"<img src={obj.game_img.url} width='40' height='50'>")

@admin.register(Visits)
class VisitsAdmin(admin.ModelAdmin):
	pass