from django.views.generic import CreateView

class CreateWithUserView(CreateView):
            
    success_url = "/"
    
    def get_initial(self):
        
        user_field = self.get_user_field()
        return { user_field : self.request.user }
        
    def form_valid(self, form):
        
        user_field = "%s_id" % self.get_user_field()
        setattr(form.instance, user_field, self.request.user.id)
        return CreateView.form_valid(self, form)
    
    def get_user_field(self):
        """
            Returns the name of the user field.
            Override it in subclasses if your field is named different to the default.
        """
        return "user"