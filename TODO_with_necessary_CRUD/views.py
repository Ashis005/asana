from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
import asana
# Create your views here.
def home(request):
    accessToken = "1/1201800762568260:f3d635fcfe882948cefcce5585990a6c"
    client = asana.Client.access_token(accessToken)
    me = client.users.me()
    print("Hello " + me['name'])
    workspace_id = me['workspaces'][0]['gid']
    result = client.tasks.get_tasks_for_project("1201823791485761", opt_pretty=True)
    createList=list()
    x = list(result)
    for i in x:
        getTask = client.tasks.get_task(i['gid'], opt_pretty=True)
        # print(list(getTask))
        createList.append(dict(getTask))
        # print(i)
    print(createList[0]['notes'])
    return render(request,"index.html",{"params":createList})