from django import forms
from ProjectDesign.models import Contact

# Contact Model
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ['slug']

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        
        # placeholder
        self.fields['name'].widget.attrs['placeholder'] = 'Your Name *'
        self.fields['email'].widget.attrs['placeholder'] = 'Your Email *'
        self.fields['phone'].widget.attrs['placeholder'] = 'Phone Number *'
        self.fields['guest_count'].widget.attrs['placeholder'] = 'Number Of Guests *'
        self.fields['date'].widget.attrs['placeholder'] = 'YYYY-MM-DD *'
        self.fields['time'].widget.attrs['placeholder'] = 'HH:MM:SS'
        self.fields['description'].widget.attrs['placeholder'] = 'Message'
        


