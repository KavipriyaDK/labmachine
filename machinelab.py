machines = [
    {"id": "M101", "plant": "Plant A", "hours": 120, "downtime": 10, "energy": 5000, "units": 1000, "maintenance": 25000},
    {"id": "M102", "plant": "Plant A", "hours": 100, "downtime": 20, "energy": 4500, "units": 700, "maintenance": 30000},
    {"id": "M103", "plant": "Plant B", "hours": 150, "downtime": 15, "energy": 6000, "units": 1400, "maintenance": 20000},
    {"id": "M104", "plant": "Plant B", "hours": 130, "downtime": 30, "energy": 5500, "units": 800, "maintenance": 35000},
    {"id": "M105", "plant": "Plant C", "hours": 110, "downtime": 5, "energy": 4800, "units": 950, "maintenance": 18000}
]

print("======================================================")
print("INDUSTRIAL IoT MACHINE PERFORMANCE MONITORING")
print("======================================================")

print("\n--- Task 1: Machine Efficiency ---")
for m in machines:
    m["efficiency"] = m["units"] / (m["hours"] - m["downtime"])
    print(f'{m["id"]}: {m["efficiency"]:.2f}')

print("\n--- Task 2: Production Cost Per Unit ---")
for m in machines:
    m["cost"] = m["maintenance"] / m["units"]
    print(f'{m["id"]}: Rs.{m["cost"]:.2f}')

print("\n--- Task 3: Inefficient Machines ---")
for m in machines:
    if m["efficiency"] < 8:
        print(m["id"], "-", m["plant"])

print("\n--- Task 4: Highest Maintenance Cost ---")
highest = max(machines, key=lambda x: x["maintenance"])
print(highest["id"], "-", highest["maintenance"])

print("\n--- Task 5: Plant Wise Efficiency ---")
plants = {}
counts = {}
for m in machines:
    plants[m["plant"]] = plants.get(m["plant"], 0) + m["efficiency"]
    counts[m["plant"]] = counts.get(m["plant"], 0) + 1

for p in plants:
    print(p, ":", round(plants[p] / counts[p], 2))

print("\n--- Task 6: Preventive Maintenance Required ---")
for m in machines:
    if m["maintenance"] > 25000:
        print(m["id"], "-", m["plant"])

print("\n--- Task 7: Machines Sorted by Efficiency ---")
rank = sorted(machines, key=lambda x: x["efficiency"], reverse=True)
for i, m in enumerate(rank, 1):
    print(f'Rank {i}: {m["id"]} - {m["efficiency"]:.2f}')

print("\n--- Task 8: Saving Report ---")
file = open("machine_report.txt", "w")
file.write("MACHINE PERFORMANCE REPORT\n")
file.write("----------------------------------\n")
for i, m in enumerate(rank, 1):
    file.write(f'Rank {i}: {m["id"]} | Plant:{m["plant"]} | Efficiency:{m["efficiency"]:.2f} | Cost/Unit:{m["cost"]:.2f}\n')
file.close()
print("Saved to machine_report.txt")

print("\n--- Task 9: Reading Report ---")
file = open("machine_report.txt", "r")
print(file.read())
file.close()

print("\n--- Task 10: Invalid Data Check ---")
for m in machines:
    if m["hours"] <= m["downtime"]:
        print("Invalid Data:", m["id"])