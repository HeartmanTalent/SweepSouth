from django.db import models
from django.utils.translation import ugettext_lazy as _
import uuid


class Tag(models.Model):
    title = models.CharField(_("Title"), max_length=100, unique=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          editable=False)

    class Meta:
        verbose_name_plural = "tags"

    def __str__(self):
        return "Tag: " + self.title


class JobType(models.Model):
    title = models.CharField(_("Title"), max_length=100, unique=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          editable=False)

    class Meta:
        verbose_name_plural = "job_types"

    def __str__(self):
        return "Job Type: " + self.title


class JobTagLink(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    job = models.ForeignKey(
        "core.Job", related_name="tag_job", on_delete=models.CASCADE)
    tag = models.ForeignKey(
        "core.Tag", related_name="tags", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "job_tag_links"
        unique_together = ('job', 'tag',)

    def __str__(self):
        return "Job Tag Link: " + str(self.id)


class JobTypeLink(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    job = models.ForeignKey(
        "core.Job", related_name="type_job", on_delete=models.CASCADE)
    job_types = models.ForeignKey(
        "core.JobType", related_name="job_types", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "job_type_links"
        unique_together = ('job', 'job_types',)

    def __str__(self):
        return "Job Type Link: " + str(self.id)


class Job(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = models.CharField(_("Slug"), max_length=500, null=True)
    company_name = models.CharField(
        _("Company Name"), max_length=500, null=True)
    title = models.CharField(_("Title"), max_length=500, null=True)
    description = models.TextField(blank=True, null=True)
    remote = models.BooleanField(_('Remote'), default=False)
    url = models.URLField(_("URL"))
    location = models.CharField(_("Location"), max_length=500, null=True)
    created_at = models.DateTimeField(_("Date Created"))

    class Meta:
        verbose_name_plural = "jobs"

    def __str__(self):
        return "Job: " + self.title
