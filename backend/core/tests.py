from datetime import datetime
from django.test import TestCase
from django.utils.timezone import make_aware
from .models import Job


class JobTestCase(TestCase):
    def setUp(self):
        Job.objects.create(
            slug="this is slug",
            company_name="sweep south",
            title="Senior Fullstake Developer",
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
            title="Senior Fullstake Developer").exists()
        self.assertEqual(exists, True)
