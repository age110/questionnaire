import random
import math
import json
from datetime import datetime, timedelta

from django.conf.urls import url
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from Myquestion.models import Questionnaire
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout


from Api.utils import *
from Myquestion.models import *
from Api.decorations import userinfo_required, customer_required, superuser_required


class Rest(object):
    def __init__(self,name=None):
        self.name = name or self.__class__.__name__.lower()
    # 定义一个方法,用于绑定到url中
    @csrf_exempt
    def enter(self, request, *args, **kwargs):
        # 取出客户端请求方法
        method = request.method
        # 根据请求方法执行相应的处理函数
        if method == 'GET':
            # 获取资源
            return self.get(request, *args, **kwargs)
        elif method == 'POST':
            # 更新资源
            return self.post(request, *args, **kwargs)
        elif method == 'PUT':
            # 添加资源
            return self.put(request, *args, **kwargs)
        elif method == 'DELETE':
            # 删除资源
            return self.delete(request, *args, **kwargs)
        else:
            # 不支持其他方法
            return method_not_allowed()

    def get(self, request, *args, **kwargs):
        return method_not_allowed()

    def post(self, request, *args, **kwargs):
        return method_not_allowed()

    def put(self, request, *args, **kwargs):
        return method_not_allowed()

    def delete(self, request, *args, **kwargs):
        return method_not_allowed()


class Register(object):
    def __init__(self, ):
        self.resources = []

    def regist(self, resource):
        self.resources.append(resource)

    @property
    def urls(self):
        urlpatterns = [
            url(r'^{name}$'.format(name=resource.name), resource.enter)
            for resource in self.resources
        ]
        return urlpatterns


class SessionRest(Rest):
    def put(self, request, *args, **kwargs):
        data = request.PUT
        username = data.get('username', '')
        password = data.get('password', '')
        # 查询数据库用户表
        user = authenticate(username=username, password=password)
        if user:
            # 保存登录状态
            login(request, user)
            return json_response({
                "msg": '登录成功'
            })
        else:
            return params_error({
                "msg": "用户名或密码错误"
            })

    def delete(self, request, *args, **kwargs):
        logout(request)
        return json_response({"msg": "退出成功"})


class UserRest(Rest):
    def get(self, request, *args, **kwargs):
        # 判断是否登录
        user = request.user
        if user.is_authenticated:
            # 获取信息
            data = dict()
            if hasattr(user, 'customer'):
                customer = user.customer
                data['name'] = customer.name
                data['email'] = customer.email
                data['user'] = user.id
                data['category'] = 'customer'
            elif hasattr(user, 'userinfo'):
                userinfo = user.userinfo
                data['name'] = userinfo.name
                data['qq'] = userinfo.qq
                data['user'] = user.id
                data['category'] = 'userinfo'
            else:
                return json_response({})
        else:
            return not_authenticated()

        return json_response(data)

    def post(self, request, *args, **kwargs):
        # 判断用户是否登录
        data = request.POST
        user = request.user
        if user.is_authenticated:
            if hasattr(user, 'customer'):
                customer = user.customer
                customer.name = data.get('name', '')
                customer.email = data.get('email', '')
                customer.save()

            elif hasattr(user, 'userinfo'):
                userinfo = user.userinfo
                userinfo.name = data.get('name', '')
                userinfo.qq = data.get('qq', '')
                userinfo.save()
            else:
                return json_response({
                    "msg": "更新成功,恭喜!"
                })
        else:
            return not_authenticated()
        return json_response({
            "msg": "更新成功"
        })

    def put(self, request, *args, **kwargs):
        data = request.PUT

        username = data.get('username', '')
        password = data.get('password', '')
        ensure_password = data.get('ensure_password', '')
        regist_code = data.get('regist_code', 0)
        session_regist_code = request.session.get('regist_code', 1)

        error = dict()

        if not username:
            error['username'] = "必须提供用户名"
        else:
            if User.objects.filter(username=username).count() > 0:
                error['username'] = "用户名已存在"

        if len(password) < 6:
            error['password'] = "密码长度不可小于6位"

        if password != ensure_password:
            error['ensure_password'] = "密码不匹配"

        if regist_code != session_regist_code:
            error['regist_code'] = "验证码不匹配"

        if error:
            return params_error(error)

        user = User()
        user.username = username
        user.set_password(password)
        user.save()

        category = data.get('category', 'userinfo')

        if category == 'userinfo':
            # 创建普通用户
            user_obj = UserInfo()
            user_obj.name = ""
            user_obj.qq = ""
        else:
            # 创建客户
            user_obj = Customer()
            user_obj.name = ""
            user_obj.email = ""
        # 为什么要写下面的那句话呢?
        user_obj.user = user
        user_obj.save()
        return json_response({"id": user.id})


class RegistCode(Rest):
    def get(self, request, *args, **kwargs):
        # 获取6位随机数字
        regist_code = random.randint(100000, 1000000)
        # 保存到session中
        request.session['regist_code'] = regist_code
        # 返回随机数
        return json_response({
            "regist_code": regist_code
        })


# class Customer_questionnaire(Rest):
#     @customer_required
#     def put(self,request,*args,**kwargs):
#         # 获取请求的数据
#         data = request.PUT
#         #创建问卷对象
#         questionnaire = Questionnaire()
#         # 赋值属性
#         questionnaire.customer = request.user.customer
#         questionnaire.title = data.get('title', '标题')
#         # 特殊处理 创建时间使用当前时间
#         questionnaire.create_date = datetime.now()
#         # 截止时间做特殊的时间处理
#         try:
#             # 获取截止时间字符串
#             deadline_str = data.get('deadline', "")
#             # 把时间字符串转化为时间对象
#             questionnaire.deadline = datetime.strptime(deadline_str, '%Y-%m-%d')
#         except Exception as e:
#             # 如果获取截止时间失败,那么使用当前时间加上10天
#             questionnaire.deadline = datetime.now()+timedelta(days=10)
#         questionnaire.title = data.get('title','标题')
#         # 特殊处理 问卷创建时,状态为草稿
#         questionnaire.state = 0
#         # 特殊处理 默认问卷数量为1份
#         questionnaire.quantity = int(data.get('quantity', 1))
#         questionnaire.free_count = int(data.get('quantity', 1))
#         questionnaire.save()
#         return json_response({
#             "id": questionnaire.id
#         })
    
#     @customer_required
#     def post(self,request,*args,**kwargs):
#         data = request.POST
#         questionnaire_id = int(data.get('questionnaire_id',0))
#         try:
#             questionnaire = Questionnaire.objects.get(
#                 id=questionnaire_id, customer=request.user.customer, state__in=[0, 2, 3])
#         except Exception as e:
#             return params_error({
#                 'questionnaire_id': "找不到对应的问卷,或者问卷不可修改"
#             })
#         questionnaire.title = data.get('title','标题')
#         # 特殊处理 截止时间
#         try:
#             # 获取截止时间字符串
#             deadline_str = data.get('deadline', "")
#             # 把时间字符串转化为时间对象
#             deadline = datetime.strptime(deadline_str, '%Y-%m-%d')
#         except Exception as e:
#             # 如果获取截止时间失败,那么使用当前时间加上10天
#             deadline = datetime.now()+timedelta(days=10)
#         questionnaire.deadline = deadline

#         state = int(data.get('state', 0))
#         if state not in [0, 1]:
#             return params_error({
#                 'state': '状态不合法'
#             })
#         # 特殊state
#         questionnaire.state = state

#         questionnaire.quantity = int(data.get('quantity', 1))
#         questionnaire.free_count = int(data.get('quantity', 1))
#         questionnaire.save()

#         return json_response({
#             "msg": '更新成功'
#         })

#     @customer_required
#     def delete(self,request,*args,**kwargs):
#         data = request.DELETE
#         ids = ids = data.get('ids', [])
#         objs = Questionnaire.objects.filter(id__in=ids,state__in=[
#             0, 2, 3], customer=request.user.customer)
#         deleted_ids = [obj.id for obj in objs]
#         objs.delete()
#         return json_response({
#             'deleted_ids': deleted_ids
#         })

#     @customer_required
#     def get(self,request,*args,**kwargs):
#         data = request.GET
#         start_id = data.get("start_id",False)
#         title = data.get("title",False)
#         state = data.get("state",False)
#         page = abs(int(data.get("page",1)))
#         limit = abs(int(data.get("limit",15)))
#         with_detail = data.get("with_detail",False)
#         create_date = data.get("create_date",False)
#         pass

# class Customer_questions(Rest):
#     @customer_required
#     def put(self,request,*args,**kwargs):
#         data = request.PUT
#         questionnaire_id = data.get('questionnaire_id', 0)
#         questionnaire_exists = Questionnaire.objects.filter(id=questionnaire_id,
#                                                             customer=request.user.customer, state__in=[0, 2, 3])
#         if questionnaire_exists:
#             questionnaire = questionnaire_exists[0]
#         else:
#             return params_error({
#                 'questionnaire_id': '找不到问卷,或者问卷不可修改'
#             })
#         # 添加问题
#         question = Question()
#         question.questionnaire = questionnaire
#         question.title = data.get('title', '题纲')
#         question.category = data.get('category', 'radio')
#         question.index = int(data.get('index', 0))
#         question.save()
#         # 修改问卷状态
#         questionnaire.state = 0
#         questionnaire.save()
#         # 添加问题选项
#         # items=['aaaa','bbbb','cccc','ddddd']
#         items = data.get('items', [])

#         for item in items:
#             question_item = QuestionItem()
#             question_item.question = question
#             question_item.content = item.get('content', '')
#             question_item.save()

#         return json_response({
#             'id': question.id
#         })

#     # 问卷的修改
#     @customer_required
#     def post(self, request, *args, **kwargs):
#         data = request.POST
#         question_id = data.get('id', 0)
#         # 判断需要修改的问题是否存在
#         question_exits = Question.objects.filter(id=question_id, questionnaire__state__in=[
#             0, 2, 3], questionnaire__customer=request.user.customer)
#         if not question_exits:
#             return params_error({
#                 'id': "该问题找不到,或者该问题所在问卷无法修改"
#             })
#         # 更新问题的属性
#         question = question_exits[0]
#         question.title = data.get('title', '题纲')
#         question.category = data.get('category', 'radio')
#         question.index = int(data.get('index', 0))
#         question.save()
#         # 更新问题所在问卷的状态
#         questionnaire = question.questionnaire
#         questionnaire.state = 0
#         questionnaire.save()

#         items = data.get('items', [])
#         question.questionitem_set.all().delete()
#         for item in items:
#             question_item = QuestionItem()
#             question_item.question = question
#             question_item.content = item.get('content', '')
#             question_item.save()

#         return json_response({
#             'msg': '更新成功'
#         })

#     @customer_required
#     def delete(self, request, *args, **kwargs):
#         data = request.DELETE
#         ids = data.get('ids', [])
#         objs = Question.objects.filter(questionnaire__id__in=ids, questionnaire__state__in=[
#             0, 2, 3], questionnaire__customer=request.user.customer)

#         deleted_ids = [obj.id for obj in objs]

#         questionnaire_set = set()
#         for obj in objs:
#             questionnaire_set.add(obj.questionnaire)

#         for questionnaire in questionnaire_set:
#             questionnaire.state = 0
#             questionnaire.save()
#         objs.delete()
#         return json_response({
#             'deleted_ids': deleted_ids
#         })