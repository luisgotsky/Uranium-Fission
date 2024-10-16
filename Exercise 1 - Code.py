# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 11:14:25 2024

@author: Luis Lucas García
"""
import matplotlib.pyplot as plt
import numpy as np
"""
The first part of the code is setting up a calculation for the binding energy.
We will then set up some plots for the uranium isotopes, this is direct using
the formula.
"""

def B(Z, A):
    
    if A%2 != 0: d = 0
    elif Z%2 != 0: d = -11.2/np.sqrt(A)
    else: d = 11.2/np.sqrt(A)
    
    aV = 15.8
    aS = 18.3
    aC = 0.714
    aA = 23.2
    B = aV*A - aS*A**(2/3) - (aC*Z**2)/(A**(1/3)) - (aA*(A-2*Z)**2)/A + d
    
    return B

#Uranium has Z = 92, we will calculate binding energy per nucleon for A = 235, 238

B1 = B(92, 235)/235
B2 = B(92, 238)/238

print("Uranium-235 has a binding energy per nucleon of", B1, 
      "MeV, and Uranium-238 of", B2, "MeV")

#Now, let's plot the binding energy per nucleon of some uranium isotopes

A = np.arange(200, 250, 1)
Bs = [B(92, i)/i for i in A]

plt.figure()
plt.xlabel("A")
plt.ylabel("$\\frac{B}{A} (MeV)$")
plt.grid()
plt.title("Uranium isotopes")
plt.scatter(A, Bs)
plt.scatter(235, B(92, 235)/235, label="Uranium-235")
plt.scatter(238, B(92, 238)/238, label="Uranium-238")
plt.legend()
plt.savefig("Images\\Uranium Isotopes.png", dpi=200)

#From this graph it can be seen that Uranium-235 is more stable

"""
For this next part we have to analyze the nuclear fission of Uranium-238. This
is a nuclear reaction in which U-238 -> Kr-92 + Ba-141.

First we will begin by calculating the total binding energy of products
and the reactant.
"""

BR = B(92, 238)
BP2 = B(36, 92)
BP3 = B(56, 141)

print("The total binding energy for Uranium-238 is", BR, "MeV, for Krypton-92 is",
      BP2, "MeV and for Barium-141 is", BP3, "MeV")

#Next, we calculate the energy this reaction would release

Er = BP2 + BP3 - BR

print("The total energy released in the fission of one Uranium-238 nuclei is", Er,
      "MeV")

#Since the reaction produces energy fission is feasible

Zs = np.arange(1, 238, 1)
Bs = [B(i, 2*i)/(2*i) for i in Zs]

plt.figure()
plt.grid()
plt.xlabel("Z")
plt.ylabel("$\\frac{B}{A} (MeV)$")
plt.scatter(Zs, Bs)
plt.title("Binding energy for nuclei verifying $A = 2Z$")
plt.plot([Zs[25], Zs[25]], [min(Bs), max(Bs)], "--", label="Fe-52", color="orange")
plt.legend()
plt.savefig("Images\\Bounding energy.png", dpi=200)

#From this graph one understands that heavy nuclei decomposes into lighter nuclei
#with higher binding energy, with means a more stable nuclei.

nuclei = ["U-238", "Kr-92", "Ba-141", "All products", "Energy released"]
energy = [BR, BP2, BP3, BP2+BP3, BP2+BP3-BR]

plt.figure(figsize=(9, 6))
plt.grid()
plt.xlabel("Nuclei")
plt.ylabel("B (MeV)")
plt.bar(nuclei, energy)
plt.title("Energy released for each product")
plt.savefig("Images\\Fission energy.png", dpi=200)

#The relative energy released

R = Er/BR

print("The energy released is", R, "times the binding energy of Uranium-238")

R2 = (2*B(0, 1) + B(56, 144) + B(36, 89) - B(92, 235))/B(92, 235)

print("The energy released is", R2, "times the binding energy of Uranium-235")

plt.show()