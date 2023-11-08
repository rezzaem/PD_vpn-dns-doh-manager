
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
        c = wmi.WMI()       
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

            
            if self.clear ==False:
                
                for interface in self.c.Win32_NetworkAdapterConfiguration(IPEnabled=True):
                    if interface.DNSServerSearchOrder:
                        dns = [self.primary_dns, self.secondary_dns]
                        
                        status=interface.SetDNSServerSearchOrder(dns)
                        icon_status["d"]=True
                        update_trey('✔️DNS','dn',provider)
                
                        
            else:
                for interface in self.c.Win32_NetworkAdapterConfiguration(IPEnabled=True):
                    interface.SetDNSServerSearchOrder()
                    icon_status["d"]=False
                    update_trey('DNS','dn','empty')

        def get_dns (self,at_first=False):
            for interface in self.c.Win32_NetworkAdapterConfiguration(IPEnabled=True):
                if interface.DNSServerSearchOrder:
                    current=interface.DNSServerSearchOrder[0]
            known=False # for show current dns if at dns list
            try:        
                    if current==self.SHECAN[0]:
                        current='shecan'
                        known=True
                    elif current==self.ELECTRO[0]:
                        current='electro'
                        known=True
                    elif current==self.F403[0]:
                        current='403'
                        known=True
                    elif current==self.RADAR[0]:
                        current='radar'
                        known=True
                    elif current==self.CLOUD[0]:
                        current='cloud'
                        known=True
                    elif current==self.GOOGLE[0]:
                        current='google'
                        known=True
                    else :
                        current='unknown'
            except:
                    current='None'
            
            if known==True:
                update_trey('✔️DNS','dn',current)

            # else :

            # if at_first==False:
            #     update_trey(,'dn',)
            # else :
            #     return f'active : {current}'



            
            # else :
            #     update_trey(None



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


def doh(txt):
    global doh_thread,doh_running,icon_status

    if str(txt)=='activate':


        def run_program():
            
                
            setunset_proxy('127.0.0.1:4500')
           
            proxy_program.run_it()
            doh_running=True

        doh_thread = threading.Thread(target=run_program)
        doh_thread.start()
    
        icon_status["p"]=True
        update_trey('✔️DOH (x,youtube tunnel) ','do','deactive')

    else:
        
        setunset_proxy()
        proxy_program.stop()
        doh_running=False

        icon_status["p"]=False
        update_trey('DOH (x,youtube tunnel) ','do','activate')



def on_quit(icon):
    global doh_running
    if doh_running==True:
        proxy_program.stop()
    setunset_proxy()
    # clear dns
    dns.change_dns('default')
    icon.stop()
    exit()
    
def update_trey(txt,place,txt2=None): # place : do=doh , dn= dns , vp= vpn, ds= dns status
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
        text_list[3]=txt2
        icon.update_menu()
    elif place =='dn':
        text_list[0]=txt
    elif place=='ds':
        if txt2!=None:
            text_list[2]=f'active : {txt2}'
        else:
            text_list[2]=f'active : {txt}'

# -------- run --------
dns=DNS()

at_first=dns.get_dns(True)
text_list=['DNS','DOH (x,youtube tunnel) ',at_first,'activate'] 
image = Image.open("pd_base2.png")  # Replace 'icon.png' with the path to your own icon
icon = Icon("Pd",image,"Pd manager :VPN Application", Menu(

    MenuItem(lambda text:text_list[0],Menu( #dns
        MenuItem(lambda text:text_list[2],lambda :dns.get_dns()),
        MenuItem('bypass',Menu(
            MenuItem('shecan',lambda:dns.change_dns('shecan')),
            MenuItem('403',lambda:dns.change_dns('f403')),
            MenuItem('radar🎮',lambda:dns.change_dns('radar')),
            MenuItem('electro🎮',lambda:dns.change_dns('electro'))
        )),
        MenuItem('better net',Menu(
            MenuItem('google',lambda:dns.change_dns('google')),
            MenuItem('cloud',lambda:dns.change_dns('cloud'))
        )),
        MenuItem('deactive',lambda:dns.change_dns('default'))
    )),
    MenuItem(lambda text:text_list[1],Menu(
        MenuItem(lambda text:text_list[3],lambda:doh(text_list[3])),
        MenuItem('isp',Menu(
            MenuItem('Irancell',None),
            MenuItem('HamrahAval',None),
            MenuItem('other',None)
        ))
    )), #doh
     MenuItem('VPN',Menu(
        MenuItem('comming soon',None)
    )),
    MenuItem('exit', on_quit)
))


icon.run()


