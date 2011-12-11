# Create your views here.
from django.views.generic import TemplateView, ModelView

class IndexView(TemplateView):
    
    template_name = "index.html"

class AboutView(TemplateView):
    
    template_name = "about.html"
    
class ProjectView(TemplateView):