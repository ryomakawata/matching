from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse

@login_required(login_url='/accounts/login/')
def before_home(request):

    return render(request,'match/before_home.html')

@login_required(login_url='/accounts/login/')
def home(request):
    data = Profile.objects.filter(id=request.user.id).count()
    params = {
        'data': data,
    }
    return render(request,'match/home.html',params)

@login_required(login_url='/accounts/login/')
def search(request):
    if (request.method == 'POST'):
        form = SearchForm(request.POST)
        str_category = request.POST['category_search']
        data = Recruit.objects.filter(recruit_title__contains=str_category)
        count = Recruit.objects.filter(recruit_title__contains=str_category).count()
    else :
        form = SearchForm()
        data = Recruit.objects.all().values('id','pub_date','category','recruit_title')
        count = Recruit.objects.all().count()
        #profileは内容表記になっている
        #for文でrecruit_idを表現できればできる。
    
    params = {
        'form': form,
        'data': data,
        'count': count,
    }
    return render(request,'match/search.html',params)

#formをRecruitFormにするかProfileFormにするか
#RecruitFormにしたらrecruit_idを受け取らないといけないので既に保存されていなければいけない
@login_required(login_url='/accounts/login/')
def recruit_create(request):
    id = request.user.id
    pro = get_object_or_404(Profile,pk=id) 
    form = RecruitForm(request.POST)
    params = {'form': form}
    if request.method == 'POST' and form.is_valid():
        post = form.save(commit=False)
        post.recruit_id = pro
        language = LanguageForm(request.POST,instance=post)  
        if language.is_valid():
            post.save()
            language.save()
            return redirect(to='recruit')

        else:
            params['language'] = language

    # GETのとき
    else:
        # 空のlanguageをテンプレートへ渡す
        params['language'] = LanguageForm()

    return render(request,'match/recruit_create.html', params)

@login_required(login_url='/accounts/login/')
def recruit(request):
    id = request.user.id
    num = Profile.objects.get(id=id)
    data = Recruit.objects.filter(recruit_id=num)
    rec_id = Recruit.objects.values('recruit_id').filter(recruit_id=num)[0]
    rec_id = rec_id['recruit_id']
    skill = Language.objects.filter(rec_id=rec_id)
    count = Recruit.objects.filter(recruit_id=num).count()
    if count > 0:
        result = count
    else :
        result = "現在募集はしていません"
    params = {
        'data':data,
        'result':result,
        'skill': skill
    }
    return render(request,'match/recruit.html',params)

@login_required(login_url='/accounts/login/')
def recruit_edit(request,num):
    obj = Recruit.objects.get(id=num)
    recruit = RecruitForm(request.POST or None,instance=obj)
    language = LanguageForm(request.POST or None,instance=obj)
    if request.method == 'POST' and recruit.is_valid() and language.is_valid():
        recruit.save()
        language.save()
        return redirect(to='recruit')
    params = {
        'id': num,
        'form': recruit,
        'language':language,
        
    }
    return render(request,'match/recruit_edit.html',params)


@login_required(login_url='/accounts/login/')
def recruit_delete(request,num):
    data = Recruit.objects.get(id=num)
    if (request.method == 'POST'):
        data.delete()
        return redirect(to='recruit')
    params = {
        'id': num,
        'data': data,
    }
    return render(request,'match/recruit_delete.html',params)

#numはプロフィールクラスのpkを受け取っている
@login_required(login_url='/accounts/login/')
def other_recruit(request,num):
    data = Recruit.objects.get(id=num)
    pro = Recruit.objects.values('recruit_id').get(id=num)
    pro = pro["recruit_id"]
    pro = int(pro)
    profile = Profile.objects.get(id=pro)
    skill = Skill.objects.filter(pro_id=pro)
    language = Language.objects.filter(rec_id=num)
    params = {
        'profile':profile,
        'data': data,
        'skill':skill,
        'language':language,
    }
    return render(request,'match/other_recruit.html',params)

@login_required(login_url='/accounts/login/')
def message(request):

    return render(request,'match/message.html')

@login_required(login_url='/accounts/login/')
def profile_create(request):
    id = request.user.id
    user_id = User.objects.get(id=id)
    form = ProfileForm(request.POST or None,files=request.FILES or None)
    params = {'form': form,'test':user_id}
    if request.method == 'POST' and form.is_valid():
        post = form.save(commit=False)
        post.id = user_id
        formset = SkillForm(request.POST,instance=post)  
        if formset.is_valid():
            post.save()
            formset.save()
            return redirect(to='profile')

        # エラーメッセージつきのformsetをテンプレートへ渡すため、contextに格納
        else:
            params['formset'] = formset

    # GETのとき
    else:
        # 空のformsetをテンプレートへ渡す
        params['formset'] = SkillForm()

    return render(request,'match/profile_create.html', params)

#postのpkをtargetに変更する
@login_required(login_url='/accounts/login/')
def profile_edit(request):
    id = request.user.id
    user_id = User.objects.get(id=id)
    post = get_object_or_404(Profile, pk=user_id)
    profile = ProfileForm(request.POST or None, files=request.FILES or None, instance=post)
    skill = SkillForm(request.POST or None, instance=post)
    if request.method == 'POST' and profile.is_valid() and skill.is_valid():
        profile.save()
        skill.save()
        return redirect('profile')

    context = {
        'profile': profile,
        'skill': skill
    }

    return render(request,'match/profile_edit.html', context)


@login_required(login_url='/accounts/login/')
def profile(request):
    id = request.user.id
    #profile = Profile.objects.get(pk=id)
    profile = get_object_or_404(Profile,pk=id)
    pro = Profile.objects.values('pk').get(pk=id)
    pro_id = pro["pk"]
    skill = Skill.objects.filter(pro_id=pro_id)
    params = {
        'profile': profile,
        'skill': skill,
    }
    return render(request,'match/profile.html',params)

@login_required(login_url='/accounts/login/')
def skill_delete(request,num):
    skill = Skill.objects.get(pk=num)
    if (request.method == 'POST'):
        skill.delete()
        return redirect(to='profile')
    params = {
        'id': num,
        'skill': skill,
    }
    return render(request,'match/skill_delete.html',params)

@login_required(login_url='/accounts/login/')
def other_profile(request,num):
    #プロフィールのrecruit_idを受け取りたい
    data = Profile.objects.get(id=num)
    params = {
        'data': data
    }
    return render(request,'match/other_profile.html',params)

def term(request):

    return render(request,'match/term.html')

def privacy(request):

    return render(request,'match/privacy.html')

def inquiry(request):

    return render(request,'match/inquiry.html')