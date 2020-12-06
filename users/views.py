from django.views import View
from django.views.generic import FormView, DetailView, UpdateView, TemplateView
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.db.models import Count
from users.forms import LoginForm, SignUpForm
from users.models import User
from movies.models import Movie
from books.models import Book


def logout_view(request):
    logout(request)
    return redirect(reverse("core:home"))


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, "users/login.html", {"form": form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse("core:home"))
        return render(request, "users/login.html", {"form": form})


class SignUpView(FormView):

    template_name = "users/signup.html"
    form_class = SignUpForm
    success_url = reverse_lazy("core:home")

    def form_valid(self, form):
        form.save()
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)


class UserProfileView(DetailView):
    model = User
    context_object_name = "user_obj"

    def def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["pref_movies"] = Movie.objects.filter(
            category=self.fav_movie_cat).order_by('-year')[:5]
        cpmtext["pref_books"] = Book.objects.filter(
            category=self.fav_book_cat).order_by('-year')[:5]
        return context


class UpdateProfileView(UpdateView):

    model = User
    template_name = "users/update_profile.html"
    fields = (
        "first_name",
        "last_name",
        "bio",
        "preference",
        "language",
        "fav_book_cat",
        "fav_movie_cat",
    )

    def get_object(self, queryset=None):
        return self.request.user


class UpdatePasswordView(PasswordChangeView):

    template_name = "users/update_password.html"
