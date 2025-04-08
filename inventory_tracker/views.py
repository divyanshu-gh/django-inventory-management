from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm

def home(request):
    items = Item.objects.all()
    low_stock_items = items.filter(quantity__lt=10)
    return render(request, 'home.html', {'items': items, 'low_stock_items': low_stock_items})

def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ItemForm()
    return render(request, 'add_item.html', {'form': form})

def edit_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ItemForm(instance=item)
    return render(request, 'edit_item.html', {'form': form})

def delete_item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    item.delete()
    return redirect('home')
