# -*- coding: utf-8 -*-
from django.http import HttpResponse

def here(request):
	return HttpResponse('Hello World! I am a python programmer! 我是Python網頁工程師!')