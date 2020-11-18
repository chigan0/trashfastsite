from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import *

def test(request):
	a = tuple(Games.objects.values())
	ip = request.META.get('REMOTE_ADDR')

	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    
	if x_forwarded_for:
		ip = x_forwarded_for.split(',')[0]
	else:
		ip = request.META.get('REMOTE_ADDR')
	

	v = Visits.objects.filter(ip__exact=ip).get()
	if v != None:
		v.views += 1
		v.save()
	else:
		views = Visits(ip=ip,views=1)
		views.save()

	return render(request,'trash_modul/base.html',context={'games':a})

def get_cate(request):
	context = tuple(Category.objects.values())

	return JsonResponse(context,safe=False,status=200)

def game_cate(request,resu):
	if resu == 'Все':
		a = tuple(Games.objects.values())
		return JsonResponse(a,safe=False,status=200)
	else:
		a = Category.objects.filter(cate_name__exact=resu).values('id')
		if a != None:
			res = tuple(Games.objects.filter(cate_id__exact=a[0]['id']).values())
			return JsonResponse(res,safe=False,status=200)

def error_404_view(request,exception):
	return render('trash_modul/404.html')	

def error_400_view(request,exception):
	return render(request,'trash_modul/500.html',context={'error':'400'})

def error_500_view(request):
	return render(request,'trash_modul/500.html',context={'error':'500'})
