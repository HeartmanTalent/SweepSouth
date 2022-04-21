from django.contrib import admin
from .models import Tag, JobType, Job, JobTypeLink, JobTagLink

admin.site.register(Job)
admin.site.register(Tag)
admin.site.register(JobType)
admin.site.register(JobTagLink)
admin.site.register(JobTypeLink)
