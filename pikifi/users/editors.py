from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView

from ..models import DatabaseUser
from ..forms import EditorSignUpForm


class EditorSignUpView(CreateView):
    model = DatabaseUser
    form_class = EditorSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'editor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('student_list')
