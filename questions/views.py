from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import AskQuestionForm
from .models import Message
from django.contrib.auth.decorators import login_required



class HomeView(LoginRequiredMixin, View):
    login_url = "/account/login/"  
    redirect_field_name = "next" 

    def get(self, request, *args, **kwargs):
        messages = Message.objects.filter(parent__isnull=True)
        template = loader.get_template("questions/home.html")
        context = {
            "messages": messages,
        }
        return HttpResponse(template.render(context, request))

@login_required(login_url="/account/login/") 
def ask_question_view(request, parent_id=None):
    if request.method == 'POST':
        form = AskQuestionForm(request.POST)
        if form.is_valid():
            if parent_id:
                parent = Message.objects.get(id=parent_id)
                question = form.save(commit=False)
                question.parent = parent
            question = form.save(commit=False)
            question.author = request.user 
            question.save()
            return redirect('/')  
    else:
        form = AskQuestionForm()  
    return render(request, 'questions/ask_question.html', {'form': form})

@login_required(login_url="/account/login/")
def delete_message(request, message_id):
    message = get_object_or_404(Message, id=message_id, author=request.user)
    message.delete()
    return redirect('/')



