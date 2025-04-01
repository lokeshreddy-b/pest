from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.core.mail import send_mail

@csrf_exempt
def book_appointment(request):
    if request.method == 'POST':
        try:
            # Parse the incoming data
            data = json.loads(request.body)
            name = data.get('name')
            phone = data.get('phone')
            email = data.get('email')
            selected_services = ', '.join(data.get('selectedServices', []))
            date = data.get('date')

            # Prepare the email content
            subject = 'New Appointment Booking Received'
            message = f"""
                You have received a new appointment.
                Name: {name}
                Phone: {phone}
                Email: {email}
                Services: {selected_services}
                Preferred Date: {date}
            """
            from_email = 'uniquepestsolutionsnlr@gmail.com'
            recipient_list = ['uniquepestsolutionsnlr@gmail.com']

            # Send the email
            send_mail(subject, message, from_email, recipient_list)

            return JsonResponse({'message': '✅ Appointment submitted successfully!'})
        except Exception as e:
            print(f"Error: {e}")
            return JsonResponse({'error': '❌ Error processing appointment. Please try again.'}, status=500)
    
    return JsonResponse({'error': 'Invalid request method'}, status=400)
