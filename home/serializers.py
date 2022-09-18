from rest_framework import serializers

from .models import BookList
from django.contrib.auth.models import User

class BookListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookList
        fields = "__all__"

class MemberListSerializer(serializers.ModelSerializer):
    password = serializers.CharField()
    class Meta:
        model = User
        fields = "__all__"

    
    
    def create(self,  validated_data):
        
        user = User.objects.create()
        for (key, value) in validated_data.items():
            setattr(user, key, value)
        

        
        user.set_password(validated_data['password'])
        user.save()

        return user


    def update(self, instance, validated_data):

        password = validated_data.pop('password', None)

        for (key, value) in validated_data.items():
            setattr(instance, key, value)

        if password is not None:
            instance.set_password(password)

        instance.save()

        return instance