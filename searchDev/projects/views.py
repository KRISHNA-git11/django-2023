from django.shortcuts import render
from django.http import HttpResponse


projectList = [
    {
        'id' : 1,
        'name' : 'Project One',
        'content' : 'Dolor do non aute Lorem velit id ullamco minim sunt. Fugiat ullamco ipsum magna ad ipsum ad ullamco. Commodo Lorem sunt fugiat sunt commodo consectetur anim do cillum commodo laboris nostrud. Nulla voluptate ipsum amet consectetur ullamco dolor voluptate nostrud sit exercitation proident qui laborum voluptate.'
    },
    {
        'id' : 2,
        'name' : 'Project Two',
        'content' : 'Dolor do non aute Lorem velit id ullamco minim sunt. Fugiat ullamco ipsum magna ad ipsum ad ullamco. Commodo Lorem sunt fugiat sunt commodo consectetur anim do cillum commodo laboris nostrud. Nulla voluptate ipsum amet consectetur ullamco dolor voluptate nostrud sit exercitation proident qui laborum voluptate.'
    },
    {
        'id' : 3,
        'name' : 'Project Three',
        'content' : 'Dolor do non aute Lorem velit id ullamco minim sunt. Fugiat ullamco ipsum magna ad ipsum ad ullamco. Commodo Lorem sunt fugiat sunt commodo consectetur anim do cillum commodo laboris nostrud. Nulla voluptate ipsum amet consectetur ullamco dolor voluptate nostrud sit exercitation proident qui laborum voluptate.'
    }

]

def returnProjects(request):
    page = 'projects'
    number = 10
    context = {'page': page, 'number': number, 'projects': projectList}

    return render(request, 'projects/projects.html', context)


def returnProject(request, pid):
    projectObj = None
    for i in projectList:
        if i['id'] == pid:
            projectObj = i
    return render(request, 'projects/single-project.html', {'project': projectObj})


# Create your views here.
