#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=============================================================================
DEMONSTRAÇÃO: Erros de Quantização e Aliasing em Conversão Analógico-Digital
=============================================================================
Autor: Assistente de IA
Data: 2026
Requisitos: numpy, scipy, matplotlib

Este script ilustra:
1. Erro de quantização em ADCs com diferentes resoluções (bits)
2. Fenômeno de aliasing quando a taxa de amostragem viola Nyquist
3. Efeito de filtros anti-aliasing na reconstrução de sinais
=============================================================================
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.fft import fft, fftfreq
import warnings
warnings.filterwarnings('ignore')

# Configurações de estilo para publicações
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams['font.size'] = 10
plt.rcParams['axes.labelsize'] = 11
plt.rcParams['axes.titlesize'] = 12
plt.rcParams['figure.figsize'] = (14, 10)

# ============================================================================
# SEÇÃO 1: FUNÇÕES AUXILIARES
# ============================================================================

def quantize_signal(analog_signal, n_bits, v_ref=1.0):
    """
    Simula a quantização de um sinal analógico.
    
    Parâmetros:
    -----------
    analog_signal : array
        Sinal de entrada com amplitude entre -v_ref e +v_ref
    n_bits : int
        Resolução do ADC em bits
    v_ref : float
        Tensão de referência do ADC (valor máximo)
    
    Retorna:
    --------
    quantized : array
        Sinal quantizado (valores discretos)
    error : array
        Erro de quantização (analógico - quantizado)
    """
    # Número de níveis de quantização
    n_levels = 2 ** n_bits
    
    # Passo de quantização (LSB - Least Significant Bit)
    q_step = 2 * v_ref / n_levels
    
    # Normaliza para [0, n_levels-1], arredonda, e retorna para escala original
    normalized = (analog_signal + v_ref) / (2 * v_ref) * n_levels
    quantized_levels = np.clip(np.round(normalized), 0, n_levels - 1)
    quantized = quantized_levels * q_step - v_ref + q_step/2
    
    # Calcula erro de quantização
    error = analog_signal - quantized
    
    return quantized, error, q_step


def calculate_sqnr(original, quantized):
    """
    Calcula a Relação Sinal-Ruído de Quantização (SQNR) em dB.
    SQNR = 10 * log10(P_signal / P_noise)
    """
    signal_power = np.mean(original ** 2)
    noise_power = np.mean((original - quantized) ** 2)
    
    if noise_power == 0:
        return np.inf
    
    sqnr_db = 10 * np.log10(signal_power / noise_power)
    return sqnr_db


def plot_frequency_spectrum(time_domain, fs, ax, title, color='blue'):
    """
    Plota o espectro de frequência (FFT) de um sinal.
    """
    n = len(time_domain)
    yf = fft(time_domain)
    xf = fftfreq(n, 1/fs)[:n//2]
    magnitude = 2.0/n * np.abs(yf[0:n//2])
    
    ax.plot(xf, magnitude, color=color, linewidth=1.5)
    ax.set_xlabel('Frequência (Hz)')
    ax.set_ylabel('Magnitude')
    ax.set_title(title)
    ax.grid(True, alpha=0.3)
    ax.set_xlim([0, fs/2])


# ============================================================================
# SEÇÃO 2: DEMONSTRAÇÃO DE ERROS DE QUANTIZAÇÃO
# ============================================================================

def demonstrate_quantization():
    """
    Demonstra como a resolução em bits afeta o erro de quantização.
    """
    print("\n" + "="*70)
    print("DEMONSTRAÇÃO 1: ERROS DE QUANTIZAÇÃO EM ADC")
    print("="*70)
    
    # Parâmetros do sinal analógico
    fs_high = 10000  # Frequência de amostragem muito alta (para simular contínuo)
    f_signal = 50    # Frequência do sinal senoidal (Hz)
    duration = 0.1   # Duração em segundos
    v_ref = 1.0      # Tensão de referência ±1V
    
    t_analog = np.linspace(0, duration, int(fs_high * duration), endpoint=False)
    analog_signal = v_ref * 0.9 * np.sin(2 * np.pi * f_signal * t_analog)
    
    # Diferentes resoluções de ADC para comparação
    bit_resolutions = [3, 5, 8]
    colors = ['red', 'orange', 'green']
    
    # Criar figura com múltiplos subplots
    fig, axes = plt.subplots(3, 2, figsize=(14, 12))
    fig.suptitle('Erros de Quantização em Conversores A/D', fontsize=16, fontweight='bold')
    
    results = []
    
    for idx, (n_bits, color) in enumerate(zip(bit_resolutions, colors)):
        # Quantizar o sinal
        quantized, error, q_step = quantize_signal(analog_signal, n_bits, v_ref)
        sqnr = calculate_sqnr(analog_signal, quantized)
        
        # Teórico: SQNR ≈ 6.02*N + 1.76 dB
        sqnr_theoretical = 6.02 * n_bits + 1.76
        
        results.append({
            'bits': n_bits,
            'q_step': q_step,
            'sqnr_measured': sqnr,
            'sqnr_theoretical': sqnr_theoretical,
            'error': error
        })
        
        print(f"\nADC de {n_bits} bits:")
        print(f"  • Passo de quantização (LSB): {q_step*1000:.3f} mV")
        print(f"  • Níveis discretos: {2**n_bits}")
        print(f"  • SQNR Medido: {sqnr:.2f} dB")
        print(f"  • SQNR Teórico: {sqnr_theoretical:.2f} dB")
        
        # Plot 1: Sinal original vs quantizado (zoom em poucos ciclos)
        ax1 = axes[idx, 0]
        zoom_mask = t_analog < 0.04  # Zoom nos primeiros 40ms
        ax1.plot(t_analog[zoom_mask]*1000, analog_signal[zoom_mask], 
                'k-', linewidth=1, label='Analógico', alpha=0.7)
        ax1.plot(t_analog[zoom_mask]*1000, quantized[zoom_mask], 
                color=color, drawstyle='steps-mid', 
                label=f'{n_bits}-bits Quantizado', linewidth=1.5)
        ax1.set_xlabel('Tempo (ms)')
        ax1.set_ylabel('Tensão (V)')
        ax1.set_title(f'Zoom Temporal - ADC {n_bits} bits')
        ax1.legend(loc='lower right', fontsize=9)
        ax1.grid(True, alpha=0.3)
        
        # Plot 2: Erro de quantização e distribuição
        ax2 = axes[idx, 1]
        ax2.hist(error[zoom_mask], bins=30, density=True, 
                color=color, alpha=0.7, edgecolor='black', linewidth=0.5)
        ax2.axvline(x=-q_step/2, color='red', linestyle='--', linewidth=1, 
                   label='±LSB/2')
        ax2.axvline(x=q_step/2, color='red', linestyle='--', linewidth=1)
        ax2.set_xlabel('Erro de Quantização (V)')
        ax2.set_ylabel('Densidade de Probabilidade')
        ax2.set_title(f'Distribuição do Erro - {n_bits} bits\nSQNR: {sqnr:.1f} dB')
        ax2.legend(fontsize=9)
        ax2.grid(True, alpha=0.3)
    
    # Ajustar layout e exibir
    plt.tight_layout()
    plt.savefig('quantization_errors.png', dpi=150, bbox_inches='tight')
    print(f"\n✓ Gráfico salvo como 'quantization_errors.png'")
    plt.show()
    
    return results


# ============================================================================
# SEÇÃO 3: DEMONSTRAÇÃO DE ALIASING
# ============================================================================

def demonstrate_aliasing():
    """
    Demonstra o fenômeno de aliasing quando fs < 2*f_max.
    """
    print("\n" + "="*70)
    print("DEMONSTRAÇÃO 2: FENÔMENO DE ALIASING")
    print("="*70)
    
    # Parâmetros
    f_signal = 70      # Frequência do sinal (Hz) - ALTA
    fs_nyquist = 2 * f_signal  # Frequência de Nyquist mínima
    fs_adequate = 200  # Taxa de amostragem adequada (> Nyquist)
    fs_inadequate = 80 # Taxa de amostragem inadequada (< Nyquist) -> ALIASING!
    
    duration = 0.5     # 500 ms de sinal
    t_continuous = np.linspace(0, duration, 10000, endpoint=False)
    
    # Sinal analógico original (contínuo)
    original_signal = np.sin(2 * np.pi * f_signal * t_continuous)
    
    # Amostrar com taxa ADEQUADA (sem aliasing)
    t_sampled_ok = np.arange(0, duration, 1/fs_adequate)
    sampled_ok = np.sin(2 * np.pi * f_signal * t_sampled_ok)
    
    # Amostrar com taxa INADEQUADA (com aliasing)
    t_sampled_bad = np.arange(0, duration, 1/fs_inadequate)
    sampled_bad = np.sin(2 * np.pi * f_signal * t_sampled_bad)
    
    # Frequência aparente devido ao aliasing (folding)
    # f_alias = |f_signal - k*fs|, onde k é inteiro que minimiza o resultado
    f_alias = np.abs(f_signal - np.round(f_signal / fs_inadequate) * fs_inadequate)
    aliased_signal = np.sin(2 * np.pi * f_alias * t_continuous)
    
    print(f"\nParâmetros do Sinal:")
    print(f"  • Frequência real do sinal: {f_signal} Hz")
    print(f"  • Frequência de Nyquist mínima: {fs_nyquist} Hz")
    print(f"\nAmostragem ADEQUADA (fs = {fs_adequate} Hz > {fs_nyquist} Hz):")
    print(f"  • Sem aliasing ✓")
    print(f"\nAmostragem INADEQUADA (fs = {fs_inadequate} Hz < {fs_nyquist} Hz):")
    print(f"  • ALIASING DETECTADO! ✗")
    print(f"  • Frequência aparente (folded): {f_alias} Hz")
    
    # Criar figura
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Fenômeno de Aliasing na Amostragem de Sinais', 
                fontsize=16, fontweight='bold')
    
    # Plot 1: Sinal original vs amostragem adequada (domínio do tempo)
    ax1 = axes[0, 0]
    ax1.plot(t_continuous*1000, original_signal, 'k-', linewidth=0.8, 
            label='Sinal Analógico Original', alpha=0.6)
    ax1.stem(t_sampled_ok*1000, sampled_ok, linefmt='g-', markerfmt='go', 
            basefmt=' ', label=f'Amostras (fs={fs_adequate}Hz)', 
            markerlineopts={'markersize': 3})
    ax1.set_xlabel('Tempo (ms)')
    ax1.set_ylabel('Amplitude')
    ax1.set_title('Amostragem Adequada (fs > 2·f_max)')
    ax1.legend(fontsize=9)
    ax1.grid(True, alpha=0.3)
    ax1.set_xlim([0, 100])  # Zoom
    
    # Plot 2: Sinal original vs amostragem com aliasing (domínio do tempo)
    ax2 = axes[0, 1]
    ax2.plot(t_continuous*1000, original_signal, 'k-', linewidth=0.8, 
            label='Sinal Analógico Original (70 Hz)', alpha=0.6)
    ax2.plot(t_continuous*1000, aliased_signal, 'r--', linewidth=1.5, 
            label=f'Sinal Reconstruído ({f_alias} Hz) - ALIASING!')
    ax2.stem(t_sampled_bad*1000, sampled_bad, linefmt='b-', markerfmt='bo', 
            basefmt=' ', label=f'Amostras (fs={fs_inadequate}Hz)', 
            markerlineopts={'markersize': 3}, alpha=0.7)
    ax2.set_xlabel('Tempo (ms)')
    ax2.set_ylabel('Amplitude')
    ax2.set_title('Amostragem Inadequada (fs < 2·f_max) → ALIASING')
    ax2.legend(fontsize=9)
    ax2.grid(True, alpha=0.3)
    ax2.set_xlim([0, 100])
    
    # Plot 3: Espectro de frequência - amostragem adequada
    ax3 = axes[1, 0]
    plot_frequency_spectrum(original_signal, 10000, ax3, 
                           'Espectro do Sinal Original', color='black')
    plot_frequency_spectrum(sampled_ok, fs_adequate, ax3, 
                           f'Espectro Amostras (fs={fs_adequate}Hz)', color='green')
    ax3.axvline(x=f_signal, color='red', linestyle=':', linewidth=1, 
               label=f'f_signal = {f_signal} Hz')
    ax3.axvline(x=fs_adequate/2, color='orange', linestyle='--', linewidth=1, 
               label=f'Nyquist = {fs_adequate/2} Hz')
    ax3.legend(fontsize=8)
    
    # Plot 4: Espectro de frequência - amostragem com aliasing
    ax4 = axes[1, 1]
    plot_frequency_spectrum(original_signal, 10000, ax4, 
                           'Espectro do Sinal Original', color='black',)
    plot_frequency_spectrum(sampled_bad, fs_inadequate, ax4, 
                           f'Espectro Amostras (fs={fs_inadequate}Hz) - ALIASING', 
                           color='blue')
    ax4.axvline(x=f_signal, color='red', linestyle=':', linewidth=1, 
               label=f'f_real = {f_signal} Hz')
    ax4.axvline(x=f_alias, color='red', linestyle='-.', linewidth=2, 
               label=f'f_alias = {f_alias} Hz (aparente)')
    ax4.axvline(x=fs_inadequate/2, color='orange', linestyle='--', linewidth=1, 
               label=f'Nyquist = {fs_inadequate/2} Hz')
    ax4.legend(fontsize=8)
    
    plt.tight_layout()
    plt.savefig('aliasing_demonstration.png', dpi=150, bbox_inches='tight')
    print(f"\n✓ Gráfico salvo como 'aliasing_demonstration.png'")
    plt.show()


# ============================================================================
# SEÇÃO 4: EFEITO DE FILTRO ANTI-ALIASING
# ============================================================================

def demonstrate_anti_aliasing_filter():
    """
    Demonstra como um filtro anti-aliasing preserva a integridade do sinal.
    """
    print("\n" + "="*70)
    print("DEMONSTRAÇÃO 3: FILTRO ANTI-ALIASING")
    print("="*70)
    
    # Parâmetros
    fs = 1000          # Taxa de amostragem: 1 kHz
    f_nyquist = fs/2   # 500 Hz
    duration = 0.1     # 100 ms
    
    # Criar sinal composto: componentes dentro e fora da banda de Nyquist
    t = np.linspace(0, duration, int(fs*duration), endpoint=False)
    
    # Componentes de frequência
    f1, f2, f3 = 100, 300, 700  # Hz (f3 > f_nyquist!)
    signal_composite = (0.5 * np.sin(2*np.pi*f1*t) + 
                       0.3 * np.sin(2*np.pi*f2*t) + 
                       0.2 * np.sin(2*np.pi*f3*t))
    
    # Projetar filtro passa-baixas Butterworth (ordem 5, cutoff em 0.9*f_nyquist)
    cutoff = 0.9 * f_nyquist  # 450 Hz
    sos = signal.butter(5, cutoff, fs=fs, btype='low', output='sos')
    signal_filtered = signal.sosfilt(sos, signal_composite)
    
    # Amostrar (simular ADC)
    samples_original = signal_composite[::10]  # Subamostragem para visualização
    samples_filtered = signal_filtered[::10]
    t_samples = t[::10]
    
    print(f"\nSinal Composto:")
    print(f"  • f₁ = {f1} Hz (dentro da banda) ✓")
    print(f"  • f₂ = {f2} Hz (dentro da banda) ✓")
    print(f"  • f₃ = {f3} Hz (ACIMA de Nyquist={f_nyquist} Hz) ✗ → Causa aliasing")
    print(f"\nFiltro Anti-Aliasing:")
    print(f"  • Tipo: Butterworth 5ª ordem")
    print(f"  • Frequência de corte: {cutoff} Hz")
    print(f"  • Atenuação em {f3} Hz: ~{20*np.log10(1/np.sqrt(1+(f3/cutoff)**(2*5))):.1f} dB")
    
    # Criar figura
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('Efeito do Filtro Anti-Aliasing', fontsize=16, fontweight='bold')
    
    # Plot 1: Sinal no tempo (com e sem filtro)
    ax1 = axes[0, 0]
    ax1.plot(t*1000, signal_composite, 'k-', linewidth=0.8, alpha=0.6, label='Original')
    ax1.plot(t*1000, signal_filtered, 'b-', linewidth=1.5, label='Com Filtro Anti-Aliasing')
    ax1.set_xlabel('Tempo (ms)')
    ax1.set_ylabel('Amplitude')
    ax1.set_title('Sinal no Domínio do Tempo')
    ax1.legend(fontsize=9)
    ax1.grid(True, alpha=0.3)
    ax1.set_xlim([0, 30])
    
    # Plot 2: Espectro de frequência (com e sem filtro)
    ax2 = axes[0, 1]
    plot_frequency_spectrum(signal_composite, fs, ax2, 'Espectro Original', color='black')
    plot_frequency_spectrum(signal_filtered, fs, ax2, 'Espectro Filtrado', color='blue')
    ax2.axvline(x=f_nyquist, color='red', linestyle='--', linewidth=1.5, 
               label=f'Nyquist = {f_nyquist} Hz')
    ax2.axvline(x=cutoff, color='orange', linestyle=':', linewidth=1, 
               label=f'Cutoff = {cutoff} Hz')
    ax2.set_title('Espectro de Frequência')
    ax2.legend(fontsize=9)
    ax2.set_xlim([0, fs/2])
    
    # Plot 3: Amostragem SEM filtro → aliasing visível
    ax3 = axes[1, 0]
    ax3.plot(t*1000, signal_composite, 'k-', linewidth=0.5, alpha=0.4)
    ax3.stem(t_samples*1000, samples_original, linefmt='r-', markerfmt='ro', 
            basefmt=' ', label='Amostras (SEM filtro)', markerlineopts={'markersize': 2})
    ax3.set_xlabel('Tempo (ms)')
    ax3.set_ylabel('Amplitude')
    ax3.set_title('Amostragem SEM Filtro → Aliasing de f₃=700Hz')
    ax3.legend(fontsize=9)
    ax3.grid(True, alpha=0.3)
    ax3.set_xlim([0, 30])
    
    # Plot 4: Amostragem COM filtro → sinal preservado
    ax4 = axes[1, 1]
    ax4.plot(t*1000, signal_filtered, 'b-', linewidth=1, alpha=0.7)
    ax4.stem(t_samples*1000, samples_filtered, linefmt='g-', markerfmt='go', 
            basefmt=' ', label='Amostras (COM filtro)', markerlineopts={'markersize': 2})
    ax4.set_xlabel('Tempo (ms)')
    ax4.set_ylabel('Amplitude')
    ax4.set_title('Amostragem COM Filtro → Sem Aliasing')
    ax4.legend(fontsize=9)
    ax4.grid(True, alpha=0.3)
    ax4.set_xlim([0, 30])
    
    plt.tight_layout()
    plt.savefig('anti_aliasing_filter.png', dpi=150, bbox_inches='tight')
    print(f"\n✓ Gráfico salvo como 'anti_aliasing_filter.png'")
    plt.show()


# ============================================================================
# SEÇÃO 5: ANÁLISE COMPARATIVA SQNR vs BITS
# ============================================================================

def analyze_sqnr_vs_bits():
    """
    Analisa teoricamente e experimentalmente a relação SQNR vs resolução em bits.
    """
    print("\n" + "="*70)
    print("ANÁLISE: SQNR Teórico vs Medido em Função da Resolução")
    print("="*70)
    
    # Gerar dados
    bit_range = np.arange(1, 17)  # 1 a 16 bits
    sqnr_theoretical = 6.02 * bit_range + 1.76
    
    # Simular medições experimentais (com pequeno ruído adicional)
    fs = 10000
    f_signal = 100
    t = np.linspace(0, 0.05, int(fs*0.05), endpoint=False)
    analog = 0.9 * np.sin(2*np.pi*f_signal*t)
    
    sqnr_measured = []
    for n_bits in bit_range:
        quant, _, _ = quantize_signal(analog, n_bits)
        sqnr_measured.append(calculate_sqnr(analog, quant))
    
    # Plot
    plt.figure(figsize=(10, 6))
    plt.plot(bit_range, sqnr_theoretical, 'b-', linewidth=2, 
            label='Teórico: SQNR = 6.02·N + 1.76 dB')
    plt.plot(bit_range, sqnr_measured, 'ro-', markersize=4, linewidth=1.5, 
            label='Medido (Simulação)')
    plt.xlabel('Resolução do ADC (bits)')
    plt.ylabel('SQNR (dB)')
    plt.title('Relação SQNR vs Resolução em Bits')
    plt.grid(True, alpha=0.3, which='both')
    plt.legend(fontsize=10)
    
    # Anotar pontos importantes
    for bits, sqnr in [(8, 6.02*8+1.76), (12, 6.02*12+1.76), (16, 6.02*16+1.76)]:
        plt.annotate(f'{bits}b: ~{sqnr:.0f}dB', 
                    xy=(bits, sqnr), xytext=(bits+1, sqnr-5),
                    arrowprops=dict(arrowstyle='->', color='gray'),
                    fontsize=9, color='darkblue')
    
    plt.tight_layout()
    plt.savefig('sqnr_vs_bits.png', dpi=150, bbox_inches='tight')
    print(f"\n✓ Gráfico salvo como 'sqnr_vs_bits.png'")
    plt.show()
    
    # Tabela resumo
    print("\n" + "-"*50)
    print(f"{'Bits':<6} {'SQNR Teórico (dB)':<20} {'Aplicação Típica'}")
    print("-"*50)
    applications = {
        8: "Áudio básico, sensores simples",
        12: "Instrumentação industrial, áudio consumer",
        16: "Áudio profissional (CD), aquisição de dados",
        24: "Áudio de alta resolução, instrumentação científica"
    }
    for bits in [8, 12, 16, 24]:
        if bits <= 16:  # Só plotamos até 16
            sqnr = 6.02*bits + 1.76
            print(f"{bits:<6} {sqnr:<20.1f} {applications[bits]}")
    print("-"*50)


# ============================================================================
# FUNÇÃO PRINCIPAL
# ============================================================================

def main():
    """
    Executa todas as demonstrações.
    """
    print("\n" + "#"*70)
    print("# CONVERSÃO ANALÓGICO-DIGITAL: QUANTIZAÇÃO E ALIASING")
    print("#"*70)
    print("\nEste script demonstra conceitos fundamentais de processamento de sinais:")
    print("  1. Erros de quantização em ADCs de diferentes resoluções")
    print("  2. Fenômeno de aliasing quando fs < 2·f_max")
    print("  3. Importância de filtros anti-aliasing")
    print("  4. Relação teórica SQNR = 6.02·N + 1.76 dB")
    
    # Executar demonstrações
    demonstrate_quantization()
    demonstrate_aliasing()
    demonstrate_anti_aliasing_filter()
    analyze_sqnr_vs_bits()
    
    print("\n" + "#"*70)
    print("# CONCLUSÕES PRINCIPAIS")
    print("#"*70)
    print("""
✓ QUANTIZAÇÃO:
  • Cada bit adicional melhora o SQNR em ~6 dB
  • Erro de quantização é modelado como ruído branco uniforme em [-LSB/2, +LSB/2]
  • ADCs de 16 bits oferecem ~98 dB de dinâmica (adequado para áudio profissional)

✓ ALIASING:
  • Ocorre quando fs < 2·f_max (violação do Teorema de Nyquist-Shannon)
  • Frequências acima de fs/2 são "dobradas" para dentro da banda base
  • Irreversível: uma vez amostrado com aliasing, a informação original é perdida

✓ FILTROS ANTI-ALIASING:
  • Devem ser ANALÓGICOS, aplicados ANTES do ADC
  • Atenuam componentes acima de fs/2 para prevenir aliasing
  • Compromisso: ordem do filtro vs fase linear vs custo

✓ BOAS PRÁTICAS:
  • Use fs ≥ 2.2·f_max para permitir transição do filtro anti-aliasing
  • Escolha resolução (bits) baseada na dinâmica do sinal e SQNR requerido
  • Considere oversampling + decimação para melhorar SQNR efetivo
    """)
    
    print("\nTodos os gráficos foram salvos como arquivos PNG no diretório atual.")
    print("Execute este script em um ambiente com matplotlib para visualização interativa.\n")


if __name__ == "__main__":
    main()