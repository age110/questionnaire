# 完成用户的问卷审核，上传的功能
# 接口 /api/v1/questionnaire_state
import json

from Api.rest import Rest
from Api.utils import *
from Api.decorations import *
from Myquestion.models import *

'''
method: POST

api: `/api/v1/questionnaire_state`

body:
- **id**: 问卷id
- **state**: 问卷状态

>  本接口用于:
> - 问卷提交审核:将问卷状态改为1,
> - 问卷发布:将问卷状态改为4

response:
```json
{
    "msg":"修改成功"
}
'''
class Questionnaire_state(Rest):
    @customer_required
    def post(self,request,*args,**kwargs):
        data = request.POST
        questionnaire_id = int(data.get('questionnaire_id',0))
        try:
            questionnaire = Questionnaire.objects.get(id=questionnaire_id,customer=
            request.user.customer,state__in=[0])
        except Exception as e:
            return params_error({
                'questionnaire_id':"找不到对应的问卷,或者问卷不可提交"
            })
        
        questionnaire.state = 1
        questionnaire.save()

        return json_response({
            "msg": '问卷已提交成功'
        })

    @customer_required
    def post(self,request,*args,**kwargs):
        data = request.POST
        questionnaire_id = int(data.get('questionnaire_id',0))
        questionnaire_exits = Questionnaire.objects.filter(
            id=questionnaire_id, customer=request.user.customer, state=3)
        if not questionnaire_exits:
            return params_error({
                'questionnaire_id': '问卷找不到,或者该问卷还未通过审核'
            })
        questionnaire = questionnaire_exits[0]
        questionnaire.state = 4
        questionnaire.save()
        return json_response({
            'state': "发布成功"
        })

        

    