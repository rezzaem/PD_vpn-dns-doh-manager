
import threading
import winreg
from pystray import Icon,Menu,MenuItem
from PIL import Image
import proxy_program
from sys import exit
import wmi
from tendo import singleton
from pathlib import Path # for images and files
import time
from tkinter import Tk,Label,PhotoImage

#======== run just one at time ===========
#check program does not run before
# This tries to create an instance of single SingleInstance, which will fail if there's already one existing.
# If it fails, it means there's already an instance running, so we exit.
try:
    me = singleton.SingleInstance()
except singleton.SingleInstanceException:
    print("Another instance is already running. Exiting.")
    exit(0)
except BaseException as e:
    print(f"An unexpected error occurred: {e}")
    exit(1)

#======= path =============
OUTPUT_PATH = Path(__file__).parent # path of program
ASSETS_PATH = OUTPUT_PATH / Path("./assests")

def relative_to_assests(path: str) -> Path:
    return ASSETS_PATH / Path(path)


doh_thread = None # for run doh in thread
doh_running=False 
icon_status={"p":False,"d":False,"v":False} # for show icon and update
icon=None 
provider='irancell'

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
            if at_first==False:
                if known==True:
                    update_trey('✔️DNS','dn',current)
                else :
                    update_trey('DNS','dn','unknown')
            else:
                if known==True:
                    return f'active : {current}'
                else :
                    return f'active : unknown'




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

def set_provider(prov):
    global provider
    provider=prov


def doh(txt):
    global doh_thread,doh_running,icon_status,provider

    if str(txt)=='activate':


        def run_program():
            
                
            setunset_proxy('127.0.0.1:4500')
           
            proxy_program.run_it(provider)
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

def vpn():
    global icon_status
    icon_status['v']=True
    update_trey(None,None)

def on_quit(icon):
    global doh_running
    if doh_running==True:
        proxy_program.stop()
    setunset_proxy()
    # clear dns
    # dns.change_dns('default')
    icon.stop()
    exit()
    
def update_trey(txt,place,txt2=None): # place : do=doh , dn= dns , vp= vpn, ds= dns status
    global icon
    global icon_status
    global text_list
    
    if icon_status['p']==True and icon_status['d']==False and icon_status['v']==False:
        icon.icon=Image.open(relative_to_assests("p.png"))
    elif icon_status['d']==True and icon_status['p']==False and icon_status['v']==False:
        icon.icon=Image.open(relative_to_assests("d.png"))
    elif icon_status['p']==True and icon_status['d']==True and icon_status['v']==False:
        icon.icon=Image.open(relative_to_assests("pd.png"))
    elif icon_status['p']==False and icon_status['d']==False and icon_status['v']==False:
        icon.icon=Image.open(relative_to_assests("off.png"))
    elif icon_status['p']==True and icon_status['d']==False and icon_status['v']==True:
        icon.icon=Image.open(relative_to_assests("pv.png"))
    elif icon_status['p']==False and icon_status['d']==True and icon_status['v']==True:
        icon.icon=Image.open(relative_to_assests("vd.png"))
    elif icon_status['p']==False and icon_status['d']==False and icon_status['v']==True:
        icon.icon=Image.open(relative_to_assests("v.png"))
    elif icon_status['p']==True and icon_status['d']==True and icon_status['v']==True:
        icon.icon=Image.open(relative_to_assests("pvd.png"))
    
    if place =='do':
        text_list[1] =txt
        text_list[3]=txt2
        icon.update_menu()
    elif place =='dn':
        text_list[0]=txt
        text_list[2]=f'active : {txt2}'


# -------- run --------

#======= make start window ==========
def start_window():
    root = Tk()
    root.overrideredirect(True)  # removes default Tk window borders

    # Get the screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calculate the x and y coordinates to center the window
    x = (screen_width - 750) // 2
    y = (screen_height - 360) // 2

    # Set the window size and position
    root.geometry(f'750x360+{x}+{y}')

    image = PhotoImage(file=relative_to_assests("start_window.png"))  # replace with your 750x360 image
    label = Label(root, image=image)
    label.pack()

    def close_window():
        root.destroy()

    root.after(5000, close_window)  # close the window after 5 seconds

    root.mainloop()

start_window()
#========== make tray icon ==========
dns=DNS()

at_first=dns.get_dns(True)
text_list=['DNS','DOH (x,youtube tunnel) ',at_first,'activate'] 
image = Image.open(relative_to_assests("off.png"))  # Replace 'icon.png' with the path to your own icon
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
            MenuItem('Irancell & adsl',lambda:set_provider('irancell')),
            MenuItem('HamrahAval & other',lambda:set_provider('hamrah'))
        ))
    )), #doh
     MenuItem('VPN',Menu(
        MenuItem('comming soon',vpn)
    )),
    MenuItem('exit', on_quit)
))


icon.run()


