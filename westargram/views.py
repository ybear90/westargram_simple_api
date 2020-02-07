import json
from django.views   import View
from django.http    import JsonResponse
from .models        import Account, Comment    

class LoginView(View):
    def post(self, request):
        data        = json.loads(request.body)
        username    = data.get('username', None)
        email       = data.get('email', None)
        password    = data.get('password', None)

        if Account.objects.filter(username=username) or Account.objects.filter(email=email):
            if Account.objects.filter(password=password):
                return JsonResponse({'message':"Login SUCCESS"}, status=200)
            return JsonResponse({'message':'Login Failed - wrong password'}, status=403)
        
        return JsonResponse({'message':'Login Failed - wrong account(username or email)'}, status=403)
        
    def get(self, request):
        pass
        
class CommentView(View):
    def post(self, request):
        data            = json.loads(request.body)
        comment_user    = data.get('comment_user', None)
        comments        = data.get('comments', None)
        
        if comment_user == None:
            return JsonResponse({'message':'Please input comment user name'}, status=403)
        elif comments == None:
            return JsonResponse({'message':'Please input comments'}, status=403)
        
        Comment(
            comment_user=comment_user,
            comments=comments
        ).save()

        return JsonResponse({'message':'Comment has saved successfully'}, status=200)

    def get(self, request):
        if Comment.objects.values():
            return JsonResponse({'comments':list(Comment.objects.values())}, status=200)
        return JsonResponse({'message':'Comments are empty!'}, status=400)