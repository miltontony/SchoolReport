# Create your views here.
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.core.paginator import Paginator, EmptyPage
from schoolreport.models import School
from jmbocomments.models import UserComment
from django.http import HttpResponse
from django.db.models import Avg


@login_required
def home(request, page=1):
    school_id = request.user.get_profile().school

    if not school_id:
        return redirect(reverse('logout'))

    school = School.objects.get(emis=int(school_id))
    learner_ratio = school.students / school.teachers
    province = school.province
    ave_learner_ratio = School.objects.filter(province=province).values('province').annotate(Avg('students'))[0]
    ave_teacher_ratio = School.objects.filter(province=province).values('province').annotate(Avg('teachers'))[0]
    ave_ratio = ave_learner_ratio.values()[1] / ave_teacher_ratio.values()[1]

    ave_passrate_2009 = School.objects.filter(province=province, passrate_2009__gt=0).values('province').annotate(Avg('passrate_2009'))[0].values()[1]
    ave_passrate_2010 = School.objects.filter(province=province, passrate_2009__gt=0).values('province').annotate(Avg('passrate_2010'))[0].values()[1]
    ave_passrate_2011 = School.objects.filter(province=province, passrate_2009__gt=0).values('province').annotate(Avg('passrate_2011'))[0].values()[1]

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
        'learner_ratio': learner_ratio,
        'ave_learner_ratio': ave_learner_ratio,
        'ave_teacher_ratio': ave_teacher_ratio,
        'ave_ratio': ave_ratio,
        'ave_passrate_2009': ave_passrate_2009,
        'ave_passrate_2010': ave_passrate_2010,
        'ave_passrate_2011': ave_passrate_2011,
        })

def browse(request):
	schools = School.objects.order_by("name").filter(province="WC")
	return render(request, 'browse.html', {'schools':schools,})

def school(request, page=1):
    emis=request.GET.get("emis")
    school = School.objects.get(emis=int(emis))
    learner_ratio = school.students / school.teachers
    province = school.province
    ave_learner_ratio = School.objects.filter(province=province).values('province').annotate(Avg('students'))[0]
    ave_teacher_ratio = School.objects.filter(province=province).values('province').annotate(Avg('teachers'))[0]
    ave_ratio = ave_learner_ratio.values()[1] / ave_teacher_ratio.values()[1]

    ave_passrate_2009 = School.objects.filter(province=province, passrate_2009__gt=0).values('province').annotate(Avg('passrate_2009'))[0].values()[1]
    ave_passrate_2010 = School.objects.filter(province=province, passrate_2009__gt=0).values('province').annotate(Avg('passrate_2010'))[0].values()[1]
    ave_passrate_2011 = School.objects.filter(province=province, passrate_2009__gt=0).values('province').annotate(Avg('passrate_2011'))[0].values()[1]

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
        'learner_ratio': learner_ratio,
        'ave_learner_ratio': ave_learner_ratio,
        'ave_teacher_ratio': ave_teacher_ratio,
        'ave_ratio': ave_ratio,
        'ave_passrate_2009': ave_passrate_2009,
        'ave_passrate_2010': ave_passrate_2010,
        'ave_passrate_2011': ave_passrate_2011,
        'can_report': request.user.get_profile().can_report(int(emis))
        })

def health(request):
    return HttpResponse("")
