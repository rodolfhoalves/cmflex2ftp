import functions, file1, file2, file3, file4, os, credential, notification, ftp

folder = functions.create_folder_files() # Criação da pasta para armazenar os arquivos que serão movidos da pasta de Download. 
os.makedirs(folder)
print(folder)
functions.rmv_files() #  Remove se tiver arquivos remanescentes da pasta de download CMFlex*

################## DOWNLOAD DOS ARQUIVOS ##############################

# ARQUIVO 1
file1.downf1() # Iniciar o login e download do arquivo
nn_file1 = file1.rename_file1() # Renomeia o arquivo com o ANO + DATA
functions.move_file(credential.default_chrome + '\\' + nn_file1, folder + '\\' + nn_file1) # Move o arquivo para o folder variable

# ARQUIVO 2
file2.downf2() # Iniciar o login e download do arquivo
nn_file2 = file2.rename_file2() # Renomeia o arquivo com o ANO + DATA
functions.move_file(credential.default_chrome + '\\' + nn_file2, folder + '\\' + nn_file2) # Move o arquivo para o folder variable


# ARQUIVO 3
file3.downf3() # Iniciar o login e download do arquivo
nn_file3 = file3.rename_file3() # Renomeia o arquivo com o ANO + DATA
functions.move_file(credential.default_chrome + '\\' + nn_file3, folder + '\\' + nn_file3) # Move o arquivo para o folder variable

# ARQUIVO 4
file4.downf4() # Iniciar o login e download do arquivo
nn_file4 = file4.rename_file4() # Renomeia o arquivo com o ANO + DATA
functions.move_file(credential.default_chrome + '\\' + nn_file4, folder + '\\' + nn_file4) # Move o arquivo para o folder variable


####################### VERIFICAÇÃO #####################################

try:
  count_files = len(os.listdir(folder))
  if count_files == 4:
    print('4 Arquivos baixados do site da cmflex')
except:
    print('Falha no download dos arquivos da cmflex')

try:
###################### ENVIO DOS ARQUIVOS ##############################
############ ARQUIVO 1 #####################
  folder_remote_ftp = 'PontesHoteis/custos'
  path_remote_file1 = folder_remote_ftp + '/' + nn_file1
  # Chama o envio passado o FROM: CAMINHO DO ARQUIVO1 + NOME DO ARQUIVO1 + NOME DA PASTA REMOTA
  ftp.ftp_upload(folder  + '\\' + nn_file1, nn_file1, folder_remote_ftp, path_remote_file1) 


############ ARQUIVO 2 #####################
  folder_remote_ftp = 'PontesHoteis/CPA/FichaTecnica'
  path_remote_file2 = folder_remote_ftp + '/' + nn_file2
  # Chama o envio passado o caminho do arquivo1 + nome do arquivo + nome da pasta remota
  ftp.ftp_upload(folder  + '\\' + nn_file2, nn_file2, folder_remote_ftp, path_remote_file2) 


############ ARQUIVO 3 #####################
  folder_remote_ftp = 'PontesHoteis/CPA'
  path_remote_file3 = folder_remote_ftp + '/' + nn_file3
  # Chama o envio passado o caminho do arquivo1 + nome do arquivo + nome da pasta remota
  ftp.ftp_upload(folder  + '\\' + nn_file3, nn_file3, folder_remote_ftp, path_remote_file3)

############ ARQUIVO 4 #####################
  folder_remote_ftp = 'PontesHoteis/CPA'
  path_remote_file4 = folder_remote_ftp + '/' + nn_file4
  # Chama o envio passado o caminho do arquivo1 + nome do arquivo + nome da pasta remota
  ftp.ftp_upload(folder  + '\\' + nn_file4, nn_file4, folder_remote_ftp, path_remote_file4) 

  notification.send_mail()
except:
  print('Erro no envio dos arquivos para o BI')
