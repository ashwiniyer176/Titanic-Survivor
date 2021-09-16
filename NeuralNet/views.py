from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .forms import InputForm
import pickle
from Titanic_Survivor.settings import BASE_DIR
import os


def makePrediction(data):
    PATH = os.path.join(BASE_DIR, 'Logistic.sav')
    model = pickle.load(open(PATH, 'rb'))
    data[1] = int(data[1])
    return model.predict([data])[0]


def index(request):
    if(request.method == "GET"):
        form = InputForm()
        return render(request, 'index.html', {'form': form})
    else:
        form = InputForm(request.POST)
        if(form.is_valid()):
            prediction = makePrediction(list(form.cleaned_data.values()))
            if(prediction == 1):
                context = {
                    'result': 'Congrats! Seems like you were one of the lucky ones..'
                }
            elif(prediction == 0):
                context = {
                    'result': 'Sad... Seems like you were unlucky'
                }
            return render(request, 'index.html', context)
