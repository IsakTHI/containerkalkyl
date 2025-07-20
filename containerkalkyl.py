# ┌───────────────────────────────────────────────┐
# │    Containerkalkyl                            │
# │    Utvecklad i Python av Isak Tranberg-Hansen │
# └───────────────────────────────────────────────┘

import pandas as pd
import openpyxl
from packed import PackedCalc
from bulk import BulkCalc
import sys

# Läs in materialdata från CSV
try:
    material_df = pd.read_excel("material.xlsx")

    # Skriv ut tillgängliga material
    print("\nTillgängliga material:")
    for _, row in material_df.iterrows():
        print(f"{row['Materialkod']}: {row['Namn']}")

    # Extrahera giltiga materialkoder
    valid_material_codes = set(str(code).strip().upper() for code in material_df["Materialkod"])
except:
    print("Materialfil hittades ej. Fil med materialinfo vid namn 'material.xlsx' måste finnas tillgänglig.")
    sys.exit()



# Fråga användaren om material och vikt
while True:
    # Välj materialkod
    material_code = input("\nAnge materialkod: ").strip().upper()
    if material_code not in valid_material_codes:
        print("Ogiltig materialkod. Försök igen.")
        continue

    # Hämta rätt rad baserat på angiven kod
    selected_row = material_df[material_df["Materialkod"].astype(str).str.upper() == material_code].iloc[0]
    material_name = selected_row["Namn"]
    material_type = selected_row["Typ"].lower()

    # Fråga om vikt att skeppa
    try:
        shipment_weight_kg = float(input("Nettovikt att skeppa (kg): "))
    except ValueError:
        print("Felaktig inmatning. Ange en siffra för vikt.")
        continue

    # Baserat på materialtyp: bulk eller packed
    if material_type == "bulk":
        # Bulkberäkning baserat på densitet
        density = selected_row["densitet"]
        bulk_calc = BulkCalc(density_kg_per_m3=density)

        max_weight_per_container = bulk_calc.calculate_per_container()
        needed_containers = bulk_calc.containers_needed(shipment_weight_kg)

        print(f"\nMaterial: {material_name} (BULK)")
        print(f"Densitet: {density} kg/m³")
        print(f"Max per tankcontainer: {max_weight_per_container:.1f} kg")
        print(f"Antal tankcontainrar: {needed_containers}")

    elif material_type == "packed":
        # Packed beräkning baserat på pallinfo
        calc = PackedCalc(
            pallet_width=selected_row["Bredd"],
            pallet_length=selected_row["Längd"],
            pallet_height=selected_row["Höjd"],
            pallet_weight=selected_row["netvikt"]
        )

        recommended_container, container_data, suggestions = calc.choose_best_container(shipment_weight_kg)

        print(f"\nMaterial: {material_name} (PACKED)")
        print(f"Rekommenderad container: {recommended_container}")
        for container_name, info in container_data.items():
            print(f"{container_name}: {info['containers_needed']}st behövs "
                  f"(max {info['max_weight_per_container']} kg/container)")

        # Visa varning om containrar inte fylls helt
        print("\nOBS! Beroende på vald container fylls visa containrar inte helt. För att optimera:")

        for name, info in suggestions.items():
            print(f"- {name}: Öka vikten med {info['öka']} kg eller minska med {info['minska']} kg för FCL.")


    else:
        print(f"\n'{material_type}' är inte en giltig typ. Endast 'bulk' eller 'packed' stöds.")
