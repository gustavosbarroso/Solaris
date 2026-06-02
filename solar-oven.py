# Imports
import numpy as np
import matplotlib.pyplot as plt

# ==================================================
# Constantes físicas
# ==================================================

sigma = 5.670374419e-8      # Stefan-Boltzmann (W/m².K⁴)

m1 = 0.243                  # massa (kg)
c1 = 900                    # calor específico (J/kg.K)

tau = 0.95                 # transmitância
A1 = 0.0660                # área (m²)
alpha = 0.90               # absortância
kappa = 1.0                # fator de concentração

G = 1362                   # irradiância solar (W/m²)

epsilon = 0.90            # emissividade
h_conv = 2.0              # coeficiente convectivo (W/m².K)

# ==================================================
# Funções dependentes do tempo
# ==================================================

def Tamb(t):
    """
    Temperatura ambiente (K)
    """
    return 293.15 + 5*np.sin(2*np.pi*t/86400)


def phi(t):
    """
    Ângulo de incidência solar (rad)
    """
    return np.pi/6


# ==================================================
# EDO
# ==================================================

def f(T, t):

    termo_solar = ( tau*A1*alpha*kappa*G*np.cos(phi(t)))

    termo_radiacao = ( -tau*epsilon*A1*sigma* (T**4 - Tamb(t)**4))

    termo_conveccao = (h_conv*A1*(Tamb(t) - T))

    dTdt = ( termo_solar+ termo_radiacao + termo_conveccao)/(m1*c1)

    return dTdt


# ==================================================
# Parâmetros do RK4
# ==================================================

a = 0                    # s
b = 4*3600               # 4 horas

N = 1000

h = (b-a)/N

tpontos = np.arange(a, b, h)

Tpontos = []

# ==================================================
# Condição inicial
# ==================================================

T = 293.15      # 20°C

# ==================================================
# Integração RK4
# ==================================================

for t in tpontos:

    Tpontos.append(T)

    k1 = h*f(T, t)

    k2 = h*f(T + 0.5*k1,t + 0.5*h)

    k3 = h*f(T + 0.5*k2,t + 0.5*h)

    k4 = h*f(T + k3, t + h )

    T += (k1 + 2*k2 + 2*k3 + k4)/6


# ==================================================
# Conversão para Celsius
# ==================================================

Tpontos = np.array(Tpontos)

Tpontos_C = Tpontos - 273.15


# ==================================================
# Plot
# ==================================================

plt.figure(figsize=(8,5))

plt.plot(tpontos/3600, Tpontos_C,lw=2,label="Temperatura do sistema")

plt.axhline( 60,linestyle="--",label="60 °C")

plt.axhline(100, linestyle=":",label="100 °C")

plt.xlabel("Tempo (h)")
plt.ylabel("Temperatura (°C)")
plt.title("Forno Solar - Evolução da Temperatura")
plt.grid(True)
plt.legend()

plt.show()
