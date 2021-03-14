# configuração para permitir importação de arquivos do diretório superior
import os, sys
atual = os.path.abspath(".") #  retorna o diretório superior
sys.path.append(atual) # inclui esse diretório no path (caminhos conhecidos)