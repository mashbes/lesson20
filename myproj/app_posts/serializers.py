from rest_framework import serializers
from .models import Post, Category
from django.contrib.auth.models import User


class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    status = serializers.ChoiceField(choices=Post.STATUSES, default=Post.STATUS_DRAFT)
    category = serializers.IntegerField(source="category_id")
    user = serializers.IntegerField(source="user_id")
    title = serializers.CharField(max_length=255, required=True)
    content = serializers.CharField(required=True)
    created_on = serializers.DateTimeField(read_only=True)
    updated_on = serializers.DateTimeField(read_only=True)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.category_id = validated_data['category']['id']
        instance.save()
        return instance

    def create(self, validated_data):
        return Post.objects.create(**validated_data)


class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    description = serializers.CharField(max_length=255)
    is_active = serializers.BooleanField()
    user = serializers.IntegerField(source="user_id")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'date-joined']
