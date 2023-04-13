import psutil
from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.views.generic import TemplateView, ListView
from accounts.models import CustomUser
from adminFES.func import graph_data


class Index(LoginRequiredMixin, TemplateView):
    template_name = 'adminFES/index.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context.update({
            'cpu': f'0.{int(psutil.cpu_percent())}',
            'ram': f'0.{int(psutil.virtual_memory().percent)}',
            'data_graph': graph_data(),
        })
        return context

class UserList(LoginRequiredMixin, ListView):
    model = CustomUser
    template_name = 'adminFES/users.html'

def logout_admin(request):
    logout(request)