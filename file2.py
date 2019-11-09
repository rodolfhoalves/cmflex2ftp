
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.common.action_chains import ActionChains
import functions
import credential
import os

def downf2():
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get(credential.file2)

    # Preenche nome de usuário
    user_input = driver.find_element_by_id('login')
    user_input.send_keys(credential.username)

    # Preenche a senha
    user_input = driver.find_element_by_name('Password')
    user_input.send_keys(credential.password)
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
    user_input = driver.find_element_by_xpath("//span[@class='rbText']")
    user_input.click()

    time.sleep(1)
    a = driver.find_element_by_xpath("//span[@class='rmText' and text()='Download dos Dados em Formato Excel']")
    time.sleep(2)
    a.click()

    time.sleep(15)
    driver.close()



def rename_file2():
    oldname = credential.default_chrome + '\\' + credential.default_name_file
    new_nn = 'CM.CMFlex.Relatorios.Reports.ConfiguracaoDeRelatorioReport.mrt_FT_' + ("{:04d}".format(functions.ano_atual)) + ("{:02d}".format(functions.mes_atual)) + ("{:02d}".format(functions.dia_atual)) + '.xlsx'
    newname = credential.default_chrome + '\\' + new_nn
    os.rename(oldname, newname)
    return new_nn





