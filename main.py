import subprocess
import platform
import nmap3

# Initialization nmap.exe
s_path=[r'.\Nmap\nmap.exe']
print(type(s_path))
#nm = nmap.PortScanner(nmap_search_path = s_path)
#nm.scan(hosts="10.255.250.1/24",arguments="-sn")
#ip_list=nm.all_hosts()
#print(ip_list)

import nmap3
nmap = nmap3.Nmap()
results = nmap.scan_top_ports("10.255.250.52", args="-sV")
print(results)



#nm = nmap.PortScanner()
#nm.scan('127.0.0.1', '22-443')
#nm.command_line()
#ip_list=nm.all_hosts()
#print(ip_list)






def trace_route(ip_address):
    result = subprocess.run(['tracert', ip_address], capture_output=True, text=True)
    
    if result.returncode == 0:
        print(result.stdout)
    else:
        print("Ошибка при выполнении трассировки:", result.stderr)

#IP - вводи адерес для выполнения трассировки 
#IP = input('Введите адрес на который надо выполнить трассировку: ')
#trace_route(IP)

def myping(host):
    # Выберите параметр в зависимости от операционной системы
    parameter = "-n" if platform.system().lower() == "windows" else "-c"
    number = input('Введите кол-во пингов:')
    # Построение команды ping
    command = ["ping", parameter, number, host]
    response = subprocess.call(command)

    # Интерпретация ответа
    return response == 0


#IPping = input('Введите адресс на который надо отправить пинг: ')
#print(myping(IPping))

