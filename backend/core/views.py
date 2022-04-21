from rest_framework import viewsets
from django.contrib.auth.models import User
from core import serializers
from .models import Tag, JobType, Job, JobTypeLink, JobTagLink


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = serializers.JobSerializer


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
