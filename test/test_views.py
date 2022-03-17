from unittest import TestCase
from base.views import AuthorViewSet
from rest_framework.test import APIClient
from base.models import Author

class TestAuthorAPI(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_all(self):
        author = self.client.get('/author/1/')
        print(author.data)
        self.assertTrue(author.status_code==200)
        # self.assertEqual(author.data['name'], "Jasur Umirov")
        self.assertIsNotNone(author.data['id'])

    # def test_post(self):
    #     data = {
    #         "name":"Adel",
    #         "age":"30",
    #         "count":"USA",
    #         "track":"Hello"
    #     }
    #     new = self.client.post('/author/',data)
    #     self.assertEqual(new.status_code, 201)
    #     self.assertIsNotNone(new.data['id']==Author.objects.last().id)
    #     self.assertFalse(new.data['name']!="Adel")

    # def put(self):
    #     data = {
    #         'id': 14,
    #         'name': 'Adel',
    #         'age': 30, 
    #         'count': 'USA', 
    #         'track': 'Hello'
    #     }
    #     result = self.client.put('/author/11/')
    #     self.assertEqual(result.data['id'],11)
    #     self.assertTrue(result.data['name']=='Adel')

    def test_delete(self):
        author = self.client.delete('/author/1/')
        self.assertEqual(author.status_code, 204)
        

