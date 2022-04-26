import textwrap
import random
from os import path

data = path.join(path.dirname(__file__), "data")
cantadastxt = path.join(data, "cantadas.txt")
  
def text(Cantada=""):
    cantada = textwrap.indent(text=Cantada, prefix='💘 ')
    print("\n")
    print(cantada)

def main():
    with open(cantadastxt, encoding='utf8') as cantadas:
        text(random.choice(cantadas.readlines()))