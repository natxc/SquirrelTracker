from django.shortcuts import render
from tracker.models import Squirrel
from django.http import HttpResponse, HttpResponseRedirect
from .forms import SquirrelAddForm



def index(request):
    return render(request, 'index.html', {})

def map(request):
    squirrels = Squirrel.objects.all()[:100]
    context = {
            'squirrels': squirrels
        }
    return render(request, 'tracker/map.html', context)

def sightings(request):
    squirrels = Squirrel.objects.all().order_by('-Date')
    context = {
            'squirrels': squirrels
            }
    return render(request, 'tracker/sightings.html', context)

def add(request):
    if request.method =='POST':
        form = SquirrelAddForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/sightings.html')
    else:
        form = SquirrelAddForm()
    context = {'form': form}           
    return render(request, 'tracker/add.html', context)

def update(request, Unique_Squirrel_ID):
    squirrel = Squirrel.objects.get(Unique_Squirrel_ID=Unique_Squirrel_ID)
    if request.method =='POST':
        form = SquirrelAddForm(request.POST, instance=squirrel)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/sightings.html')
    else:
        form = SquirrelAddForm(instance=squirrel)
    context = {'form': form}
    return render(request, 'tracker/update.html', context)

def stats(request): 
    total_seen = Squirrel.objects.all().count()
    number_running = Squirrel.objects.filter(Running=True).count()
    number_climbing = Squirrel.objects.filter(Climbing=True).count()
    juvenile_seen = Squirrel.objects.filter(Age='Juvenile').count()
    adults_seen = Squirrel.objects.filter(Age='Adult').count()
   
    context = {
            'total_seen': total_seen,
            'number_running': number_running,
            'number_climbing': number_climbing,
            'juvenile_seen': juvenile_seen,
            'adults_seen': adults_seen,
            }
    return render(request, 'tracker/stats.html', context)

