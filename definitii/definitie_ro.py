import re
import urllib.request as urllib
from bs4 import BeautifulSoup

def definitie_ro(cuv):
    '''user_agent = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.63 Safari/534.3'
    headers = { 'User-Agent' : user_agent }'''
    try:
        url = f'https://dex.ro/{cuv}'
        #url  =urljoin('https://dex.ro','//dex.ro/{}'.format(cuv))
        req = urllib.Request(url, data=None, headers={'User-Agent': 'Mozilla/5.0'}, origin_req_host=None, unverifiable=True , method=None)
        response = urllib.urlopen(req)
        #response =requests.get(url, headers=headers)
        page = response.read()
        #page = response.content
        soup = BeautifulSoup(page.decode(), 'html.parser')
        results = soup.find_all('div',class_='res')
        res = results[0]
        ##print(res)
        
        response.close() 
    except: soup = ''
   
    pt0 = r'<strong>(\d*.)<\/strong>((\w*\s*\)?\(?î?ț?ă?ș?â?,?;?)+.) '
    pt1 = r'</i>\)? \d\)?.? ?((\w*\s*,?)*.) '
    pt2 = r'</span>((\w*\s*,*\(?\)?\*?)*.) '
    pt3 = r'<meta content=\"\w+,? ?-?\w+,? ?\w+?,? ? -?(\w*\s*,? ?-?.*)◊?\" '
    pt4 =r'</strong> ((\w*\s*,*;?)*.) '
    definitie=''
    definitie0=''
    definitie1=''
    definitie2=''
    definitie3=''
    definitie4=''
    #0
    try:
        dfn=[]   
        defn = re.findall(pt0,str(res))        
        for x in defn:
            for y in x:
                if len(y) >10:
                    dfn.append(y.strip()+' | ')
        for x in dfn:
            definitie0 += x
        definitie0 = definitie0.lstrip(') ')
        #print('defitie0: ',definitie0)
    except:pass
    #1
    try:
        dfn1=[]
        defn1 = re.findall(pt1,str(res))        
        for x1 in defn1:
                for y1 in x1:
                    if len(y1) >10:
                        dfn1.append(y1.strip()+' | ')
      
         
        for df1 in dfn1:
            definitie1 += df1
        #print('defitie1: ',definitie1)
    except:pass
    #2        
    try: 
        dfn2=[]
        defn2 = re.findall(pt2,str(res))
        for x2 in defn2:
                for y2 in x2:
                    if len(y2) >10:
                        dfn2.append(y2.strip()+' | ')
      
         
        for df2 in dfn2:
            definitie2 += df2
        definitie2 = definitie2.lstrip(') ')
        #print('defitie2: ',definitie2) 
        
    except:pass
    #3
    try: 
        dfn3=[]
        defn3 = re.findall(pt3,str(res))
        for x3 in defn3:
                for y3 in x3:
                    if len(y3) >10:
                        dfn3.append(y3.strip()+' | ')
      
         
        for df3 in dfn3:
            definitie3 += df3
        #print('defitie3: ',definitie3)
        
    except:pass
    #4
    try: 
        dfn4 = []
        defn4 = re.findall(pt4,str(res))
        for x4 in defn4:
                for y4 in x4:
                    if len(y4) >10:
                        dfn4.append(y4.strip()+' | ')
      
         
        for df4 in dfn4:
            definitie4 += df4
        #print('defitie4: ',definitie4)
    except:pass
    defn_list = [definitie0,definitie1,definitie2,definitie3,definitie4]
    definitie_list=[]
    for defn in defn_list:
        for d in defn.split(' | '):
            if d not in definitie_list:
                definitie_list.append(d)
                #print('***',d)
    for defn in definitie_list:
        if defn != '':
            definitie += defn + ' | '
        '''if len(str(defn)) >= len(str(definitie)):
            definitie = defn
    if definitie == ', , Definiţie , sinonime, declinari, conjugari pentru cuvântul ':
        definitie = '...'''
    return definitie
    
#print('**************')
#print('definitie casa: ',definitie_ro('casa'))
#print('****************')
#print('definitie cal: ',definitie_ro('cal'))
#print('****************')
#print('definitie albastru: ',definitie_ro('albastru'))
#print('****************')
#print('definitie dinoxaur: ',definitie_ro('dinozaur'))
#print('********************')
#print('definitie berbec: ',definitie_ro('berbec'))
#print('******************')
#print('definitie vagin: ',definitie_ro('vagin'))
#print('******************')
#print('definitie tghdf: ',definitie_ro('fgfhgf'))