from django import forms
from .models import StudentInfo, DatabaseUser, Viewer
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction


class ProfileForm(forms.ModelForm):
    class Meta:
        model = StudentInfo
        fields = ['profile_image',
                  'family_name',
                  'first_name',
                  'middle_name',
                  'gender',
                  'birthdate',
                  'age',
                  'address',
                  'parent_guardian_1',
                  'parent_guardian_2',
                  'parent_civil_status',
                  'child_status',
                  'level',
                  'section',
                  'course',
                  'school_last_attended',
                  'school_current',
                  'date_ikp_enrollment',
                  'sponsors_name',
                  'student_bio',
                  'educational_status']
        widgets = {'gender': forms.Select,
                   'level': forms.Select,
                   'course': forms.Select,
                   'birthdate': forms.SelectDateWidget(years=range(1995, 2100)),
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


class ViewerSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = DatabaseUser

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_viewer = True
        user.save()
        viewer = Viewer.objects.create(user=user)
        return user


class EditorSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = DatabaseUser

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_editor = True
        if commit:
            user.save()
        return user
