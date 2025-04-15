from colorama import Fore, Style, Back
from datetime import datetime
import os
import yaml
with open('config.yml') as cfg:
  cfgs = yaml.safe_load(cfg)
  config = cfgs["data"]["config"]
# skid = gay
theme = config["ui-choices"]["theme"]

class Logger:
  @staticmethod
  def stamp():
    return datetime.now().strftime('%H:%M:%S') + ';' + datetime.now().strftime('%Y-%m-%d')
  
  @staticmethod
  def stamp2():
    return datetime.now().strftime('%H:%M:%S')
  
  @staticmethod
  def success(file,content:str) -> None:
    if theme == "normal":
      fullt = Logger.stamp()
      time = fullt.split(';')[1]
      day = fullt.split(';')[0]
      return print(f'{Style.BRIGHT}{Fore.BLACK}{time} ◦ {Fore.GREEN}DBG{Fore.BLACK} ◦ {day} ◦ {file}     >>    {content}{Fore.RESET}{Style.RESET_ALL}')
    
    elif theme == "checkout":
       return print(f'{Style.BRIGHT}{Fore.WHITE}[{Fore.MAGENTA}{Logger.stamp2()}{Fore.WHITE}] [{Fore.BLUE}>{Fore.WHITE}] {Fore.MAGENTA}- {Fore.WHITE}{content}')
    
    elif theme == "light":
       return print(f'{Style.BRIGHT}{Fore.WHITE}[{Logger.stamp2()}] [DBG] - {content}')
    
    elif theme == "dark":
       return print(f'{Style.BRIGHT}{Fore.BLACK}[{Fore.MAGENTA}{Logger.stamp2()}{Fore.BLACK}] [DBG] - {Fore.CYAN}{content}')
    
    else:
       return print(f"{Style.BRIGHT}{Fore.WHITE}[{Fore.MAGENTA}{Logger.stamp2()}{Fore.WHITE}] [DBG] - {Fore.BLUE}{content}")
  
  @staticmethod
  def remove_content(filename: str, delete_line: str) -> None:
        with open(filename, "r+") as io:
            content = io.readlines()
            io.seek(0)
            for line in content:
                if not (delete_line in line):
                    io.write(line)
            io.truncate()

  @staticmethod
  def mainsuc(content:str) -> None:
   if theme == "normal":
    fullt = Logger.stamp()
    time = fullt.split(';')[1]
    day = fullt.split(';')[0]
    return print(f'{Style.BRIGHT}{Fore.BLACK}{time} ◦ {Fore.GREEN}INF{Fore.BLACK} ◦ {day} ◦ redeempromo.py >>    {Fore.GREEN}{content}{Fore.RESET}{Style.RESET_ALL}')
   
   elif theme == "checkout":
       return print(f'{Style.BRIGHT}{Fore.WHITE}[{Fore.MAGENTA}{Logger.stamp2()}{Fore.WHITE}] [{Fore.GREEN}${Fore.WHITE}] {Fore.MAGENTA}- {Fore.WHITE}{content}')
   
   elif theme == "light":
       return print(f'{Style.BRIGHT}{Fore.WHITE}[{Logger.stamp2()}] [HIT] - {content}')
   
   elif theme == "dark":
       return print(f'{Style.BRIGHT}{Fore.BLACK}[{Fore.MAGENTA}{Logger.stamp2()}{Fore.BLACK}] [HIT] - {Fore.CYAN}{content}')
   
   else:
       return print(f"{Style.BRIGHT}{Fore.WHITE}[{Fore.MAGENTA}{Logger.stamp2()}{Fore.WHITE}] [HIT] - {Fore.BLUE}{content}")
   
  
  @staticmethod
  def error(file,content:str) -> None:
   if theme == "normal":
    fullt = Logger.stamp()
    time = fullt.split(';')[1]
    day = fullt.split(';')[0]
    return print(f'{Style.BRIGHT}{Fore.BLACK}{time} ◦ {Fore.RED}ERR {Fore.BLACK}◦ {day} ◦ {file}     >>    {Fore.RED}{content}{Fore.RESET}{Style.RESET_ALL}')
   elif theme == "checkout":
       return print(f'{Style.BRIGHT}{Fore.WHITE}[{Fore.MAGENTA}{Logger.stamp2()}{Fore.WHITE}] [{Fore.RED}-{Fore.WHITE}] {Fore.MAGENTA}- {Fore.RED}{content}')
   
   elif theme == "light":
       return print(f'{Style.BRIGHT}{Fore.WHITE}[{Logger.stamp2()}] [ERR] - {content}')
   
   elif theme == "dark":
       return print(f'{Style.BRIGHT}{Fore.BLACK}[{Fore.MAGENTA}{Logger.stamp2()}{Fore.BLACK}] [ERR] - {Fore.CYAN}{content}')
   
   else:
       return print(f"{Style.BRIGHT}{Fore.WHITE}[{Fore.MAGENTA}{Logger.stamp2()}{Fore.WHITE}] [ERR] - {Fore.BLUE}{content}")
   
   
def retrievecounter() -> list:
  return {
    'success': 0,
    'errors': 0,
    'proccesed': 0
  }
