from django import forms
from .models import Profile,Recruit,Skill,Language

#参考サイト https://django-docs-ja.readthedocs.io/en/1.0-maint/ref/models/fields.html

class SearchForm(forms.Form):
    #name_search = forms.CharField(label='名前検索',required=False)
    category_search = forms.CharField(label='キーワード検索',required=False)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name','school','image','self_introduction']
        labels = {
            "name": "名前",
            'school': "学校",
            'image': "写真",
            'skill': "スキル",
            'experience': "経験年数",
            'self_introduction': "自己紹介",
        }
        widgets = {
            'self_introduction': forms.Textarea(attrs={'rows':20, 'cols':100}),
        }

class RecruitForm(forms.ModelForm):
    class Meta:
        model = Recruit
        fields = ['recruit_title','category','recruit_content']
        labels = {
            'recruit_title': "タイトル",
            'category': "カテゴリ",
            'language': "言語",
            'recruit_content': "募集内容",
        }
        widgets = {
            'recruit_content': forms.Textarea(attrs={'rows':20, 'cols':100}),
        }
        
SkillForm = forms.inlineformset_factory(
            Profile,Skill,
            fields='__all__',
            labels={'skill':"スキル",'experience':"経験年数"},
            extra=5,
            max_num=5,
            can_delete=False
        )

LanguageForm = forms.inlineformset_factory(
            Recruit,Language,
            fields='__all__',
            labels={'language':"使用言語"},
            extra=5,
            max_num=5,
            can_delete=False
        )