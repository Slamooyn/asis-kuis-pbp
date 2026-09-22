from django.test import TestCase, Client
from django.utils import timezone
from main.models import Experience


class MainTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_main_url_is_exist(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertContains(response, '/experience/')

    def test_nonexistent_page_returns_404(self):
        response = self.client.get('/nonexistent-page-url/')
        self.assertEqual(response.status_code, 404)

    def test_experience_model_and_is_ongoing_property(self):
        exp1 = Experience.objects.create(
            title='Backend Intern',
            description='Building APIs',
            category='internship',
        )
        self.assertEqual(str(exp1), 'Backend Intern')
        self.assertTrue(exp1.is_ongoing)

        exp2 = Experience.objects.create(
            title='Research Assistant',
            description='ML Research',
            category='research',
            ended_at=timezone.now(),
        )
        self.assertFalse(exp2.is_ongoing)

    def test_experience_page_shows_data(self):
        Experience.objects.create(
            title='Software Engineer',
            description='Working on Django project',
            category='full-time',
        )
        response = self.client.get('/experience/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'experience.html')
        self.assertContains(response, 'Software Engineer')

    def test_experience_page_empty_message(self):
        response = self.client.get('/experience/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Belum ada pengalaman yang ditambahkan.')

    def test_experience_finished_status_display(self):
        Experience.objects.create(
            title='Past Volunteer',
            description='Community helper',
            category='volunteer',
            ended_at=timezone.now(),
        )
        response = self.client.get('/experience/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Selesai')
