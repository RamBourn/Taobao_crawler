import requests as rq 
import json
import re
import numpy as np
url_model='https://s.taobao.com/search?q=type__&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306'
headers={
    'user-agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0',
    'Cookie':'thw=cn; isg=BNLSi5Nt23i4ISeYICyQpubfIJG-718xg6syRJwr9QVwr3KphXfsj_jNH8M2xE4V; t=bc09aeb5c7987372590b3844c1db89b1; cna=cA0hFYkqZxgCAd3oFKW9s+al; l=bBEIiYYrqjhJoJCSBOCwZZOfdibTjIOYYuWfcS4Hi_5wV6Y168_OkY6WSFv6V15Rsd8p4U7ZIUJ9-etei; _cc_=URm48syIZQ%3D%3D; tg=0; mt=ci=6_1; enc=ZlZXBgo2w19A7N9SLwq8yZTQUK%2FaZtwbJ9i8ctPhcjznc0exhTiULzvRT8AbIu2sR1QDkF1lzLEiCFRU8bq0UA%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; swfstore=232337; JSESSIONID=FF19CD75F0120EBEAFFD2CE43E5CA402; cookie2=1c660390930209b50962f289b5bb0427; _tb_token_=5fee1e11e380a; alitrackid=www.taobao.com; lastalitrackid=www.taobao.com; whl=-1%260%260%261561690235025; _m_h5_tk=cb075ae581cd77289b15c1749d4e57a0_1561545572154; _m_h5_tk_enc=4b006e2cd7d8fc33eb21865d77b5268b; x5sec=7b227365617263686170703b32223a223336653532343031616133323262646631386636343066623264323366336664434f654131756746454c54323834477a6a724c626f514561444449354e6a51344f5463324e7a45374e513d3d227d; v=0; unb=2964897671; uc1=cookie16=U%2BGCWk%2F74Mx5tgzv3dWpnhjPaQ%3D%3D&cookie21=VFC%2FuZ9aiKCaj7AzMHh1&cookie15=W5iHLLyFOGW7aA%3D%3D&existShop=false&pas=0&cookie14=UoTaGduooAvf9A%3D%3D&tag=8&lng=zh_CN; sg=n12; _l_g_=Ug%3D%3D; skt=4fcb1fac7f08afd0; cookie1=B0T8IUbSQbqkCt%2FJYe82ma8UsOb%2BSAISz2tQ2m6C378%3D; csg=ea7da42c; uc3=vt3=F8dBy34bbqSVBss8Uos%3D&id2=UUGk2t2yeTDPWA%3D%3D&nk2=EUZGfwdnTO0%3D&lg2=V32FPkk%2Fw0dUvg%3D%3D; existShop=MTU2MTY5MDE1Mw%3D%3D; tracknick=rambourn; lgc=rambourn; dnk=rambourn; _nk_=rambourn; cookie17=UUGk2t2yeTDPWA%3D%3D'

}
device_list=['扫描仪','投影仪','打印机','高拍仪','碎纸机','装订机','传真机']
for i in np.arange(len(device_list)):
    f=open(str(i+1)+'.txt','wb')
    type__=device_list[i]
    f.write((type__+'\n\n').encode(encoding='utf-8'))
    for num in np.arange(5):
        url=url_model.replace('type__',type__)
        url=url+'&s='+str(num*44)
        res=rq.get(url,headers=headers)
        data = re.search(r'g_page_config = (.+);',res.text)
        data = json.loads(data.group(1),encoding='utf-8')
        for item in data['mods']['itemlist']['data']['auctions']:
            description=item['raw_title']
            raw_title=description
            if type__.endswith('机'):
                name=raw_title.split('机')[0]+'机'
            else:
                name=raw_title.split('仪')[0]+'仪'
            if len(name)>10:
                continue
            price=float(item['view_price'])
            if price<100:
                continue
            repair_cost=str(int(price/8))+'~'+str(int(price/4))
            shop_location=item['item_loc']
            shop_name=item['nick']
            link=item['detail_url']
            shop_link=item['shopLink']
            if shop_link.startswith(r'//'):
                shop_link='https:'+shop_link
            if link.startswith(r'//'):
                link='https:'+link
            total=('设备名称:%s\n类型:%s\n价格:%s\n维修成本:%s\n设备描述:%s\n购买链接:%s\n店铺名称:%s\n店铺位置:%s\n店铺链接:%s\n\n\n'%(name,type__,price,repair_cost,description,link,shop_name,shop_location,shop_link)).encode(encoding='utf-8')
            f.write(total)
    f.close()





#cookie=thw=cn; isg=BA4O0CR932mrMGtUhHAU0rrLXO3aJvikbx9-iDhXepHMm671oB8imbRV0w9SmMqh; t=bc09aeb5c7987372590b3844c1db89b1; cna=cA0hFYkqZxgCAd3oFKW9s+al; l=bBEIiYYrqjhJoEZXBOCMcZ_dHNQOSIOYYuWfpJ1Bi_5Ia1LsF-_OkxI38ep6V15RsIYB4U7ZIUJ9-etes; _cc_=VT5L2FSpdA%3D%3D; tg=0; mt=ci=6_1; enc=ZlZXBgo2w19A7N9SLwq8yZTQUK%2FaZtwbJ9i8ctPhcjznc0exhTiULzvRT8AbIu2sR1QDkF1lzLEiCFRU8bq0UA%3D%3D; hng=CN%7Czh-CN%7CCNY%7C156; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; cookie2=1c660390930209b50962f289b5bb0427; _tb_token_=5fee1e11e380a; whl=-1%260%260%261561378795709; v=0; unb=2964897671; uc1=cookie16=UtASsssmPlP%2Ff1IHDsDaPRu%2BPw%3D%3D&cookie21=UIHiLt3xThH8t7YQoFNq&cookie15=U%2BGCWk%2F75gdr5Q%3D%3D&existShop=false&pas=0&cookie14=UoTaGd6Z0Z5xKQ%3D%3D&tag=8&lng=zh_CN; sg=n12; _l_g_=Ug%3D%3D; skt=3245d241a1c07e07; cookie1=B0T8IUbSQbqkCt%2FJYe82ma8UsOb%2BSAISz2tQ2m6C378%3D; csg=39888d0a; uc3=vt3=F8dBy3kXkjRwi8lygDE%3D&id2=UUGk2t2yeTDPWA%3D%3D&nk2=EUZGfwdnTO0%3D&lg2=WqG3DMC9VAQiUQ%3D%3D; existShop=MTU2MTM2NTA4MQ%3D%3D; tracknick=rambourn; lgc=rambourn; dnk=rambourn; _nk_=rambourn; cookie17=UUGk2t2yeTDPWA%3D%3D
