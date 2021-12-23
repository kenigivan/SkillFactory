from django.contrib.auth.models import User
from django.views.generic import CreateView

from .models import BaseRegisterForm
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin



class BaseRegisterView(CreateView):
    model = User
    form_class = BaseRegisterForm
    success_url = '/'


@login_required
def upgrade_me(request):
    user = request.user
    authors_group = Group.objects.get(name='authors')
    if not request.user.groups.filter(name='authors').exists():
        authors_group.user_set.add(user)
    return redirect('/')


# Ограничение прав доступа (Не разобрался)
# from django.contrib.auth.mixins import PermissionRequiredMixin
#
# class MyView(PermissionRequiredMixin, View):
#     permission_required = ('<app>.<action>_<model>',
#                            '<app>.<action>_<model>')
#
# from django.views.generic.edit import CreateView
#
# class AddProduct(PermissionRequiredMixin, CreateView):
#     permission_required = ('shop.add_product', )
#     // customize form view
