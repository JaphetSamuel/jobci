from .models import *
from django.template import RequestContext
from django.http import request

def mescontext(req):
    list_type = []
    cat_list = []
    exp_list = []
    for type in Job.jobtype:
        list_type.append(type[0])
    
    for cat in Job.Categories:
        cat_list.append(cat[0])

    for exp in Job.Experiences:
        exp_list.append(exp[0])

    return {
        "monmsg":"le message nous parle de jesus",
        "list_type" : list_type,
        "cat_list":cat_list,
        "exp_list": exp_list
    }
    