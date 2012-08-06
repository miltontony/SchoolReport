# Create your views here.
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator, EmptyPage
from schoolreport.models import School
from jmbocomments.models import UserComment


@login_required
def home(request, page=1):
    school_id = request.user.get_profile().school

    if not school_id:
        return redirect(reverse('logout'))

    school = School.objects.get(emis=int(school_id))
    article_content_type = ContentType.objects.get_for_model(School)

    user_report_qs = UserComment.objects\
                               .filter(content_type=article_content_type,
                                    object_pk=school.pk)\
                               .select_related('user')\
                               .order_by('-submit_date')

    reports_per_page = 5
    #if hasattr(settings, 'COMMENTS_PER_PAGE'):
    #    comments_per_page = settings.COMMENTS_PER_PAGE

    paginator = Paginator(user_report_qs, reports_per_page)

    try:
        user_report_list = paginator.page(page)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        user_report_list = paginator.page(paginator.num_pages)

    return render(request, 'index.html', {
        'school': school,
        'user_report_list': user_report_list,
        })
