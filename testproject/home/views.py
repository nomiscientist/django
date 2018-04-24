from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView

from home import forms
from home import models


class HomeView(TemplateView):
    template_name = "home/home.html"

    def get(self,request):
        form = forms.HomeForm()
        posts = models.Post.objects.all()

        # print(posts)
        args = {'form':form,'posts':posts}

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


