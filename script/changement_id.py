import os

# Dossier contenant les fichiers YOLO
labels_dir = "../datasets/TACO/dataYOLO/labels"  # <-- adapte ce chemin si besoin

# Mapping des anciens IDs vers les nouveaux IDs (0–15)
id_map = {
    4: 0,   # Other plastic bottle
    27: 0,  # Plastic lid
    5: 0,   # Clear plastic bottle
    7: 0,   # Plastic bottle cap

    6: 1,   # Glass bottle
    9: 1,   # Broken glass
    26: 1,  # Glass jar
    23: 1,  # Glass cup

    8: 2,   # Metal bottle cap
    10: 2,  # Food Can
    11: 2,  # Aerosol
    12: 2,  # Drink can
    50: 2,  # Pop tab
    28: 2,  # Metal lid
    52: 2,  # Scrap metal

    14: 3,  # Other carton
    15: 3,  # Egg carton
    16: 3,  # Drink carton
    17: 3,  # Corrugated carton
    18: 3,  # Meal carton
    19: 3,  # Pizza box

    30: 4,  # Magazine paper
    32: 4,  # Wrapping paper
    33: 4,  # Normal paper
    34: 4,  # Paper bag
    56: 4,  # Paper straw
    31: 4,  # Tissues
    13: 4,  # Toilet tube

    36: 5,  # Plastic film
    38: 5,  # Garbage bag
    35: 5,  # Plastified paper bag
    40: 5,  # Single-use carrier bag
    41: 5,  # Polypropylene bag

    43: 6,  # Spread tub
    44: 6,  # Tupperware
    45: 6,  # Disposable food container
    46: 6,  # Foam food container
    47: 6,  # Other plastic container

    21: 7,  # Disposable plastic cup
    22: 7,  # Foam cup
    24: 7,  # Other plastic cup
    48: 7,  # Plastic glooves
    55: 7,  # Plastic straw
    49: 7,  # Plastic utensils

    29: 8,  # Other plastic
    37: 8,  # Six pack rings
    39: 8,  # Other plastic wrapper
    54: 8,  # Squeezable tube
    42: 8,  # Crisp packet

    2: 9,   # Aluminium blister pack
    3: 9,   # Carded blister pack
    0: 9,   # Aluminium foil

    51: 10, # Rope & strings
    53: 10, # Shoe

    25: 11, # Food waste

    58: 12, # Unlabeled litter
    59: 12, # Cigarette

    20: 13, # Paper cup

    1: 14,  # Battery

    57: 15  # Styrofoam piece
}

# Script pour appliquer le mapping
for root, _, files in os.walk(labels_dir):
    for file in files:
        if file.endswith(".txt"):
            path = os.path.join(root, file)
            with open(path, "r") as f:
                lines = f.readlines()

            updated_lines = []
            for line in lines:
                parts = line.strip().split()
                if len(parts) >= 5:
                    old_id = int(parts[0])
                    if old_id in id_map:
                        new_id = id_map[old_id]
                        parts[0] = str(new_id)
                        updated_lines.append(" ".join(parts) + "\n")
                    else:
                        print(f"[!] ID non trouvé ({old_id}) dans {file}")
                else:
                    print(f"[!] Ligne malformée dans {file} : {line.strip()}")

            with open(path, "w") as f:
                f.writelines(updated_lines)

print("✅ Tous les IDs ont été remplacés selon les 16 catégories.")
