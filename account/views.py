import json
import bcrypt
import jwt
from django.views               import View
from django.http                import HttpResponse, JsonResponse
from .models                    import Account
from westargram_api.settings    import SECRET_KEY
from .auth                      import login_required

class SignInView(View):
    def post(self, request):
        account_data = json.loads(request.body)

        try:
            if Account.objects.filter(user_account=account_data['user_account']).exists():
                account = Account.objects.get(user_account=account_data['user_account'])

                if bcrypt.checkpw(account_data['password'].encode('utf-8'), account.password.encode('utf-8')):
                    token = jwt.encode({ 'account_id' : account.id }, SECRET_KEY, algorithm='HS256')
                    return JsonResponse({ 'access_token' : token.decode('utf-8') }, status=200)
                return HttpResponse(status=401)
            
            return HttpResponse(status=400)
        
        except KeyError:
            return HttpResponse(status=400)


class SignUpView(View):
    def post(self, request):
        account_data = json.loads(request.body)

        try:
            if not Account.objects.filter(user_account=account_data['user_account']).exists():
                Account(
                    user_account=account_data['user_account'],
                    password=bcrypt.hashpw(account_data['password'].encode('utf-8'), bcrypt.gensalt()).decode() 
                ).save()
            else:
                return HttpResponse(status=409)
        except KeyError:
            return HttpResponse(status=400)

        return JsonResponse({'message':'SUCCESS'}, status=200)

class CheckAccessView(View):
    @login_required
    def get(self, request):
        return JsonResponse({'user_info' : {
            'user_account' : request.user.user_account,
        }})