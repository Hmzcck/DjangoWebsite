from django.http import BadHeaderError, JsonResponse
from django.http.response import HttpResponse
from django.core.mail import send_mail
from django.shortcuts import render
from django.conf import settings

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # send email
        try:
            send_mail(
                subject,
                f'Name: {name}\nEmail: {email}\nMessage: {message}',
                settings.EMAIL_HOST_USER,
                ['ArmWreslters@hotmail.com'],
                fail_silently=False,
            )
            return JsonResponse({'success': True})
        except BadHeaderError:
            return JsonResponse({'success': False})
        except Exception as e:
            return JsonResponse({'success': False})

    # render contact form
    return render(request, 'index.html')

def normal(request):

    return render(request, 'index.html')
