import datetime, credential, shutil, calendar, glob, os

### Gera as datas 

ano_atual = datetime.datetime.now().year
mes_atual = datetime.datetime.now().month
dia_atual = datetime.datetime.now().day

'''
dia_atual = ("{:02d}".format(datetime.datetime.now().day))
mes_atual = ("{:02d}".format(datetime.datetime.now().month))
ano_atual = ("{:04d}".format(datetime.datetime.now().year))
'''

def ultimo_dia_mes(mes_atual, ano_atual):

    return calendar.monthrange(ano_atual, mes_atual)[1]

ultimo_dia_mes = ultimo_dia_mes(mes_atual, ano_atual)

# Gera as datas iniciais para serem preenchindas no CMFLEX
data_ultimo_dia = (str(ultimo_dia_mes) + '/' + ("{:02d}".format(mes_atual)) + '/' + str(ano_atual))
#data_primeiro_dia = (str(1) + '/' + str(mes_atual) + '/' + str(ano_atual))
data_primeiro_dia = '01' + '/' + ("{:02d}".format(mes_atual)) + '/' + str(ano_atual) #Gera a data do prinmeiro dia para preencher no cmflex


def rmv_files():
    for filename in glob.glob(credential.download_chrome_folder):
        os.remove(filename) 


local_path = os.getcwd()

def create_folder_files():
    ano_atual = ("{:04d}".format(datetime.datetime.now().year))
    mes_atual = ("{:02d}".format(datetime.datetime.now().month))
    dia_atual = ("{:02d}".format(datetime.datetime.now().day))
    hora_atual = ("{:02d}".format(datetime.datetime.now().hour))
    minuto_atual = ("{:02d}".format(datetime.datetime.now().minute))
    segundo_atual = ("{:02d}".format(datetime.datetime.now().second))

    folder_files = 'C:\\Export.CMFlex\\' + (ano_atual) + (mes_atual) + (dia_atual) + '_' + (hora_atual) + (minuto_atual) + '_' + (segundo_atual)
    return folder_files



    

def move_file(old_path, new_path):
    shutil.move(old_path, new_path)



