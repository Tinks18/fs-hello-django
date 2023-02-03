from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic, View
# from .models import Post
from .models import Item
from .forms import ItemForm

# Create your views here.


# class PostList(generic.ListView):
#     model = Post
#     queryset = Post.objects.filter(status=1).order_by("-created_on")
#     template_name = "index.html"
#     paginate_by = 6

def home(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'todo/index.html', context)


def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = ItemForm()
    context = {
            'form': form
            }
    return render(request, 'todo/add_item.html', context)


def edit_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('home')
    form = ItemForm(instance=item)    
    context = {
            'form': form
            }
    return render(request, 'todo/edit_item.html', context)


def toggle_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.done = not item.done
    item.save()
    return redirect('home')


def delete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect('home')




