from django.shortcuts import render, get_object_or_404,redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

def index(request):
    quizzes = Quiz.objects.filter(is_ready_to_publish=True)
    context = {"quizzes":quizzes}
    return render(request,"index.html",context=context)

@login_required(login_url='login')

def quiz_detail(request,quiz_id):
    quiz = get_object_or_404(Quiz,id=quiz_id)
    questions = quiz.questions.all()
    context = {"quiz":quiz,"questions":questions}
    return render(request,"quiz_detail.html",context)

@login_required(login_url='login')
def quiz_submit(request,quiz_id):
    if request.method == 'POST':
        quiz = get_object_or_404(Quiz, id=quiz_id)
        questions = quiz.questions.all()
        error_message = None
        has_attempted = False

    for question in questions:
        choice_id = request.POST.get(f"question_{question.id}", None)
        if choice_id:
            choice = get_object_or_404(Choices, id=choice_id)
            UserResponse.objects.create(
                user=request.user,
                quiz=quiz,
                question=question,
                selected_choice=choice
            )
            has_attempted = True  # Mark that the user has attempted at least one question

    if not has_attempted:
        error_message = "Attempt at least one question!"

    if error_message:
        messages.error(request, error_message)
        return redirect("quiz_detail", quiz_id=quiz_id)

        messages.success(request, "Quiz Submitted")
        return redirect("index")

    return redirect("quiz_detail", quiz_id=quiz_id)  


