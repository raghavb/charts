from django.db import models

#The File model is the only database table
#The stock_id is a primary key as it has to be unique
#The company's name can be used to search for this,
#which in turn will lead to the css file in the form:
#(stock_id).csv

class File(models.Model):
    stockId = models.CharField(max_length=30, primary_key=True, )
    company = models.CharField(max_length=30)
    docfile = models.FileField(upload_to='csv/')

