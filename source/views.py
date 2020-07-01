from django.shortcuts import render, redirect
from .forms import UserEditForm, UploadBookForm, CommentForm
from .models import UserInfo, Book, Comment, Interested


def index(request):
    return render(request, 'source/index.html', {})


def edit(request):
    if request.method == 'POST':
        user_inst = UserInfo()
        form = UserEditForm(request.POST)

        user_inst.user = request.user
        user_inst.telegram_alias = form.data["telegram_alias"]
        user_inst.messenger_alias = form.data["messenger_alias"]

        query = UserInfo.objects.filter(user=request.user)

        if not query:
            user_inst.save()
        else:
            user_inst.save(update_fields=["telegram_alias", "messenger_alias"])

        return redirect("/")
    else:
        telegram = ""
        messenger = ""
        # in order to have values from database in forms
        query = UserInfo.objects.filter(user=request.user)
        if not query:
            telegram = "@.."
            messenger = "@.."
        else:
             telegram = UserInfo.objects.get(user=request.user).telegram_alias
             messenger = UserInfo.objects.get(user=request.user).messenger_alias
        form = UserEditForm(initial={'telegram_alias':telegram, 'messenger_alias': messenger})
    return render(request, 'source/edit.html', {'form': form})


def publish(request):
    if request.method == 'POST':
        book_inst = Book()
        form = UploadBookForm(request.POST)

        book_inst.name = form.data["name"]
        book_inst.price = form.data["price"]
        book_inst.cover = form.data["cover"]
        book_inst.owner = request.user
        book_inst.description = form.data["description"]
        book_inst.type = form.data["type"]

        book_inst.save()
        return redirect("/")
    form = UploadBookForm()
    return render(request, 'source/publish.html', {'form': form})
