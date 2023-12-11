from django.shortcuts import render, redirect
from .forms import *
from .models import Profile, Game
from rest_framework import viewsets
from .serializers import ProfileSerializer, GameSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist:
        return None


def index(request):
    profile = get_profile()
    context = {
        'profile': profile,
    }

    return render(request, 'common/home-page.html', context)


def profile_create(request):
    profile = get_profile()
    form = ProfileCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('game-dashboard')
    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'profile/create-profile.html', context)


def profile_details(request):
    profile = get_profile()
    games_count = Game.objects.all().count()
    rating_list = [game.rating for game in Game.objects.all()]
    if rating_list:
        average_rating = sum(rating_list) / len(rating_list)
        average_rating = f'{average_rating:.1f}'
    else:
        average_rating = 0.0
    context = {
        'profile': profile,
        'games_count': games_count,
        'average_rating': average_rating,
    }
    return render(request, 'profile/details-profile.html', context)


def profile_edit(request):
    profile = get_profile()
    form = ProfileEditForm(request.POST or None, instance=profile)
    if form.is_valid():
        form.save()
        return redirect('profile-details')
    context = {
        'form': form,
        'profile': profile,

    }
    return render(request, 'profile/edit-profile.html', context)


def profile_delete(request):
    profile = Profile.objects.first()
    game = Game.objects.all()
    if request.method == 'POST':
        profile.delete()
        game.delete()

        return redirect('index')

    return render(request, 'profile/delete-profile.html')


def game_dashboard(request):
    profile = get_profile()
    games = Game.objects.all()
    context = {
        'profile': profile,
        'games': games,
    }
    return render(request, 'common/dashboard.html', context)


def game_create(request):
    profile = get_profile()
    form = GameCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('game-dashboard')
    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'game/create-game.html', context)


def game_details(request, pk):
    profile = get_profile()
    game = Game.objects.filter(pk=pk).get()
    context = {
        'game': game,
        'profile': profile,
    }
    return render(request, 'game/details-game.html', context)


def game_edit(request, pk):
    profile = get_profile()
    game = Game.objects.filter(pk=pk).get()
    form = GameEditForm(request.POST or None, instance=game)
    if form.is_valid():
        form.save()
        return redirect('game-dashboard')
    context = {
        'form': form,
        'profile': profile,
        'game': game
    }
    return render(request, 'game/edit-game.html', context)


def game_delete(request, pk):
    profile = get_profile()
    game = Game.objects.filter(pk=pk).get()
    form = GameDeleteForm(request.POST or None, instance=game)
    if form.is_valid():
        form.save()
        return redirect('game-dashboard')
    context = {
        'form': form,
        'profile': profile,
        'game': game
    }
    return render(request, 'game/delete-game.html', context)
