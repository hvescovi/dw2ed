# apenas o teste do aplicativo contém este código
# a seguir que permite execução isolada do teste
# (sem precisar ser chamado por outro arquivo)
if __name__ == "__main__":
  # configuração para permitir importação de arquivos do diretório superior
  # https://codeolives.com/2020/01/10/python-reference-module-in-parent-directory/
  import os, sys
  currentdir = os.path.dirname(os.path.realpath(__file__)) # /home/friend/01-github/dw2ed/fund/python/pacote/ex5/classes
  parentdir = os.path.dirname(currentdir) # /home/friend/01-github/dw2ed/fund/python/pacote/ex5
  sys.path.append(parentdir)

from classes.aplicativo import Aplicativo

def run():
  print("* Teste da classe Aplicativo")
  whats = Aplicativo("WhatsApp", "Envie mensagens em texto, fotos e "+\
      "vídeos para seus amigos", "WhatsApp LLC")
  print(whats)

if __name__ == "__main__":
  run()