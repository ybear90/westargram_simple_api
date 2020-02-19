import json
from django.views   import View
from django.http    import HttpResponse, JsonResponse
from .models        import Account

class SignInView(View):
    def post(self, request):
        account_data = json.loads(request.body)

        try:
            if Account.objects.filter(user_account=account_data['user_account']).exists():
                account = Account.objects.get(user_account=account_data['user_account'])

                if account.password == account_data['password']:
                    return JsonResponse({'message':'Welcome back!'}, status=200)
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
                    password=account_data['password']
                ).save()
            else:
                return HttpResponse(status=409)
        except KeyError:
            return HttpResponse(status=400)

        return JsonResponse({'message':'SUCCESS'}, status=200)