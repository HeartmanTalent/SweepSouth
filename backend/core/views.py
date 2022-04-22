from rest_framework import viewsets, generics
from django.contrib.auth.models import User
from core import serializers
from .models import Tag, JobType, Job, JobTypeLink, JobTagLink


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class JobViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.JobSerializer
    queryset = Job.objects.all()

    def get_queryset(self):
        """
        Optionally restricts the returned jobs by filtering against a `parameter` query parameter in the URL.
        """
        queryset = Job.objects.all()
        company = self.request.query_params.get("company")
        location = self.request.query_params.get("location")
        title = self.request.query_params.get("title")
        tag = self.request.query_params.get("tag")
        typ = self.request.query_params.get("type")

        if company is not None:
            queryset = queryset.filter(company_name__icontains=company)
        if location is not None:

            queryset = queryset.filter(location__icontains=location)
        if title is not None:
            queryset = queryset.filter(title__icontains=title)
        if tag is not None:
            tg = Tag.objects.filter(title=tag).first()
            if tg is not None:
                queryset = queryset.filter(tag_job__tag=tg)
            else:
                queryset = Job.objects.none()
        if typ is not None:
            jt = JobType.objects.filter(title=typ).first()
            if jt is not None:
                queryset = queryset.filter(type_job__job_types=jt)
            else:
                queryset = Job.objects.none()
        return queryset


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializer


class JobTypeViewSet(viewsets.ModelViewSet):
    queryset = JobType.objects.all()
    serializer_class = serializers.JobTypeSerializer


class JobTagLinkViewSet(viewsets.ModelViewSet):
    queryset = JobTagLink.objects.all()
    serializer_class = serializers.JobTagLinkSerializer


class JobTypeLinkiewSet(viewsets.ModelViewSet):
    queryset = JobTypeLink.objects.all()
    serializer_class = serializers.JobTypeLinkSerializer
