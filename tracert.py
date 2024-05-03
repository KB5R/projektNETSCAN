import subprocess

def trace_route(ip_address):
    result = subprocess.run(['tracert', ip_address], capture_output=True, text=True)
    
    if result.returncode == 0:
        print(result.stdout)
    else:
        print("Error executing tracert:", result.stderr)

# Замените '8.8.8.8' на IP-адрес, к которому вы хотите выполнить трассировку маршрута
trace_route('ya.ru')
