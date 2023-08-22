from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Laboratorio
from .forms import LaboratorioForm

# Create your views here.

class IndexPageView(TemplateView):
    template_name = 'base.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = LaboratorioForm()
        return context
    
    def post(self, request, *args, **kwargs):
        form = LaboratorioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('informacion')
        else:
            context = self.get_context_data()
            context['form'] = form
            return self.render_to_response(context)
   
def informacion(request):
    visitas = request.session.get('visitas_informacion', 0)
    visitas += 1
    request.session['visitas_informacion'] = visitas
    Laboratorios = Laboratorio.objects.all() 
    context = {'Laboratorios': Laboratorios, 'visitas_informacion': visitas}
    return render(request, 'informacion.html', context)

def actualizar(request, laboratorio_id):
    laboratorio = Laboratorio.objects.get(id=laboratorio_id)

    if request.method == 'POST':
        form = LaboratorioForm(request.POST, instance=laboratorio)
        if form.is_valid():
            form.save()
            return redirect('informacion')

    else:
        form = LaboratorioForm(instance=laboratorio)

    context = {'form': form}
    return render(request, 'actualizar.html', context)


def confirmacion(request, laboratorio_id):
    laboratorio = Laboratorio.objects.get(id=laboratorio_id)

    if request.method == 'POST':
        laboratorio.delete()
        return redirect('informacion')

    context = {'laboratorio': laboratorio}
    return render(request, 'confirmacion.html', context)