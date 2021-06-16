from django.http import response
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Snack
from django.urls import reverse

# Create your tests here.
class SnackTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='aboud', email='aboud@gmail.com', password='aboud1234'
        )

        self.user_2 = get_user_model().objects.create_user(
            username='hamza', email='hamza@gmail.com', password='hamza1234'
        )

        self.snack = Snack.objects.create(
            title='falafel', purchaser=self.user, description='extra homos'
        )

    def test_model_representation(self):
        self.assertEqual(str(self.snack),'falafel')

    def test_model_content(self):
        self.assertEqual(self.snack.title,'falafel')
        self.assertEqual(str(self.snack.purchaser),'aboud')
        self.assertEqual(self.snack.description,'extra homos')

    def test_snack_list_view(self):
        url = reverse('snack_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'falafel')
        self.assertTemplateUsed(response,'snack_list.html')

    def test_snack_detail_view(self):
        url = reverse('snack_detail',args=['1'])
        response = self.client.get(url)
        no_response = self.client.get('/2/')
        self.assertEqual(response.status_code,200)
        self.assertEqual(no_response.status_code,404)
        self.assertContains(response,'extra homos')
        self.assertTemplateUsed(response,'snack_detail.html')

    def test_snack_ceate_view(self):
        url = reverse('snack_create')
        response_get = self.client.get(url)
        response_post = self.client.post(
            url,
            {
                'title':'fahita',
                'purchaser':self.user_2.id,
                'description': 'no onions'
            },
            follow=True
            )
        redirct_url = reverse('snack_detail',args=['2'])
        self.assertRedirects(response_post,redirct_url)
        self.assertContains(response_post,'fahita')
        self.assertTemplateUsed(response_post,'snack_detail.html')
        self.assertEqual(response_get.status_code,200)
        self.assertTemplateUsed(response_get,'snack_create.html')

    def test_snack_update_view(self):
        url = reverse('snack_update',args='1')
        response_get = self.client.get(url)
        response_post = self.client.post(
            url,
            {
                'title':'falafel',
                'purchaser':self.user.id,
                'description':'no salad'
            },
        )
        redirct_url = reverse('snack_detail',args='1')
        self.assertRedirects(response_post,redirct_url)
        self.assertEqual(response_get.status_code,200)
        self.assertTemplateUsed(response_get,'snack_update.html')

    def test_snack_delete_view(self):
        url = reverse('snack_delete',args='1')
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'snack_delete.html')