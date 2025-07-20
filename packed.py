# ┌───────────────────────────────────────────────┐
# │    Containerkalkyl                            │
# │    Utvecklad i Python av Isak Tranberg-Hansen │
# └───────────────────────────────────────────────┘

import math

class PackedCalc:
    def __init__(self, pallet_width, pallet_length, pallet_height, pallet_weight):
        # Initiera pallens dimensioner och vikt
        self.pallet_width = pallet_width
        self.pallet_length = pallet_length
        self.pallet_height = pallet_height
        self.pallet_weight = pallet_weight

        # Definiera dimensioner för olika containertyper i cm
        self.containers = {
            "20ft": {
                "length": 590,
                "width": 235,
                "height": 239
            },
            "40ft": {
                "length": 1200,
                "width": 235,
                "height": 239
            },
            "40ft HC": {
                "length": 1200,
                "width": 235,
                "height": 269
            }
        }

        self.max_payload = 28000  # Maxvikt i kg per container (lagligt max)

    def _calculate_capacity(self, container_dims):
        # Beräkna hur många pallar som får plats i bredd och längd
        pallets_per_width = math.floor(container_dims["width"] / self.pallet_width)
        pallets_per_length = math.floor(container_dims["length"] / self.pallet_length)
        pallets_per_layer = pallets_per_width * pallets_per_length

        # Antal lager som får plats i höjd
        layers = math.floor(container_dims["height"] / self.pallet_height)

        total_pallets = pallets_per_layer * layers
        total_weight = total_pallets * self.pallet_weight

        # Begränsa av max tillåten lastvikt
        limited_weight = min(total_weight, self.max_payload)

        return {
            "pallets": total_pallets,
            "max_weight": limited_weight
        }

    def choose_best_container(self, total_weight_to_ship):
        results = {}      # Här sparas containerval
        suggestions = {}  # Här sparas rekommendationer om viktjusteringar

        for name, dims in self.containers.items():
            capacity = self._calculate_capacity(dims)
            max_wt = capacity["max_weight"]

            if max_wt == 0:
                containers_needed = float("inf")
            else:
                containers_needed = math.ceil(total_weight_to_ship / max_wt)
                remainder = total_weight_to_ship % max_wt

                # Om containern inte fylls exakt, ge förslag på justeringar
                if remainder != 0:
                    decrease = remainder
                    increase = max_wt - remainder
                    suggestions[name] = {
                        "öka": round(increase, 2),
                        "minska": round(decrease, 2)
                    }

            # Spara resultatet för varje containertyp
            results[name] = {
                "containers_needed": containers_needed,
                "max_weight_per_container": round(max_wt, 2)
            }

        # Välj det alternativ med minst antal containrar
        best_choice = min(results.items(), key=lambda x: x[1]["containers_needed"])
        return best_choice[0], results, suggestions
