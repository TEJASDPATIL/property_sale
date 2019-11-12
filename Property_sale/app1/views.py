from django.shortcuts import render

# Create your views here.
def showMain(request):
    return render(request,"index.html")


def loginCheck(request):
    username = request.POST.get("uname")
    password = request.POST.get("pass")
    if username=="admin": 
        if password=="admin":
            return render(request, "usercheck.html")
        else:
            return render(request, "index.html", {"message": "Incorrect PASSWORD"})
    else:
        return render(request,"index.html",{"message":"Incorrect USERNAME"})

def newPlot(request):
    return render(request,"newplot.html")

from .models import PlotModel
def savePlot(request):
    p_no  = request.POST.get("pno")
    r_no = request.POST.get("rdno")
    s_no = request.POST.get("sno")
    area = request.POST.get("ar")
    cost = request.POST.get("rate")
    other = request.POST.get("exp")
    bound = request.POST.get("bn")
    fac = request.POST.get("fc")
    stat = request.POST.get("st")
    total_cost = request.POST.get("tc")
    PlotModel(plotno=p_no,roadno=r_no,surveyno=s_no,areasqyrd=area,costpryard=cost,otherexp=other,boundaries=bound,facing=fac,status=stat,totalcost=total_cost).save()
    return render(request,"usercheck.html",{"message":"Plot added."})


def getPlot(request):
    return render(request,"getplot.html")


def viewPlot(request):
    pn = request.POST.get("pltno")
    qs = PlotModel.objects.filter(plotno=pn)
    return render(request,"viewplot.html",{"data":qs})


def viewPlotDetail(request):
    plot_no = request.GET.get("plno")
    qs = PlotModel.objects.filter(plotno=plot_no)
    return render(request, "viewplotdetail.html",{"data":qs})


def editPlot(request):
    return render(request, "editplot.html")


def updatePlot(request):
    pno = request.POST.get("plno")
    up = PlotModel.objects.get(plotno=pno)
    return render(request,"update.html",{"data":up})


def plotUpdate(request):
    p_no = request.POST.get("p")
    r_no = request.POST.get("r")
    s_no = request.POST.get("s")
    area = request.POST.get("a")
    cost = request.POST.get("c")
    other = request.POST.get("o")
    bound = request.POST.get("b")
    fac = request.POST.get("f")
    stat = request.POST.get("st")
    total_cost = request.POST.get("t")
    PlotModel(plotno=p_no, roadno=r_no, surveyno=s_no, areasqyrd=area, costpryard=cost, otherexp=other,
              boundaries=bound, facing=fac, status=stat, totalcost=total_cost).save()
    return render(request, "usercheck.html", {"message": "Plot added."})

from  .models import ApartmentModel
def newFlat(request):
    return render(request,"newflat.html")


def saveFlat(request):
    f_no = request.POST.get("flno")
    ap_name = request.POST.get("apname")
    ap_loc = request.POST.get("apl")
    ar_sqft = request.POST.get("asqft")
    cost_sqft = request.POST.get("cpsqft")
    m_charge = request.POST.get("mcharge")
    fac = request.POST.get("facing")
    stat = request.POST.get("st")
    t_cost = request.POST.get("tc")
    ApartmentModel(flatno=f_no,apname=ap_name,aplocation=ap_loc,areasqft=ar_sqft,costpsqft=cost_sqft,maintcost=m_charge,facing=fac,status=stat,totalcost=t_cost).save()
    return render(request, "usercheck.html", {"message": "Flat added."})


def getFlat(request):
    return render(request, "getflat.html")


def viewFlat(request):
    qs1 = ApartmentModel.objects.all()
    return render(request, "viewflat.html", {"data1": qs1})


def newEmp(request):
    return render(request,"newemp.html")

from  .models import  EmployeeModel
def saveEmp(request):
    e_id = request.POST.get("ei")
    e_name = request.POST.get("en")
    e_email = request.POST.get("ee")
    e_loc = request.POST.get("el")
    e_doj = request.POST.get("doj")
    e_role = request.POST.get("er")
    e_remark = request.POST.get("ere")
    EmployeeModel(eid=e_id,ename=e_name,eemail=e_email,elocation=e_loc,edoj=e_doj,erole=e_role,eremark=e_remark).save()

    return render(request, "usercheck.html", {"message": "Employee added."})


def viewEmp(request):
    qs = EmployeeModel.objects.all()
    return render(request, "viewemp.html", {"data": qs})


def editEmp(request):
    e_id = request.GET.get("eid")
    up = EmployeeModel.objects.get(eid=e_id)
    return render(request,"updateemp.html",{"data":up})


def updateEmp(request):
    e_id = request.POST.get("ei")
    e_name = request.POST.get("en")
    e_email = request.POST.get("ee")
    e_loc = request.POST.get("el")
    e_doj = request.POST.get("doj")
    e_role = request.POST.get("er")
    e_remark = request.POST.get("ere")
    EmployeeModel(eid=e_id, ename=e_name, eemail=e_email, elocation=e_loc, edoj=e_doj, erole=e_role,
                  eremark=e_remark).save()

    return render(request, "usercheck.html", {"message": "Employee Updated."})


def deleteEmp(request):
    e_id = request.GET.get("eid")
    EmployeeModel.objects.filter(eid=e_id).delete()
    qs = EmployeeModel.objects.all()
    return render(request, "viewemp.html", {"data":qs},{"message":"Employee Deleted"})


def home(request):
    return render(request, "usercheck.html")


def about(request):
    return render(request, "about.html")
