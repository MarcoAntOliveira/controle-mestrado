import sympy as sp
from sympy.printing.dot import dotprint
from graphviz import Source
import os
# Variáveis
s = sp.symbols('s')
Kp, Ki = sp.symbols('Kp Ki')

# Exemplo: controlador PI em domínio de Laplace
Gc = Kp + Ki/s

# Planta (1ª ordem)
G = 1 / (s + 1)

# Malha fechada
T = (Gc * G) / (1 + Gc * G)

sp.pretty_print(T)

# Gera o grafo em formato DOT (Graphviz)
dot = dotprint(T)

# Renderiza a imagem
# Caminho absoluto do script atual
output_path = os.path.join(os.path.dirname(__file__), "diagrama")

# Gera e renderiza o PNG
src = Source(dot, filename=output_path, format="png")
src.render(cleanup=True)  # Gera diagrama.png

# Abre automaticamente o arquivo (Linux)
os.system(f"xdg-open {output_path}.png")

