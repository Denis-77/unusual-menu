from django.shortcuts import render, redirect


def empty(request):
    return redirect('/goods')


def main_view(request, path):
    category = path.split("/").pop()
    return render(request, 'menu_app/index.html', context={
        'path': path,
        'category': category,
    })
