from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .models import TaskModel

class TaskList(ListView):
    model = TaskModel
    paginate_by = 4
    template_name = 'todo/index.html'

class TaskCreate(CreateView):
    model = TaskModel
    template_name = 'todo/create_task.html'
    fields = ['name', 'desc']
    success_url = reverse_lazy('index')

class TaskEdit(UpdateView):
    model = TaskModel
    fields = ['name', 'desc', 'status']
    success_url = reverse_lazy('index')
    template_name = 'todo/edit_task.html'
    context_object_name = 'task'

class TaskDelete(DeleteView):
    model = TaskModel
    context_object_name = 'task'
    success_url = reverse_lazy('index')
    template_name = 'todo/delete_task.html'

# class ChangeStatus(UpdateView):
#     model = TaskModel
#     fields = ('status',)
#     success_url = reverse_lazy('index')
#     # context_object_name = 'task'

#     def form_valid(self, form):
#         # new_status = form.save(commit=False)
#         # print(new_status.status)
#         # print(new_status.id)
#         print(self.object.status)
#         if self.object.status:
#             self.object.status = False
#         else:
#             self.object.status = True
#         self.object.save()
#         # new_status.save()
#         return redirect(self.get_success_url())
#         # return super().form_valid(form)

def change_status(request, **kwargs):
    obj = get_object_or_404(TaskModel, id=kwargs['pk'])
    if obj.status:
        obj.status = False
    else:
        obj.status = True
    obj.save()
    return redirect(reverse('index'))
