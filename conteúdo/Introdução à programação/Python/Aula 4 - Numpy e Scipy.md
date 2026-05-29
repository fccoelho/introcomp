# 📘 Introdução ao NumPy e SciPy para Ciência de Dados

### 1. Numpy

#### ✅ 1.1 Instalação e Importação
```python
# No terminal ou célula do notebook
# !pip install numpy scipy

import numpy as np
```

#### ✅ 1.2 Criação de Arrays
```python
a = np.array([1, 2, 3, 4])               # 1D
b = np.array([[1, 2], [3, 4]])           # 2D
c = np.zeros((3, 4), dtype=np.float32)   # Matriz de zeros
d = np.ones(5)                           # Vetor de uns
e = np.arange(0, 10, 2)                  # [0, 2, 4, 6, 8]
f = np.linspace(0, 1, 5)                 # [0. , 0.25, 0.5 , 0.75, 1. ]

# Boa prática moderna para aleatórios
rng = np.random.default_rng(seed=42)
g = rng.random((3, 3))                   # Uniforme [0,1)
h = rng.normal(loc=0, scale=1, size=100) # Normal(0,1)
```

#### ✅ 1.3 Atributos e Tipos
```python
print(b.shape)   # (2, 2)
print(b.ndim)    # 2
print(b.dtype)   # int64
print(b.size)    # 4
```

#### ✅ 1.4 Indexação, Slicing e Máscaras Booleanas
```python
mat = np.arange(1, 10).reshape(3, 3)
print(mat[0, :])      # Primeira linha
print(mat[:, -1])     # Última coluna
print(mat[mat > 5])   # [6, 7, 8, 9]
mat[mat % 2 == 0] = 0 # Substitui pares por 0
```

#### ✅ 1.5 Operações Vetoriais e Broadcasting
```python
x = np.array([1, 2, 3])
y = np.array([10, 20, 30])
print(x + y)          # [11 22 33]
print(x * y)          # [10 40 90]

# Broadcasting: vetor (3,) + matriz (3,2)
A = np.arange(6).reshape(3, 2)
v = np.array([10, 20])
print(A + v)  # Soma v a cada linha
```

#### ✅ 1.6 Agregação e Eixos (`axis`)
```python
dados = rng.normal(loc=50, scale=10, size=(100, 4)) # Simula 4 métricas para 100 amostras
print(dados.mean())          # Média global
print(dados.mean(axis=0))    # Média por coluna (por métrica)
print(dados.std(axis=1)[:5]) # Desvio padrão das 5 primeiras amostras
print(dados.max(axis=0))     # Valor máximo por coluna
```

### 🔹 2. SciPy: Ferramentas Científicas

```python
import scipy.stats as stats
import scipy.optimize as opt
import scipy.linalg as linalg
import scipy.integrate as integrate
```

#### ✅ 2.1 Estatística (`scipy.stats`)
```python
# Teste t para duas amostras independentes
grupo_a = rng.normal(10, 2, 50)
grupo_b = rng.normal(11.5, 2, 50)
t_stat, p_val = stats.ttest_ind(grupo_a, grupo_b)
print(f"t={t_stat:.3f}, p={p_val:.4f}")

# Ajuste a distribuição normal
params = stats.norm.fit(grupo_a)
print(f"μ={params[0]:.2f}, σ={params[1]:.2f}")
```

#### ✅ 2.2 Otimização (`scipy.optimize`)
```python
def custo(x):
    return (x[0] - 3)**2 + (x[1] + 1)**2  # Mínimo em (3, -1)

res = opt.minimize(custo, x0=[0, 0])
print(f"Ótimo: {res.x}, Valor: {res.fun:.4f}, Sucesso: {res.success}")
```

#### ✅ 2.3 Álgebra Linear (`scipy.linalg`)
```python
# Sistema linear Ax = b
A = np.array([[2, 1], [1, 3]])
b = np.array([5, 7])
x = linalg.solve(A, b)
print(f"Solução: {x}")

# Autovalores e autovetores
vals, vecs = linalg.eig(A)
print(f"Autovalores: {vals}")
```


---

## 🧩 4. Exercícios

### 🔸 Exercício 1: Pré-processamento de Features
Crie um array 2D `X` com 200 linhas e 5 colunas contendo dados simulados de 5 sensores (`rng.normal(loc=10, scale=3, size=(200,5))`).
1. Normalize cada coluna para média 0 e desvio padrão 1 **manualmente** (use `axis`).
2. Substitua valores outliers (acima de 2.5 desvios padrão da coluna) por `np.nan`.
3. Calcule a média de cada coluna ignorando os `NaN`.

### 🔸 Exercício 2: Teste de Hipótese com Dados Reais
Simule duas campanhas de marketing:
- Campanha A: taxa de conversão ~ 12%, 500 usuários.
- Campanha B: taxa de conversão ~ 15%, 500 usuários.
1. Gere vetores binários (0/1) representando conversões.
2. Use `scipy.stats.proportions_ztest` ou `ttest_ind` para testar se B é estatisticamente melhor que A (α=0.05).
3. Imprima o p-valor e a conclusão.

### 🔸 Exercício 3: Ajuste de Curva e Otimização
Dados experimentais: `x = np.linspace(0, 10, 20)`, `y = 2.5*x + 1.2 + noise` (noise ~ N(0, 1)).
1. Use `scipy.optimize.curve_fit` para ajustar `y = a*x + b`.
2. Compare os coeficientes encontrados com os reais.
3. Calcule o RMSE do ajuste.

---

## ✅ Gabarito / Soluções

<details>
<summary><b>Exercício 1</b></summary>

```python
X = rng.normal(loc=10, scale=3, size=(200, 5))

# 1. Normalização manual
mean = X.mean(axis=0)
std = X.std(axis=0)
X_norm = (X - mean) / std

# 2. Outliers > 2.5 std
mask = np.abs(X_norm) > 2.5
X_clean = np.where(mask, np.nan, X_norm)

# 3. Média ignorando NaN
print("Médias por coluna:", np.nanmean(X_clean, axis=0))
```
</details>

<details>
<summary><b>Exercício 2</b></summary>

```python
camp_a = rng.binomial(1, 0.12, 500)
camp_b = rng.binomial(1, 0.15, 500)

t, p = stats.ttest_ind(camp_b, camp_a, alternative='greater')
print(f"p-valor: {p:.4f}")
if p < 0.05:
    print("Rejeitamos H0: Campanha B é estatisticamente superior.")
else:
    print("Falhamos em rejeitar H0: Sem evidência de superioridade.")
```
*Nota:* `proportions_ztest` também é válido, mas exige `statsmodels`. `ttest_ind` é puramente SciPy e adequado para demonstração.
</details>

<details>
<summary><b>Exercício 3</b></summary>

```python
x = np.linspace(0, 10, 20)
y_true = 2.5 * x + 1.2
y_obs = y_true + rng.normal(0, 1, size=20)

def linear(x, a, b):
    return a * x + b

popt, pcov = opt.curve_fit(linear, x, y_obs)
a_fit, b_fit = popt

y_pred = linear(x, a_fit, b_fit)
rmse = np.sqrt(np.mean((y_obs - y_pred)**2))

print(f"a={a_fit:.3f}, b={b_fit:.3f}, RMSE={rmse:.3f}")
```
</details>

