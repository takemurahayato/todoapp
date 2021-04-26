from django.shortcuts import render, redirect
from .models import List
from .forms import ListForm
from .forms import ChoiceForm
from django.contrib import messages
from django.views import View
from . import forms

#ホーム　タスク一覧
def home(request):

    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = List.objects.all
            messages.success(request, ('リストに追加されました'))
            return render(request, 'home.html', {'all_items': all_items})
    else:
        all_items = List.objects.all
        return render(request, 'home.html', {'all_items': all_items})

#削除
def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ('リストが削除されました!'))
    return redirect('home')

#タスク未完了
def uncomplete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect('home')

#タスク完了
def complete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect('home')


#編集
def edit(request, list_id):
    if request.method == 'POST':
        item = List.objects.get(pk=list_id)
        form = ListForm(request.POST or None, instance=item)
        priority = ChoiceForm(request.POST.get('choice'))

        if form.is_valid():
            form.save()
            messages.success(request, ('編集されました!'))
            return redirect('home')

        else:
            return redirect('home')
    else:
        item = List.objects.get(pk=list_id)
        return render(request, 'edit.html', {'item': item})





