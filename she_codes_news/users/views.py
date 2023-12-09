from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from .models import CustomUser, Profile
from .forms import CustomUserCreationForm, EditProfileForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from news.models import NewsStory


class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'


@login_required
def profile(request, username):
    user = get_object_or_404(CustomUser, username=username)
    profile = get_object_or_404(Profile, user=user)
    posts = NewsStory.objects.all().filter(author=user)
    return render(request, 'users/profile.html', {'profile': profile, 'user': user, 'posts': posts})


@login_required
def edit_profile(request):
    if request.method == "POST":
        # request.user.username is the original username
        form = EditProfileForm(request.user.username, request.POST, request.FILES)
        if form.is_valid():
            about_me = form.cleaned_data["about_me"]
            username = form.cleaned_data["username"]
            image = form.cleaned_data["image"]

            user = CustomUser.objects.get(id=request.user.id)
            profile = Profile.objects.get(user=user)
            user.username = username
            user.save()
            profile.about_me = about_me
            if image:
                profile.image = image
            profile.save()
            return redirect("users:profile", username=user.username)
    else:
        form = EditProfileForm(request.user.username)  # <-- add also here
    return render(request, "users/edit_profile.html", {'form': form})
