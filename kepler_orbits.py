import math
G = 6.674e-11
M_earth = 5.972e24
R_earth = 6371
print("="*50)
print(" KEPLER ORBITAL PERIOD CALCULATOR ")
print("Based on Kepler's Third Law: T = 2π × √(a³/GM)")
print("="*50)


print("\nChoose orbit type:")
print("1. Circular orbit (one altitude)")
print("2. Elliptical orbit - Kepler (perigee and apogee)")

option = input("\nOption (1 or 2): ")
if option== "1":
    altitude = float(input("\nAltitude above surface (km): "))
    a = R_earth + altitude
elif option == "2":
    print("\nEnter orbit points:")
    perigee = float(input("Perigee - CLOSEST point (km): "))
    apogee = float(input("Apogee - FARTHEST point (km): "))

    r_perigee = R_earth + perigee
    r_apogee = R_earth + apogee
    a = (r_perigee + r_apogee) / 2
    e = (r_apogee - r_perigee) / (r_apogee + r_perigee)
    print(f"\nEccentricity: {e:.4f}")
    if e < 0.01:
        print("(Nearly circular orbit)")
    elif e < 0.1:
        print("(Slightly elliptical orbit)")
    elif e < 0.5:
        print("(Moderately elliptical orbit)")
    else:
        print("Highly elliptical orbit)")

a_meters = a * 1000
T = 2 * math.pi * math.sqrt(a_meters**3 / (G * M_earth))

hours = T / 3600
minutes = (T % 3600) / 60
days = T / 86400
v_avg = (2 * math.pi * a_meters) / T

# Orbit classification
altitude_avg = a - R_earth

print(f"\n{'='*50}")
print(" ORBITAL PERIOD RESULTS ")
print(f"{'='*50}")
print(f"Seconds: {T:.0f}")

if hours < 1:
    print(f"Minutes: {minutes:.1f}")
elif hours < 24:
    print(f"Time: {int(hours)} hours and {minutes:.0f} minutes")
else:
    print(f"Days: {days:.2f}")

print(f"\nAverage velocity: {v_avg/1000:.2f} km/s")

print(f"\n{'='*50}")
print(" ORBIT CLASSIFICATION " )
print(f"\n{'='*50}")

if altitude_avg < 2000:
    print("LEO - Low Earth Orbit (Like ISS)")
elif altitude_avg < 35000:
    print("MEO - Medium Earth Orbit (Like GPS)")
elif abs(altitude_avg - 35786) < 500:
    print("GEO - Geostationary Orbit ( like TV satellites)")
else:
    print("HEO - High Earth Orbit ( like the Moon)")

print(f"\n{'='*50}")
print("Made by IvanSpaceCoder | Age: 14 | Goal: Astronaut | First time programming in english")
print("="*50)

