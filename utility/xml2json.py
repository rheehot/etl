'''
XML2JSON
사용방법: python xml2json.py source.xml > target.json
xmltodict 설치 필요 (pip install xmltodict)
'''

import sys
reload(sys)
import json
import xmltodict

def convert(xml_file, xml_attribs=True):
    with open(xml_file, "rb") as f:    # notice the "rb" mode
        d = xmltodict.parse(f, xml_attribs=xml_attribs)
    return json.dumps(d, indent=4)

result = convert(sys.argv[1], xml_attribs=True)
print(result)