"""
from match.models import Profile

class BlogProfileMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # リクエストへの前処理を記述
        # reqeust.profileに、Profileモデルからブログ情報を取得する
        request.proflie = Profile.objects.get(pk=1)

        # 固定
        response = self.get_response(request)

        # レスポンスへの後処理を記述

        return response
"""