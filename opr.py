#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

auth_key = 'c2xpZrkWoRAnGNl3fDmXwbg7eKLIdzs0ADRG0xXhqEFyeHOtFcW1PF3jr8qVIcUx'
headers = {'X-TBA-Auth-Key' : auth_key}

r = requests.get('https://www.thebluealliance.com/api/v3', headers = headers)
print(r.url)
print(r.status_code)
