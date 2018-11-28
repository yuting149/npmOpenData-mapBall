# import wikipediaapi
# from hanziconv import HanziConv

# wiki = wikipediaapi.Wikipedia('zh-tw')
# mutcd = wiki.page('蒙娜麗莎')
# zz = "\n".join([s.title for s in mutcd.sections])
# print(HanziConv.toTraditional(zz))


import wptools
# 找圖
# fela = wptools.page('蒙娜麗莎', lang='zh').get_query().image('page')['url']
# fela2 = wptools.page('蒙娜麗莎', lang='zh').get_query().image('thumb')['url']
# 找圖

# infobox
lisa = wptools.page('翠玉白菜', lang='zh').get_parse()
print('=====')
print(lisa.infobox)
print('=====')
# infobox
lisa = wptools.page('蒙娜麗莎', lang='zh').get()
print('=====')
print(lisa.wikidata)
print('=====')
