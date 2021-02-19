from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
import numpy as np
import matplotlib as pl
pl.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sb
import os
 
# Create your views here.
class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)
 
class LinksPageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'links.html', context=None)

class Customers(TemplateView):
    def getCust(request):
        name='liran'
        return HttpResponse('{ "name":"' + name + '", "age":31, "city":"New York" }')
    
    def getNums(request):
        n = np.array([2, 3, 4])
        name1 = "avi-" + str(n[1])
        return HttpResponse('{ "name":"' + name1 + '", "age":31, "city":"New York" }')

    def getAvg(request):
        s1=request.GET.get("val","")
        if len(s1)==0:
            return HttpResponse("none")
        l1=s1.split(',')
        ar=np.array(l1,dtype=int)
 
        return HttpResponse(str(np.average(ar)))
    
    def getImage(request):
        x = np.arange(0, 2 * np.pi, 0.01)
        y = np.cos(x) ** 2
        plt.plot(x, y)
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.title('Graph of cos^2(x)!')
        plt.grid(True)
        response = HttpResponse(content_type="image/jpeg")
        plt.savefig(response, format="png")
        return response

    def getSine(request):
        multiplier=request.GET.get("val","")
        ll=multiplier.split(',')
        arr1=np.array(ll,dtype=int)
        x = np.arange(0, 2 * np.pi, 0.01)
        y = np.sin(x*arr1[0])
        plt.plot(x, y)
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.title('Graph of your sine wave!')
        plt.grid(True)
        response = HttpResponse(content_type="image/jpeg")
        plt.savefig(response, format="png")
        return response

    def getData(request):
        samp = np.random.randint(100, 600, size=(4, 5))
        df = pd.DataFrame(samp, index=['avi', 'dani', 'rina', 'dina'],
                          columns=['Jan', 'Feb', 'Mar', 'Apr', 'May'])
        return HttpResponse(df.to_html(classes='table table-bordered'))

    def getSBData(request):
        module_dir = os.path.dirname(__file__)
        file_path = os.path.join(module_dir, 'tested.csv')
        df = pd.read_csv(file_path)
        gr=sb.factorplot(x='Survived', hue='Sex', data=df, col='Pclass', kind='count')
        response = HttpResponse(content_type="image/jpeg")
        gr.savefig(response, format="png")
        return response