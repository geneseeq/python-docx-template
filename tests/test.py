# -*- coding: utf-8 -*-
'''
Created : 2015-03-12

@author: Eric Lapouyade
'''

from docxtpl import DocxTemplate, RichText
import json
tpl=DocxTemplate('/home/code/python-docx-template/tests/test_files/cellbg_tpl.docx')

context = {'date':'2015年3-10','name':'小明','female':'男','card':'37078787','phone':'6236891'}
encodedjson = json.dumps(context)
decodejson = json.loads(encodedjson)
#test = {"name":"高高高"}
print decodejson
#print json.loads()
#print json.loads(str(test))
tpl.render(decodejson)
tpl.save('cellbg.docx')

