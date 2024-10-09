# from jiraone import LOGIN, PROJECT

# user = "sebastianaa@unisabana.edu.co"
# password = "ATATT3xFfGF01JVAQZ6oJigSRi6xHdQXPLYK7lqHAXBrIUPh910t39hSN0FIQu5TKEjNIyM_AhFKC0odZeeo4guE6A-wwm1KXsLyzcMFdXj5sAYK8WQWzEdzSbRI4rNH3lHMw9wabkspkhVNhaesN2Yc_985zlZ5NvgBGyX--zHkdlqffkRruJQ=4C5093DB"
# link = "https://unisabana.atlassian.net/"
# LOGIN.api = False  # comment out line, if you want to extract history from a cloud instance
# LOGIN(user=user, password=password, url=link)

# if __name__ == '__main__':
#     # the output of the file would be absolute to the directory where this python file is being executed from
#     jql = jql = "project in (PAFI3) AND issuetype in (StandardIssueTypes(), SubTaskIssueTypes()) ORDER BY Rank DESC" # A valid JQL query
#     PROJECT.change_log(jql=jql)

from jiraone import LOGIN, PROJECT
import pandas as pd

user = "sebastianaa@unisabana.edu.co"
password = "ATATT3xFfGF01JVAQZ6oJigSRi6xHdQXPLYK7lqHAXBrIUPh910t39hSN0FIQu5TKEjNIyM_AhFKC0odZeeo4guE6A-wwm1KXsLyzcMFdXj5sAYK8WQWzEdzSbRI4rNH3lHMw9wabkspkhVNhaesN2Yc_985zlZ5NvgBGyX--zHkdlqffkRruJQ=4C5093DB"
link = "https://unisabana.atlassian.net/"
LOGIN.api = False  # comment out line, if you want to extract history from a cloud instance
LOGIN(user=user, password=password, url=link)

if __name__ == '__main__':
    # El archivo de salida será generado en la carpeta de ejecución de este archivo
    jql = "project in (PAFI3) AND issuetype in (StandardIssueTypes(), SubTaskIssueTypes()) ORDER BY Rank DESC"  # JQL válido
    PROJECT.change_log(jql=jql)

    # Reemplaza 'archivo_salida.csv' por la ruta correcta al archivo generado
    file_path = '/home/sebastian/Documents/PythonProjects/ChangeLog/change_log.csv'
    df = pd.read_csv(file_path)  

    # Guardar el archivo con el nuevo separador, asegurando que los textos que contienen comas estén entre comillas dobles
    df.to_csv('/home/sebastian/Documents/PythonProjects/ChangeLog/change_log_modificado.csv', sep='|', index=False, quoting=1)
