from django.shortcuts import render, redirect, HttpResponse
import random, datetime
# Create your views here.
def index(request):
    if 'gold' in request.session:
        pass
    else:
        request.session['gold']=0
    if 'feed' not in request.session:
        request.session['feed']=[]
    return render(request, 'index.html')

def process_gold(request):
    farm = random.randint(10,20)
    cave = random.randint(5,10)
    house = random.randint(2,5)
    casino = random.randint(-50,50)
    if request.POST['location'] == 'farm':
        request.session['gold'] += farm
        activity = f'Earned {farm} golds from the farm!'
        request.session['feed'].insert(0, activity)
    if request.POST['location'] == 'cave':
        request.session['gold'] += cave
        activity = f'Earned {cave} golds from the cave!'
        request.session['feed'].insert(0, activity)
    if request.POST['location'] == 'house':
        request.session['gold'] += house
        activity = f'Earned {house} golds from the house!'
        request.session['feed'].insert(0, activity)
    if request.POST['location'] == 'casino':
        request.session['gold'] += casino
        if casino < 0:
            activity = f'Entered a casino and lost {casino} ... Ouch..'
            request.session['feed'].insert(0, activity)
        else:
            activity = f'Entered a casino and earned {casino}... Great Job!'
            request.session['feed'].insert(0, activity)
    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')