# ## see, read me in the root directory first




from dotenv import load_dotenv
load_dotenv()
import requests
import random
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings

def home(request):
    if request.method == 'POST':
        mobile_number = request.POST.get('phone_number')
        # generate OTP
        otp = str(random.randint(100000, 999999))
        request.session['mobile_number'] = mobile_number  #request.session is a dictionary-like object
        request.session['otp'] = otp
        print('OTP $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ --->', otp)
        # Send OTP request to provider using API key
        url = f'https://2factor.in/API/V1/{settings.API_KEY}/SMS/+91{mobile_number}/{otp}'
        #https://2factor.in/API/V1/{api_key}/SMS/{phone_number}/{otp}
        # url = f'https://api.textlocal.in/send/?apiKey={settings.API_KEY}&numbers=91{mobile_number}&message={otp}'

        print('***********************************')
        response = requests.get(url)

        if response.ok:
            # OTP sent successfully
            messages.success(request, 'OTP sent successfully')
            print(response.status_code)
            print(response.text)
            return redirect('validate_otp')
        else:
            # Error sending OTP
            messages.error(request, 'Error sending OTP. Please try again later.')

    return render(request, 'otp_app/home.html')



def validate_otp(request):
    if request.method == 'POST':
        user_otp = request.POST.get('otp')
        print("User OTP:", user_otp, type(user_otp))

        try:
            mobile_number = request.session['mobile_number']
            session_otp = request.session['otp']

            print("Session OTP:", session_otp, type(session_otp))
            print('Boolean ---> ', user_otp == session_otp)
            if user_otp == session_otp:
                messages.success(request, 'OTP validation successful')
                print('OTP VALIDATED SUCCESSFUL....')
                # do something with the validated mobile number
                # e.g. store it in the database or use it for authentication
                # and then clear the session data
                request.session.pop('mobile_number')
                request.session.pop('otp')
                return redirect('home')
            else:
                messages.error(request, 'Invalid OTP')
        except KeyError:
            messages.error(request, 'OTP validation failed')
    return render(request, 'otp_app/validate_otp.html')








#
# def validate_otp(request):
#     if request.method == 'POST':
#         user_otp = request.POST.get('otp')
#         print("User OTP:", user_otp)
#
#         try:
#             mobile_number = request.session['mobile_number']
#             session_otp = request.session['otp']
#
#             print("Session OTP:", session_otp)
#             if user_otp == session_otp:
#                 messages.success(request, 'OTP validation successful')
#                 # do something with the validated mobile number
#                 # e.g. store it in the database or use it for authentication
#                 # and then clear the session data
#                 request.session.pop('mobile_number')
#                 request.session.pop('session_otp')
#                 return redirect('home')
#             else:
#                 messages.error(request, 'Invalid OTP')
#         except KeyError:
#             messages.error(request, 'OTP validation failed')
#     return render(request, 'otp_app/validate_otp.html')










#
# from django.shortcuts import render, redirect
# from django.http import HttpResponse
# from django.conf import settings
# from django.contrib import messages
# import random
# from twilio.rest import Client
#
#
# def home(request):
#     if request.method == 'POST':
#         phone_number = request.POST['phone_number']
#         request.session['phone_number'] = phone_number
#         otp = random.randint(1000, 9999)
#         request.session['otp'] = otp
#         try:
#             account_sid = settings.TWILIO_ACCOUNT_SID
#             auth_token = settings.TWILIO_AUTH_TOKEN
#             client = Client(account_sid, auth_token)
#
#             message = client.messages \
#                 .create(
#                      body=f'Your OTP is {otp}',
#                      from_=settings.TWILIO_FROM_NUMBER,
#                      to=f'+91{phone_number}'
#                  )
#             print(message.sid)
#
#         except Exception as e:
#             print(e)
#             messages.error(request, "OTP sending failed, please try again later.")
#             return redirect('home')
#
#         return redirect('validate_otp')
#
#     return render(request, 'otp_app/home.html')
#
#
# def validate_otp(request):
#     if request.method == 'POST':
#         session_otp = request.session.get('otp')
#         user_otp = request.POST['otp']
#         if int(session_otp) == int(user_otp):
#             return HttpResponse('OTP verified successfully')
#         else:
#             messages.error(request, "Invalid OTP, please try again.")
#             return redirect('validate_otp')
#
#     return render(request, 'otp_app/validate_otp.html')
#
#




#----------------------------------------------------------------------------------------------------------------

