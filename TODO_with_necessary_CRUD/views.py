from django.http import HttpResponse
from django.shortcuts import render,redirect
import asana
from datetime import datetime
# Create your views here.
def home(request):
    accessToken = "1/1201800762568260:f3d635fcfe882948cefcce5585990a6c"
    client = asana.Client.access_token(accessToken)
    me = client.users.me()
    # print("Hello " + me['name'])
    workspace_id = me['workspaces'][0]['gid']
    result = client.tasks.get_tasks_for_project("1201823791485761", opt_pretty=True)
    createList=list()
    x = list(result)
    for i in x:
        getTask = client.tasks.get_task(i['gid'], opt_pretty=True)
        # print(list(getTask))
        createList.append(dict(getTask))
        # print(i)
    # print(createList)
    return render(request,"index.html",{"params":createList})
def addTask(request):
    if request.method=="POST":
        title = request.POST.get("title")
        desc = request.POST.get("desc")
        status = request.POST.get("status")
        accessToken = "1/1201800762568260:f3d635fcfe882948cefcce5585990a6c"
        client = asana.Client.access_token(accessToken)
        me = client.users.me()
        # print("before", me['workspaces'][0]['gid'])
        # cresult = client.custom_fields.get_custom_field("1201806637088983", opt_pretty=True)

        data = {
            "name": f"{title}",
            "custom_fields": {1201806637088983: f"{status}"},
            "projects": [
                "1201823791485761"
            ],
            "due_on": datetime.today().strftime("%Y-%m-%d"),
            "resource_subtype": "default_task",
            "notes": f"{desc}",
            "assignee": me['gid']
        }
        result = client.tasks.create_task(data, opt_pretty=True)
        return redirect("/")
    else:
        return HttpResponse(405)

def update(request):
    if request.method == "POST":
        title = request.POST.get("title")
        desc = request.POST.get("desc")
        status = request.POST.get("status")
        taskGid = request.POST.get("taskGid")

        accessToken = "1/1201800762568260:f3d635fcfe882948cefcce5585990a6c"
        client = asana.Client.access_token(accessToken)
        me = client.users.me()
        if len(title)!=0 and len(desc)!=0:
            data = {
                "name": f"{title}",
                "custom_fields": {1201806637088983: f"{status}"},
                "notes": f"{desc}",
            }
            result = client.tasks.update_task(taskGid, data, opt_pretty=True)
            print(result)

        elif len(desc)!=0:
            data = {
                "custom_fields": {1201806637088983: f"{status}"},
                "notes": f"{desc}",

            }
            print(taskGid)
            result = client.tasks.update_task(taskGid, data, opt_pretty=True)
        elif len(title)!=0:
            data = {
                "name": f"{title}",
                "custom_fields": {1201806637088983: f"{status}"},

            }
            result = client.tasks.update_task(taskGid, data, opt_pretty=True)
        return redirect("/")
    else:
        print(request.method)
        return HttpResponse(405)
