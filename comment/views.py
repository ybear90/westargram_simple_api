import json
from django.views   import View
from django.http    import HttpResponse, JsonResponse
from account.auth   import login_required
from .models        import Comment

class CommentView(View):
    @login_required
    def post(self, request):
        comments_data = json.loads(request.body)
        Comment(
            user_account=request.user.user_account,
            comments=comments_data['comments']
        ).save()

        return JsonResponse({'message':'SUCCESS'}, status=200)

    def get(self, request):
        return JsonResponse({'comments':list(Comment.objects.values())}, status=200)