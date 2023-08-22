from django.test import TestCase, Client
from django.urls import reverse
from .models import Laboratorio

# Create your tests here.

class LaboratorioTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.laboratorio = Laboratorio.objects.create(
            nombre="Laboratorio A",
            ciudad="Ciudad A",
            pais="Pais A",
        )

    def test_model_creacion_laboratorio(self):
        self.assertEqual(self.laboratorio.nombre, "Laboratorio A")
        self.assertEqual(self.laboratorio.ciudad, "Ciudad A")
        self.assertEqual(self.laboratorio.pais, "Pais A")
         

    def test_vista_confirmacion(self):
        response = self.client.get(reverse('confirmacion', args=[self.laboratorio.id]))
        self.assertEqual(response.status_code, 200)

    def test_vista_informacion(self):
        response = self.client.get(reverse('informacion'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'informacion.html')
        self.assertContains(response, "Usted ha visitado esta página")
