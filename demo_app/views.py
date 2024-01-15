from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Inventory
from .forms import InventoryForm



# Inventory List View
@login_required
def list_items(request):
    inventory = Inventory.objects.all()
    return render(request, 'list_items.html', {'inventory': inventory})

# Inventory Create View
@login_required
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
@login_required
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
@login_required
def delete_item(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)
    if request.method == 'POST':
        inventory.delete()
        return redirect('list_items')
    return render(request, 'delete_item.html', {'inventory': inventory})

# Inventory Search Feature
@login_required
def search_feature(request):
    # Check if the request is a post request.
    if request.method == 'POST':
        # Retrieve the search query entered by the user
        search_query = request.POST['search_query']
        # Filter your model by the search query
        items = Inventory.objects.filter(title_contains=search_query)
        return render(request, 'list_items.html', {'inventory':items})
    else:
        return render(request, 'list_items.html',{})
