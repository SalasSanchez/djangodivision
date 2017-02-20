from django.test import TestCase
from .views import get_result
from django.test import Client



class DivisionTestCase(TestCase):
    def test_division1(self):
        dividend = 243856
        divisor = 432
        self.assertEqual(get_result(dividend, divisor), 564.4814814814815)

    def test_division2(self):
        dividend = 432.65895
        divisor = 3954872.432
        self.assertEqual(get_result(dividend, divisor), 0.00010939896480585142)

    def test_division3(self):
        dividend = 243
        divisor = 3
        self.assertEqual(get_result(dividend, divisor), 81.0)

    def test_division4(self):
        dividend = 0
        divisor = 3345
        self.assertEqual(get_result(dividend, divisor), 0)

    def test_post(self):
        client = Client()
        response = client.post('/division/', {'dividend': 102345, 'divisor': 43})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['division']['result'], 2380.1162790697676)


