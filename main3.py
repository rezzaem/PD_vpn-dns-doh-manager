
import threading
import winreg
from pystray import Icon,Menu,MenuItem
from PIL import Image
import proxy_program
from sys import exit
import wmi
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

        
        def change_dns(self, provider): #def change_dns(self, provider,prime=None,second=None):
            global icon_status
            self.clear=False

            if provider == 'default': #if prime!=None :
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

            c = wmi.WMI()
            if self.clear ==False:
                for interface in c.Win32_NetworkAdapterConfiguration(IPEnabled=True):
                    if interface.DNSServerSearchOrder:
                        dns = [self.primary_dns, self.secondary_dns]
                        
                        status=interface.SetDNSServerSearchOrder(dns)
                        icon_status["d"]=True
                        update_trey('✔️DNS','dn')
                        
            else:
                for interface in c.Win32_NetworkAdapterConfiguration(IPEnabled=True):
                    status=interface.SetDNSServerSearchOrder()
                    icon_status["d"]=False
                    update_trey('DNS','dn')


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


def doh(item):
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
    global text_list
    if icon_status['p']==True and icon_status['d']==False:
        icon.icon=Image.open("pd_p_on.png")
    elif icon_status['d']==True and icon_status['p']==False:
        icon.icon=Image.open("pd_d_on.png")
    elif icon_status['p']==True and icon_status['d']==True:
        icon.icon=Image.open("pd_both_on.png")
    elif icon_status['p']==False and icon_status['d']==False:
        icon.icon=Image.open("pd_base2.png")
    
    if place =='do':
        text_list[1] =txt
        icon.update_menu()
    elif place =='dn':
        text_list[0]=txt
# -------- run --------
dns=DNS()


dns_result='چک کردن وضعیت دی ان اس'
doh_text='تونل یوتوب '
dns_text='DNS'
text_list=['DNS','تونل یوتوب ']
image = Image.open("pd_base2.png")  # Replace 'icon.png' with the path to your own icon
icon = Icon("Pd",image,"Pd manager :VPN Application", Menu(
    # MenuItem(lambda text:dns_result,dns_for_first_time),
    MenuItem(lambda text:text_list[0],Menu(
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
    MenuItem(lambda text:text_list[1],doh),

    MenuItem('خروج', on_quit)
))


icon.run()


