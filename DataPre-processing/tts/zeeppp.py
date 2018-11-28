import zeep
import time

wsdl = 'http://tts.itri.org.tw/TTSService/Soap_1_3.php?wsdl'
client = zeep.Client(wsdl=wsdl)

rs = client.service.ConvertSimple("dodokey", "830725", "安安安安")

print(rs, rs[-5:])
time.sleep(1.5)

rst = client.service.GetConvertStatus("dodokey", "830725", rs[-5:]).split('&')
print(rst[4])


from tqdm import tqdm
import requests

url = rst[4]
response = requests.get(url, stream=True)

with open("10MB.wav", "wb") as handle:
    for data in tqdm(response.iter_content()):
        handle.write(data)


import os
os.system("start 10MB.wav")
