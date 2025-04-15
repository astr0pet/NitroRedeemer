import os
import sys
import uuid
import json
import time
import yaml
import ctypes
import random
import colorama
import requests
import threading
import tls_client
import itertools
from modules.Logger import *
from colorama import init, Fore, Style
from concurrent.futures import ThreadPoolExecutor
theme = config["ui-choices"]["theme"]
counter = retrievecounter()
try:
  os.system('cls')
except:
  pass
ascii_text = Style.BRIGHT+f'''
{Fore.CYAN} __      __   _                    _        {Fore.GREEN}            _                       
{Fore.CYAN} \ \    / /__| |__ ___ _ __  ___  | |_ ___  {Fore.GREEN} _ _ ___ __| |___ ___ _ __  ___ _ _ 
{Fore.CYAN}  \ \/\/ / -_) / _/ _ \ '  \/ -_) |  _/ _ \ {Fore.GREEN}| '_/ -_) _` / -_) -_) '  \/ -_) '_|
{Fore.CYAN}   \_/\_/\___|_\__\___/_|_|_\___|  \__\___/ {Fore.GREEN}|_| \___\__,_\___\___|_|_|_\___|_|  
 
{Fore.MAGENTA}[CREDITS] Developed By {Fore.BLUE}@response., .gg/vintageboosts , .gg/ncert, for a paid and inbuilt 1m gen redeemer visit https://discord.gg/X58SEnfz
{Fore.MAGENTA}[NOTE]    {Fore.BLUE}Skid {Fore.MAGENTA}or change credits = no leaks!
{Fore.MAGENTA}[NOTE]    Some retards like **** have autism ignore the haters!
'''
print(ascii_text + Style.RESET_ALL)

with open('config.yml') as cfg:
  cfgs = yaml.safe_load(cfg)
  config = cfgs["data"]["config"]
success = 0
failed = 0
proccessed = 0
try:
  license_key = config["licensing"]["license-key"]
  vcc_usage = config["important"]["vcc-uses"]
  promo_type = config["important"]["promotype"]
  auth_retry = config["important"]["auth-retry"]
  sleep_after_redeem = int(config["important"]["sleep-after-redeem"])
  remove_vccs = config["important"]["remove-vccs"]
  use_wh = config["webhook-support"]["use-webhook"]
  url = config["webhook-support"]["url"]
  billings = config["custom-billing"]
  country = billings["country"]
  state = billings["state"]
  address = billings["address"]
  zipcode = billings["postal-code"]
  card_name = billings["card-name"]
  city = billings["city"]
  proxyusage = config["proxy-support"]
  use_proxy = proxyusage["use-proxies"]
  proxy = proxyusage["proxy"]
  custombranding = config["custom-branding"]
  use_custom_branding = custombranding["use-custom-branding"]
  display_name = custombranding["display-name"]
  console_title = config["title"]
  update_console_title = console_title["update-console-title"]
except:
  Logger.error("readconfig.py", "failed to read config, recheck it.")
  time.sleep(1000)
  sys.exit(0)
def obt_cookies() -> list:
        session = tls_client.Session(
           client_identifier="chrome_109",
           random_tls_extension_order=True
        )
        cookies = {}
        try:
          response = session.get('https://discord.com')
          for cookie in response.cookies:
            if cookie.name.startswith('__') and cookie.name.endswith('uid'):
                cookies[cookie.name] = cookie.value
          return cookies
        except Exception as e:
          Logger.error('cookie.py', 'failed to obtain cookies, excp: {}'.format(e))
          return {}
def update_console_title():
  if console_title == True:
    try:
      ctypes.windll.kernel32.SetConsoleTitleW(f'title @response | Claimed[{success}] | Proccessed[{proccessed}] | Failed[{failed}]')
    except:
      return
  else:
    return
def edit_embed_webhook(new_embed):
  if use_wh == True:
    data = {
        "embeds": [new_embed]
    }
    response = requests.post(url, json=data)
    if response.status_code == 200:
        return response.json()["id"]
    else:
        return None

edit_embed_webhook({
        "title": "# DISCORD NITRO REDEEMER",
        "description": f">> TOOL STARTED AT: `{Logger.stamp2()}`\nWILL SEND DETAILED INFO AFTER COMPLETION.",
        "color": 16711680,
    })
class Redeemer:
  
  def __init__(self, vcc, promo, token):
    global proccessed
    try:
      update_console_title()
    except:
       return
    proccessed += 1
    self.full_token = token

    if '@' and ':' in token:
      self.token = token.split(':')[2]

    elif not '@' and not ':' in token:
      self.token = token

    else:
      Logger.error("formatassets.py", "invalid token format.")
      return
    
    self.full_vcc = vcc

    if ':' in vcc:
          self.ccn = vcc.split(':')[0]
          self.expMa = vcc.split(':')[1]
          self.expM = self.expMa[:2]
          self.expY = self.expMa[2:]
          self.cvv = vcc.split(':')[2]

    else:
      Logger.error("formatassets.py", "invalid vcc format.")
      return
    
    self.session = tls_client.Session(
            client_identifier="chrome_109",
            random_tls_extension_order=True
    )

    self.session2 = tls_client.Session(
            client_identifier="chrome_109",
            random_tls_extension_order=True
    )

    if use_proxy == True:
       self.session.proxies = {
          'http': f'http://{proxy}',
          'https': f'https://{proxy}'
       }

       self.session2.proxies = {
          'http': f'http://{proxy}',
          'https': f'https://{proxy}'
       }

    else:
       
       self.session.proxies = None
       self.session2.proxies = None
    self.fullpromo = promo

    if '1180231712274387115' in self.fullpromo:
      self.promoorigin = "opera"

    elif '1m' in promo_type and not '1180231712274387115' in self.fullpromo:
      self.promoorigin = "alienware"

    elif promo_type == "3m":
      self.promoorigin = "xbox_gamepass"

    else:
      self.promoorigin = None
      Logger.error('initialize.py', f'invalid promo type : {promo_type}')
    self.retried = 0

  def cancle_subscription(self,subsid):    
        headers = {
    'authority': 'discord.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'authorization': self.token,
    'content-type': 'application/json',
    'origin': 'https://discord.com',
    'referer': 'https://discord.com/channels/@me',
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Microsoft Edge";v="122"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0',
    'x-debug-options': 'bugReporterEnabled',
    'x-discord-locale': 'en-US',
    'x-discord-timezone': 'Europe/Budapest',
    'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyMi4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMjIuMC4wLjAiLCJicm93c2VyX3ZlcnNpb24iOiIxMjIuMC4wLjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MjcxMjE2LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==',
}
        payload = {
            "payment_source_token": None,
            "gateway_checkout_context": None,
            "items": []
        }
        params = {
    'location_stack': [
        'user settings',
        'subscription header',
        'premium subscription cancellation modal',
    ],
}
        
        response = self.session.patch(
    f'https://discord.com/api/v9/users/@me/billing/subscriptions/{subsid}',
    params=params,
    headers=headers,
    json=payload,
    cookies=obt_cookies()
)
        if response.status_code in (200, 201, 202, 203, 204):
            return True
        Logger.error('removecard.py', f'failed to cancle subscription, status-code: {response.status_code}')
        return False
  
  def getsubid(self) -> str|None: 
      self.__headers = {
    'authority': 'discord.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'authorization': self.token,
    'referer': 'https://discord.com/channels/@me',
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Microsoft Edge";v="122"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0',
    'x-debug-options': 'bugReporterEnabled',
    'x-discord-locale': 'en-US',
    'x-discord-timezone': 'Europe/Budapest',
    'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyMi4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMjIuMC4wLjAiLCJicm93c2VyX3ZlcnNpb24iOiIxMjIuMC4wLjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MjcxMjE2LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==',
}
      response = self.session2.get('https://discord.com/api/v9/users/@me/billing/subscriptions',
                                    headers=self.__headers,
                                    cookies=obt_cookies())
      json_data = response.json()
      
      try:
        return json_data[0]["id"]
      
      except:
        Logger.error('removecard.py', f'failed to get subscription id, status-code: {response.status_code}')
        return None
      
  def formatpromo(self) -> str|None:

    if '1180231712274387115' in self.fullpromo:
      self.headers = {
           'authority': 'discord.com',
           'accept': '*/*',
           'accept-language': 'en-US,en;q=0.9',
           'authorization': self.token,
           'content-type': 'application/json',
           'origin': 'https://discord.com',
           'referer': self.fullpromo,
           'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Microsoft Edge";v="122"',
           'sec-ch-ua-mobile': '?0',
           'sec-ch-ua-platform': '"Windows"',
           'sec-fetch-dest': 'empty',
           'sec-fetch-mode': 'cors',
           'sec-fetch-site': 'same-origin',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0',
           'x-debug-options': 'bugReporterEnabled',
           'x-discord-locale': 'en-US',
           'x-discord-timezone': 'Europe/Budapest',
           'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyMi4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMjIuMC4wLjAiLCJicm93c2VyX3ZlcnNpb24iOiIxMjIuMC4wLjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6Imh0dHBzOi8vZGlzY29yZC5jb20vP2Rpc2NvcmR0b2tlbj1NVEEzTURReU56RXhNVGM1TVRJNE5ESTROQS5HYWNhYnIuVE9NZUVzbHdiczJ2OFRlck4wOTM3SzVvS0ZFMFZyZW5fdWF6Q1kiLCJyZWZlcnJpbmdfZG9tYWluIjoiZGlzY29yZC5jb20iLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MjY4NjAwLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==',
           }
      self.json = {
           'jwt': self.fullpromo.split('https://discord.com/billing/partner-promotions/1180231712274387115/')[1]
      }

      try:
        response = self.session.post('https://discord.com/api/v9/entitlements/partner-promotions/1180231712274387115',
                          headers=self.headers,
                          json=self.json,
                          cookies=obt_cookies())
        
      except Exception as e:
        Logger.error("formatpromo.py", f"failed to fetch promo code : {e}")
        return None
      
      if response.status_code in (200, 204):
        code = response.json()["code"]
        return code
      
      else:
        Logger.error("formatpromo.py", f"failed to retrieve promo code : {e}")
        return None
      
    elif '1m' in promo_type and not '1180231712274387115' in self.fullpromo:

      if 'https://discord.com/billing/promotions/' in self.fullpromo:
        code = self.fullpromo.split('https://discord.com/billing/promotions/')[1]

      else:
        code = self.fullpromo.split('https://promos.discord.gg/')[1]

      return code
    
    elif promo_type == '3m':
      if 'https://discord.com/billing/promotions/' in self.fullpromo:
        code = self.fullpromo.split('https://discord.com/billing/promotions/')[1]

      else:
        code = self.fullpromo.split('https://promos.discord.gg/')[1]

      return code
    
  def removeCard(self, idz: str):
       __headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'authorization': self.token,
    # 'cookie': '__dcfduid=b0acdb80f0fb11ee9a525321991f465a; __sdcfduid=b0acdb81f0fb11ee9a525321991f465a607b4dd48b37d3be4b32bfeca8dc0fe7d91a1c41229dfe6f4c295ec62a8d01bb; __cfruid=253617cc01d14de1da0af0ccedd6b96ee7a5afce-1712067428; _cfuvid=uKpTNJI9eSqV3i6MEDJ1HKgEFeCYSJKzWDletQVMehc-1712067428667-0.0.1.1-604800000; cf_clearance=684xejLT.5uX.KQQv2FX_1YP.6BQrKr_9Ho_7KeiPBw-1712067430-1.0.1.1-AFRjTAbwGb6kDUjykVA5a.KnuPOX2iXRmHc1gMrXmTB7I0nHg684wbe.ed4LSlJLdkKDNMySUxykWDxs01r.vg',
    'origin': 'https://discord.com',
    'referer': 'https://discord.com/channels/@me',
    'sec-ch-ua': '"Microsoft Edge";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0',
    'x-debug-options': 'bugReporterEnabled',
    'x-discord-locale': 'en-US',
    'x-discord-timezone': 'Europe/Budapest',
    'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyMy4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMjMuMC4wLjAiLCJicm93c2VyX3ZlcnNpb24iOiIxMjMuMC4wLjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MjgwNzA0LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==',
}
       responsez = self.session2.delete(
    f'https://discord.com/api/v9/users/@me/billing/payment-sources/{idz}',
    headers=__headers,
    cookies=obt_cookies()
)
       if responsez.status_code == 204:
          Logger.success('removecard.py', f'Successfully Removed Vcc -> {Fore.BLUE}{self.full_vcc[:13]}***:****:***{Fore.RESET}, Token -> {Fore.BLUE}{self.token[:13]}')
          return True
       
       else: 
          Logger.error('removecard.py', f'failed to remove card {self.full_vcc[:13]}***:****:*** from {self.token[:19]}***.**-**.***')
          return False
       
  def redeempromo(self, pmid: str) -> bool:
    global success, failed

    code = self.formatpromo()

    if not code == None:

      headers = {
        'authority': 'discord.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': self.token,
        'content-type': 'application/json',
        'origin': 'https://discord.com',
        'referer': f'https://discord.com/billing/promotions/{code}',
        'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Microsoft Edge";v="122"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0',
        'x-debug-options': 'bugReporterEnabled',
        'x-discord-locale': 'en-US',
        'x-discord-timezone': 'Europe/Budapest',
        'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyMi4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMjIuMC4wLjAiLCJicm93c2VyX3ZlcnNpb24iOiIxMjIuMC4wLjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MjY4NjAwLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==',
        }
      json = {
         'channel_id': None,
         'payment_source_id': pmid,
         'gateway_checkout_context': None,
      }

      try:
        response = self.session2.post(f'https://discord.com/api/v9/entitlements/gift-codes/{code}/redeem',
                                    headers=headers,
                                    json=json,
                                    cookies=obt_cookies())
        
      except Exception as e:
        Logger.error('redeempromo.py', f'failed to post request : {e}')
        counter["errors"] += 1
        with open('output/main/unhandled.txt', 'a') as f:
          f.write(self.full_token+'\n')
        return False
      
      try:

        claimid = response.json()["id"]
        if theme != "checkout":
          Logger.mainsuc(f'redeemed promo successfully, promo: {code[:24]}***, vcc: {self.full_vcc[:13]}***:****:***, token={self.token[:18]}***.**-**.***')
        else:
           Logger.mainsuc(f'Redeemed Promo, Promo: {Fore.GREEN}{code[:24]}***{Fore.RESET}, VCC: {Fore.GREEN}{self.full_vcc[:13]}***:****:***{Fore.RESET}, Token: {Fore.GREEN}{self.token[:18]}***.**-**.***')
        success+=1
        with open('output/main/success.txt', 'a') as f:
           f.write(self.full_token+'\n')
        try:

          if remove_vccs == True:
            subsid = self.getsubid()

            if not subsid == None:
              self.cancle_subscription(subsid)
              if not subsid == None:
                PaymentMthdId = pmid
                self.removeCard(PaymentMthdId)
              else:
                 pass

            else:
              pass

          else:
            pass
        except Exception as e:
           Logger.error('vccwrk.py', f'{Fore.WHITE}Failed to Remove VCC: {Fore.YELLOW}{self.ccn[:13]}***:****:***, Exc: {Fore.YELLOW}{e}')
           pass

        return True
      
      except:

        if 'Authentication' in response.text:
          if theme != "checkout":
            Logger.error('redeempromo.py', f'failed to redeem promo, response: auth error detected.')
          else:
             Logger.error('redeempromo.py', f'Failed to Redeem Promo, Reason: {Fore.YELLOW}Auth Error')
          failed+=1
          with open('output/main/auth_errors.txt', 'a') as f:
            f.write(self.full_token+'\n')
          time.sleep(4)
          spid = pmid

          if auth_retry > 0 and self.retried < auth_retry:
            self.redeempromo(spid)
            self.retried += 1

          else:
             pass

        else:
          if theme != "checkout":
            Logger.error('redeempromo.py', f'failed to redeem promo, response: {response.json()}')
          else:
             Logger.error('redeempromo.py', f'Failed to Redeem Promo, Response: {Fore.RED}{response.json()}')
          failed+=1
          with open('output/main/failed.txt', 'a') as f:
            f.write(self.full_token+'\n')
          with open('output/main/vcc_errors.txt', 'a') as f:
            f.write(self.full_vcc+'\n')
          return False
  
  def addcard(self):

    global failed

    if theme != "checkout":
     Logger.success('addcard.py', f'using card: {self.full_vcc[:13]}***:****:***, token: {self.token[:18]}***.**-**.***, promo: {self.fullpromo[:35]}***, promo-origin: {self.promoorigin}')
     
    else:
       Logger.success('addcard.py', f'Using VCC: {Fore.BLUE}{self.full_vcc[:13]}***:****:***{Fore.RESET}, token: {Fore.BLUE}{self.token[:18]}***.**-**.***{Fore.WHITE}, promo: {Fore.BLUE}{self.fullpromo[:35]}***{Fore.RESET}, promo-origin: {Fore.BLUE}{self.promoorigin}')

    header = {
       'authority': 'api.stripe.com',
       'accept': 'application/json',
       'accept-language': 'en-US,en;q=0.9',
       'content-type': 'application/x-www-form-urlencoded',
       'origin': 'https://js.stripe.com',
       'referer': 'https://js.stripe.com/',
       'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Microsoft Edge";v="122"',
       'sec-ch-ua-mobile': '?0',
       'sec-ch-ua-platform': '"Windows"',
       'sec-fetch-dest': 'empty',
       'sec-fetch-mode': 'cors',
       'sec-fetch-site': 'same-site',
       'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0',
      }
    data = f'card[number]={self.ccn}&card[cvc]={self.cvv}&card[exp_month]={self.expM}&card[exp_year]={self.expY}&guid={uuid.uuid4()}&muid={uuid.uuid4()}&sid={uuid.uuid4()}&payment_user_agent=stripe.js%2F28b7ba8f85%3B+stripe-js-v3%2F28b7ba8f85%3B+split-card-element&referrer=https%3A%2F%2Fdiscord.com&time_on_page=415638&key=pk_live_CUQtlpQUF0vufWpnpUmQvcdi&pasted_fields=number%2Ccvc'

    try:
      response = self.session.post('https://api.stripe.com/v1/tokens', headers=header, data=data)

    except Exception as e:
      Logger.error('addcard.py', f'failed to post request : {e}')
      failed+=1
      return
    
    try:
      cardTok = response.json()["id"]

    except:
      Logger.error('addcard.py', f'failed to add card, response: {response.json()}')
      failed+=1
      with open('output/main/vcc_errors.txt', 'a') as f:
        f.write(self.full_token+'\n')
      with open('output/main/failed.txt', 'a') as f:
        f.write(self.full_token+'\n')
      with open('output/main/failed_promos.txt', 'a') as f:
         f.write(self.fullpromo+'\n')
      return
    
    headers = {
        'authority': 'discord.com',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'authorization': self.token,
        'origin': 'https://discord.com',
        'referer': 'https://discord.com/channels/@me',
        'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Microsoft Edge";v="122"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0',
        'x-debug-options': 'bugReporterEnabled',
        'x-discord-locale': 'en-US',
        'x-discord-timezone': 'Europe/Budapest',
        'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyMi4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMjIuMC4wLjAiLCJicm93c2VyX3ZlcnNpb24iOiIxMjIuMC4wLjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MjY4NjAwLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==',
        }
    
    try:
      response = self.session.post('https://discord.com/api/v9/users/@me/billing/stripe/setup-intents',
                                   headers = headers)
      
    except:
      Logger.error('addcard.py', f'failed to add card, response: {response.json()}')
      failed+=1
      with open('output/main/vcc_errors.txt', 'a') as f:
        f.write(self.full_token+'\n')
      return
    
    try:
          csTok = response.json()["client_secret"]
          Stok = str(csTok).split('_secret_')[0]

    except: 
      with open('output/main/vcc_errors.txt', 'a') as f:
        f.write(self.full_token+'\n')
      failed+=1
      with open('output/main/failed.txt', 'a') as f:
        f.write(self.full_token+'\n')
      if response.status_code == 401:
        Logger.error('addcard.py', f'{Fore.WHITE}Invalid Token: {Fore.YELLOW}{self.token}')
        with open('output/main/invalid_token.txt', 'a') as f:
               f.write(self.full_token+'\n')
      else:
         Logger.error('addcard.py', f'failed to get client secret, response: {response.json()}') 
      return
    
    headers = {
       'authority': 'discord.com',
       'accept': '*/*',
       'accept-language': 'en-US,en;q=0.9',
       'authorization': self.token,
       'content-type': 'application/json',
       'origin': 'https://discord.com',
       'referer': 'https://discord.com/channels/@me',
       'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Microsoft Edge";v="122"',
       'sec-ch-ua-mobile': '?0',
       'sec-ch-ua-platform': '"Windows"',
       'sec-fetch-dest': 'empty',
       'sec-fetch-mode': 'cors',
       'sec-fetch-site': 'same-origin',
       'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0',
       'x-debug-options': 'bugReporterEnabled',
       'x-discord-locale': 'en-US',
       'x-discord-timezone': 'Europe/Budapest',
       'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyMi4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMjIuMC4wLjAiLCJicm93c2VyX3ZlcnNpb24iOiIxMjIuMC4wLjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MjY4NjAwLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==',
       }
    
    json = {
      'billing_address': {
        'name': card_name,
        'line_1': address,
        'line_2': '',
        'city': city,
        'state': state,
        'postal_code': zipcode,
        'country': country,
        'email': '',
    },
  }
    
    try:
      response = self.session.post('https://discord.com/api/v9/users/@me/billing/payment-sources/validate-billing-address',
                                   headers=headers,
                                   json=json)
      
    except:
      Logger.error('addcard.py', f'failed to retrieve billing token response!')
      with open('output/main/vcc_errors.txt', 'a') as f:
        f.write(self.full_token+'\n')
      with open('output/main/failed.txt', 'a') as f:
        f.write(self.full_token+'\n')
      failed+=1
      return
    
    try:
      BTok = response.json()["token"]

    except:
      Logger.error('addcard.py', f'failed to retrieve billing token response : {response.json()}')

    headersz = {
       'authority': 'api.stripe.com',
       'accept': 'application/json',
       'accept-language': 'en-US,en;q=0.9',
       'content-type': 'application/x-www-form-urlencoded',
       'origin': 'https://js.stripe.com',
       'referer': 'https://js.stripe.com/',
       'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Microsoft Edge";v="122"',
       'sec-ch-ua-mobile': '?0',
       'sec-ch-ua-platform': '"Windows"',
       'sec-fetch-dest': 'empty',
       'sec-fetch-mode': 'cors',
       'sec-fetch-site': 'same-site',
       'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0',
    }
    dataz = f'payment_method_data[type]=card&payment_method_data[card][token]={cardTok}&payment_method_data[billing_details][address][line1]={address}&payment_method_data[billing_details][address][line2]=&payment_method_data[billing_details][address][city]={city}&payment_method_data[billing_details][address][state]={state}&payment_method_data[billing_details][address][postal_code]={zipcode}&payment_method_data[billing_details][address][country]={country}&payment_method_data[billing_details][name]={card_name}&payment_method_data[guid]={uuid.uuid4()}&payment_method_data[muid]={uuid.uuid4()}&payment_method_data[sid]={uuid.uuid4()}&payment_method_data[payment_user_agent]=stripe.js%2F28b7ba8f85%3B+stripe-js-v3%2F28b7ba8f85&payment_method_data[referrer]=https%3A%2F%2Fdiscord.com&payment_method_data[time_on_page]=707159&expected_payment_method_type=card&use_stripe_sdk=true&key=pk_live_CUQtlpQUF0vufWpnpUmQvcdi&client_secret={csTok}' 

    try:
      response = self.session.post(f'https://api.stripe.com/v1/setup_intents/{Stok}/confirm',
                                   headers=headersz,
                                   data=dataz
                                   )
      
    except:
      Logger.error('addcard.py', f'failed to setup intents')
      with open('output/main/vcc_errors.txt', 'a') as f:
        f.write(self.full_token+'\n')
      with open('output/main/failed.txt', 'a') as f:
        f.write(self.full_token+'\n')
      failed+=1
      return
    
    try:
          CardSCMAIN = response.json()["id"]
          pmTok = response.json()["payment_method"]

    except:
      if response.status_code == 401:
         if theme != "checkout":
          Logger.error('addcard.py', f'invalid token: {self.token}***.***')
         else:
            Logger.error('addcard.py', f'Invalid Token: {Fore.YELLOW}{self.token}')
            with open('output/main/invalid_token.txt', 'a') as f:
               f.write(self.full_token+'\n')
      else:
        Logger.error('addcard.py', f'{Fore.WHITE}Failed to scrape payment token: {Fore.YELLOW}{response.json()["error"]["message"]}')
      with open('output/main/vcc_errors.txt', 'a') as f:
        f.write(self.full_token+'\n')
      with open('output/main/failed.txt', 'a') as f:
        f.write(self.full_token+'\n')
      with open('output/main/failed_promos.txt', 'a') as f:
         f.write(self.fullpromo+'\n')
      return
    
    headers = {
       'authority': 'discord.com',
       'accept': '*/*',
       'accept-language': 'en-US,en;q=0.9',
       'authorization': self.token,
       'content-type': 'application/json',
       'origin': 'https://discord.com',
       'referer': 'https://discord.com/channels/@me',
       'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Microsoft Edge";v="122"',
       'sec-ch-ua-mobile': '?0',
       'sec-ch-ua-platform': '"Windows"',
       'sec-fetch-dest': 'empty',
       'sec-fetch-mode': 'cors',
       'sec-fetch-site': 'same-origin',
       'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0',
       'x-debug-options': 'bugReporterEnabled',
       'x-discord-locale': 'en-US',
       'x-discord-timezone': 'Europe/Budapest',
       'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyMi4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMjIuMC4wLjAiLCJicm93c2VyX3ZlcnNpb24iOiIxMjIuMC4wLjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MjY4NjAwLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==',
      }
    
    json = {
       'payment_gateway': 1,
       'token': pmTok,
       'billing_address': {
        'name': card_name,
        'line_1': address,
        'line_2': None,
        'city': city,
        'state': state,
        'postal_code': zipcode,
        'country': country,
        'email': '',
        },
       'billing_address_token': BTok
      }
    try:
      response = self.session.post('https://discord.com/api/v9/users/@me/billing/payment-sources',
                                   headers=headers,
                                   json=json,
                                   cookies=obt_cookies())
      
    except Exception as e:
       Logger.error('addcard.py', f'failed to post req to add card, excp: {e}')
    
    try:
          purchaseId = response.json()["id"]
          if theme != "checkout":
            Logger.success('addcard.py', f'added card : {self.full_vcc[:13]}***:****:***')
          else:
             Logger.success('addcard.py', f'Added VCC: {Fore.GREEN}{self.full_vcc[:13]}***:****:***')
          self.redeempromo(purchaseId)
          return purchaseId
    
    except Exception as e:

      if 'captcha_key' in str(response.json()):
        Logger.error('addcard.py', f'{Fore.WHITE}Failed to add card: {Fore.YELLOW}captcha-required!')
        with open('output/main/captcha_tokens.txt', 'a') as f:
          f.write(self.full_token+'\n')
        failed+=1

      else:
        Logger.error('addcard.py', f'failed to add card, response: {response.json()}')
        with open('output/main/unhandled.txt', 'a') as f:
          f.write(self.full_token+'\n')
        with open('output/main/failed.txt', 'a') as f:
          f.write(self.full_token+'\n')
        failed+=1

def nameChanger(token: str, dName: str):
    __sessionx = tls_client.Session(
       client_identifier="chrome_112",
       random_tls_extension_order=True
    )
    if '@' in token:
      token = token.split(':')[2]
    else:
      token=token
    headers = {
      'authority': 'discord.com',
      'accept': '*/*',
      'accept-language': 'en-US,en;q=0.9',
      'authorization': token,
      'content-type': 'application/json',
      'origin': 'https://discord.com',
      'referer': 'https://discord.com/channels/@me',
      'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Microsoft Edge";v="122"',
      'sec-ch-ua-mobile': '?0',
      'sec-ch-ua-platform': '"Windows"',
      'sec-fetch-dest': 'empty',
      'sec-fetch-mode': 'cors',
      'sec-fetch-site': 'same-origin',
      'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0',
      'x-debug-options': 'bugReporterEnabled',
      'x-discord-locale': 'en-US',
      'x-discord-timezone': 'Europe/Budapest',
      'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyMi4wLjAuMCBTYWZhcmkvNTM3LjM2IEVkZy8xMjIuMC4wLjAiLCJicm93c2VyX3ZlcnNpb24iOiIxMjIuMC4wLjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MjcxMjE2LCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==',
    }
    json_data = {
    'global_name': str(dName),
}
    
    try:
      response = __sessionx.patch('https://discord.com/api/v9/users/@me', headers=headers, json=json_data,
                                  cookies=obt_cookies())
      
    except Exception as e:
       return
    
    if response.status_code == 200:
        Logger.success("customization.py", f"Customized Token, type: {Fore.BLUE}display-name{Fore.RESET}, name: {Fore.BLUE}{dName}")

    else:
        Logger.error("customization.py", f"Failed To Customize {token[:17]}***.**-**.***, response: " + f'{Fore.YELLOW}Captcha-Required!' if 'captcha_key' in response.text else str(response.json()))
    
def process_token(vcc, promo, token):
  instance = Redeemer(vcc, promo, token)
  instance.addcard()
  nameChanger(token, display_name)
  Logger.remove_content("input/tokens.txt", token)
  Logger.remove_content("input/promos.txt", promo)

from itertools import cycle
token_finished = False
vcc_finished = False
if __name__ == "__main__":
    init()
    threads = int(input(Style.BRIGHT +
                        Fore.LIGHTWHITE_EX + '[' + Fore.LIGHTBLACK_EX + Logger.stamp2() + Fore.LIGHTWHITE_EX + ']' +
                        Fore.LIGHTWHITE_EX + ' [' + Fore.BLUE + '?' + Fore.LIGHTWHITE_EX + ']' +
                        Fore.LIGHTMAGENTA_EX + ' -> ' + Fore.LIGHTCYAN_EX +
                        'Enter Threads To Run -> ' + Fore.RESET + Style.RESET_ALL))
    os.system('cls')

    with open('input/tokens.txt') as f:
        tokens = f.read().splitlines()
    with open('input/promos.txt') as f:
        promos = f.read().splitlines()
    with open('input/vccs.txt') as f:
        vccs = f.read().splitlines()

    num_vcc_repeats = vcc_usage
    num_tokens = len(tokens)
    num_promos = len(promos)

    with ThreadPoolExecutor(max_workers=threads) as exc:
        vcc_batch = cycle(vccs)
        token_batch = cycle(tokens)
        promo_batch = cycle(promos)
        while True:
            vcc = vcc_batch.__next__()
            for _ in range(num_vcc_repeats):
                token = token_batch.__next__()
                promo = promo_batch.__next__()
                exc.submit(process_token, vcc, promo, token)
                if token == tokens[-1]:
                    token_finished = True
                if vcc == vccs[-1]:
                    vcc_finished = True
                if token_finished or (token_finished and vcc_finished):
                    break
            if token_finished or (token_finished and vcc_finished):
                break

edit_embed_webhook({
        "title": "# THREADS COMPLETED",
        "description": f">> THREADS COMPLETED AT: `{Logger.stamp2()}`\n* CLAIMS: `{success}`\n* PROCCESSED: `{proccessed}`\n* FAILED: `{failed}`",
        "color": 16711680,
    })

input('Materials completed, press enter to exit...')
