from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.core.mail import send_mail
from django.conf import settings
import json
import re

from .models import ContactMessage, Project


def index(request):
    projects = Project.objects.filter(is_visible=True)
    return render(request, 'index.html', {'projects': projects})


@require_POST
def contact_submit(request):
    try:
        data = json.loads(request.body)

        name = data.get('name', '').strip()
        email = data.get('email', '').strip()
        subject = data.get('subject', '').strip()
        message = data.get('message', '').strip()

        errors = {}
        if not name or len(name) < 2:
            errors['name'] = 'Please enter your name.'
        if not email or not re.match(r'^[^@]+@[^@]+\.[^@]+$', email):
            errors['email'] = 'Please enter a valid email.'
        if not subject or len(subject) < 3:
            errors['subject'] = 'Please enter a subject.'
        if not message or len(message) < 10:
            errors['message'] = 'Message must be at least 10 characters.'

        if errors:
            return JsonResponse({'success': False, 'errors': errors}, status=400)

        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        ip = x_forwarded_for.split(',')[0] if x_forwarded_for else request.META.get('REMOTE_ADDR')

        # DB mein save karo
        ContactMessage.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message,
            ip_address=ip,
        )

        # Email send karo
        email_body = f"""
New message from your Portfolio Contact Form
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Name    : {name}
Email   : {email}
Subject : {subject}

Message :
{message}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Sent from: prajjwaldixit.portfolio
        """

        send_mail(
            subject=f'[Portfolio] {subject} — from {name}',
            message=email_body,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.CONTACT_EMAIL],
            fail_silently=False,
        )

        return JsonResponse({
            'success': True,
            'message': "Message sent successfully! I'll get back to you soon."
        })

    except json.JSONDecodeError:
        return JsonResponse({'success': False, 'errors': {'general': 'Invalid request.'}}, status=400)
    except Exception as e:
        return JsonResponse({'success': False, 'errors': {'general': 'Something went wrong. Please try again.'}}, status=500)