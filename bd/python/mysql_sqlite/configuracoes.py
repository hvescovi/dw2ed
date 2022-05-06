from config_comum import *

if utilizar == "sqlite":
    from config_sqlite import *
elif utilizar == "mysql":
    from config_mysql import *
else:
    print("SEM CONFIGURAÇÃO DE USO DE BANCO DE DADOS!!")