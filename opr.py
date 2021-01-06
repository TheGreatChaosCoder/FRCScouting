#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

baseUrl = 'https://www.thebluealliance.com/api/v3'
auth_key = 'c2xpZrkWoRAnGNl3fDmXwbg7eKLIdzs0ADRG0xXhqEFyeHOtFcW1PF3jr8qVIcUx'
headers = {'X-TBA-Auth-Key' : auth_key}

def getTBAJson(url):
	return requests.get(baseUrl + url, headers=headers).json()

opr = getTBAJson('/event/2020mokc/oprs')
oprDict = opr["oprs"]

for team in opr["oprs"]:

    print(team+': ' + str(oprDict[team]));

