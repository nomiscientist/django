from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.models import User

from home import forms
from home import models


class HomeView(TemplateView):
    template_name = "home/home.html"

    def get(self,request):
        form = forms.HomeForm()
        posts = models.Post.objects.all().order_by('-created')
        users = User.objects.exclude(id=request.user.id)
        friend = models.Friend.objects.get(current_user=request.user)

        friends = friend.users.all()


        # print(posts)
        args = {'form':form,'posts':posts,'users':users,'friends':friends}

        return render(request,self.template_name,args)

    
    def post(self,request):
        form = forms.HomeForm(request.POST)
        text = ''
        if form.is_valid():
            
            post = form.save(commit=False)
            post.user = request.user
            post.save()


            text = form.cleaned_data['post']
            # print("text:"+text)
            form = forms.HomeForm()
            return redirect("home:home")
            

        args = {'form':form, 'text':text}
        return render(request,self.template_name,args)


def change_friends(request,operation,pk):
    new_friend = User.objects.get(pk=pk)
    if operation == "add":
        models.Friend.make_friend(request.user,new_friend)
    
    elif operation == "remove":
        models.Friend.lose_friend(request.user,new_friend)
        

    return redirect("home:home")
