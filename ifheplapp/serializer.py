from rest_framework import serializers
from EmployeeProfile.models import EmployeeProfile
from ifheplapp.models import Attendance, Slider
from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ('employeeID', 'employeeName',
                  'location', 'image', 'uploaded_at')

class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = ('title', 'image')


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = EmployeeProfile
        fields = ('id', 'name', 'phone_number', 'email', 'gender', 'emmloyeeid',
                  "designation", "job_location", 'bloodgroup', 'dob', 'Address', 'image')


class EmployeeRegistrationSerializer(serializers.ModelSerializer):

    profile = EmployeeSerializer(required=False)

    class Meta:
        model = User
        fields = ('profile',)

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create_user(username = profile_data['emmloyeeid'], email =profile_data['email'],  password = str(profile_data['dob']).replace("-",""))
        user.is_active = False
        user.save()
        EmployeeProfile.objects.create(
            user=user,
            emmloyeeid=profile_data['emmloyeeid'],
            email=profile_data['email'],
            name=profile_data['name'],
            phone_number=profile_data['phone_number'],
            gender=profile_data['gender'],
            designation=profile_data['designation'],
            job_location=profile_data['job_location'],
            bloodgroup=profile_data['bloodgroup'],
            dob=profile_data['dob'],
            Address=profile_data['Address'],
            image=profile_data['image']
        )
        return user


WT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER


class UserLoginSerializer(serializers.Serializer):

    username = serializers.CharField(max_length=14)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        username = data.get("username", None)
        password = data.get("password", None)
        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError(
                'A user with this username and password is not found.'
            )
        try:
            payload = WT_PAYLOAD_HANDLER(user)
            jwt_token = JWT_ENCODE_HANDLER(payload)
            update_last_login(None, user)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                'User with given email and password does not exists'
            )
        return {
            'username': user.username,
            'token': jwt_token
        }
