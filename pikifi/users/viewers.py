from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView

from ..forms import ViewerSignUpForm
from ..models import DatabaseUser

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from ..decorators import viewer_required


class ViewerSignUpView(CreateView):
    model = DatabaseUser
    form_class = ViewerSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'viewer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('student_list')
