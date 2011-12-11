# Create your views here.
from django.views.generic import TemplateView
from django.shortcuts import render_to_response, redirect, get_object_or_404
from ..models import Project

class IndexView(TemplateView):
    
    template_name = "main.html"
    
    def render_to_response(self, context):
        
        if not self.request.user.is_authenticated():
            return redirect('accounts/register')
        
        return TemplateView.render_to_response(self, context)
    

class AboutView(TemplateView):
    
    template_name = "about.html"
    
    
class ProjectView(TemplateView):
    
    model = Project
    
    