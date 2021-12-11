# -*- coding: utf-8 -*-
from collections import OrderedDict
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json
import pymysql
import requests

MyPassWord = ''

with open('apis/password.json', 'r') as f:
    temp = json.loads(f.read())
    MyPassWord = temp['password']

# MySQL语句 插入数据行，即注册行为
register_sql = 'insert into user(name,password) values(%s,%s)'
# MySQL语句 查看name=username的数据行 判断是否已存在该用户
check_sql = 'select name from user where BINARY name =%s '  # 加入BINARY关键字，可使查询结果区分大小写
# check_sql = 'select name from user where name =%s '  # 这种查询无法区分大小写

# MySQL语句 查看所有符合该账号与密码的用户  若无则有误，若有则输出登录成功
login_sql = 'select * from user where name=%s and password=%s'

update_sql = 'update user set name=%s,password=%s where name=%s'

query_sql = 'select * from apis_chatmsg'

delete_sql = "delete from apis_chatmsg where username=%s and msg=%s and gentime=%s"

store_sql = 'insert into apis_chatmsg(username,msg,gentime) values(%s,%s,%s)'

add_chat_room_sql = 'insert into chatroom(room_name,create_user_name,gentime) values(%s,%s,%s)'

join_room_sql = 'insert into userInRoom(room_name,user_name) values(%s,%s)'

add_dynamic_sql = 'insert into dynamic(user_name,content,gen_time) values(%s,%s,%s)'

add_comment_sql = 'insert into comment(user_name,dynamic_id,content,gen_time) values(%s,%s,%s,%s)'

query_dynamics_sql = 'select * from dynamic'

query_comment_sql = 'select * from comment where dynamic_id=%s order by id'

add_feedback_sql = 'insert into feedback(user_name,content,gen_time) values(%s,%s,%s)'

query_withdrawMessages_sql = 'select * from withdrawMessage'

# Create your views here.


@api_view(['POST'])
def api_login(request):
    user_name = request.data.get("username")
    pass_word = request.data.get("password")
    db = pymysql.connect(host="127.0.0.1", port=3306,
                         user="root", password=MyPassWord, database="tempdb")
    cursor = db.cursor()
    res = cursor.execute(login_sql, (user_name, pass_word))
    db.commit()
    if res:
        print("登陆成功！")
        res = {"role": "admin", "code": 0,
               "msg": "登录成功", "username": user_name}
    else:
        print("用户名或密码错误！")
        res = {"role": "admin", "code": 0,
               "msg": "登录失败", "username": user_name}
    return Response(res, status=status.HTTP_200_OK)


@api_view(['POST'])
def api_register(request):
    user_name = request.data.get("username")
    pass_word = request.data.get("password")
    db = pymysql.connect(host="127.0.0.1", port=3306,
                         user="root", password=MyPassWord, database="tempdb")
    cursor = db.cursor()
    res = cursor.execute(check_sql, (user_name))
    db.commit()
    if res:
        print("用户名【%s】已存在，请重新输入！" % user_name)
        res = {"role": "admin", "code": 0,
               "msg": "注册失败", "username": user_name}
    else:
        cursor.execute(register_sql, (user_name, pass_word))
        res = {"role": "admin", "code": 0,
               "msg": "注册成功", "username": user_name}

    return Response(res, status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def history_msg(request):
    if request.method == 'GET':
        db = pymysql.connect(host="127.0.0.1", port=3306,
                             user="root", password=MyPassWord, database="tempdb")
        cursor = db.cursor()
        res = cursor.execute(query_sql)
        res = cursor.fetchall()
        newres = [OrderedDict([('id', obj[0]), ('username', obj[1]),
                              ('msg', obj[2]), ('gentime', str(obj[3]))]) for obj in res]
        return Response(newres, status=status.HTTP_200_OK)
    if request.method == 'POST':
        username = request.data.get('username')
        msg = request.data.get('msg')
        gentime = request.data.get('gentime')
        gentime = gentime.replace('T', ' ')
        gentime = gentime.replace('Z', '000')
        db = pymysql.connect(host="127.0.0.1", port=3306,
                             user="root", password=MyPassWord, database="tempdb")
        cursor = db.cursor()
        print(username, msg, gentime)
        cursor.execute(store_sql, (username, msg, gentime))
        db.commit()
        res = {'code': 0, 'msg': '消息创建成功'}
        return Response(res, status=status.HTTP_200_OK)


@api_view(['POST'])
def delete_msg(request):
    username = request.data.get('username')
    msg = request.data.get('msg')
    gentime = request.data.get('gentime')
    gentime = gentime.replace('T', ' ')
    gentime = gentime.replace('Z', '000')
    print(username, msg, gentime)
    db = pymysql.connect(host="127.0.0.1", port=3306,
                         user="root", password=MyPassWord, database="tempdb")
    cursor = db.cursor()
    cursor.execute(delete_sql, (username, msg, gentime))
    db.commit()
    res = {'code': 0, 'msg': '消息删除成功'}
    return Response(res, status=status.HTTP_200_OK)


@api_view(['POST'])
def update_password(request):
    user_name = request.data.get("username")
    pass_word = request.data.get("password")
    db = pymysql.connect(host="127.0.0.1", port=3306,
                         user="root", password=MyPassWord, database="tempdb")
    cursor = db.cursor()
    res = cursor.execute(update_sql, (user_name, pass_word, user_name))
    db.commit()
    res = {"role": "admin", "code": 0, "msg": "修改密码成功", "username": user_name}
    return Response(res, status=status.HTTP_200_OK)


@api_view(['POST'])
def add_chat_room(request):
    admin_name = request.data.get("admin_name")
    room_name = request.data.get("room_name")
    gen_time = request.data.get("gen_time")
    db = pymysql.connect(host="127.0.0.1", port=3306,
                         user="root", password=MyPassWord, database="tempdb")
    cursor = db.cursor()
    res = cursor.execute(add_chat_room_sql, (admin_name, room_name, gen_time))
    db.commit()
    res = {"role": "admin", "code": 0,
           "msg": "添加聊天室成功", "username": admin_name}
    return Response(res, status=status.HTTP_200_OK)


@api_view(['POST'])
def join_room(request):
    user_name = request.data.get("user_name")
    room_name = request.data.get("room_name")
    db = pymysql.connect(host="127.0.0.1", port=3306,
                         user="root", password=MyPassWord, database="tempdb")
    cursor = db.cursor()
    res = cursor.execute(update_sql, (user_name, room_name))
    db.commit()
    res = {"role": "admin", "code": 0, "msg": "加入聊天室成功", "username": user_name}
    return Response(res, status=status.HTTP_200_OK)


@api_view(['POST'])
def add_dynamic(request):
    user_name = request.data.get("user_name")
    content = request.data.get("content")
    gen_time = request.data.get("gen_time")
    gen_time = gen_time.replace('T', ' ')
    gen_time = gen_time.split(".")[0]
    db = pymysql.connect(host="127.0.0.1", port=3306,
                         user="root", password=MyPassWord, database="tempdb")
    cursor = db.cursor()
    res = cursor.execute(add_dynamic_sql, (user_name, content, gen_time))
    db.commit()
    res = {"role": "admin", "code": 0, "msg": "添加动态成功", "username": user_name}
    return Response(res, status=status.HTTP_200_OK)


@api_view(['POST'])
def add_comment(request):
    user_name = request.data.get("user_name")
    dynamic_id = request.data.get("dynamic_id")
    content = request.data.get("content")
    gen_time = request.data.get("gen_time")
    gen_time = gen_time.replace('T', ' ')
    gen_time = gen_time.split(".")[0]
    print(gen_time)
    db = pymysql.connect(host="127.0.0.1", port=3306,
                         user="root", password=MyPassWord, database="tempdb")
    cursor = db.cursor()
    res = cursor.execute(
        add_comment_sql, (user_name, dynamic_id, content, gen_time))
    db.commit()
    res = {"role": "admin", "code": 0, "msg": "添加评论成功", "username": user_name}
    return Response(res, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_dynamics(request):
    if request.method == 'GET':
        db = pymysql.connect(host="127.0.0.1", port=3306,
                             user="root", password=MyPassWord, database="tempdb")
        cursor = db.cursor()
        res = cursor.execute(query_dynamics_sql)
        res = cursor.fetchall()
        dynamic_comments = []
        for obj in res:
            id = obj[0]
            res_new = cursor.execute(query_comment_sql, (id))
            res_new = cursor.fetchall()
            res_tmp = [OrderedDict([('id', obj[0]), ('username', obj[1]), (
                'content', obj[3]), ('gentime', str(obj[4]))]) for obj in res_new]
            dynamic_comments.append(res_tmp)

        newres = [OrderedDict([('id', res[i][0]), ('username', res[i][1]), ('content', res[i][2]), (
            'gentime', str(res[i][3])), ('comments', dynamic_comments[i])]) for i in range(len(res)-1, -1, -1)]
        return Response(newres, status=status.HTTP_200_OK)


@api_view(['POST'])
def feedback(request):
    user_name = request.data.get("username")
    content = request.data.get("content")
    gen_time = request.data.get("gen_time")
    gen_time = gen_time.replace('T', ' ')
    gen_time = gen_time.split(".")[0]
    url = 'https://sctapi.ftqq.com/SCT82924TUHiwkqNmhueXluFlvX8ht3Gb.send?title=用户反馈&desp=' + \
        content+' --from '+user_name
    requests.get(url)
    db = pymysql.connect(host="127.0.0.1", port=3306,
                         user="root", password=MyPassWord, database="tempdb")
    cursor = db.cursor()
    res = cursor.execute(
        add_feedback_sql, (user_name, content, gen_time))
    db.commit()
    res = {"role": "admin", "code": 0, "msg": "反馈成功", "username": user_name}
    return Response(res, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_withdrawMessages(request):
    db = pymysql.connect(host="127.0.0.1", port=3306,
                         user="root", password=MyPassWord, database="tempdb")
    cursor = db.cursor()
    res = cursor.execute(query_withdrawMessages_sql)
    res = cursor.fetchall()
    newres = [OrderedDict([('id', obj[0]), ('username', obj[1]),
                           ('msg', obj[2]), ('gentime', str(obj[3]))]) for obj in res]
    return Response(newres, status=status.HTTP_200_OK)
