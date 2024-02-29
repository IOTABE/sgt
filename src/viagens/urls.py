from django.urls import path
from . import views


urlpatterns = [
    path("viagem",views.ViagensListView.as_view(), name='t_lista'),
    path("cad_viagem",views.cad_viagem, name='t_inclue'),
    path('det_viagem/<int:pk>', views.ViagensDetailView.as_view() , name='det_viagem'),
    path('del_viagem/<int:pk>', views.ViagensDeleteView.as_view() , name='del_viagem'),
    path('upd_viagem/<int:pk>', views.ViagensUpdateView.as_view() , name='upd_viagem'),       
    
]