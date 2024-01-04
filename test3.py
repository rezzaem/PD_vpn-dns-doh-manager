
import winreg

# Set the proxy server and port
proxy_server = "proxy.example.com"
proxy_port = "8080"

# Open the Internet Settings registry key
internet_settings = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Software\Microsoft\Windows\CurrentVersion\Internet Settings', 0, winreg.KEY_ALL_ACCESS)

# Set the proxy server and port values
winreg.SetValueEx(internet_settings, "ProxyServer", 0, winreg.REG_SZ, f"{proxy_server}:{proxy_port}")
winreg.SetValueEx(internet_settings, "ProxyEnable", 0, winreg.REG_DWORD, 1)

# Close the registry key
winreg.CloseKey(internet_settings)
