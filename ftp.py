from ftplib import FTP 
import os
import fileinput
import ftplib

def ftp_upload(localfile, remotefile, ftp_folder, full_remote_file_path):
  ftp = FTP()
  ftp.set_debuglevel(2)
  ftp.connect('endereço_ip', 21) 
  ftp.login('usuário_ftp', 'senha')
  ftp.cwd(ftp_folder)

  fp = open(localfile, 'rb')
  ftp.storbinary('STOR %s' % os.path.basename(localfile), fp, 1024)
  fp.close()
  print("after upload " + localfile + " to " + remotefile)
  
  