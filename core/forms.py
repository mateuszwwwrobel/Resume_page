from django import forms

from .models import Message


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = [
            'message_name',
            'message_email',
            'message_phone',
            'message_text',
        ]

        labels = {
            'message_name': "Enter your Name:",
            'message_email': "Enter your e-mail address:",
            'message_phone': "Enter your phone number:",
            'message_text': "Enter your message:",
        }

