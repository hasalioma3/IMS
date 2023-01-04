from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from .models import Inventory
from .forms import AddInventoryForm

# Create your views here.

@login_required
def inventory_list(request):
    inventories = Inventory.objects.all()
    context = {
        "title": "Inventory List",
        "inventories": inventories
    }
    return render(request, "inventory/inventory_list.html", context=context)

@login_required
def per_product_view(request, pk):
    inventory = get_object_or_404(Inventory, pk=pk)
    context ={
        'inventory': inventory
    }
    return render(request, "inventory/per_product.html", context=context)


@login_required
def add_product_view(request):
    if request.method =="POST":
        add_form = AddInventoryForm(data=request.POST)
        if add_form.is_valid():
            new_inventory = add_form.save(commit=False)
            new_inventory.sales = float(add_form.data['cost_per_item']) * float(add_form.data['quantity_sold'])
            new_inventory.save()
            return redirect("/inventory/")
    else:
        add_form = AddInventoryForm()
    return render(request, "inventory/add.html", {"form":add_form})