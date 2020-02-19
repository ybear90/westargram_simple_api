import jwt
import json
from django.http                import JsonResponse
from .models                    import Account
from westargram_api.settings    import SECRET_KEY


def login_required(func):
    def wrapper(self, request, *args, **kwargs):
        access_token = request.headers.get("Authorization", None)
        # print("access_token : ", access_token)
        if access_token is not None:
            try:
                decode_token = jwt.decode(access_token, SECRET_KEY, algorithm='HS256')
                # print(decode_token)
                account_id = decode_token['account_id']
                account = Account.objects.get(id=account_id)
                request.user = account

                return func(self, request, *args, **kwargs)
            except jwt.DecodeError:
                return JsonResponse({'message' : 'INVALID TOKEN'}, status=400)
            except Account.DoesNotExist:
                return JsonResponse({'message' : 'ACCOUNT NOT EXIST'}, status=400)
        else:
            return JsonResponse({'message' : "LOGIN REQUIRED"}, status=401)


    return wrapper