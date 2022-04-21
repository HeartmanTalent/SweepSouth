import datetime
import json
import requests
from django.core.management.base import BaseCommand
from core.models import Job, JobType, Tag, JobTypeLink, JobTagLink
from django.utils.timezone import make_aware
from datetime import datetime


class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            response = requests.get(
                "https://www.arbeitnow.com/api/job-board-api")
            if response.status_code == 200:

                # avoid duplication when the system in initialised
                Job.objects.all().delete()
                JobType.objects.all().delete()
                Tag.objects.all().delete()
                JobTypeLink.objects.all().delete()
                JobTagLink.objects.all().delete()

                self.stdout.write(self.style.SUCCESS(
                    "Successfully cleaned the database"))
                data = json.loads(response.content)
                jobs = data["data"]
                tag_list = []
                job_type_list = []
                bulk_jobs = []
                t_list = []
                jt_list = []
                jtl_list = []
                jtk_list = []
                for job in jobs:
                    slug, company_name, title, description, remote, url, tags, job_types, location, created_at = job.values()
                    created_at = make_aware(datetime.fromtimestamp(created_at))
                    j = Job(slug=slug, company_name=company_name, title=title,
                            description=description, remote=remote, url=url, location=location, created_at=created_at)

                    for tag in tags:
                        if tag not in tag_list:  # avoid duplication of tags
                            t = Tag(title=tag)
                            jtk = JobTagLink(job=j, tag=t)
                            t_list.append(t)
                            jtk_list.append(jtk)
                            tag_list.append(tag)
                        else:
                            for t in t_list:
                                if t.title == tag:
                                    jtk = JobTagLink(job=j, tag=t)
                                    jtk_list.append(jtk)

                    for job_type in job_types:
                        if job_type not in job_type_list:   # avoid duplication of job types
                            jt = JobType(title=job_type)
                            jtl = JobTypeLink(job=j, job_types=jt)
                            jt_list.append(jt)
                            jtl_list.append(jtl)
                            job_type_list.append(job_type)
                        else:
                            for jt in jt_list:
                                if jt.title == tag:
                                    jtl = JobTypeLink(job=j, job_types=jt)
                                    jtl_list.append(jtl)

                    bulk_jobs.append(j)

                # bulk create of objects for performance , avoiding bulk create with when the list is empty
                # the order of creation matters for foreign keys
                if t_list:
                    Tag.objects.bulk_create(t_list)

                if jt_list:
                    JobType.objects.bulk_create(jt_list)

                if bulk_jobs:
                    Job.objects.bulk_create(bulk_jobs)

                if jtl_list:
                    JobTypeLink.objects.bulk_create(jtl_list)

                if jtk_list:
                    JobTagLink.objects.bulk_create(jtk_list)
                self.stdout.write(self.style.SUCCESS(
                    "Successfully added new data"))
            else:
                self.stdout.write(self.style.ERROR(
                    "Failed to load data, on error HTTP CODE : " + response.status_code))
        except Exception as e: # display the error for the developer 
            self.stdout.write(self.style.ERROR(
                              "Failed to load data due to: " + str(e)))
