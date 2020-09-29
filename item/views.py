from mixins import AjaxableFormMixin
from django.template import RequestContext
from django.views.generic import (
    CreateView,
    DetailView,
    DeleteView,
    ListView,
    UpdateView)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django.urls import reverse_lazy
from django.db.models import Q

from .models import Item
from accounts.models import Employee
from store.models import Store
# Create your views here.


class ItemUpdateView(LoginRequiredMixin, UpdateView):
    model = Item
    template_name = "item/update_item.html"
    success_url = reverse_lazy('item:index')


class ItemDeleteView(LoginRequiredMixin, DeleteView):
    model = Item
    success_url = reverse_lazy('item:index')


class ListAndCreate(LoginRequiredMixin, AjaxableFormMixin, CreateView):
    model = Item
    fields = [
        "name",
        "item_num",
        "fragile",
        "weight",
        'units',
        "item_class",
        'item_store',
    ]
    template_name = "item/create.html"
    success_url = reverse_lazy('item:index')

    def form_valid(self, form):
        print(form.instance.item_store)
        form.instance.added_by = self.request.user
        store = Store.objects.get(
            name=form.instance.item_store).number_of_items
        Store.objects.filter(name=form.instance.item_store).update(number_of_items=store +
                                                                   form.instance.item_num)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        employee = Employee.objects.get(username=self.request.user.username)
        context = super(ListAndCreate, self).get_context_data(**kwargs)
        context["object_list"] = self.model.objects.filter(added_by=employee)
        return context


class ListAndDetail(LoginRequiredMixin, DetailView):
    model = Item
    template_name = "item/item.html"

    def get_context_data(self, **kwargs):
        employee = Employee.objects.get(username=self.request.user.username)
        context = super(ListAndDetail, self).get_context_data(**kwargs)
        context["object_list"] = self.model.objects.filter(added_by=employee)
        return context


class ItemSearchView(LoginRequiredMixin, ListView):
    model = Item
    template_name = "item/create.html"

    def get_context_data(self, **kwargs):
        query = self.request.GET.get('query')
        employee = Employee.objects.get(username=self.request.user.username)
        context = super(ItemSearchView, self).get_context_data(**kwargs)
        context["object_list"] = self.model.objects.filter(
            Q(added_by=employee) & (Q(name__icontains=query) | Q(item_id__icontains=query)))
        return context
