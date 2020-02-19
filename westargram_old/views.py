import json
from django.views   import View
from django.http    import JsonResponse, HttpResponse
from .models        import Account, Comment    

class LoginView(View):
    def post(self, request):
        user_data   = json.loads(request.body)
        username    = user_data.get('username', None)
        email       = user_data.get('email', None)
        password    = user_data.get('password', None)


        if Account.objects.filter(username=username).exists():
            account = Account.objects.get(username=username)
            
            if account.password == password:
                return JsonResponse({'message':'Login SUCCESS'}, status=200)
            return HttpResponse(status=401)
        
        elif Account.objects.filter(email=email).exists():
            account = Account.objects.get(email=email)

            if account.password == password:
                return JsonResponse({'message':'Login SUCCESS'}, status=200)
            return HttpResponse(status=401)

        return HttpResponse(status=400)

        # 로직이 틀렸다
        # if Account.objects.filter(username=username) or Account.objects.filter(email=email):
        #     if Account.objects.filter(password=password):
        #         return JsonResponse({'message':"Login SUCCESS"}, status=200)
        #     return JsonResponse({'message':'Login Failed - wrong password'}, status=403)
        
        # return JsonResponse({'message':'Login Failed - wrong account(username or email)'}, status=403)
class CommentView(View):
    def post(self, request):
        data            = json.loads(request.body)
        comment_user    = data.get('comment_user', None)
        comments        = data.get('comments', None)
        
        if comment_user == None:
            return JsonResponse({'message':'Please input comment user name'}, status=400)
        elif comments == None:
            return JsonResponse({'message':'Please input comments'}, status=400)
        
        Comment(
            comment_user=comment_user,
            comments=comments
        ).save()

        return JsonResponse({'message':'Comment has saved successfully'}, status=200)

    def get(self, request):
        return JsonResponse({'comments':list(Comment.objects.values())}, status=200)