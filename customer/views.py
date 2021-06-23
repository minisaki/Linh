from django.shortcuts import render
from django.views import View
from user.models import MyUser, RateUser
from products.models import Products
from django.http import JsonResponse
from http import HTTPStatus
from .models import TextReport, Report, Follow
import json
# Create your views here.

class profileSaler(View):
    def get(self, request, user_id):
        user_saler = MyUser.objects.get(id=user_id)
        products = Products.objects.filter(created_by=user_saler)
        title = TextReport.objects.all()
        follow = Follow.objects.filter(user_get_follow=user_saler)
        lenFollow = len(follow)
        check = False
        try:
            status = Follow.objects.get(user_get_follow=user_saler,
                                    user_follow=request.user)
            if status:
                check = True
        except:
            return render(request,
                          "customer/profile_saler_body.html",
                          {"products": products, 'user_saler': user_saler,
                           'title': title, 'lenFollow': lenFollow,
                           'check': check})
        return render(request,
                      "customer/profile_saler_body.html",
                      {"products": products, 'user_saler': user_saler,
                        'title':title, 'lenFollow': lenFollow, 'check': check})


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


class ReportView(View):
    def post(self, request):
        user_get_id = request.POST.get('user_get_id')
        report_list = request.POST.get('report_title')
        text = request.POST.get('text')
        user_report = request.user
        if not user_report.is_authenticated:
            return JsonResponse({'message': 'bạn chưa đăng nhập tài khoản'})
        user_get_report = MyUser.objects.get(id=user_get_id)
        if user_report == user_get_report:
            return JsonResponse({'message': 'Bạn không thể báo cáo chính '
                                            'mình'})
        data = json.loads(report_list)
        if data:
            try:
                instance = Report.objects.get(user_report=user_report,
                                              user_get_report=user_get_report)
                instance.text = text
                for item in data:
                    instance.content_report.add(TextReport.objects.get(
                        id=item))
            except:
                instance = Report()
                instance.user_report = user_report
                instance.user_get_report = user_get_report
                for item in report_list:
                    instance.content_report.add(TextReport.objects.get(
                        id=item))

            instance.save()

            return JsonResponse({'message': 'báo cáo thành công'})
        else:
            return JsonResponse({'message': 'bạn chưa chọn lý do'})

class FollowView(View):
    def post(self, request):
        user_get_id = request.POST.get('user_get_id')
        user_follow = request.user

        if not user_follow.is_authenticated:
            return JsonResponse({'message': 'bạn chưa đăng nhập tài khoản'})
        user_get_follow = MyUser.objects.get(id=user_get_id)
        if user_follow == user_get_follow:
            return JsonResponse({'message': 'Bạn không thể theo dõi chính '
                                            'mình'})
        try:
            instance = Follow.objects.get(user_follow=user_follow,
                                          user_get_follow=user_get_follow)
            if instance:
                instance.delete()
            return JsonResponse({'message': 'bạn đã bỏ theo dõi'})
        except:
            instance = Follow()
            instance.user_follow = user_follow
            instance.user_get_follow = user_get_follow
            instance.save()

            return JsonResponse({'message': 'bạn đang theo dõi'})