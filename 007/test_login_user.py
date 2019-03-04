import json
import pytest
import requests

def test_login_valid(supply_url):
  url = supply_url + "/login/"
  payload = {'email': 'test@test.com', 'password': 'something'}
  resp = requests.post(url, data=payload)
  json_resp = json.loads(resp.text)
  assert resp.status_code == 200, resp.text
  assert json_resp['token'] == "QpwL5tke4Pnpja7X", resp.text

def test_login_no_password(supply_url):
  url = supply_url + "/login/"
  payload = {'email': 'test@test.com'}
  resp = requests.post(url, data=payload)
  json_resp = json.loads(resp.text)
  assert resp.status_code == 400, resp.text
  assert json_resp['error'] == "Missing password", resp.text

def test_login_no_email(supply_url):
  url = supply_url + "/login/"
  payload = {}
  resp = requests.post(url, data=payload)
  json_resp = json.loads(resp.text)
  assert resp.status_code == 400, resp.text
  assert json_resp['error'] == "Missing email or username", resp.text
