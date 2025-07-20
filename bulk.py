# ┌───────────────────────────────────────────────┐
# │    Containerkalkyl                            │
# │    Utvecklad i Python av Isak Tranberg-Hansen │
# └───────────────────────────────────────────────┘

import math

class BulkCalc:
    def __init__(self, density_kg_per_m3):
        # Initiera densitet (kg/m³) för materialet
        self.density = density_kg_per_m3

        # Max lastkapacitet och volym för 20ft tankcontainer
        self.max_payload_kg = 26000     # Maxvikt i kg
        self.max_volume_m3 = 25         # Intern volym i m^3

    def calculate_per_container(self):
        # Räkna ut hur mycket vikt som kan fyllas i en container baserat på densitet
        max_fillable_weight = self.density * self.max_volume_m3
        actual_max_weight = min(max_fillable_weight, self.max_payload_kg)  # Begränsat av legala viktgränser
        return actual_max_weight

    def containers_needed(self, total_weight_kg):
        # Räkna hur många containrar som behövs för en given totalvikt
        per_container_weight = self.calculate_per_container()
        return math.ceil(total_weight_kg / per_container_weight)
