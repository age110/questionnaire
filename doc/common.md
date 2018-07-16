# 通用接口

## 获取验证码

method: GET

api: `/api/v1/registcode`

body: None

response:

```json
{
    "regist_code":345693//返回的验证码
}
```

## 用户接口

### 注册用户

method: PUT

api: `/api/v1/user`

body:
- **username**:用户名
- **password**:密码
- **ensure_password**:确认密码
- **regist_code**:注册码
- category:注册的用户类型

response:

```json
{
    "id":1//新建的用户id
}
```

### 获取用户信息

method: GET

api: `/api/v1/user`

body: None

response:
```json
{
    "name":"千锋",//名称
    "email":"1000@phone.com",//邮箱
    "user":1,//用户id
    "category":"customer",//用户类型,可以是['customer','userinfo']
}
//或者
{
    "name":"张三",//姓名
    "qq":"123123123",//QQ号
    "user":2,//用户id
    "category":"userinfo"//用户类型
}
```

### 更新用户信息

method: POST

api: `/api/v1/user`

body:
- name:名称
- email: 邮箱
- qq:QQ号

response:
```json
{
    "msg":"更新成功"
}
```

## 会话

### 登录

method: PUT

api: `/api/v1/session`

body:
- **username**: 用户名
- **password**: 密码

response:
```json
{
    "msg":"登录成功"
}
```

### 退出

method: DELETE

api: `/api/v1/sessoin`

body: None

response:
```json
{
    "msg":"退出成功"
}
```







