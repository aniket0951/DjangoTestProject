from asyncio.log import logger
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from numpy import lookfor
from .forms import *
from django.views.generic.edit import FormView
import logging

logger = logging.getLogger("django")
# logger = logging.getLogger(__name__)

# Create your views here.
class TestFunc(FormView):
    form_class = TestForm
    logger.debug("Aniket Suryawanshi") 
    # specify name of template
    template_name = "TestForm.html"
 
    # can specify success url
    # url to redirect after successfully
    # updating details
    success_url ="/thanks/"

def TestMe(request):
    import os
    directory = os.getcwd()
    print(f"Test me called {directory}")
    logger.debug("logger got called")
    return JsonResponse("bsjfjdfj", safe=False)
