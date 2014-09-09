from django.shortcuts import render, redirect

#Django User model is used to save users
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from assignment.forms import *
from assignment.models import *
from django.contrib.auth.decorators import login_required

import random
import datetime
import time
from time import mktime
from datetime import datetime
import os
import re

import csv
from django.conf import settings

# Method to render the about display
def about(request):
  return render(request, 'assignment/about.html')

# Method to display the charts once a user has logged in 
@login_required
def displayCharts(request, stock=None):
  context = {}
  fields=("date", "open", "high", "low", "close", "volume", "adjClose")
  if stock == None:
    stock = "apple"
  
  #Using Django's ORM to obtain the csv file name
  try:
    file_obj = File.objects.get(company=stock)
  except File.DoesNotExist:
    context['issue'] = "Please enter a valid name. Defaulting to Apple."
    file_obj = File.objects.get(company="apple")

  c=open(os.path.join(settings.MEDIA_ROOT,file_obj.docfile.name), 'r')
  csvReader = csv.DictReader(c,fields)
  x = file_obj.company
  x = x.split(" ")
  name = ""

  for word in x:
    name = name + word[0].upper() + word[1:len(word)] + " "

  context['key'] = name

  #x and y data points
  xd =[]
  yd = []

  r = re.compile("[A-Z][a-z]")

  for row in csvReader:
    if r.match(row['date']):
      continue
    struct = time.strptime(row['date'], "%Y-%m-%d")
    struct = datetime.fromtimestamp(mktime(struct))
    xd.append(int(time.mktime(struct.timetuple()) * 1000))
    yd.append(float(row['close']))

  context['x'] = xd
  context['y'] = yd
  return render(request, 'assignment/piechart.html', context)

def register(request):
  context = {}
  # Just display the registration form if this is a GET request.
  if request.method == 'GET':
    context['form'] = RegistrationForm()
    return render(request, 'assignment/register.html', context)

  # Creates a bound form from the request POST parameters and makes the 
  # form available in the request context dictionary.
  form = RegistrationForm(request.POST)
  context['form'] = form

  # Validates the form.
  if not form.is_valid():
    context['form'] = form
    return render(request, 'assignment/register.html', context)

  # If we get here the form data was valid.  Register and login the user.
  new_user = User.objects.create_user(username=form.cleaned_data['email'], 
                                      password=form.cleaned_data['password'])
  new_user.save()

  # Logs in the new user and redirects to his/her todo list
  new_user = authenticate(username=form.cleaned_data['email'], \
                          password=form.cleaned_data['password'])
  login(request, new_user)
  return redirect('/charts/apple')

@login_required
def search(request):
  if 'searchIn' in request.POST:
    query = request.POST['searchIn']
    return redirect('charts/'+query)
  return render(request, 'assignment/404.html')

@login_required
def upload(request):
  # Handle file upload
  if request.method == 'POST':
    form = DocumentForm(request.POST, request.FILES)
    if form.is_valid():
      newdoc = File(docfile=request.FILES['docfile'], company=request.POST['companyName'], 
        stockId=request.POST['stockId'])
      newdoc.save()
      return redirect('charts/'+request.POST['companyName'])

  else:
    form = DocumentForm() # A empty, unbound form

  return render(request, 'assignment/upload.html', {'form': form})


#Helps raise 404 for url's that are not routed
def raise404(request):
  return render(request, 'assignment/404.html')

  


