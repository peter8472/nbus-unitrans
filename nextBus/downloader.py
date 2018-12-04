'''
usage: downloader.save(url)
'''

import urllib.request
import pickle
import sqlite3
import boto3
import os
import os.path
import tempfile

def get(url):
    dynam = boto3.resource('dynamodb')
    table= dynam.Table('cache')
    tjh= table.get_item(
        Key={
            'url':url
            
            })

    print(tjh['Item'])


def safeopen(fn):
    if not os.path.exists(fn):
        return open(fn, 'wb')
    else:
        raise FileExistsError



def save(url):
    outf = safeopen("data.txt")  # or throw
    u=urllib.request.urlopen(url)
    stuff = u.read()
    dynam = boto3.resource('dynamodb')
    table= dynam.Table('cache')
    table.put_item(
        Item={
            'url':url,
            'data':stuff
            })
    
    outf.write(stuff)
    outf.close()
        

    print(stuff)


