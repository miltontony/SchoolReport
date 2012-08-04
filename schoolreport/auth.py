import urlparse
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import (REDIRECT_FIELD_NAME, login as auth_login,
                                authenticate)
from django.contrib.auth.forms import AuthenticationForm
from schoolreport.utils import process_post_data_username
from schoolreport.forms import MobiUserCreationForm


def login(request, template_name='registration/login.html',
          redirect_field_name=REDIRECT_FIELD_NAME,
          authentication_form=AuthenticationForm,
          current_app=None, extra_context=None):

    """
    Displays the login form and handles the login action.
    """
    redirect_to = request.REQUEST.get(redirect_field_name, '')

    if request.method == "POST":
        form = authentication_form(data=process_post_data_username(request.POST))
        if form.is_valid():
            netloc = urlparse.urlparse(redirect_to)[1]

            # Use default setting if redirect_to is empty
            if not redirect_to:
                redirect_to = '/'
            elif netloc and netloc != request.get_host():
                redirect_to = '/'

            # Okay, security checks complete. Log the user in.
            auth_login(request, form.get_user())

            if request.session.test_cookie_worked():
                request.session.delete_test_cookie()

            return redirect(redirect_to)
    else:
        form = authentication_form(request)

    request.session.set_test_cookie()

    return render(request, template_name,
              {'form': form, redirect_field_name: redirect_to})

def join(request):
    if request.method == 'POST':
        post_data = process_post_data_username(request.POST)
        username = post_data['username']
        form = MobiUserCreationForm(post_data)
        if form.is_valid():
            form.save()
            #auto-login user
            password = request.POST.get('password1')
            user = authenticate(username=username,  password=password)
            auth_login(request, user)

            #save school
            profile = user.get_profile()
            profile.school = form.cleaned_data['school']
            profile.save()

            return redirect(reverse('home'))
    else:
        form = MobiUserCreationForm()

    return render(request, 'registration/register.html', {'form': form})
