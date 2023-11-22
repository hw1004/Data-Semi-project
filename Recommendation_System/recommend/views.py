from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Reply
from .forms import StudentForm, ReplyForm

from django.views.decorators.http import require_safe


@require_safe
def index(request):
    # return render(request, 'recommend/index.html', {
    # })
    pass


