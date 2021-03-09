# configuração para importar config da 
# pasta superior
import os
import sys
currentdir = os.path.dirname(
    os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)