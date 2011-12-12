# Create your views here.
from django.views.generic import TemplateView, CreateView, ListView
from django.shortcuts import render_to_response, redirect, get_object_or_404
from generics import CreateWithUserView

from ..models import *
from ..forms import ProjectForm

class IndexView(TemplateView):
    
    template_name = "main.html"
    
    def render_to_response(self, context):
        
        if not self.request.user.is_authenticated():
            return redirect('accounts/register')
        
        return TemplateView.render_to_response(self, context)
    

class AboutView(TemplateView):
    
    template_name = "about.html"
    

class ProjectCreateView(CreateWithUserView):
    
    template_name = "projects/create.html"
    model = Project    
    form_class = ProjectForm    


class ProjectListView(ListView):
    
    template_name = "projects/list.html"
    model = Project
    
    def get_queryset(self):
        
        projects = Project.objects.all()
        
        for project in projects:
            if self.request.user.id in [u.id for u in project.followers.all()]:
                project.followed = True
            else:
                project.followed = False
        
        return projects
    

class ProjectFollowView(TemplateView):
    
    def render_to_response(self, context):
        
        user = self.request.user
        project = Project.objects.get(id=self.kwargs['project_id'])
        project.followers.add(user)
        project.save()
        
        return redirect("/projects")
