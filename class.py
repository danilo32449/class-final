import re
import json
import matplotlib.pyplot as plt
from collections import Counter
from datetime import datetime

# Lee el archivo de logs
with open('logs.txt', 'r') as file:
    logs = file.readlines()

# Expresiones regulares para extraer datos
ip_pattern = r'(\d{1,3}\.){3}\d{1,3}'
date_pattern = r'(\d{2}/\w{3}/\d{4}:\d{2}:\d{2}:\d{2})'
method_pattern = r'(?P<method>GET|POST|PUT|DELETE)'
resource_pattern = r'(?P<resource>\S+)'
status_code_pattern = r'(?P<status_code>\d{3})'

# Lista para almacenar los datos extraídos
data = []

# Procesa cada línea del log
for line in logs:
    ip_match = re.search(ip_pattern, line)
    date_match = re.search(date_pattern, line)
    method_match = re.search(method_pattern, line)
    resource_match = re.search(resource_pattern, line)
    status_code_match = re.search(status_code_pattern, line)

    if ip_match and date_match and method_match and resource_match and status_code_match:
        entry = {
            'ip': ip_match.group(),
            'date': datetime.strptime(date_match.group(), '%d/%b/%Y:%H:%M:%S'),
            'method': method_match.group('method'),
            'resource': resource_match.group('resource'),
            'status_code': status_code_match.group('status_code')
        }
        data.append(entry)

# Guarda los datos extraídos en formato JSON
with open('logs_extracted.json', 'w') as json_file:
    json.dump(data, json_file, default=str)

# Visualización de Datos
methods = [entry['method'] for entry in data]
method_counts = Counter(methods)

# Gráfico de distribución de métodos de solicitud HTTP
plt.figure(figsize=(10, 6))
plt.bar(method_counts.keys(), method_counts.values(), color='blue')
plt.title('Distribución de Métodos de Solicitud HTTP')
plt.xlabel('Método')
plt.ylabel('Frecuencia')
plt.savefig('http_methods_distribution.png')
plt.show()

# Gráfico de frecuencia de errores por día
error_codes = [entry['status_code'] for entry in data if entry['status_code'].startswith('4') or entry['status_code'].startswith('5')]
error_counts = Counter(error_codes)

plt.figure(figsize=(10, 6))
plt.bar(error_counts.keys(), error_counts.values(), color='red')
plt.title('Frecuencia de Errores HTTP')
plt.xlabel('Código de Error')
plt.ylabel('Frecuencia')
plt.savefig('http_error_frequency.png')
plt.show()

if ip_match and date_match and method_match and resource_match and status_code_match:
    entry = {
        'ip': ip_match.group(),
        'date': datetime.strptime(date_match.group(), '%d/%b/%Y:%H:%M:%S'),
        'method': method_match.group('method'),
        'resource': resource_match.group('resource'),
        'status_code': status_code_match.group('status_code')
    }
    data.append(entry)