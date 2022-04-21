from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Tag, JobType, Job, JobTypeLink, JobTagLink


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class JobTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobType
        fields = '__all__'


class JobTypeLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobTypeLink
        fields = '__all__'


class JobTagLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobTagLink
        fields = '__all__'
