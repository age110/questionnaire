from django.db import models

# Create your models here.

from datetime import date
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Customer(models.Model):
    """
    # 客户信息 1
    """
    user = models.OneToOneField(User)
    name = models.CharField(default='名称', max_length=32, help_text="客户名称")
    email = models.EmailField(default='', null=True,blank=True, help_text="邮箱")

    class Meta:
        db_table = 'customers'

class UserInfo(models.Model):
    """
    # 用户信息 2
    """
    user = models.OneToOneField(User)
    name = models.CharField(default='姓名', max_length=32, help_text="姓名")
    # age = models.IntegerField(default=1, help_text="年龄")
    # gender = models.CharField(max_length=8, default="male", help_text="性别")
    # phone = models.CharField(default='', max_length=16,
    #                          blank=True, null=True, help_text="手机号码")
    # email = models.EmailField(default='', blank=True,
    #                           null=True, help_text="邮箱")
    # address = models.CharField(
    #     default='', max_length=256, blank=True, null=True, help_text="地址")
    # birthday = models.DateField(default=date(
    #     2018, 1, 1), null=True, help_text="出生日期")
    qq = models.CharField(default='', max_length=16,
                          blank=True, null=True, help_text="QQ")
    # wechat = models.CharField(
    #     default='', max_length=64, blank=True, null=True, help_text="微信号")
    # job = models.CharField(default='', max_length=32,
    #                        blank=True, null=True, help_text="职业")
    # favo = models.CharField(default='',max_length=32,blank=True,null=True,help_text="爱好")
    # salary = models.CharField(
    #     default='', max_length=32, blank=True, null=True, help_text="收入水平")

    class Meta:
        db_table = 'userinfos'


# 创建问卷模型
class Questionnaire(models.Model):
    """
    # 问卷
    """
    customer = models.ForeignKey('Customer', help_text="客户信息")
    title = models.CharField(default="标题", max_length=64, help_text="标题")
    create_date = models.DateTimeField(help_text="创建时间")
    deadline = models.DateTimeField(help_text="截止时间")
    state = models.IntegerField(default=0, help_text="""状态,0-->草稿,1-->待审核,2-->审核失败,
                                                        3-->审核成功,4-->发布成功""")
    quantity = models.IntegerField(default=1, help_text='发布数量')
    free_count = models.IntegerField(default=1, help_text='可用问卷数量')

# 创建问题模型
class Question(models.Model):
    """
    # 题目
    """
    category_choices = [
        ('radio', '单选'),
        ('select', '多选'),
    ]
    questionnaire = models.ForeignKey(
        'Questionnaire', help_text="问卷", on_delete=models.CASCADE)
    title = models.CharField(max_length=128, help_text="题纲")
    index = models.IntegerField(default=0, help_text="题目题号", db_index=True)
    category = models.CharField(
        choices=category_choices, default='radio', max_length=16, help_text="是否多选")


class QuestionItem(models.Model):
    """
    # 题目选项
    """
    question = models.ForeignKey(
        'Question', help_text="题目", on_delete=models.CASCADE)
    content = models.CharField(max_length=32, help_text="选项内容")
    
'''
问卷批注
'''
class QuestionnaireComment(models.Model):
    """
    # 问卷审核
    """
    questionnaire = models.ForeignKey(
        'Questionnaire', help_text="问卷", on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now=True, help_text="审核时间")
    comment = models.TextField(help_text="审核批注")


class Answer(models.Model):
    """
    # 回答问卷题目
    """
    userinfo = models.ForeignKey('UserInfo', null=True, help_text="用户信息")
    questionnaire = models.ForeignKey('Questionnaire', help_text="问卷")
    create_date = models.DateTimeField(auto_now=True, help_text="参与时间")
    is_done = models.BooleanField(default=False, help_text="是否已经完成")

class AnswerItem(models.Model):
    """
    # 回答题目选项
    """
    userinfo = models.ForeignKey('UserInfo', null=True, help_text="用户信息")
    item = models.ForeignKey('QuestionItem', help_text="选项")