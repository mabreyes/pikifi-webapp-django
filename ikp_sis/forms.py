from django import forms
from .models import StudentInfo


class ProfileForm(forms.ModelForm):
    class Meta:
        model = StudentInfo
        fields = ['profile_image', 'family_name', 'first_name', 'gender', 'level', 'school_last_attended',
                  'school_current', 'date_ikp_enrollment', 'sponsors_name', 'student_bio', 'educational_status']
        widgets = {'gender': forms.Select,
                   'level': forms.Select,
                   'date_ikp_enrollment': forms.SelectDateWidget(years=range(2005, 2100)),
                   'educational_status': forms.Select}

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        for key, field in self.fields.items():
            if isinstance(field.widget, forms.TextInput) or \
                    isinstance(field.widget, forms.Textarea) or \
                    isinstance(field.widget, forms.DateInput) or \
                    isinstance(field.widget, forms.DateTimeInput) or \
                    isinstance(field.widget, forms.Select) or \
                    isinstance(field.widget, forms.SelectDateWidget) or \
                    isinstance(field.widget, forms.TimeInput):
                field.widget.attrs.update({'placeholder': field.label.title})
                field.widget.attrs['class'] = 'form-control'
            if isinstance(field.widget, forms.RadioSelect):
                field.widget.attrs['class'] = 'form-check form-check-input'
            if isinstance(field.widget, forms.ImageField):
                field.widget.attrs['class'] = 'custom-file-input'
