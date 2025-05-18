from django.views.generic import TemplateView,ListView,DetailView,UpdateView,DeleteView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Folder,File
from .forms import FolderForm,FileForm
from django.urls import reverse_lazy

class DashboardHomeView(LoginRequiredMixin,TemplateView):
    template_name='dashboard/home.html'

class DashboadFolderListView(LoginRequiredMixin,ListView):
    template_name = 'dashboard/folder-list.html'
    context_object_name='folders'

    def get_queryset(self):
        query_set=Folder.objects.filter(parent__isnull=True)
        return query_set
    
class DashboardFolderDetailView(LoginRequiredMixin,DetailView):
    template_name='dashboard/folder-detail.html'
    model=Folder
    context_object_name='folder'

class DashboardFolderEditView(LoginRequiredMixin,UpdateView):
    model = Folder
    form_class = FolderForm
    template_name = 'dashboard/folder-form.html'

    def get_success_url(self):
        return reverse_lazy('dashboard:folder-detail', kwargs={'pk': self.object.pk})
    

class DashboardFolderDeleteView(LoginRequiredMixin,DeleteView):
    model = Folder
    template_name = 'dashboard/folder-confirm-delete.html'
    success_url = reverse_lazy('dashboard:folder-list')


class DashboardFileUpdateView(UpdateView):
    model = File
    form_class = FileForm
    template_name = 'dashboard/folder-form.html'

    def get_success_url(self):
        return reverse_lazy('dashboard:folder-detail', kwargs={'pk': self.object.folder.pk})
    
class DashboardFileDeleteView(DeleteView):
    model = File
    template_name = 'dashboard/folder-confirm-delete.html'

    def get_success_url(self):
        return reverse_lazy('dashboard:folder-detail', kwargs={'pk': self.object.folder.pk})
    

class DashboardFolderCreateView(LoginRequiredMixin, CreateView):
    model = Folder
    form_class = FolderForm
    template_name = 'dashboard/folder-form.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        parent_id = self.kwargs.get('parent_id')
        if parent_id:
            kwargs['initial'] = {'parent': Folder.objects.get(id=parent_id)}
            kwargs['parent_locked'] = True
        return kwargs

    def form_valid(self, form):
        form.instance.owner = self.request.user
        parent_id = self.kwargs.get('parent_id')
        if parent_id:
            form.instance.parent = Folder.objects.get(id=parent_id)
        return super().form_valid(form)

    def get_success_url(self):
        parent_id = self.object.parent.id if self.object.parent else ''
        return reverse_lazy('dashboard:folder-detail', kwargs={'pk': parent_id}) if parent_id else reverse_lazy('folder-list')
    
class DashboardFileCreateView(LoginRequiredMixin, CreateView):
    model = File
    form_class = FileForm
    template_name = 'dashboard/folder-form.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        folder_id = self.kwargs.get('folder_id')
        if folder_id:
            kwargs['initial'] = {'folder': Folder.objects.get(id=folder_id)}
            kwargs['folder_locked'] = True
        return kwargs

    def form_valid(self, form):
        form.instance.owner = self.request.user  # ✅ set owner
        folder_id = self.kwargs.get('folder_id')
        if folder_id:
            form.instance.folder = Folder.objects.get(id=folder_id)
        return super().form_valid(form)


    def get_success_url(self):
        return reverse_lazy('dashboard:folder-detail', kwargs={'pk': self.object.folder.id})
    
