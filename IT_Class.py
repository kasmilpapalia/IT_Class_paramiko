import paramiko
import time

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect('192.20.20.30',port=22,username='admin',password='')

print("\n Berhasil Terkoneksi Ke Router 1 \n")

stdin, stdout, stderr = ssh_client.exec_command('system identity set name=IT_Calss')
time.sleep(1)
stdin, stdout, stderr = ssh_client.exec_command('ip dhcp-client add interface=ether1 disabled=no')
time.sleep(1)
stdin, stdout, stderr = ssh_client.exec_command('ip hotspot ')
time.sleep(1)

print("\n Berhasil")
print("\n confignya sukses")

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect('192.20.20.25',port=22,username='admin',password='')

print("\n Berhasil Terkoneksi Ke Router 1 \n")

stdin, stdout, stderr = ssh_client.exec_command('system identity set name=_Calss')
time.sleep(1)
stdin, stdout, stderr = ssh_client.exec_command('ip dhcp-client add interface=ether1 disabled=no')
time.sleep(1)
stdin, stdout, stderr = ssh_client.exec_command('ip hotspot ')
time.sleep(1)

print("\n Berhasil")
print("\n confignya sukses")
