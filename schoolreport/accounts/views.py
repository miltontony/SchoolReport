from random import randint

from django import http
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.shortcuts import render


def profile_detail(request, pk=None):

    if request.method == 'POST' and request.user.is_authenticated():
        request.user.first_name = request.POST.get('nickname', '')
        request.user.save()

    # is the user viewing their own profile, and therefore editing it?
    if not pk and request.user.is_authenticated():
        profile_user = request.user
        editable = True
    else:
        profile_user = get_object_or_404(User, pk=pk)
        editable = False
        if profile_user == request.user:
            editable = True

    nickname = profile_user.get_full_name() or 'Anon.'

    return render(request, 'accounts/profile_detail.html', {
        'profile_user': profile_user,
        'nickname': nickname,
        'editable': editable
    })
