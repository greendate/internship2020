from django.shortcuts import render, redirect
from .forms import UserEditForm, UploadBookForm, CommentForm
from .models import UserInfo, Book, Comment, Interested
from django.contrib.auth.models import User

types = [ [1, 'Action and adventure'],
    [2, 'Art/architecture'],
    [3, 'Autobiography'],
    [4, 'Business/economics'],
    [5, 'Classic'],
    [6, 'Cookbook'],
    [7, 'Dictionary'],
    [8, 'Crime'],
    [9, 'Encyclopedia'],
    [10, 'Drama'],
    [11, 'Guide'],
    [12, 'Fairytale'],
    [13, 'Health/fitness'],
    [14, 'Fantasy'],
    [15, 'History'],
    [16, 'Humor'],
    [17, 'Horror'],
    [18, 'Journal'],
    [19, 'Mystery'],
]


def my(request):
    books = Book.objects.filter(owner=request.user)
    return render(request, 'source/mybooks.html', {'books': books, 'user': request.user})


def delete(request, identity):
    Book.objects.filter(id=identity).delete()
    return redirect("my")


def user(request, identity):
    books = Book.objects.filter(owner_id=identity)
    user = User.objects.get(id=identity).username
    return render(request, 'source/user.html', {'books': books, 'user': user})


def index(request):
    if request.method == 'POST':
         type = request.POST.get('types')
         print(type)
         books = Book.objects.filter(type=type)
         return render(request, 'source/index.html', {'books': books, 'types': types})
    books = Book.objects.all()
    return render(request, 'source/index.html', {'books': books, 'types': types})


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
        book_inst.author = form.data["author"]
        book_inst.price = form.data["price"]
        book_inst.cover = form.data["cover"]
        book_inst.owner = request.user
        book_inst.description = form.data["description"]
        book_inst.type = form.data["type"]

        book_inst.save()
        return redirect("/")
    form = UploadBookForm()
    return render(request, 'source/publish.html', {'form': form})


def order(request, book_id):
    order = Interested()
    order.user = request.user
    order.book = Book.objects.get(id=book_id)
    order.save()
    owner = Book.objects.get(id=book_id).owner_id
    print(owner)
    print(request.user)
    if owner == User.objects.get(username=request.user).id:
        return render(request, "source/orderfail.html", {})
    else:
        email = User.objects.get(id=owner).email
        telegram = UserInfo.objects.get(user_id=owner).telegram_alias
        messenger = UserInfo.objects.get(user_id=owner).messenger_alias
        return render(request, "source/contact.html", {'email': email, 'telegram': telegram, 'messenger': messenger})


def recommended(request):
    user_id = User.objects.get(username=request.user).id
    orders = Interested.objects.filter(user_id=user_id)
    types = []
    for order in orders:
        type = Book.objects.get(id=order.book_id).type
        if type not in types:
            types.append(type)
    rec_books = []
    for type in types:
         books = Book.objects.filter(type=type)
         for book in books:
             rec_books.append(book)
    return render(request, 'source/recommended.html', {'books': rec_books})


def book(request, book_id):
    if request.method == 'POST':
        comment = Comment()
        form = CommentForm(request.POST)
        comment.user = request.user
        comment.book = Book.objects.get(id=book_id)
        comment.text = form.data["text"]
        comment.save()
        return redirect(request.path_info)
    book = Book.objects.get(id=book_id)
    form = CommentForm(request.POST)
    comments = Comment.objects.filter(book_id=book_id)
    return render(request, "source/book.html", {'book': book, 'form': form, 'comments': comments})
