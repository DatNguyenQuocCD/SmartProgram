import re
from decimal import *
getcontext().prec = 3
def in_ra_mh():
    print('Khong hop le! Vui long nhap lai')
def lich():
    while True:
        try:
            thang=int(input('Nhap thang: '))
            if 1<=thang<=12:
                break
            in_ra_mh()
        except:
            in_ra_mh()
    while True:
        try:
            nam=int(input('Nhap nam: '))
            if nam>=1:
                break
            in_ra_mh()
        except:
            in_ra_mh()
    def in_ngay():
            print('thang:',thang,'nam:',nam,'co so ngay la:',ngay)
    def ngay():
        if thang%2==1:
            ngay=31
            print('thang:',thang,'nam:',nam,'co so ngay la:',ngay)
        elif thang%2==0 and thang!=2:
            ngay=30
            print('thang:',thang,'nam:',nam,'co so ngay la:',ngay)
    if nam%4!=0:
        if thang!=2:
            ngay()
        else:
            ngay=28
            in_ngay()
    else:
        if thang!=2:
            ngay()
        else:
            ngay=29
            in_ngay()
def tinh_luong():
    while True:
        try:
            gio=float(input('Nhap so gio lam: '))
            if gio>0:
                break
            in_ra_mh()
        except:
            in_ra_mh()
    while True:
        try:
            luong=float(input('Nhap he so luong: '))
            if luong>0:
                break
            in_ra_mh()
        except:
            in_ra_mh()
    don_vi=str(input('Nhap don vi tien: '))
    def in_ra_mh1():
        print('Tong luong nhan duoc khi lam: ',gio,' gio la: ',tong,'(',don_vi,')')
    if gio<=40:
        tong=gio*luong
        in_ra_mh1()
    else:
        gio_doi=gio-40
        tong=(gio_doi*luong*1.5)+(40*luong)
        in_ra_mh1()
def xem_luong():
    while True:
        try:
            so_nhan_vien = int(input('Nhap so luong nhan vien: '))
            ds_luong = []
            ds_ten = []
            luong1 = []
            max_ten = []
            max_luong = []
            if so_nhan_vien > 1:
                break
            in_ra_mh()
        except:
            in_ra_mh()
    for i in range(so_nhan_vien):
        ktr2 = True
        while ktr2: 
            ktr  = True
            ktr1 = True
            while ktr+ktr1:
                print('Nhap ten cua nhan vien thu ', i + 1, ': ')
                ten = str(input())
                ten_hoa = ten.title()
                if re.match("^[a-z' '_]*$", ten):
                    ktr1 = False
                ktr=any(i.isdigit() for i in ten)
            ktr2 = ten.isspace()
        ds_ten.append(ten_hoa)
        max_ten.append(len(ds_ten[i]))
        while True:
            try:
                print('Nhap luong cua nhan vien ', ten_hoa, ': ')
                luong = int(input())
                if luong > 0:
                    luong1.append(luong)
                    a = len(luong1)
                    break
                in_ra_mh()
            except:
                in_ra_mh()
    for x in range(0, a - 1):
        for j in range(x + 1, a):
            if luong1[x] > luong1[j]:
                b = luong1[x]
                luong1[x] = luong1[j]
                luong1[j] = b
                d = ds_ten[x]
                ds_ten[x] = ds_ten[j]
                ds_ten[j] = d
    for i in range(so_nhan_vien):
        pattern = "(\d)(?=(\d{3})+(?!\d))"
        repl = r"\1."
        string = str(luong1[i])
        ds_luong.append(re.sub(pattern, repl, string))
        max_luong.append(len(ds_luong[i]))
    maxluong = 0
    maxten = 0
    max_stt = len(str(so_nhan_vien))
    for z in max_luong:
        if z > maxluong:
            maxluong = z
    for y in max_ten:
        if y > maxten:
            maxten = y
    d = ('STT')
    c = ('Ten Nhan Vien')
    e = ('Tien Luong')
    if max_stt < (len(d)):
        max_stt = (len(d))
    if maxten < (len(c)):
        maxten = (len(c))
    if maxluong < (len(e)):
        maxluong = (len(e))
    print((max_stt + maxten + maxluong + 13) * '-')
    print('|', d, (max_stt - (len(d))) * ' ', '|', c, (maxten - (len(c))) * ' ', '|', e, (maxluong - (len(e))) * ' ',
          '|')
    print((max_stt + maxten + maxluong + 13) * '-')
    for i in range(so_nhan_vien):
        print('|', i + 1, (max_stt - len(str(i + 1))) * ' ', '|', ds_ten[i], (maxten - len(ds_ten[i])) * ' ', '|',
              ds_luong[i], (maxluong - len(ds_luong[i])) * ' ', '|')
        print((max_stt + maxten + maxluong + 13) * '-')
def xem_thong_tin_nhan_vien():
   ds_full_name =[]
   ds_last_name =[]
   ds_first_name=[]
   max_full_name=[]
   max_last_name=[]
   max_first_name=[]
   while True:
      try:
         n=int(input('nhap so nhan vien can xem thong tin: '))
         if n>0:
            break
         in_ra_mh()
      except:
         in_ra_mh()
   max_stt=len(str(n))
   for i in range(n):
      ktr=True
      while ktr:
         ktr1=True
         ktr2=True
         while ktr2+ktr1:
            print('Nhap ten nhan vien thu',i+1,': ')
            name=str(input())
            ktr2=any(i.isdigit() for i in name)
            if re.match("^[a-zA-Z' '_]*$", name):
               ktr1 = False
         ktr = name.isspace()
      ten_viet_hoa=name.title()
      ds_full_name.append(ten_viet_hoa)
   def bi():
      for i in range(n):
          tach_ten=ds_full_name[i].rsplit(' ',1)
          #print('Ho va ten lot cua nhan vien: ',tach_ten[0])
          ds_last_name.append(tach_ten[0])
          #print('Ten cua nhan vien: ',tach_ten[1])
          ds_first_name.append(tach_ten[1])
          #print('Ho ten day du cua nhan vien la: ',ten_viet_hoa)
          max_full_name.append(len(ds_full_name[i]))
          max_last_name.append(len(ds_last_name[i]))
          max_first_name.append(len(ds_first_name[i]))
      max1=0
      max2=0
      max3=0
      max_stt=len(str(n))
      for i in max_full_name:
         if i>max1:
            max1=i
      for i in max_last_name:
         if i>max2:
            max2=i
      for i in max_first_name:
         if i>max3:
            max3=i
      a=('STT')
      b=('Ten day du cua Nhan Vien')
      c=('Ho va Ten lot')
      d=('Ten')
      if max_stt<(len(a)):
         max_stt=(len(a))
      if max1<(len(b)):
         max1=(len(b))
      if max2<(len(c)):
         max2=(len(c))
      if max3<(len(d)):
         max3=(len(d))
      print((max_stt+max1+max2+max3+17)*'-')
      print('|',a,(max_stt-(len(a)))*' ','|',b,(max1-(len(b)))*' ','|',c,(max2-(len(c)))*' ','|',d,(max3-(len(d)))*' ','|')
      print((max_stt+max1+max2+max3+17)*'-')
      for i in range(n):
         print('|',i+1,(max_stt-(len(str(i+1))))*' ','|',ds_full_name[i],(max1-(len(ds_full_name[i])))*' ','|',ds_last_name[i],(max2-(len(ds_last_name[i])))*' ','|',ds_first_name[i],(max3-(len(ds_first_name[i])))*' ','|')
         print((max_stt+max1+max2+max3+17)*'-')   
   bi()
def tinh_diem_cua_hoc_sinh():
    while True:
        try:
            print('nhap so hoc sinh: ')
            n = int(input())
            if n > 0:
                break
            in_ra_mh()
        except:
            in_ra_mh()
    ds_ten_hs = []
    ds_xep_loai = []
    ds_dtb = []
    j = 0
    max_dtb = []
    max_xep_loai = []
    max_ten = []
    while j < n:
        ds_diem = []
        ds_he_so = []
        ds_ten_mon_hoc = []
        ktr  = True
        while ktr:
            ktr1 = True
            ktr2 = True
            while ktr2 + ktr1:
                print('nhap ten hoc sinh thu', j + 1, ': ')
                ten_hs = str(input())
                ktr2=any(i.isdigit() for i in ten_hs)
                if re.match("^[a-zA-Z' '_]*$", ten_hs):
                    ktr1 = False
            ktr = ten_hs.isspace()
        ten_hoa = ten_hs.title()
        ds_ten_hs.append(ten_hoa)
        max_ten.append(len(ds_ten_hs[j]))
        while True:
            try:
                print('nhap so mon hoc cua', ds_ten_hs[j], ': ')
                so_mon_hoc = int(input())
                if so_mon_hoc > 0:
                    so_mon_hoc
                    break
                in_ra_mh()
            except:
                in_ra_mh()
        for t in range(so_mon_hoc):
            ktr=True
            while ktr:
                ktr1=True
                ktr2=True
                while ktr2 + ktr1:
                    print('nhap ten mon hoc thu', t+1, ': ')
                    ten_mon_hoc = str(input())
                    ktr2=any(i.isdigit() for i in ten_mon_hoc)
                    if re.match("^[a-zA-Z' '_]*$", ten_mon_hoc):
                        ktr1 = False
                ktr = ten_mon_hoc.isspace()
            ten_mon_hoc_hoa=ten_mon_hoc.upper()
            ds_ten_mon_hoc.append(ten_mon_hoc_hoa)
            while True:
                try:
                    print('Nhap diem mon hoc', ds_ten_mon_hoc[t], ': ')
                    diem = float(input())
                    if 0 <= diem <= 10:
                        ds_diem.append(diem)
                        break
                    in_ra_mh()
                except:
                    in_ra_mh()
            while True:
                try:
                    print('Nhap he so mon hoc', ten_mon_hoc_hoa, ': ')
                    he_so = float(input())
                    if he_so == 1 or he_so == 1.5 or he_so == 2 or he_so == 2.5 or he_so == 3:
                        ds_he_so.append(he_so)
                        break
                    in_ra_mh()
                except:
                    in_ra_mh()
        for x in range(so_mon_hoc):
            print('Diem mon hoc', ds_ten_mon_hoc[x], ':', ds_diem[x])
            print('He so mon hoc', ds_ten_mon_hoc[x], ':', ds_he_so[x])

        tong_he_so = 0
        for i in range(so_mon_hoc):
            tong_he_so = tong_he_so + ds_he_so[i]
        tong_diem = 0
        for o in range(so_mon_hoc):
            tong_diem = tong_diem + ds_diem[o] * ds_he_so[o]
        diem_tb = Decimal(tong_diem) / Decimal(tong_he_so)
        ds_dtb.append(diem_tb)
        max_dtb.append(len(str(ds_dtb[j])))
        print('So mon hoc: ', so_mon_hoc)
        print('Tong he so: ', tong_he_so)
        print('Diem trung binh cua: ', ds_ten_hs[j], ': mon hoc la: ', diem_tb)
        j = j + 1
    h = len(ds_dtb)
    for a in ds_dtb:
        if a >= 8.5:
            b = ('gioi')
            ds_xep_loai.append(b)
        elif 6.5 <= a < 8.5:
            b = ('kha')
            ds_xep_loai.append(b)
        else:
            b = ('trung binh')
            ds_xep_loai.append(b)
    for z in range(0, h - 1):
        for j in range(z + 1, h):
            if ds_dtb[z] < ds_dtb[j]:
                d = ds_dtb[z]
                ds_dtb[z] = ds_dtb[j]
                ds_dtb[j] = d
                b = ds_ten_hs[z]
                ds_ten_hs[z] = ds_ten_hs[j]
                ds_ten_hs[j] = b
                c = ds_xep_loai[z]
                ds_xep_loai[z] = ds_xep_loai[j]
                ds_xep_loai[j] = c
    max_xep_hang = len(str(n))
    maxten = 0
    maxdiem = 0
    maxxl = 0
    for x in range(n):
        max_xep_loai.append(len(ds_xep_loai[x]))
    for x in max_ten:
        if x > maxten:
            maxten = x
    for x in max_dtb:
        if x > maxdiem:
            maxdiem = x
    for x in max_xep_loai:
        if x > maxxl:
            maxxl = x
    a = ('Xep Hang')
    b = ('Ten Nhan Hoc Sinh')
    c = ('Diem Trung Binh')
    d = ('Xep Loai')
    if max_xep_hang < (len(a)):
        max_xep_hang = (len(a))
    if maxten < (len(b)):
        maxten = (len(b))
    if maxdiem < (len(c)):
        maxdiem = (len(c))
    if maxxl < (len(d)):
        maxxl = (len(d))
    print((max_xep_hang + maxten + maxdiem + maxxl + 17) * '-')
    print('|', a, (max_xep_hang - (len(a))) * ' ', '|', b, (maxten - (len(b))) * ' ', '|', c,
          (maxdiem - (len(c))) * ' ', '|', d, (maxxl - (len(d))) * ' ', '|')
    print((max_xep_hang + maxten + maxdiem + maxxl + 17) * '-')
    for x in range(n):
        print('|', x + 1, (max_xep_hang - (len(str(x + 1)))) * ' ', '|', ds_ten_hs[x],
              (maxten - (len(ds_ten_hs[x]))) * ' ', '|', ds_dtb[x],
              (maxdiem - (len(str(ds_dtb[x])))) * ' ', '|', ds_xep_loai[x], (maxxl - (len(ds_xep_loai[x]))) * ' ', '|')
        print((max_xep_hang + maxten + maxdiem + maxxl + 17) * '-')
def thoat_truong_trinh():
    print('Ban da thoat ra khoi chuong trinh')
    exit()

def bang_chon():
    while True:
        try:
            p=int(input('Xin vui long chon: '))
            if 1<=p<=6:
                break
            in_ra_mh()
        except:
            in_ra_mh()
    if p==1:
        lich()
    elif p==2:
        tinh_luong()
    elif p==3:
        xem_luong()
    elif p==4:
        xem_thong_tin_nhan_vien()
    elif p==5:
        tinh_diem_cua_hoc_sinh()
    else:
        thoat_truong_trinh()
a='*'*41
b='*'*6
c=' '*75
d='='*95
print(c,a)
print(c,b,'Chuong Trinh Hoc Thong Minh',b)
print(c,a)
print(d,'MENU',d)
print('1.Xem lich')
print('2.Tinh luong')
print('3.Xem luong')
print('4.Xem thong tin nhan vien')
print('5.Tinh diem cua hoc sinh')
print('6.Thoat chuong trinh')
bang_chon()
def tiep():
    print("Ban co muon tiep tuc khong: neu co thi ghi muc 'chon' la 'YES', neu khong thi ghi bat ky ky tu nao tru 'yes'")
    chon=str(input('chon: '))
    chon1=chon.upper()
    if chon1=='YES':
        bang_chon()
        tiep()
    else:
        print('Ban da thoat ra khoi chuong trinh')
    exit()
tiep()




