from __future__ import absolute_import, unicode_literals
import unittest
from google.appengine.ext import ndb
from base import GAETestCase
from mock import Mock
from web.curso import rest
from web.curso.rest import Curso


class RestTests(GAETestCase):
    def test_salvar(self):
        rest.salvar("Python Pro","323.33")
        lista = Curso.query().fetch()
        self.assertEqual(1,len(lista))
        curso = lista[0]
        self.assertEqual("Python Pro",curso.nome)
        self.assertEqual(323.33,curso.preco)

    def test_listar(self):
        cursos = [Curso(nome="Python pra quem sabe Python",preco=323.45),
                  Curso (nome="Python pra quem estudou Java",preco=383.35)]
        ndb.put_multi(cursos)
        resp = Mock()
        rest.listar(resp)
        resp.write.assert_called_onde_with("")

