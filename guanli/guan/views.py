from django.shortcuts import render,HttpResponseRedirect,HttpResponse
import models
# Create your views here.
def index(req):
    guanli = models.guan.objects.all()
    try:
        guanli_id=req.GET.get('guan_id')
        if guanli_id:
            guanli_id=int(guanli_id)
            models.guan.objects.get(id=guanli_id).delete()
    except Exception,e:
        print e
    return render(req,"index.html",locals())
def zenjia(req):
    if req.method == "GET":
        texs = models.tex.objects.all()
        return render(req,"zenjia.html",locals())
    else:
        tex_x =models.tex.objects.get(id=req.POST.get("tex"))
        ceng_x = models .ceng.objects.get(name=req.POST.get("ceng"))
        zhuangtai_x = models.zhuangtai.objects.get(name=req.POST.get("zhuangtai"))
        models.guan.objects.create(
        num =req.POST.get("num"),
        tex = tex_x,
        ceng = models.ceng.objects.get(id=ceng_x.id),
        zhuangtai = models.zhuangtai.objects.get(id=zhuangtai_x.id),
        jiage = req.POST.get("jiage"),
        )
        return HttpResponseRedirect("/")

def update(req):
    if req.method == "GET":
        allroom = models.guan.objects.all()
        texs = models.tex.objects.all()
        return render(req,"update.html",locals())
    else:
        num =req.POST.get("num")
        tex_x =models.tex.objects.get(id=req.POST.get("tex"))
        ceng_x = models .ceng.objects.get(name=req.POST.get("ceng"))
        zhuangtai_x = models.zhuangtai.objects.get(name=req.POST.get("zhuangtai"))
        room_obj = models.guan.objects.get(num=num)
        room_obj.num = req.POST.get("num")
        room_obj.tex = tex_x
        room_obj.ceng = models.ceng.objects.get(id=ceng_x.id)
        room_obj.zhuangtai = models.zhuangtai.objects.get(id=zhuangtai_x.id)
        room_obj.jiage = req.POST.get("jiage")
        room_obj.save()
        return HttpResponseRedirect("/")

def see(req):
    room_type = models.tex.objects.all()
    return render(req,"see.html",locals())
