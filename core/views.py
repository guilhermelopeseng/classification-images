from django.shortcuts import render
from django.http import HttpRequest 
from django.contrib import messages

import clothesClassification
from clothesClassification.settings import BASE_DIR

from .forms import ImageModelForm
from .models import Image

def index(request):
  form_valid = False
  if str(request.method) == 'POST':
    form = ImageModelForm(request.POST, request.FILES)
    if form.is_valid():
      form_valid = True
      form.save()
      message = f'Imagem enviada com sucessor, resultado retornado é: {Image.objects.all().last().predict}'
      filenameImage = Image.objects.all().last().image
      messages.success(request=request,message=message)
    else:
      messages.error(request, 'Erro ao enviar a imagem.')
    context = {
    'form': form,
    'image': filenameImage,
    'form_valid': form_valid
    }
    return render(request, 'index.html', context)
  else:
    form_valid = False
    form = ImageModelForm()
    context = {
    'form': form,
    'form_valid': form_valid
    }
    return render(request, 'index.html',context)