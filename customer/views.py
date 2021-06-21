from django.shortcuts import render
from django.views import View
from user.models import MyUser, RateUser
from products.models import Products
from django.http import JsonResponse
from http import HTTPStatus
# Create your views here.

class profileSaler(View):
    def get(self, request, user_id):
        user_saler = MyUser.objects.get(id=user_id)
        products = Products.objects.filter(created_by=user_saler)
        return render(request, "customer/profile_saler_body.html", {"products":
                                                                 products,
                                                             'user_saler': user_saler})


class RateUserView(View):
    def get(self, request, user_id):
        user_from = request.user
        user_to = MyUser.objects.get(id=user_id)
        star = request.GET.get('star')
        if not user_from.is_authenticated:
            return JsonResponse({'message': 'bạn chưa đăng nhập tài khoản'})
        if user_from.id == user_to.id:
            return JsonResponse({'message': 'bạn không thể đánh giá cho '
                                            'chính mình'})
        try:
            rating = RateUser.objects.get(user_from=user_from.id,
                                          user_to=user_to)
            rating.stars = star
            rating.save()
            return JsonResponse({'message': f'cảm ơn bạn đã chấm {star} sao'
                                 })
        except Exception as e:
            rating = RateUser()
            rating.user_from = user_from
            rating.user_to = user_to
            rating.stars = star
            rating.save()
            return JsonResponse({'message': f'cảm ơn bạn đã chấm {star} sao'})
        except Exception as e:
            return JsonResponse({'message': e})
        # finally:
        #     return JsonResponse({'message': 'có lỗi khi đánh giá người bán '
        #                                     'này'})
