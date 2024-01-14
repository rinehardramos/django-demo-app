from django.shortcuts import render, get_object_or_404, redirect
from .models import Inventory
from .forms import InventoryForm



# Inventory List View
def list_items(request):
    inventory = Inventory.objects.all()
    return render(request, 'list_items.html', {'inventory': inventory})

# Inventory Create View

def create_item(request):
    if request.method == 'POST':
        form = InventoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_items')
    else:
        form = InventoryForm()
    return render(request, 'create_item.html', {'form': form})

# Inventory Update View
def update_item(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)
    if request.method == 'POST':
        form = InventoryForm(request.POST, instance=inventory)
        if form.is_valid():
            form.save()
            return redirect('list_items')
    else:
        form = InventoryForm(instance=inventory)
    return render(request, 'update_item.html', {'form': form})

# Inventory Delete View
def delete_item(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)
    if request.method == 'POST':
        inventory.delete()
        return redirect('list_items')
    return render(request, 'delete_item.html', {'inventory': inventory})
