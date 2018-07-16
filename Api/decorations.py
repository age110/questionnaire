from Api.utils import *


# 客户装饰器
def customer_required(func):
    def wrapper(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return not_authenticated()
        user = request.user
        if not hasattr(user, 'customer'):
            return not_authenticated()
        return func(self, request, *args, **kwargs)
    return wrapper


# 普通用户装饰器
def userinfo_required(func):
    def wrapper(self, request,*args, **kwargs):
        if not request.user.is_authenticated():
            return not_authenticated()
        user = request.user
        if not hasattr(user, 'userinfo'):
            return not_authenticated()
        return func(self, request, *args, **kwargs)
    return wrapper

# 管理员装饰器
def superuser_required(func):
    def wrapper(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return not_authenticated()
        return func(self, request, *args, **kwargs)
    return wrapper
