from django.db import models
from django.contrib.auth.models import User
import io, base64
from django.utils import timezone

#makemigrations をする時に前のmakemigrationsファイルを消していたらややこしくなる
#どうしてもマイグレーションできないときは　del db.sqlite3　を使う
#Modelに新たな列を追加するときは null=True を指定する。

class Profile(models.Model):
    id = models.OneToOneField(User,primary_key=True,on_delete=models.CASCADE,blank=True)
    name = models.CharField(max_length=25,null=True)
    school = models.CharField(max_length=25)
    image = models.ImageField(upload_to='documents/')
    self_introduction = models.TextField()
    
    def __str__(self):
        return str(self.pk) + str(self.id)

    def image_src(self):
        with self.image.open() as img:
            base64_img = base64.b64encode(img.read()).decode()

            return 'data:' + img.file.content_type + ';base64' + base64_img

PERIOD = (
    ('選択してください','選択してください'),
    ('半年未満','半年未満'),
    ('～１年','～１年'),
    ('～２年','～２年'),
    ('～３年','～３年'),
    ('３年～','３年～'),
)

class Skill(models.Model):
    skill = models.CharField(max_length=25,null=True)
    experience = models.CharField(choices=PERIOD,max_length=25,null=True)
    pro_id = models.ForeignKey(Profile,blank=True,null=True,on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.pk) + str(self.pro_id)

CATEGORY = (
    ('勉強会','勉強会'),
    ('サービス開発','サービス開発'),
    ('その他','その他'),
)

class Recruit(models.Model):
    recruit_id = models.ForeignKey(Profile,on_delete=models.CASCADE,blank=True,null=True)
    recruit_title = models.CharField(max_length=100)
    recruit_content = models.TextField()
    category = models.CharField(choices=CATEGORY,max_length=25,null=True)
    pub_date = models.DateTimeField(default=timezone.now,null=True)

    def __str__(self):
        return str(self.recruit_id) + str(self.pk)

    class Meta:
        ordering = ('-pub_date',)

LANGUAGE = (
    ('JAVA','JAVA'),
    ('C','C'),
    ('C++','C++'),
    ('C#','C#'),
    ('Javascript','Javascript'),
    ('jQuery','jQuery'),
    ('HTML・CSS','HTML・CSS'),
    ('PHP','PHP'),
    ('Ruby','Ruby'),
    ('Python','Python'),
    ('Objective-c','Objective-c'),
    ('Swift','Swift'),
    ('その他','その他'),
)

class Language(models.Model):
    language = models.CharField(choices=LANGUAGE,max_length=25,null=True)
    rec_id = models.ForeignKey(Recruit,blank=True,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.rec_id) + str(self.language) + str(self.pk)
