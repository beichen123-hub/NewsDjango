from django.shortcuts import render,redirect
from play.models import NewsType,NewsInfo
from django.http import HttpResponse


def insert(request):
    n1 = NewsType(tName="体育",username="zhang@qq.com",password="123456")
    n1.save()
    n2 = NewsType(tName="娱乐",username="zhang@qq.com",password="123456")
    n2.save()
    n3 = NewsType(tName="科技",username="zhang@qq.com",password="123456")
    n3.save()

    NewsInfo.objects.create(tid=n1, nTitle='CAB被控ns苏州',nAuthor='搜狐新闻',nContent='两人交战，情势非常激烈',Nstatus=True)
    NewsInfo.objects.create(tid=n1, nTitle='足球', nAuthor='搜狐新闻', nContent='十年巨大巨星',Nstatus=True)
    NewsInfo.objects.create(tid=n1, nTitle='5G时代', nAuthor='搜狐新闻', nContent='5G来临',Nstatus=False)
    NewsInfo.objects.create(tid=n2, nTitle='CAB被控ns苏州', nAuthor='搜狗新闻', nContent='两人交战，情势非常激烈',Nstatus=True)
    NewsInfo.objects.create(tid=n2, nTitle='足球', nAuthor='搜狗新闻', nContent='十年巨大巨星',Nstatus=False)
    NewsInfo.objects.create(tid=n2, nTitle='5G时代', nAuthor='搜狗新闻', nContent='5G来临',Nstatus=False)
    NewsInfo.objects.create(tid=n3, nTitle='CAB被控ns苏州', nAuthor='新浪新闻', nContent='两人交战，情势非常激烈',Nstatus=True)
    NewsInfo.objects.create(tid=n3, nTitle='足球', nAuthor='新浪新闻', nContent='十年巨大巨星',Nstatus=False)
    NewsInfo.objects.create(tid=n2, nTitle='5G时代', nAuthor='新浪新闻', nContent='5G来临',Nstatus=True)
    return HttpResponse('数据添加成功')





def login(request):
    if request.method== 'GET':
        return render(request,"login.html")
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
        z = NewsType.objects.filter(username=username, password=password).first()
        if z:
            return redirect("show")
        else:
            return redirect("login")

# 展示正常版本
# def show(request):
#     t_all = NewsType.objects.all()
#     i_all = NewsInfo.objects.all()
#     if request.method == 'GET':
#         return render(request, "Index.html",{
#             "t_all":t_all,
#             "i_all":i_all,
#         })



# 展示带模糊查询
def show(request):
    t_all =NewsType.objects.all()
    if request.method == 'GET':
        i_all = NewsInfo.objects.all()
        return render(request, "Index.html",{
            "t_all":t_all,
            "i_all":i_all,
        })
    else:
        q = request.POST.get('n1')
        i_all = NewsInfo.objects.filter(nTitle__contains=q)
        return render(request, "Index.html",{
            "t_all": t_all,
            "i_all": i_all,
        })





def zeng(request):
    if request.method== 'GET':
        return render(request,"InsertNewsInfo.html")
    else:
        nTitle = request.POST.get('nTitle')
        nAuthor = request.POST.get('nAuthor')
        tName = request.POST.get('tName')
        Nstatus = request.POST.get('Nstatus')
        nContent = request.POST.get('nContent')
        z = NewsType.objects.filter(tName=tName).first()
        if z:
            NewsInfo.objects.create(nTitle=nTitle, nAuthor=nAuthor, nContent=nContent, Nstatus=Nstatus, tid=z)
        else:
            zz = NewsType(tName=tName)
            zz.save()
            NewsInfo.objects.create(nTitle=nTitle, nAuthor=nAuthor, nContent=nContent, Nstatus=Nstatus, tid=zz)
        return redirect("show")



def delete(request, id):
    s1 = NewsInfo.objects.filter(id=id).first()
    s1.delete()
    return redirect("show")

def zhuce(request):
    if request.method== 'GET':
        return render(request,"zhuce.html")
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
        z = NewsType.objects.filter(username=username).first()
        if z:
            return HttpResponse("此账号已被注册")
        else:
            NewsType(username=username, password=password).save()
            return redirect("login")


