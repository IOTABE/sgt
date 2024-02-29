from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='inicio'),
    path("motoristas",views.MotoristaListView.as_view(), name='m_lista'),
    path("cad_motorista",views.cad_motorista, name='m_inclue'),
    path('det_motorista/<int:pk>', views.MotoristaDetailView.as_view() , name='det_motorista'),
    path('del_motorista/<int:pk>', views.MotoristaDeleteView.as_view() , name='del_motorista'),
    path('upd_motorista/<int:pk>', views.MotoristaUpdateView.as_view() , name='upd_motorista'),       
    
    path("veiculo",views.VeiculoListView.as_view(), name='v_lista'),
    path("cad_veiculo",views.cad_veiculo, name='v_inclue'),
    path('det_veiculo/<int:pk>', views.VeiculoDetailView.as_view() , name='det_veiculo'),
    path('del_veiculo/<int:pk>', views.VeiculoDeleteView.as_view() , name='del_veiculo'),
    path('upd_veiculo/<int:pk>', views.VeiculoUpdateView.as_view() , name='upd_veiculo'),      

    path("setor",views.SetorListView.as_view(), name='s_lista'),
    path("cad_setor",views.cad_setor, name='s_inclue'),
    path('det_setor/<int:pk>', views.SetorDetailView.as_view() , name='det_setor'),
    path('del_setor/<int:pk>', views.SetorDeleteView.as_view() , name='del_setor'),
    path('upd_setor/<int:pk>', views.SetorUpdateView.as_view() , name='upd_setor'),       
        
        
]
