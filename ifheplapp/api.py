from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from ifheplapp.models import Slider
from ifheplapp.serializer import AttendanceSerializer, EmployeeRegistrationSerializer, SliderSerializer, UserLoginSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from EmployeeProfile.models import EmployeeProfile


class AttendanceView(CreateAPIView):

    serializer_class = AttendanceSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        status_code = status.HTTP_201_CREATED
        response = {
            'success': 'True',
            'status code': status_code,
            'message': 'Attendance Submitted successfully',
        }

        return Response(response, status=status_code)


class EmployeeRegistrationView(CreateAPIView):

    serializer_class = EmployeeRegistrationSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        status_code = status.HTTP_201_CREATED
        response = {
            'success': 'True',
            'status code': status_code,
            'message': 'User registered  successfully',
        }

        return Response(response, status=status_code)


class UserLoginView(CreateAPIView):

    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        response = {
            'success': 'True',
            'status code': status.HTTP_200_OK,
            'message': 'User logged in  successfully',
            'token': serializer.data['token'],
        }
        status_code = status.HTTP_200_OK

        return Response(response, status=status_code)


class UserProfileView(RetrieveAPIView):

    permission_classes = (IsAuthenticated,)
    authentication_class = JSONWebTokenAuthentication

    def get(self, request):
        try:
            user_profile = EmployeeProfile.objects.get(user=request.user)
            status_code = status.HTTP_200_OK
            response = {
                'success': 'true',
                'status code': status_code,
                'message': 'User profile fetched successfully',
                'data': [{
                    'emmloyeeid': user_profile.emmloyeeid,
                    'name': user_profile.name,
                    'email': user_profile.email,
                    'phone_number': user_profile.phone_number,
                    'gender': user_profile.gender,
                    'bloodgroup': user_profile.bloodgroup,
                    'dob': user_profile.dob,
                    'job_location': user_profile.job_location,
                    'designation': user_profile.designation,
                    'dob': user_profile.dob,
                    'Address': user_profile.Address,
                    'image': "https://ifhepl.in"+user_profile.image.url,
                }]
            }

        except Exception as e:
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                'success': 'false',
                'status code': status.HTTP_400_BAD_REQUEST,
                'message': 'User does not exists',
                'error': str(e)
            }
        return Response(response, status=status_code)

class SliderList(ListAPIView):
    """
    List all snippets, or create a new snippet.
    """
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer
    permission_classes = (AllowAny,)