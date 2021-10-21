from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['title', 'email' , 'content']
        labels = {
           'title':'題目',
           'email': 'メールアドレス',
           'content':'内容',
        }
        error_messages = {
            'title': {
                'max_length': '100文字以内で入力してください'
            }
        }