from django.http import response
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Snack
from django.urls import reverse

# Create your tests here.
class SnackTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='test1', email='test1@gmail.com', password='test1234'
        )

        self.user_2 = get_user_model().objects.create_user(
            username='test2', email='test2@gmail.com', password='test1234'
        )

        self.snack = Snack.objects.create(
            title='test', purchaser=self.user, description='descriptions'
        )

    def test_model_representation(self):
        self.assertEqual(str(self.snack),'test')

    def test_model_content(self):
        self.assertEqual(self.snack.title,'test')
        self.assertEqual(str(self.snack.purchaser),'test1')
        self.assertEqual(self.snack.description,'descriptions')

    def test_snack_list_view(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'test')
        self.assertTemplateUsed(response,'snack_list.html')

    def test_snack_detail_view(self):
        url = reverse('snack_detail',args=['1'])
        response = self.client.get(url)
        no_response = self.client.get('/2/')
        self.assertEqual(response.status_code,200)
        self.assertEqual(no_response.status_code,404)
        self.assertContains(response,'descriptions')
        self.assertTemplateUsed(response,'snack_detail.html')

    def test_snack_create_view(self):
        url = reverse('snack_create')
        response_get = self.client.get(url)
        response_post = self.client.post(
            url,
            {
                'title':'testT2',
                'purchaser':self.user_2.id,
                'description': 'no onions'
            },
            follow=True
            )
        redirect_url = reverse('snack_detail',args=['2'])
        self.assertRedirects(response_post,redirect_url)
        self.assertContains(response_post,'testT2')
        self.assertTemplateUsed(response_post,'snack_detail.html')
        self.assertEqual(response_get.status_code,200)
        self.assertTemplateUsed(response_get,'snack_create.html')

    def test_snack_update_view(self):
        url = reverse('snack_update',args='1')
        response_get = self.client.get(url)
        response_post = self.client.post(
            url,
            {
                'title':'test',
                'purchaser':self.user.id,
                'description':'no salad'
            },
        )
        redirect_url = reverse('snack_detail',args='1')
        self.assertRedirects(response_post,redirect_url)
        self.assertEqual(response_get.status_code,200)
        self.assertTemplateUsed(response_get,'snack_update.html')

    def test_snack_delete_view(self):
        url = reverse('snack_delete',args='1')
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'snack_delete.html')