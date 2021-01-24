from django.conf.urls import url 
from apps.shipments import views 
 
urlpatterns = [ 
    url(r'^list/$', views.getAndFilterShipments_list),
]
