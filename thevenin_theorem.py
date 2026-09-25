# Python Program to Calculate Thevenin's Theorem
# Electrical Engineering - Network Analysis

print("==============================================")
print("          THEVENIN'S THEOREM")
print("==============================================")

# Input values
V = float(input("Enter source voltage V (V): "))
R1 = float(input("Enter R1 (ohm): "))
R2 = float(input("Enter R2 (ohm): "))
RL = float(input("Enter load resistance RL (ohm): "))

# ------------------------------------------------
# Step 1: Calculate Thevenin Voltage
# ------------------------------------------------
# Open-circuit voltage across the load

Vth = V * R2 / (R1 + R2)

# ------------------------------------------------
# Step 2: Calculate Thevenin Resistance
# ------------------------------------------------
# Voltage source is replaced by a short circuit

Rth = (R1 * R2) / (R1 + R2)

# ------------------------------------------------
# Step 3: Calculate Load Current
# ------------------------------------------------

IL = Vth / (Rth + RL)

# ------------------------------------------------
# Step 4: Calculate Load Voltage
# ------------------------------------------------

VL = IL * RL

# Display results
print("\n------------- RESULTS ----------------")
print(f"Thevenin Voltage (Vth) = {Vth:.2f} V")
print(f"Thevenin Resistance (Rth) = {Rth:.2f} ohm")
print(f"Load Current (IL) = {IL:.4f} A")
print(f"Load Voltage (VL) = {VL:.2f} V")
print("--------------------------------------")
print("Thevenin Equivalent Circuit Calculated")
print("======================================")
