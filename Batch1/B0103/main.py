nama_hero = "Cavallum"
level = 60
hp = 120.5
is_alive = True
inventory = ["Pedang", "Panah", "Anak Panah"]
atribut = {
    "Kekuatan": 80,
    "Kelincahan": 65 
}

print(
    "--- Profile Karakter ---",
    "\nHero Name      :", nama_hero,
    "\nLevel          :", level,
    "\nHP             :", hp,
    "\nAlive          :", is_alive,
    "\nInventory      :", inventory,
    "\nAtribute       :", atribut
)
print(
    "--- Tipe Data ---",
    "\nHero Name      :", type(nama_hero),
    "\nLevel          :", type(level),
    "\nHP             :", type(hp),
    "\nAlive          :", type(is_alive),
    "\nInventory      :", type(inventory),
    "\nAtribute       :", type(atribut)
)

inventori_baru = "Ramuan HP"
level_baru = float(level + 0.5)
inventory.append(inventori_baru)

print(
    "--- Profile Karakter Baru ---",
    "\nHero Name      :", nama_hero,
    "\nLevel          :", level_baru,
    "\nHP             :", hp,
    "\nAlive          :", is_alive,
    "\nInventory      :", inventory,
    "\nAtribute       :", atribut
)