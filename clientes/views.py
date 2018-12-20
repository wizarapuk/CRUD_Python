from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Person
from .forms import PersonForm

# Create your views here.


@login_required
def person_list(request):
    pessoas = Person.objects.all()
    return render(request, 'person.html', {'pessoas': pessoas})


@login_required
def person_new(request):
    form = PersonForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('person_list')
    return render(request, 'person_form.html', {'form': form})


@login_required
def person_update(request, id):
    pessoa = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=pessoa)

    if form.is_valid():
        form.save()
        return redirect('person_list') #depois de salvar, redireciona para person_list

    return render(request, 'dados_clientes.html', {'form': form}) #aqui são as páginas html de cada função


@login_required()
def person_delete(request, id):
    pessoa = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=pessoa)

    if request.method == 'POST':
        pessoa.delete()
        return redirect('person_list')

    return render(request, 'person_delete_confirm.html', {'form': form})