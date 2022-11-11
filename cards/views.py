from django.shortcuts import render, redirect
from .forms import CardForm, CommentForm
from .models import Card, Comment

# Create your views here.


def index(request):
    cards = Card.objects.order_by("-pk")
    context = {"cards": cards}
    return render(request, "cards/index.html", context)


def createindiv(request):
    if request.method == "POST":
        form = CardForm(request.POST)
        if form.is_valid():
            temp = form.save(commit=False)
            # temp.user = request.user
            # 개인이면 is_indiv에 1
            temp.is_indiv = 1
            temp.save()
            form.save()
            return redirect("cards:index")
    else:
        form = CardForm()
    context = {
        "form": form,
    }

    return render(request, "cards/create_indiv.html", context)


def creategroup(request):
    if request.method == "POST":
        form = CardForm(request.POST)
        if form.is_valid():
            temp = form.save(commit=False)
            # temp.user = request.user
            # 그룹이면 is_indiv에 0
            temp.is_indiv = 0
            temp.save()
            form.save()
            return redirect("cards:index")
    else:
        form = CardForm()
    context = {
        "form": form,
    }
    return render(request, "cards/create_group.html", context)


def detail(request, pk):
    cards = Card.objects.get(pk=pk)
    context = {
        "cards": cards,
        'comments' : cards.comment_set.all(),
    }

    return render(request, "cards/detail.html", context)


def comment_create(request, pk):
    if request.method == "POST":
        card = Card.objects.get(pk=pk)
        comment_form = CommentForm(request.POST, request.FILES)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            # comment.user = request.user
            comment.card = card
            comment.save()
            comment_form.save()
        return redirect("cards:detail", pk)
    else:
        comment_form = CommentForm()
    context = {"comment_form": comment_form}

    return render(request, "cards/comment_create.html", context)
