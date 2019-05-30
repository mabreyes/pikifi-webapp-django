from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.contrib import messages

from .forms import ProfileForm
from .models import StudentInfo


def student_list(request):
    students = StudentInfo.objects.order_by('created_date')
    return render(request, 'student_list.html', {'students': students})


def student_detail(request, pk):
    student = get_object_or_404(StudentInfo, pk=pk)
    return render(request, 'student_info.html', {'student': student})


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
