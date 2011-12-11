from django.views.generic import CreateView

class CreateWithUserView(CreateView):
            
    success_url = "/"
    
    def get_initial(self):
        
        return { "user": self.request.user }
        
    def form_valid(self, form):
                
        form.instance.user_id = self.request.user.id
        return CreateView.form_valid(self, form)