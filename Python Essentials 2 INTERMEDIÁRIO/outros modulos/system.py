# função chamada system, executa um comando que lhe é passado como uma string.
import os
print("Diretório atual: ", os.listdir())
os.system("mkdir pastaOlaJota")
print("Diretório atual: ", os.listdir())
os.system("rmdir pastaOlaJota")
print("Diretório atual: ", os.listdir())