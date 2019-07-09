from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import viewer_required, editor_required

from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

from .forms import ProfileForm
from .models import StudentInfo


def student_list(request):
    students = StudentInfo.objects.order_by('pk')
    return render(request, 'student_list.html', {'students': students})


@login_required(login_url='/accounts/login/')
def student_detail(request, pk):
    student = get_object_or_404(StudentInfo, pk=pk)
    return render(request, 'student_info.html', {'student': student})


# @login_required(login_url='/accounts/login/')
def student_new(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)

        if form.is_valid():
            student = form.save(commit=False)
            student.author = request.user
            student.created_date = timezone.now()
            student.save()
            return redirect('student_detail', pk=student.pk)

    else:
        form = ProfileForm()

    return render(request, 'student_edit.html', {'form': form})


# @login_required(login_url='/admin/login/?next=/')
@editor_required
def student_edit(request, pk):
    student = get_object_or_404(StudentInfo, pk=pk)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=student)

        if form.is_valid():
            student = form.save(commit=False)
            student.author = request.user
            student.created_date = timezone.now()
            student.save()
            return redirect('student_detail', pk=student.pk)
    else:
        form = ProfileForm(instance=student)

    return render(request, 'student_edit.html', {'form': form})


# @login_required(login_url='/accounts/login')
@editor_required
def student_delete(request, pk):
    student = get_object_or_404(StudentInfo, pk=pk)

    author = student.author

    if request.method == "POST" and request.user.is_authenticated and request.user == author:
        student.delete()
        messages.success(request, "Student successfully deleted!")
        return HttpResponseRedirect("/")

    context = {'student': student,
               'author': author,
               }

    return render(request, 'student_delete.html', context)


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(
                request, 'Your password was successfully updated!')
            return redirect('password_changed')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/change_password.html', {
        'form': form
    })


def password_changed(request):
    return render(request, 'registration/password_updated.html')


def signout_prompt(request):
    return render(request, 'registration/signout.html')
