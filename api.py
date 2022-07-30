import http.client
import datetime
import json
from pandas import json_normalize

f = open('out.csv', 'w')

def get_data(aile,tarih):
    url = "/api/data/searchbyaile?aile="
    url += str(aile)
    url += "&tarih="
    url += str(tarih)
    print(url)
    conn = http.client.HTTPSConnection("api.akademetre.com")
    payload = ''
    headers = {
      'apiKey': 'CBD947DB-F458-4718-9CF5-E87E934F07D0'
    }
    conn.request("GET", url, payload, headers)
    res = conn.getresponse()
    data = res.read()
    new_line = data.decode("utf-8")
    print("res len:"+ str(len(new_line)))

    if (len(new_line) > 1):
        dict = json.loads(new_line)
        df2 = json_normalize(dict)
        df2.to_csv("out.csv", mode='a', header=False)
        # f.write(df2 + '\n')
        # print(new_line)

# by foods name

start_time  = 1514764800 #2018.1.1
now = 1655457589 #2022.6.17

aile_arr = ["PATLICAN/", "PATLICAN", "MUZ/", "MUZ", "KARPUZ", "KARPUZ/", "KABAK/", "KABAK", "HAVUC/", "BIBER/", "BIBER", "SALATALIK/", "SALATALIK", "SARIMSAK/",
    "SARIMSAK", "FASULYE", "SEFTALI/", "SEFTALI", "UZUM", "LIMON", "LIMON/", "DOMATES", "DOMATES/", "ARMUT", "AYVA/", "LAHANA", "CILEK/", "ELMA", "ISPANAK/", "KARNABAHAR/",
    "KAVUN", "MANDALINA/", "NAR/", "PIRASA/", "PORTAKAL", "SOGAN", "MANTAR", "PATATES", "PATATES/"
]

for epoc in range(start_time,now,86400*7):
    idate = datetime.datetime.fromtimestamp(epoc).strftime('%Y-%m-%d')

    for aile in aile_arr:
        print(aile, idate)
        get_data(aile, idate)
        
        

##############################################################

import http.client
import datetime
import json
from pandas import json_normalize

# get the data year by year

f = open('out_2021.csv', 'w')

def get_data(barkod, tarih):
    url = "/api/data/SearchByBarkod?barkod="
    url += str(barkod)
    url += "&tarih="
    url += str(tarih)
    print(url)
    conn = http.client.HTTPSConnection("api.akademetre.com")
    payload = ''
    headers = {
      'apiKey': 'CBD947DB-F458-4718-9CF5-E87E934F07D0'
    }
    conn.request("GET", url, payload, headers)
    res = conn.getresponse()
    data = res.read()
    new_line = data.decode("utf-8")
    print("res len:"+ str(len(new_line)))

    if (len(new_line) > 1):
        dict = json.loads(new_line)
        df2 = json_normalize(dict)
        df2.to_csv("out_2021.csv", mode='a', header=False)
        # f.write(df2 + '\n')
        # print(new_line)


# it will change for every year
start_time  = 1619827200
now = 1622419200

# by barcode numbers

barkod_arr = ["2120350000005", "2124650000000", "2120520000002", "2121640000002", "2121700000003", "2121950000006", "2121920000005", "2120670000006", "2122890000002",
            "2050000559389", "2125160000009", "2120290000004", "2158020000000", "2120300000000", "2127700000005", "2120310000007", "2125150000002", "2120320000004","2125550000008",
            "2120100000002", "2050002305359", "2120120000006", "10475072", "2127530000008", "3729", "2120970000003", "2120390000003", "2050002209725", "2121840000000", "2123750000002", "2121810000009", "2121150000004",
            "2125290000009", "2136630000009", "2124360000000", "2121290000001", "2153260000001", "2125690000005", "2120540000006", "2120530000009", "2110480000006", "2110640000006",
            "2119100000006", "2126040000003", "2124160000002", "2121510000002", "2122950000003", "2183470000003", "2123850000001", "2133570000007", "2167610000009", "2122390000007", "2050002099098",
            "2135600000001","2121530000006", "2121540000003", "2167900000009", "10630570", "2122100000006", "2121380000003", "2122500000002", "2124900000002", "2128820000005", "2135780000006", "2121430000007",
            "2050002294110", "2128540000002", "2112210000003", "2121410000003", "2159430000000", "2111100000000", "2121350000002", "2121360000009", "2126540000008", "8690982100960", "8680853030502", "2120610000004",
            "8690982100977", "2120510000005", "8697412600052", "2121900000001", "2125520000007", "2121870000001", "2125210000003", "2121880000008", "2121890000005", "2175800000005", "2123450000005", "2122380000000",
            "2123600000008", "8697453690036", "2129540000009", "2129900000007", "2050002172609", "10581384", "2128550000009", "2132860000000", "2128990000003", "2132820000002", "2121090000003", "2121050000005",
            "8694769002454", "8707441600517", "2127010000009", "2120920000008", "8697054100385", "2120840000003", "8697880430908", "8691797001237", "2188660000009", "2050001285300", "2121000000000", "8697432651133",
            "2134020000004", "2115500000004", "2121020000004"]

for epoc in range(start_time,now, 86400):
    idate = datetime.datetime.fromtimestamp(epoc).strftime('%Y-%m-%d')

    for barkod in barkod_arr:
        print(barkod, idate)
        get_data(barkod, idate)


##############################################################
# append data

import http.client
import datetime
import json
from pandas import json_normalize


def get_data(barkod, tarih):
    url = "/api/data/SearchByBarkod?barkod="
    url += str(barkod)
    url += "&tarih="
    url += str(tarih)
    print(url)
    conn = http.client.HTTPSConnection("api.akademetre.com")
    payload = ''
    headers = {
      'apiKey': 'CBD947DB-F458-4718-9CF5-E87E934F07D0'
    }
    conn.request("GET", url, payload, headers)
    res = conn.getresponse()
    data = res.read()
    new_line = data.decode("utf-8")
    print("res len:"+ str(len(new_line)))

    if (len(new_line) > 1):
        dict = json.loads(new_line)
        df2 = json_normalize(dict)
        df2.to_csv("last.csv", mode='a', header=False)
        # f.write(df2 + '\n')
        # print(new_line)

f = open('last.csv', 'w')

import time
from datetime import datetime
import datetime
from datetime import date

# get weekly data

now = datetime.datetime.now()
today_timestamp = datetime.datetime.timestamp(now)
int(today_timestamp)
start_time = today_timestamp - 86400*7
int(start_time)
barkod_arr = ["2120350000005", "2124650000000", "2120520000002", "2121640000002", "2121700000003", "2121950000006", "2121920000005", "2120670000006", "2122890000002",
            "2050000559389", "2125160000009", "2120290000004", "2158020000000", "2120300000000", "2127700000005", "2120310000007", "2125150000002", "2120320000004","2125550000008",
            "2120100000002", "2050002305359", "2120120000006", "10475072", "2127530000008", "3729", "2120970000003", "2120390000003", "2050002209725", "2121840000000", "2123750000002", "2121810000009", "2121150000004",
            "2125290000009", "2136630000009", "2124360000000", "2121290000001", "2153260000001", "2125690000005", "2120540000006", "2120530000009", "2110480000006", "2110640000006",
            "2119100000006", "2126040000003", "2124160000002", "2121510000002", "2122950000003", "2183470000003", "2123850000001", "2133570000007", "2167610000009", "2122390000007", "2050002099098",
            "2135600000001","2121530000006", "2121540000003", "2167900000009", "10630570", "2122100000006", "2121380000003", "2122500000002", "2124900000002", "2128820000005", "2135780000006", "2121430000007",
            "2050002294110", "2128540000002", "2112210000003", "2121410000003", "2159430000000", "2111100000000", "2121350000002", "2121360000009", "2126540000008", "8690982100960", "8680853030502", "2120610000004",
            "8690982100977", "2120510000005", "8697412600052", "2121900000001", "2125520000007", "2121870000001", "2125210000003", "2121880000008", "2121890000005", "2175800000005", "2123450000005", "2122380000000",
            "2123600000008", "8697453690036", "2129540000009", "2129900000007", "2050002172609", "10581384", "2128550000009", "2132860000000", "2128990000003", "2132820000002", "2121090000003", "2121050000005",
            "8694769002454", "8707441600517", "2127010000009", "2120920000008", "8697054100385", "2120840000003", "8697880430908", "8691797001237", "2188660000009", "2050001285300", "2121000000000", "8697432651133",
            "2134020000004", "2115500000004", "2121020000004"]

for epoc in range(int(start_time), int(today_timestamp), 86400):
    idate = datetime.datetime.fromtimestamp(epoc).strftime('%Y-%m-%d')

    for barkod in barkod_arr:
        print(barkod, idate)
        get_data(barkod, idate)

# append the data to all yearly data

import pandas as pd
import glob
import os

files = os.path.join("/Users/..", "out_*.csv")
files = glob.glob(files)
print("Resultant CSV after joining all CSV files at a particular location...")

# joining files with concat and read_csv
df = pd.concat(map(pd.read_csv, files), ignore_index=True)
print(df)

# there was some error in the end but I finished here
