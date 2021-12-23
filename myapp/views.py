
from django.db.models import Q
from django.shortcuts import render, redirect

# Create your views here.
from django.template.context_processors import request
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView

from .forms import CreateUserForm, audiocreate
from .models import kitob, audio_kitob, audio


class ListViews(ListView):
    model = kitob
    template_name = 'myapp/index.html'
    paginate_by = 6
    queryset = kitob.objects.order_by('-update_time')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        cat = audio_kitob.objects.all()
        context['audio'] = cat
        return context
class CreateViews(CreateView):
    model = kitob
    fields = '__all__'
    template_name = 'myapp/employee_form.html'
    success_url = reverse_lazy('home')

class DeleteViews(DeleteView):
        model = kitob
        success_url = '/'
        template_name = 'myapp/delete.html'
        fields = '__all__'
class EmployeeUpdate(UpdateView):
    model = kitob
    template_name = 'myapp/employee_form.html'
    fields = '__all__'
    success_url = '/'

class DetailViews(DetailView):
    model = kitob
    template_name = 'myapp/detail.html'
class AudioCreateViews(CreateView):
    model = audio_kitob
    fields = '__all__'
    template_name = 'myapp/audio_form.html'
    success_url = reverse_lazy('home')
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        cat = audio.objects.all()

        return context
def create(request):
    form = audiocreate()
    context = {'crete':form}
    if request.method == "POST":
        form = audiocreate(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request,'myapp/audio_form.html',context)
class AudioUpdate(UpdateView):
    model = audio_kitob
    template_name = 'myapp/employee_form.html'
    fields = '__all__'
    success_url = '/'
class AudioDetailViews(DetailView):
    model = audio_kitob
    template_name = 'myapp/audio_detail.html'
class Book(ListView):
    model = kitob
    template_name = 'myapp/book.html'
    queryset = kitob.objects.order_by('-update_time')
class AudioBook(ListView):
    model = audio_kitob
    template_name = 'myapp/audio_book.html'
    queryset = audio_kitob.objects.order_by('-update_time')
def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'form':form}
    return render(request,'registration/register.html',context=context)
def search_result(request):
    query = request.GET.get('search')
    search_obj = kitob.objects.filter(
        Q(title__icontains=query) | Q(author_name__icontains=query)
    )
    print(query)
    context = {
        'women': search_obj,
        'query': query,
    }
    return render(request, 'myapp/book.html', context=context)

class AudioDeleteViews(DeleteView):
        model = audio_kitob
        success_url = '/'
        template_name = 'myapp/delete.html'
        fields = '__all__'





