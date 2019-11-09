from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
import datetime
import calendar
from selenium.webdriver.common.action_chains import ActionChains

username = 'rodolfho.queiroz'
password = 'Pontes@1234'

### Gera as datas 
ano_atual = datetime.datetime.now().year
mes_atual = datetime.datetime.now().month

def ultimo_dia_mes(mes_atual, ano_atual):

    return calendar.monthrange(ano_atual, mes_atual)[1]

ultimo_dia_mes = ultimo_dia_mes(mes_atual, ano_atual)

data_ultimo_dia = (str(ultimo_dia_mes) + '/' + str(mes_atual) + '/' + str(ano_atual))
data_primeiro_dia = (str(1) + '/' + str(mes_atual) + '/' + str(ano_atual))
#######


driver = webdriver.Chrome('chromedriver.exe')
#driver.get('https://pontes.cmflex.com.br')
driver.get('https://pontes.cmflex.com.br/Contabilidade/Reports/Filters/ReportFilterGenerico.aspx?reportClassName=CM.CMFlex.Relatorios.Reports.ConfiguracaoDeRelatorioReport&id=59')

# Preenche nome de usuário
user_input = driver.find_element_by_id('login')
user_input.send_keys(username)

# Preenche a senha
user_input = driver.find_element_by_name('Password')
user_input.send_keys(password)
time.sleep(1)

# Dar o submit na página
login_button = driver.find_element_by_name('submit')
login_button.click()


time.sleep(1)
# Seleciona a empresa Mar Hotel e entra
s1 = Select(driver.find_element_by_id('idEmpresaSelecionada'))
s1.select_by_index(2)
login_button = driver.find_element_by_name('submit')
login_button.click()


time.sleep(1)
user_input = driver.find_element_by_id('ctl00_ctl00_ctl00_placeHolderMain_mainWebCad_FilterControls_frmFiltro_dcpDataInicialCtrl11_dateInput')
user_input.send_keys(data_primeiro_dia)
time.sleep(1)
user_input = driver.find_element_by_id('ctl00_ctl00_ctl00_placeHolderMain_mainWebCad_FilterControls_frmFiltro_dcpDataFinalCtrl12_dateInput')
user_input.send_keys(data_ultimo_dia)

time.sleep(1)
user_input = driver.find_element_by_xpath("//span[@class='rbText']")
user_input.click()

time.sleep(1)
#a =  driver.find_element_by_xpath("//span[@class='rmText']/option[text()='Download dos Dados em Formato Excel']").click()
a = driver.find_element_by_xpath("//span[@class='rmText' and text()='Download dos Dados em Formato Excel']")
time.sleep(2)
a.click()

time.sleep(30)
driver.close()

''''
time.sleep(1)
#from selenium.webdriver.common.action_chains import ActionChains

elem = driver.find_element("//span[@class='rmText' and text()='Download dos Dados em Formato Excel']")
action = ActionChains(driver)
action.move_to_element("//span[@class='rmText' and text()='Download dos Dados em Formato Excel']")
action.click()
action.perform()
'''

