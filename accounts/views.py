from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView
from django.views.generic import UpdateView, ListView

from .models import FavoriteTalk


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class PublicFavoriteTalkList(ListView):
    template_name = "home.html"
    context_object_name = "talks"

    def get_queryset(self):
        return FavoriteTalk.objects.select_related("user").order_by("-id")


class FavoriteTalkList(LoginRequiredMixin, ListView):
    template_name = "accounts/favorite_talk_list.html"
    context_object_name = "talks"

    def get_queryset(self):
        return FavoriteTalk.objects.filter(user=self.request.user).order_by("-id")


class FavoriteTalkCreate(LoginRequiredMixin, CreateView):
    model = FavoriteTalk
    fields = ["title", "speaker", "notes", "presentation_link", "user_notes"]
    template_name = "accounts/favorite_talk_form.html"
    success_url = reverse_lazy("accounts:favorite_talk_list")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class FavoriteTalkUpdate(LoginRequiredMixin, UpdateView):
    model = FavoriteTalk
    fields = ["title", "speaker", "notes", "presentation_link", "user_notes"]
    template_name = "accounts/favorite_talk_form.html"
    success_url = reverse_lazy("accounts:favorite_talk_list")

    def get_queryset(self):
        return FavoriteTalk.objects.filter(user=self.request.user)


class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect(reverse_lazy('login'))
