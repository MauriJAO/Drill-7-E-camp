from django.urls import path
from .views import IndexPageView, informacion, actualizar, confirmacion

urlpatterns = [
    path('', IndexPageView.as_view(), name="index"),
    path('informacion/',informacion , name="informacion"),
    path('actualizar/<int:laboratorio_id>/', actualizar, name='actualizar'),
    path('confirmacion/<int:laboratorio_id>/', confirmacion, name='confirmacion')
    
]
