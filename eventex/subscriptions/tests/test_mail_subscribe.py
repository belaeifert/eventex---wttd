from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):

    def setUp(self):
        data = dict(name='Testando Silva', cpf='12345678901',
                        email='teste@gmail.com', phone='0123')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato@eventex.com.br', 'teste@gmail.com']

        self.assertEqual(expect, self.email.to)


    def teste_subscription_email_body(self):
        email = mail.outbox[0]

        contents = ['Testando Silva', '12345678901', 'teste@gmail.com', '0123']

        for content in contents:
            with self.subTest():
                self.assertIn(content, email.body)

