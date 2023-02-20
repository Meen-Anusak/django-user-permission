from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import Group, Permission
from rest_framework.views import exception_handler
from member.models import Member
from rest_framework.permissions import DjangoModelPermissions

# Create your views here.

def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        response.data['status_code'] = response.status_code

    return response


class GetPermission(APIView):
    permission_classes = (DjangoModelPermissions,)

    
    def get(self,request):
        try:
            permissions_group = Group.objects.get(name='member_crud')
            member = Member.objects.filter(email='admin@mail.com').first()
            
            if not permissions_group:
                raise

            permissions_group.user_set.add(member)
            return Response({
                'status': 'errors',
                'code': '200',
                'message':'permission match'
            })

        except Exception as e:
  
            return Response({
                'status': 'errors',
                'code': '404',
                'message':'{0}'.format(e)
            })
            
            


