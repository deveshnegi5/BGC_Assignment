from django.shortcuts import render, redirect 
from .models import Customer
from django.contrib import messages
from django.db.models import Count
from django.db.models.functions import TruncMonth


def home(request):
    objCust = Customer.objects.all()
    return render(request, 'home.html', {'objCust': objCust})

def edit(request,id):       
    obj = Customer.objects.get(pk = id)
    if request.method == 'POST':
        obj.Policy_id = request.POST.get('Policy_id')
        # obj.Date_of_Purchase = request.POST.get('Date_of_Purchase')
        obj.Customer_id	= request.POST.get('Customer_id')
        obj.Fuel = request.POST.get('Fuel')
        obj.VEHICLE_SEGMENT =request.POST.get('VEHICLE_SEGMENT')
        obj.Premium	= request.POST.get('Premium')
        obj.bodily_injury_liability	 =request.POST.get('bodily_injury_liability')
        obj.personal_injury_protection = request.POST.get('personal_injury_protection')
        obj.property_damage_liability = request.POST.get('property_damage_liability')
        obj.collision =request.POST.get('collision') 
        obj.comprehensive = request.POST.get('comprehensive')
        obj.Customer_Gender	= request.POST.get('Customer_Gender')
        obj.Customer_Income_group = request.POST.get('Customer_Income_group')
        obj.Customer_Region	= request.POST.get('Customer_Region')
        obj.Customer_Marital_status =bool(request.POST.get('Customer_Marital_status'))
        if int(request.POST.get('Premium')) > 1000000:
            messages.info(request,'preminum should be less than 1 million')
            return render(request,'update.html',{'new':obj})
        else:
            obj.save()
            return redirect('/')
    return render(request,'update.html', {'new':obj})

def search(request):
    search = request.GET['search']
    obj = Customer.objects.filter(Policy_id__icontains=search)
    return render(request,'search.html',{'obj': obj})

def ChartData(request):
    region = request.POST.get('region')
    # objregionfilter = Customer.objects.filter(Customer_Region = region).values('Date_of_Purchase').annotate(c=Count('Date_of_Purchase')).annotate(month=ExtractMonth('Date_of_Purchase')).order_by('Date_of_Purchase').distinct()
    objregionfilter = Customer.objects.filter(Customer_Region = region).annotate(month=TruncMonth('Date_of_Purchase')).values('month').annotate(c=Count('id')).order_by()
    objregion = Customer.objects.order_by('Customer_Region').values('Customer_Region').distinct()
    context= {
        'objregion': objregion,
        'objregionfilter': objregionfilter,
        }
    return render(request, 'graph.html', context)
