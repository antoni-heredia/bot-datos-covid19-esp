from apscheduler.schedulers.blocking import BlockingScheduler
from six.moves import urllib
import os
import requests


sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=0.1)
def timed_job():

    data_path = './datos/data.csv'
    if os.path.exists(data_path):
        os.remove(data_path)
    else:
        print("No existe el fichero data.csv")

    url = 'https://covid19.isciii.es/resources/data.csv'

    urllib.request.urlretrieve(url,data_path)



    ccaa_path = './datos/ccaa.csv'
    if os.path.exists(ccaa_path):
        os.remove(ccaa_path)
    else:
        print("No existe el fichero ccaa.csv")

    url = 'https://covid19.isciii.es/resources/ccaa.csv'
    urllib.request.urlretrieve(url,ccaa_path)


    pdf_path = "./datos/actualizaciones_estado"
    mayor = 0
    for file in os.listdir(pdf_path):
        numero = int(file.split("_")[1])
        if(numero > mayor):
            mayor = numero
    mayor += 1
    url = "https://www.mscbs.gob.es/profesionales/saludPublica/ccayes/alertasActual/nCov-China/documentos/Actualizacion_"+str(mayor)+"_COVID-19.pdf"
    r = requests.get(url, verify=False)
    if r.status_code == 200:
        os.remove(pdf_path+"/ultimo_"+str(mayor-1))
        with open(pdf_path+"/ultimo_"+str(mayor), 'w') as fp: 
            pass

sched.start()