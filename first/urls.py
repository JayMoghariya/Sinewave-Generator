from django.conf.urls import url
from first import views
 
urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^links/$' , views.LinksPageView.as_view()),
    url(r'^getcust/$',views.Customers.getCust),
    url(r'^getnums/$',views.Customers.getNums),
    url(r'^getavg/$',views.Customers.getAvg),
    url(r'^getimg/$',views.Customers.getImage),
    url(r'^getdata/$',views.Customers.getData),
    url(r'^getsbdata/$', views.Customers.getSBData),
    url(r'^getsine/$',views.Customers.getSine),
]