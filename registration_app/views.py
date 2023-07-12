from django.shortcuts import render
from django.views.generic import View, TemplateView
from .models import Topic, Webpage, AccessRecords
from . import forms
# Create your views here.

class IndexView(TemplateView):
    template_name = 'registration_app/index.html'

def webpg(request):
    webpg_list = AccessRecords.objects.order_by('date')
    date_dict = {'access_records': webpg_list}
    return render(request, 'registration_app/webpg.html', context=date_dict)



def login(request):
    return render(request, 'registration_app/login.html')

def formView(request):
    form = forms.FormName()

    if request.method == 'POST':
        form = forms.FormName(request.POST)

        if form.is_valid():

            print('Validation Success!')
            print('Name: '+form.cleaned_data['name'])
        else:
            print('Validation insuccesful')
    return render(request, 'registration_app/form.html', {'form' : form})