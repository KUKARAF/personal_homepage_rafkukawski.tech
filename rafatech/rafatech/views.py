#!/usr/bin/env python
# -*- coding: utf-8 -*-


from django.http import HttpResponse


def robots(request): 
    robots = '''
        User-agent: * \n
        Disallow: /todo/* \n
    '''
    return HttpResponse(robots)
