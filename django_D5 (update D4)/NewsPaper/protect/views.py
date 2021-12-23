from django.shortcuts import render
from django.contrib.auth.views import redirect_to_login
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin



class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'protect/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_not_authors'] = not self.request.user.groups.filter(name='authors').exists()
        return context

    def handle_no_permission(self):
         # pass None to redirect_field_name in order to remove the next param
         return redirect_to_login(self.request.get_full_path(), self.get_login_url(), None)


