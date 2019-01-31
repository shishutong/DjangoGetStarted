# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from models import UserMessage

# Create your views here.

def getform(request):
    #all_message = UserMessage.objects.filter(name='gcd', address=u"北京")
      # UserMessage默认的数据管理器objects。
    # 方法all()是将所有数据返回成一个queryset类型(django的内置类型)
    #all_message = UserMessage.objects.all()

    #我们可以对于all_message进行遍历操作
    #for message in all_message:
        # 每个message实际就是一个UserMessage对象（这时我们就可以使用对象的相关方法）。
    #    print message.name

# html表单部分

   # 此处对应html中的method="post"，表示我们只处理post请求
    #if request.method == "POST":
       # 就是取字典里key对应value值而已。取name，取不到默认空
    #   name = request.POST.get('name', '')
    #   message = request.POST.get('message', '')
    #   address = request.POST.get('address', '')
    #   email = request.POST.get('email', '')

       # 实例化对象
    #   user_message = UserMessage()

       # 将html的值传入我们实例化的对象.
    #   user_message.name = name
    #   user_message.message = message
    #   user_message.address = address
    #   user_message.email = email
    #   user_message.object_id = "ijkf"

       # 调用save方法进行保存
    #   user_message.save()

    # 方法2 :filter取出指定条件值，逗号代表and 必须同时满足两个条件才返回。
    #all_message = UserMessage.objects.filter(name='dvadv', address='比萨饼')

    # 我的数据库里保存着可以匹配到该条数据的一行。

    # 删除操作：使用delete方法删除all_message

    #all_message.delete()

    #for message in all_message:
        # 删除取到的message对象
    #    message.detele()
        # print message.name
    #return render(request, 'message_form.html')
    message = None
    all_message = UserMessage.objects.filter(name='gcd', )

    # if 判断是否存在数据
    if all_message:
        # all_message是一个list，可以使用切片。
        message = all_message[0]

    return render(request, 'message_form.html',{
        "my_message" : message})
