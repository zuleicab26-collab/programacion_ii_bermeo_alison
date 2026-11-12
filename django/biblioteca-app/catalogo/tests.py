from datetime import date

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from catalogo.forms.libro_form import LibroForm
from catalogo.models import Autor, Categoria, Libro


class FlujoBibliotecaTests(TestCase):
    def setUp(self):
        self.admin = User.objects.create_superuser('admin', 'a@a.com', 'clave12345')
        self.cat = Categoria.objects.create(nombre='Novela')
        self.autor = Autor.objects.create(
            nombre='García',
            apellido='Márquez',
        )
        self.libro = Libro.objects.create(
            titulo='Cien años', autor=self.autor, categoria=self.cat,
            fecha_publicacion=date(1967, 5, 30), isbn='0060883286000')

    def test_login_requerido(self):
        r = self.client.get(reverse('home'))
        self.assertRedirects(r, '/cuentas/login/?next=/')

    def test_login_y_home(self):
        r = self.client.get(reverse('login'))
        self.assertContains(r, 'type="submit"')
        r = self.client.post(reverse('login'), {'username': 'admin', 'password': 'clave12345'})
        self.assertRedirects(r, reverse('home'))
        self.assertContains(self.client.get(reverse('home')), 'Bienvenido a la Biblioteca')

    def test_logout(self):
        self.client.force_login(self.admin)
        r = self.client.post(reverse('logout'))
        self.assertRedirects(r, reverse('home'), fetch_redirect_response=False)

    def test_paginas_get(self):
        self.client.force_login(self.admin)
        for name, args in [
            ('libro_list', []), ('create_libro', []), ('update_libro', [self.libro.pk]),
            ('delete_libro', [self.libro.pk]), ('categoria_list', []),
            ('categoria_create', []), ('categoria_update', [self.cat.pk]),
            ('categoria_delete', [self.cat.pk]), ('autor_list', []),
            ('autor_create', []),
        ]:
            with self.subTest(name):
                self.assertEqual(self.client.get(reverse(name, args=args)).status_code, 200)

    def test_listado_filtros(self):
        self.client.force_login(self.admin)
        r = self.client.get(reverse('libro_list'), {'pista': 'cien', 'categoria_id': self.cat.pk})
        self.assertContains(r, 'Cien años')
        self.assertContains(r, '<option value="%d"' % self.cat.pk)
        r = self.client.get(reverse('libro_list'), {'pista': 'zzz'})
        self.assertContains(r, 'No hay libros disponibles')

    def test_crud_libro(self):
        self.client.force_login(self.admin)
        datos = {'titulo': 'Otro', 'autor': self.autor.pk, 'categoria': self.cat.pk,
                 'fecha_publicacion': '2000-01-01', 'isbn': '1234567890123'}
        self.assertRedirects(self.client.post(reverse('create_libro'), datos), reverse('libro_list'))
        nuevo = Libro.objects.get(isbn='1234567890123')
        datos['titulo'] = 'Editado'
        self.client.post(reverse('update_libro', args=[nuevo.pk]), datos)
        nuevo.refresh_from_db()
        self.assertEqual(nuevo.titulo, 'Editado')
        self.client.post(reverse('delete_libro', args=[nuevo.pk]))
        self.assertFalse(Libro.objects.filter(pk=nuevo.pk).exists())

    def test_libro_form_valida_isbn_y_fecha(self):
        datos = {
            'titulo': 'Otro',
            'autor': self.autor.pk,
            'categoria': self.cat.pk,
            'fecha_publicacion': '2000-01-01',
            'isbn': '1234567890123',
        }
        self.assertTrue(LibroForm(data=datos).is_valid())

        datos['isbn'] = '123'
        form = LibroForm(data=datos)
        self.assertFalse(form.is_valid())
        self.assertIn('isbn', form.errors)

        datos['isbn'] = '1234567890123'
        datos['fecha_publicacion'] = '2999-01-01'
        form = LibroForm(data=datos)
        self.assertFalse(form.is_valid())
        self.assertIn('fecha_publicacion', form.errors)

    def test_formulario_libro_muestra_errores_como_en_ejemplo(self):
        self.client.force_login(self.admin)
        response = self.client.post(
            reverse('create_libro'),
            {
                'titulo': 'Programación funcional',
                'autor': self.autor.pk,
                'fecha_publicacion': '2999-12-12',
                'categoria': self.cat.pk,
                'isbn': '123',
            },
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<h1>Crear Libro</h1>')
        self.assertContains(response, 'La fecha de publicación no puede ser futura.')
        self.assertContains(response, 'El ISBN debe tener 13 dígitos y ser numérico.')

    def test_crud_categoria_y_proteccion(self):
        self.client.force_login(self.admin)
        self.client.post(reverse('categoria_create'), {'nombre': 'Ciencia', 'descripcion': ''})
        c = Categoria.objects.get(nombre='Ciencia')
        self.client.post(reverse('categoria_update', args=[c.pk]), {'nombre': 'Ciencias', 'descripcion': 'x'})
        c.refresh_from_db()
        self.assertEqual(c.nombre, 'Ciencias')
        self.client.post(reverse('categoria_delete', args=[c.pk]))
        self.assertFalse(Categoria.objects.filter(pk=c.pk).exists())
        # categoría con libros no se puede eliminar
        self.client.post(reverse('categoria_delete', args=[self.cat.pk]))
        self.assertTrue(Categoria.objects.filter(pk=self.cat.pk).exists())

    def test_crud_autor_y_proteccion(self):
        self.client.force_login(self.admin)
        datos = {'nombre': 'Gabriel', 'apellido': 'Márquez'}
        self.assertRedirects(
            self.client.post(reverse('autor_create'), datos),
            reverse('autor_list'),
        )
        autor = Autor.objects.get(nombre='Gabriel', apellido='Márquez')
        datos['nombre'] = 'Gabriel José'
        self.assertRedirects(
            self.client.post(reverse('autor_update', args=[autor.pk]), datos),
            reverse('autor_list'),
        )
        autor.refresh_from_db()
        self.assertEqual(autor.nombre, 'Gabriel José')

        self.libro.autor = autor
        self.libro.save()
        self.client.post(reverse('autor_delete', args=[autor.pk]))
        self.assertTrue(Autor.objects.filter(pk=autor.pk).exists())

        otro_autor = Autor.objects.create(nombre='Autor', apellido='Libre')
        self.client.post(reverse('autor_delete', args=[otro_autor.pk]))
        self.assertFalse(Autor.objects.filter(pk=otro_autor.pk).exists())

    def test_listado_autores_muestra_tabla_y_navegacion(self):
        self.client.force_login(self.admin)
        autor = Autor.objects.create(
            nombre='Pablo',
            apellido='Escobar',
            nacionalidad='Colombiano',
        )

        response = self.client.get(reverse('autor_list'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<h1>Biblioteca</h1>')
        self.assertContains(response, '<h2>Listado de Autores</h2>')
        self.assertContains(response, '<th>ID</th>')
        self.assertContains(response, '<th>Nombre</th>')
        self.assertContains(response, '<th>Apellido</th>')
        self.assertContains(response, '<th>Nacionalidad</th>')
        self.assertContains(response, 'Colombiano')
        self.assertContains(response, reverse('libro_list'))
        self.assertContains(response, reverse('home'))
        self.assertContains(response, reverse('autor_update', args=[autor.pk]))

    def test_sin_permisos(self):
        User.objects.create_user('lector', password='clave12345')
        self.client.login(username='lector', password='clave12345')
        self.assertEqual(self.client.get(reverse('create_libro')).status_code, 403)
        self.assertEqual(self.client.get(reverse('categoria_list')).status_code, 403)
        self.assertEqual(self.client.get(reverse('libro_list')).status_code, 200)
