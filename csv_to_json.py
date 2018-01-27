#!/usr/bin/python
#-*-coding:utf-8 -*-
import numpy as np
import pandas as pd
import csv
import os
import sys
import json
print sys.getdefaultencoding()

pfile = '/Users/XXX/Downloads/get_psu_from_nbs/province.csv'
p_cfile = '/Users/XXX/Downloads/get_psu_from_nbs/province_city.csv'
c_cfile = '/Users/XXX/Downloads/get_psu_from_nbs/city_county.csv'

def parse_csv(datafile):
    data = []
    n = 0
    with open(datafile,'rU') as sd:
        r = csv.reader(sd) #将数据读取为列表， 将第一行作为Key
        for line in r:
            data.extend(line)
    return(data)
    
    def parse_csv_dict(datafile):
    data = []
    n = 0
    with open(datafile,'rU') as sd:
        r = csv.DictReader(sd) #将数据读取为字典， 将第一行作为Key
        for line in r:
            data.extend(line)
    return(data)

province = parse_csv(pfile)
print json.dumps(province, encoding='UTF-8', ensure_ascii=False) #got dictionary of province

#dictionary of province to city
    p_c = []
with open(p_cfile, 'rU') as sd:
    r = csv.reader(sd, delimiter =",")
    r.next()
    for line in r:
        p_c.append(line)
c_c = []
with open(c_cfile, 'rU') as sd:
    r = csv.reader(sd, delimiter =",")
    r.next()
    for line in r:
        c_c.append(line)
        
city = {}
for line in province:
    city[line] = []

city_keys = [city.keys]
for line in city_keys:
    for row in p_c:
        if city.get(row[0]) != None:
            city[row[0]].append(row[1])
print json.dumps(city, encoding='UTF-8', ensure_ascii=False)  #got json format of province to city

#dictionary of city to county
county = {}
for line in p_c:
    county[line[1]] = []

county_keys = [county.keys]
for line in county_keys:
    for row in c_c:
        if county.get(row[0]) != None:
            county[row[0]].append(row[1])
print json.dumps(county, encoding='UTF-8', ensure_ascii=False) #got json format of city to county
