"""
from match.models import Profile
from django import template
import markdown
from django.shortcuts import render,redirect,get_object_or_404

register = template.Library()

#@login_required(login_url='/accounts/login/')
@register.filter
def get_profile(request):
    data = Profile.objects.filter(id=request.user.id)
    return render(request,'match/base.html',data)
"""