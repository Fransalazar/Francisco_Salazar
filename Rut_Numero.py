aclNum1 = int(input("Ingresar número de VLAN a crear en SW1: "))

# Números de VLAN ya creados en SW1
vlans_creadas_sw1 = [99, 10, 20, 30]

if aclNum1 in vlans_creadas_sw1:
    print("Esta VLAN ya está creada en SW1, favor indicar otra.")
elif aclNum1 >= 1 and aclNum1 < 99:
    print("VLAN permitida, además es una VLAN estándar IPv4.")
else:
    print("Número de VLAN no válido en SW1.")



aclNum2 = int(input("Ingresar número de VLAN a crear en SW2: "))

# Números de VLAN ya creados en SW2
vlans_creadas_sw2 = [200, 40, 50, 60]

if aclNum0 in vlans_creadas_sw2:
    print("Esta VLAN ya está creada en SW2, favor indicar otra.")
elif aclNum2 >= 1 and aclNum2 < 99:
    print("VLAN permitida, además es una VLAN extendida IPv4.")
else:
    print("Número de VLAN no válido en SW2.")

