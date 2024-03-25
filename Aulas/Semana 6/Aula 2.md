# Convertendo de Analógico para Digital
Sinais analógicos são sinais que variam continuamente no tempo. Sinais digitais são sinais que variam discretamente no tempo. A conversão de um sinal analógico para um sinal digital é chamada de conversão analógico-digital (A/D). A conversão de um sinal digital para um sinal analógico é chamada de conversão digital-analógico (D/A).

## Conversão A/D
A conversão A/D é realizada em três etapas: amostragem, quantização e codificação.

### Amostragem
A amostragem é o processo de capturar o valor do sinal analógico em intervalos regulares de tempo. O teorema de Nyquist estabelece que a taxa de amostragem deve ser pelo menos o dobro da maior frequência presente no sinal analógico. Caso contrário, ocorre o fenômeno de aliasing, que distorce o sinal digitalizado.

#### Teorema de Nyquist
O teorema de Nyquist estabelece que a taxa de amostragem deve ser pelo menos o dobro da maior frequência presente no sinal analógico. Caso contrário, ocorre o fenômeno de aliasing, que distorce o sinal digitalizado.


#### Exemplo
Considere um sinal analógico com frequência máxima de 4 kHz. A taxa de amostragem mínima para evitar o aliasing é de 8 kHz.

```python
import numpy as np
import matplotlib.pyplot as plt
fs = 8000
t = np.arange(0, 1, 1/fs)
x = np.sin(2*np.pi*4000*t)
plt.plot(t, x)
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.title('Sinal analógico')
plt.show()
```


### Quantização

A quantização é o processo de mapear os valores amostrados para um conjunto finito de valores discretos. A resolução da quantização é o número de bits utilizados para representar cada amostra. Quanto maior a resolução, maior a fidelidade da representação digital em relação ao sinal analógico.

#### Exemplo
Considere um sinal analógico com amplitude máxima de 5 V. A resolução da quantização é de 4 bits. O intervalo de quantização é de 5 V / 2^4 = 0.3125 V.

```python
import numpy as np
import matplotlib.pyplot as plt
fs = 8000
amplitude = 5
bits = 4
resolucao = amplitude / (2**bits)
t = np.arange(0, 1, 1/fs)
x = amplitude*np.sin(2*np.pi*3800*t)
xq = (np.floor(x/resolucao))*resolucao
plt.plot(t, x, label='Sinal analógico')
plt.stem(t, xq, linefmt='r-', markerfmt='ro', basefmt='r-', label='Sinal quantizado')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.show()
```

### Codificação
A codificação é o processo de representar os valores quantizados em formato digital. A codificação mais comum é a codificação binária, que utiliza apenas dois níveis de tensão para representar os valores quantizados.

#### Exemplo
Considere um sinal quantizado com resolução de 8 bits. A codificação binária utiliza 8 bits para representar cada amostra.

```python
import numpy as np
import matplotlib.pyplot as plt
fs = 8000
t = np.arange(0, 1, 1/fs)
x = 5*np.sin(2*np.pi*3500*t)
xq = np.round(x/0.01953)*0.01953
xb = np.unpackbits(xq.astype(np.uint8))
plt.stem(xb, linefmt='r-', markerfmt='r*', basefmt='r-')
plt.xlabel('Tempo (s)')
plt.ylabel('Amample')
plt.title('Sinal codificado')
plt.show()
```
## Conversão D/A
A conversão D/A é realizada em duas etapas: decodificação e reconstrução.
### Decodificação
A decodificação é o processo de converter os valores codificados em valores quantizados.
#### Exemplo
Considere um sinal codificado com resolução de 8 bits. A decodificação é realizada convertendo os valores binários para valores quantizados.

```python
import numpy as np
import matplotlib.pyplot as plt
fs = 8000
t = np.arange(0, 1, 1/fs)
x = 5*np.sin(2*np.pi*4000*t)
xq = np.round(x/0.01953)*0.01953
xb = np.unpackbits(xq.astype(np.uint8))
xq = xb*0.01953
plt.stem(t, xq, linefmt='r-', markerfmt='ro', basefmt='r-')
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.title('Sinal quantizado')
plt.show()
```
### Reconstrução
A reconstrução é o processo de converter os valores quantizados em um sinal analógico.
#### Exemplo
Considere um sinal quantizado com resolução de 8 bits. A reconstrução é realizada convertendo os valores quantizados para valores analógicos.

```python
import numpy as np
import matplotlib.pyplot as plt
fs = 8000
t = np.arange(0, 1, 1/fs)
x = 5*np.sin(2*np.pi*4000*t)
xq = np.round(x/0.01953)*0.01953
plt.plot(t, xq)
plt.xlabel('Tempo (s)')
plt.ylabel('Amplitude')
plt.title('Sinal reconstruído')
plt.show()
```

