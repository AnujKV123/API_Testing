# http://127.0.0.1:8000/VerifyOTP
# http://127.0.0.1:8000/SaveOTPContact


from django.shortcuts import HttpResponse
from rest_framework.decorators import api_view
from rest_framework import status
from .models import OTPcontact
from .serializers import verify_serializers

from rest_framework.response import Response
import random, math
# from twilio.rest import Client

# Create your views here.
def home(request):
    return HttpResponse('server not found')

@api_view(['POST'])
def SaveOTPContact(request):
    if request.method == 'POST':
        print(request.data)
        contactX = request.data
        contact = contactX['Contact']
        name= contactX['Name']
        email = contactX['Email']
        string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        otp = ""
        length = len(string)
        for i in range(6) :
            otp += string[math.floor(random.random() * length)]
        if(OTPcontact.objects.filter(Contact=contact)):
            OTPcontact.objects.filter(Contact=contact).update(OTP = otp)
            request.session['MatchContact'] = contact
            return Response(status=status.HTTP_201_CREATED)
        else:
            createOTP = OTPcontact(Contact = contact, OTP = otp, Name = name, Email = email)
            createOTP.save()
            request.session['MatchContact'] = contact
            request.session['MatchOTP'] = otp
            return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def VerifyOTP(request):
        snippets = OTPcontact.objects.all()
        serializer = verify_serializers(snippets, many=True)
        return Response(serializer.data)