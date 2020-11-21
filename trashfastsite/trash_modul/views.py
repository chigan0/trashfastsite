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
	

	v = Visits.objects.filter(ip__exact=ip).all()
	
	if len(v) > 0:
		v[0].views += 1
		v[0].save()
	else:
		views = Visits(ip=ip,views=1)
		views.save()

	return render(request,'trash_modul/base.html',context={'games':a})

def get_cate(request,cons):
	context = tuple(Category.objects.values())

	consol = ConsoleName.objects.filter(name__exact=cons).all()
	if len(consol)>0:
		a = Category.objects.filter(console__exact=consol[0].id).values()

		return JsonResponse(tuple(a),safe=False,status=200)
#---------------------------------------------------------------------------------------
def game_cate(request):
	catecpry = request.GET['cate']

	con = ConsoleName.objects.get(name__exact=request.GET['console'])

	if catecpry == 'Все':
		
		a = tuple(Games.objects.filter(console__exact=con.id).values())
		return JsonResponse(a,safe=False,status=200)
	
	else:
		a = Category.objects.filter(cate_name__exact=catecpry,console__exact=con.id).values('id')
		if a != None:
			print(a)
			res = tuple(Games.objects.filter(cate_id__exact=a[0]['id']).values())
			return JsonResponse(res,safe=False,status=200)

#---------------------------------------------------------------------------------------
def check_console(request,chec):
	a = ConsoleName.objects.filter(name__exact=chec).all()

	if len(a) > 0:
		cate = Category.objects.filter(console__exact=a[0].id).all()
		if len(cate) > 0:
			print(cate)

			return JsonResponse({'status':True},safe=False,status=200)
	return JsonResponse({'status':False},safe=False,status=200)
#---------------------------------------------------------------------------------------
def error_404_view(request,exception):
	return render('trash_modul/404.html')	

def error_400_view(request,exception):
	return render(request,'trash_modul/500.html',context={'error':'400'})

def error_500_view(request):
	return render(request,'trash_modul/500.html',context={'error':'500'})
