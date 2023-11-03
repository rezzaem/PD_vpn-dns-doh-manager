
from tkinter import messagebox
import subprocess
import threading
import os
import signal
import winreg
from pystray import Icon,Menu,MenuItem
from PIL import Image
from command_runner import command_runner
import socket
import proxy_program
from sys import exit
#---------------------------------------
doh_thread = None
doh_running=False
icon_status={"p":False,"d":False}

icon=None

class DNS :
               
        SHECAN = ['178.22.122.100', '185.51.200.2']
        F403 = ['10.202.10.202', '10.202.10.102']
        RADAR=['10.202.10.10','10.202.10.11']
        ELECTRO = ['78.157.42.100', '78.157.42.101']
        CLOUD = ['1.1.1.1', '1.0.0.1']
        GOOGLE = ['8.8.8.8', '8.8.4.4']

        def get_active_interfaces(self):
            try:
                exit_code, output = command_runner('netsh interface show interface')
                output = output.split("\n")
                interface_list = []
                for i in output:
                    if 'Connected' in i:
                        interface_list.append(i[47:])
                return interface_list
            except:
                return '-1'
        
        def change_dns(self, provider):
            global icon_status
            interface = self.get_active_interfaces()
            if interface=='-1':
                messagebox.show('ERROR','there is some problem with the data, please check the connections...')
            
            else :
                self.clear=False
                if provider == 'default':
                    self.clear=True
                elif provider == 'shecan':
                    self.primary_dns=self.SHECAN[0]
                    self.secondary_dns=self.SHECAN[1]
                elif provider == 'electro':
                    self.primary_dns=self.SHECAN[0]
                    self.secondary_dns=self.SHECAN[1]
                elif provider == 'f403':
                    self.primary_dns=self.F403[0]
                    self.secondary_dns=self.F403[1]
                elif provider=='radar':
                    self.primary_dns=self.RADAR[0]
                    self.secondary_dns=self.RADAR[1]
                elif provider == 'cloud':
                    self.primary_dns=self.CLOUD[0]
                    self.secondary_dns=self.CLOUD[1]
                elif provider == 'google':
                    self.primary_dns=self.GOOGLE[0]
                    self.secondary_dns=self.GOOGLE[1]

                for i in interface:
                    self.exit_code, self.output = command_runner(f'netsh interface ipv4 delete dnsservers "{i}" all')
                    if self.clear != True:
                        self.exit_code, self.output =command_runner(f'netsh interface ipv4 add dnsservers "{i}" address={self.primary_dns} index=1')
                        self.exit_code, self.output = command_runner(f'netsh interface ipv4 add dnsservers "{i}" address={self.secondary_dns} index=2')
                        icon_status["d"]=True
                        update_trey()
                    else:
                        icon_status["d"]=False
                        update_trey()
                    



# def get_dns_address(icon):
    
#     global dns_result

#     SHECAN = ['178.22.122.100', '185.51.200.2']
#     F403 = ['10.202.10.202', '10.202.10.102']
#     RADAR=['10.202.10.10','10.202.10.11']
#     ELECTRO = ['78.157.42.100', '78.157.42.101']
#     CLOUD = ['1.1.1.1', '1.0.0.1']
#     GOOGLE = ['8.8.8.8', '8.8.4.4']
    
#     try:
#         hostname = "www.google.com"  # You can use any valid hostname here
#         dns_address = socket.gethostbyname(hostname)
#         if dns_address in SHECAN :
#             dns_result="شکن"
#         elif dns_address in F403:
#             dns_result="403"
#         elif dns_address in RADAR:
#             dns_result="رادار"
#         elif dns_address in ELECTRO:
#             dns_result="الکترو"
#         else :
#             dns_result=dns_address

#         dns_result=f'{dns_result}:دی ان اس فعال'
#         icon.update_menu()
#     except socket.gaierror:
#         dns_result = "DNS address not found"

# def dns_for_first_time(icon):
#     global dns_result
#     dns_thread = threading.Thread(target=get_dns_address(icon))
#     dns_thread.start()
    



def setunset_proxy(proxy=None):

    INTERNET_SETTINGS = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
            r'Software\Microsoft\Windows\CurrentVersion\Internet Settings',
            0, winreg.KEY_ALL_ACCESS)
    
    if proxy is not None:
        winreg.SetValueEx(INTERNET_SETTINGS, "ProxyEnable", 0, winreg.REG_DWORD, 1)
        winreg.SetValueEx(INTERNET_SETTINGS, "ProxyServer", 0, winreg.REG_SZ, proxy)
    else :
        winreg.SetValueEx(INTERNET_SETTINGS, "ProxyEnable", 0, winreg.REG_DWORD, 0)
        winreg.SetValueEx(INTERNET_SETTINGS, "ProxyServer", 0, winreg.REG_SZ, '')



def doh(icon,item):
    global doh_thread,doh_running,icon_status

    if str(item)=='تونل یوتوب ':

        

        def run_program():
            
                
            setunset_proxy('127.0.0.1:4500')
           
            proxy_program.run_it()
            doh_running=True

        doh_thread = threading.Thread(target=run_program)
        doh_thread.start()
    
        icon_status["p"]=True
        update_trey('✔️تونل یوتوب ','do')



    else:
        
        setunset_proxy()
        proxy_program.stop()
        doh_running=False

        icon_status["p"]=False
        update_trey('تونل یوتوب ','do')




    
    

def on_quit(icon):
    global doh_running
    if doh_running==True:
        proxy_program.stop()
    setunset_proxy()
    # clear dns
    dns.change_dns('default')
    icon.stop()
    exit()
    
def update_trey(txt,place): # place : do=doh , dn= dns , vp= vpn
    global icon
    global icon_status
    global doh_text
    if icon_status['p']==True and icon_status['d']==False:
        icon.icon=Image.open("pd_p_on.png")
    elif icon_status['d']==True and icon_status['p']==False:
        icon.icon=Image.open("pd_d_on.png")
    elif icon_status['p']==True and icon_status['d']==True:
        icon.icon=Image.open("pd_both_on.png")
    elif icon_status['p']==False and icon_status['d']==False:
        icon.icon=Image.open("pd_base2.png")
    
    if place =='do':
        doh_text =txt
        icon.update_menu()
    



    
    

dns=DNS()


dns_result='چک کردن وضعیت دی ان اس'
doh_text='تونل یوتوب '

image = Image.open("pd_base2.png")  # Replace 'icon.png' with the path to your own icon
icon = Icon("Pd",image,"Pd manager :VPN Application", Menu(
    # MenuItem(lambda text:dns_result,dns_for_first_time),
    MenuItem('DNS',Menu(
        MenuItem('تحریم گذر',Menu(
            MenuItem('شکن',lambda:dns.change_dns('shecan')),
            MenuItem('403',lambda:dns.change_dns('f403')),
            MenuItem('رادار🎮',lambda:dns.change_dns('radar')),
            MenuItem('الکترو🎮',lambda:dns.change_dns('electro'))
        )),
        MenuItem('بهبود دهنده',Menu(
            MenuItem('گوگل',lambda:dns.change_dns('google')),
            MenuItem('کلود',lambda:dns.change_dns('cloud'))
        )),
        MenuItem('خاموش',lambda:dns.change_dns('default'))
    )),
    MenuItem(lambda text:doh_text,doh),

    MenuItem('خروج', on_quit)
))


icon.run()


