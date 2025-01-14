from django.test import TestCase
from .models import Mercancia

class MercanciaTestCase(TestCase):
    def setUp(self):
        # Crear algunos datos de prueba si es necesario
        pass

    def test_create_mercancia(self):
        mercancia = Mercancia.objects.create(
            nombre='Producto de prueba',
            descripcion='Descripción del producto',
            precio_unitario=10.99,
            qr_number='ABCD123',
            stock=10
        )
        self.assertEqual(mercancia.nombre, 'Producto de prueba')

    def test_precio_unitario_positivo(self):
        with self.assertRaises(ValidationError):
            Mercancia.objects.create(
                nombre='Producto negativo',
                precio_unitario=-5
            )

    # Agrega más pruebas para cubrir otros escenarios

    def test_nombre_unico(self):
        # Prueba que no se puedan crear dos mercancías con el mismo nombre
        pass

