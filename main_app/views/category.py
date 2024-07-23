from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from ..models import Category
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib import messages

class Category_ListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Category
    paginate_by = 10
    template_name = 'category/list.html'
    permission_required = 'main_app.view_category'

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            messages.error(self.request, 'You need to be logged in to access the category list')
            return redirect('login_page')
        
        messages.error(self.request, 'You do not have permission to view the categories')
        return redirect(self.request.META.get('HTTP_REFERER', '')) # TODO Definir página inicial
    
class Category_CreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Category
    fields = ['name', 'description']
    template_name = 'category/create.html'
    permission_required = 'main_app.add_category'
    success_url = reverse_lazy('category-list')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        messages.success(self.request, f"Category '{form.cleaned_data['name']}' created successfully")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'There was an error creating the category. Please check the form and try again.')
        return super().form_invalid(form)

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            messages.error(self.request, 'You need to be logged in to create a new category')
            return redirect('login_page')
        
        messages.error(self.request, 'You do not have permission to add a new category')
        return redirect(self.request.META.get('HTTP_REFERER', '')) # TODO Definir página inicial
    
class Category_UpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Category
    fields = ['name', 'description']
    template_name = 'category/update.html'
    permission_required = 'main_app.change_category'
    success_url = reverse_lazy('category-list')

    def form_valid(self, form):
        messages.success(self.request, f"Category '{form.instance.name}' changed with success")
        return super().form_valid(form)

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            messages.error(self.request, 'You need to be logged in to edit a category')
            return redirect('login_page')
        
        messages.error(self.request, 'You do not have permission to edit a category')
        return redirect(self.request.META.get('HTTP_REFERER', '')) # TODO Definir página inicial
    
class Category_DeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Category
    template_name = 'category/delete.html'
    permission_required = 'main_app.delete_category'
    success_url = reverse_lazy('category-list')

    def form_valid(self, form):
        messages.success(self.request, f"Category '{self.get_object().name}' deleted with success")
        return super().form_valid(form)

    def handle_no_permission(self):
        if not self.request.user.is_authenticated:
            messages.error(self.request, 'You need to be logged in to delete a category')
            return redirect('login_page')
        
        messages.error(self.request, 'You do not have permission to delete a category')
        return redirect(self.request.META.get('HTTP_REFERER', '')) # TODO Definir página inicial