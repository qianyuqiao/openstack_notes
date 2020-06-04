import requests
import json
url = 'http://219.245.185.226:8088/bind_fip'
url2 = 'http://219.245.185.226:8088/unbind_fip'
url3 = 'http://219.245.185.226:8088/get_fips'

def bind():
    data1 = {"fip_id": "11caa377-4e4a-417f-aa0f-75325441febd", "pod_name": "qyqubuntuadmin"}
    resp = requests.post(url, data=json.dumps(data1))
    print resp.content

def unbind():

    data1 = {"fip_id": "11caa377-4e4a-417f-aa0f-75325441febd"}
    resp = requests.post(url2, data=json.dumps(data1))


def list_floatingips():
    resp = requests.post(url3)
    print resp.content

bind()
unbind()
list_floatingips()
