'''
Python crawling helper
'''

import requests
from bs4 import BeautifulSoup
from selenium import webdriver

def request(url, sess=requests, method='get', **kwargs):
    '''
    Send API request

    url: url. proto://addr
    sess: if you want to maintain the state, set it to requests.Session obj.
    method: http method. Default 'get'.
    kwargs: parameter
    '''
    # request
    resp = None
    if method == 'get':
        if kwargs == {}:
            resp = sess.get(url)
        else:
            resp = sess.get(url, params=kwargs)
    elif method == 'post':
        resp = sess.post(url, data=kwargs)
    # error
    resp.raise_for_status()
    return resp

def html_to_bs(html):
    '''
    Convert HTML to BeautifulSoup obj
    
    html: HTML source
    '''
    return BeautifulSoup(html, 'html.parser')

def resp_to_bs(resp):
    '''
    Convert Requests's Response obj to BeautifulSoup obj
    
    resp: Requests library Response obj
    '''
    return html_to_bs(resp.text)

def view_resp(resp):
    '''
    Print response's status code, header.
    
    resp: Requests library Response obj
    '''
    print('Response to ' + resp.url + ':\n\tStatus code: ' + str(resp.status_code) + '\n\tHeader: ' + str(resp.headers))

