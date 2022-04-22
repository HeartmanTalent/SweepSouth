from model_bakery import baker
from datetime import datetime
from io import StringIO
from rest_framework.test import APITestCase, RequestsClient
from rest_framework import status
from django.test import TestCase
from django.utils.timezone import make_aware
from django.contrib.auth.models import User
from django.core.management import call_command
from .models import Job, Tag
from .views import TagViewSet


class JobTestCase(TestCase):
    def setUp(self):
        Job.objects.create(
            slug="this is slug",
            company_name="sweep south",
            title="Senior Full Stack Developer",
            description="Wir suchen Dich ab sofort als: \
            EVENTMANAGER (m/w/d)(Level: Senior/Junior/Trainee) an  \
            unserem Standort in 58313 Herdecke Du hast noch keine oder \
            erst wenig Erfahrung in diesem Bereich?Dann starte jetzt  \
            gerne als Quereinsteiger oder Trainee bei uns durch. W \
             as wir bieten: Eine abwechslungsreiche Tätigkeit in einem modernen JobEine",
            url="https://www.arbeitnow.com/view/eventmanager-senior\
            -junior-trainee-atz-marketing-solutions-gmbh-herdecke-germany-299169",
            location="Berlin",
            created_at=make_aware(
                datetime.fromtimestamp(1650611057))
        )

    def test_job_created(self):
        """A job that was created correctly is correctly identified"""
        exists = Job.objects.filter(
            title="Senior Full Stack Developer").exists()
        self.assertEqual(exists, True)

    def test_model_str(self):
        job = Job.objects.filter(
            title="Senior Full Stack Developer").first()
        self.assertEqual(str(job), "Job: Senior Full Stack Developer")

    def test_crowded_job(self):
        job = baker.make(
            Job, title="Plumber wanted")
        self.assertEqual(str(job), "Job: Plumber wanted")

    def test_can_send_message(self):
        response = self.client.get("/api/jobs/?title=Senior")
        self.assertEqual(len(response.data), 1)
        response = self.client.get(
            "/api/jobs/id/ce3a7651-f05d-47e5-9bda-9bb9f99fe085")
        self.assertEqual(response.status_code, 404)


class TestUserAPI(APITestCase):
    def test_anonymous_cannot_see_users(self):
        response = self.client.get("/api/users/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_authenticated_user_can_see_users(self):
        user = User.objects.create_user(
            "Heartman," "heartman@dev.io", "demo_pass")
        self.client.force_login(user=user)
        response = self.client.get("/api/users/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_request_can_create_new_tag(self):
        data = {
            "title": "Maid",
        }
        self.client.post("/api/tags", data=data)
        self.assertEqual(Tag.objects.count(), 0)


class TestTagAPI(APITestCase):
    def test_tag_api(self):
        response = self.client.get('/api/tags/')
        self.assertEqual(response.status_code, 200)

class CommandsTestCase(TestCase):
    def call_command(self, *args, **kwargs):
        out = StringIO()
        call_command(
            "InitializeData",
            *args,
            stdout=out,
            stderr=StringIO(),
            **kwargs,
        )
        return out.getvalue()

    def test_dry_run(self):
        out = self.call_command()
        self.assertEqual(out, "Successfully added new data\n")
