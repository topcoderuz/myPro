from django.test import TestCase
from django.urls import reverse
from .models import Post

# Create your tests here.
class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(title = 'Sarlavha', text = 'Yangilish shu shaklda namoyish etiladi')
    
    def test_text_content(self):
        post = Post.objects.get(id=1)
        excepted_object_title = f'{post.title}'
        excepted_object_text = f'{post.text}'
        self.assertEqual(excepted_object_title, 'Sarlavha')
        self.assertEqual(excepted_object_text, 'Yangilish shu shaklda namoyish etiladi')

class NewsPageView(TestCase):
    def setUp(self):
        Post.objects.create(title = 'Sarlavha', text = 'Yangilish shu shaklda namoyish etiladi')

    def test_views_url_exists_at_proper_location(self):
        resp = self.client.get(reverse('news'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'news.html')