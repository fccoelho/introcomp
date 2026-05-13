Aqui está a explicação completa em português, mantendo o mesmo nível técnico e estrutura:

### 🔑 Resposta Rápida
Em Python (e na maioria das linguagens modernas), o operador de negação bit a bit `~` segue esta regra matemática:
```python
~x = -(x + 1)
```
Portanto: `~1234 = -(1234 + 1) = -1235`.

Mas para entender **por quê** isso acontece no nível binário, precisamos ver como os computadores representam números inteiros negativos: o sistema de **Complemento de Dois**.

---

### 🔍 Passo a Passo em Nível Binário

#### Passo 1: Converter `1234` para binário
```
1234₁₀ = 10011010010₂
```
Para facilitar a visualização, vamos completar com zeros à esquerda até 16 bits (o Python não tem limite fixo, mas isso ajuda a enxergar o padrão):
```
0000 0100 1101 0010  ← 1234 em binário (16 bits)
```

#### Passo 2: Aplicar o NOT bit a bit (`~`)
O operador `~` inverte **todos** os bits: `0 → 1` e `1 → 0`.
```
Original:  0000 0100 1101 0010
Invertido: 1111 1011 0010 1101
```

#### Passo 3: Interpretar o resultado como número negativo
No sistema de **Complemento de Dois**, se o bit mais à esquerda (MSB) for `1`, o número é negativo. Para descobrir seu valor decimal, fazemos o processo inverso:
1. Invertemos todos os bits novamente
2. Somamos `1`
3. Aplicamos o sinal negativo

Aplicando ao nosso resultado invertido:
```
Invertido:   1111 1011 0010 1101
Inverte:     0000 0100 1101 0010
Soma 1:      0000 0100 1101 0011  ← Isso vale 1235 em decimal
Aplica `-`: -1235
```

✅ Resultado final: `-1235`

---

### 🐍 Por que o Python se comporta assim?
Diferente de C ou Java, o Python usa **inteiros de precisão arbitrária**. Isso significa que os números não ficam presos a 32 ou 64 bits. Conceitualmente:
- `1234` é armazenado com **infinitos zeros à esquerda**:  
  `...0000000010011010010`
- `~1234` inverte **todos** eles, criando **infinitos uns à esquerda**:  
  `...1111111101100101101`

No sistema de Complemento de Dois, uma sequência infinita de `1`s à esquerda é exatamente a representação de um número negativo. É daí que nasce naturalmente a fórmula `~x = -(x + 1)` para qualquer inteiro.

### 💡 Tabela Resumo
| Operação | Binário (visão 16 bits) | Decimal |
|----------|-------------------------|---------|
| `x`      | `0000 0100 1101 0010`   | `1234`  |
| `~x`     | `1111 1011 0010 1101`   | `-1235` |

Esse comportamento é padrão em praticamente todas as linguagens que usam inteiros sinalizados no formato de Complemento de Dois. Se quiser ver como outros operadores (`&`, `|`, `^`, `<<`, `>>`) funcionam no mesmo nível, é só pedir!