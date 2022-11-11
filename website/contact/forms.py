from django import forms

class contactForm(forms.Form):
    name = forms.CharField(label='', required=False, max_length=100, help_text='100 characters max.', widget= forms.TextInput
                           (attrs={'placeholder':'Name', 'class':'wpcf7-form-control wpcf7-text',
                   }))
    email = forms.EmailField(label='', required=True, widget= forms.EmailInput
                           (attrs={'placeholder':'Email', 'class':'wpcf7-form-control wpcf7-text wpcf7-email wpcf7-validates-as-required wpcf7-validates-as-email',
                   }))
    subject = forms.CharField(label='', required=True, max_length=500, help_text='500 characters max.', widget= forms.TextInput
                           (attrs={'placeholder':'Subject', 'class':'wpcf7-form-control wpcf7-text',
                   }))
    comment = forms.CharField(label='', required=True, widget= forms.Textarea
                           (attrs={'placeholder':'Comment', 'class':'wpcf7-form-control wpcf7-textarea',
                   }))
