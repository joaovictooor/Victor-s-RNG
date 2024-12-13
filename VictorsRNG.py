import random
import os
import time
import json

# Variáveis globais
 # Jogador começa com 10 Roll Points

RollPoints = 0


# Salvando os RollPoints
def save_roll_points(roll_points, filename="rollpoints.json"):
    with open(filename, "w") as file:
        json.dump({"RollPoints": roll_points}, file)
    print("RollPoints salvos com sucesso!")

# Carregando os RollPoints
def load_roll_points(filename="rollpoints.json"):
    try:
        with open(filename, "r") as file:
            data = json.load(file)
            print("RollPoints carregados com sucesso!")
            return data.get("RollPoints", 0)  # Retorna 0 se RollPoints não estiver no arquivo
    except FileNotFoundError:
        print("Nenhum RollPoints encontrado. Iniciando com o valor padrão (10).")
        return 10  # Valor padrão para novos jogos


# Função para carregar os dados
def load_inventory(filename="inventory.json"):
    try:
        with open(filename, "r") as file:
            items_owned = json.load(file)
        print("Inventário carregado com sucesso!")
        return items_owned
    except FileNotFoundError:
        print("Nenhum inventário encontrado. Criando um novo...")
        return {}  # Retorna um inventário vazio se o arquivo não existir

ItemsOwned = load_inventory()


RollPoints = load_roll_points()






dmgtaken = 0
# Inicialização de variáveis de dano
DumbDMG = 0
RockDMG = 0
BOMBDMG = 0
BaldeDMG = 0
FakeDummyDMG = 0
NerdDMG = 0
DouglasDMG = 0
AstolfoDMG = 0
CubeDMG = 0
SphereDMG = 0
PyramidDMG = 0
StarDMG = 0
VicDMG = 0
PauloDMG = 0
CaioDMG = 0
NicolasDMG = 0
WoodDMG = 0
CaCawDMG = 0
GodDMG = 0
SupremeDMG = 0


# Personagens (cada personagem começa com vida e dano próprio)
characters = {
    "fruit": {"Rarity": "common","regen": 0},
    "Dummy": {"Rarity": "common", "Health": 5, "Attack": 1},
   
    "Rock": {"Rarity": "common", "Health": 1, "Attack": 10},
    "Big Ol Metal Bar (B.O.M.B)": {"Rarity": "common", "Health": 120, "Attack": 1},
    "Balde Portugues": {"Rarity": "common", "Health": 10, "Attack": 20},
    "Fake Dummy": {"Rarity": "common", "Health": 1, "Attack": 1},
    "Nerd": {"Rarity": "uncommon", "Health": 20, "Attack": 5},
    "Douglas": {"Rarity": "uncommon", "Health": 90, "Attack": 30},
    "Especificamente o Astolfo, o nerd daquele canal la": {"Rarity": "uncommon", "Health": 50, "Attack": 50},
    "Cube": {"Rarity": "rare", "Health": 60, "Attack": 20},
    "Sphere": {"Rarity": "rare", "Health": 60, "Attack": 40},
    "Pyramid": {"Rarity": "rare", "Health": 60, "Attack": 60},
    "Star (platinum star)": {"Rarity": "rare", "Health": 60, "Attack": 80},
    "Victor": {"Rarity": "epic", "Health": 300, "Attack": 60},
    "Paulo": {"Rarity": "epic", "Health": 600, "Attack": 50},
    "Caio": {"Rarity": "epic", "Health": 450, "Attack": 190},
    "Nicolas": {"Rarity": "epic", "Health": 700, "Attack": 670},
    "Woodpecker": {"Rarity": "mythic", "Health": 900, "Attack": 300},
    "Ca-Caw": {"Rarity": "legendary", "Health": 4000, "Attack": 900},
    "God": {"Rarity": "legendary", "Health": 6000, "Attack": 900},
    "Supreme Nerd": {"Rarity": "legendary", "Health": 10000, "Attack": 6000},
}

# Função para limpar a tela
def ClearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para mostrar texto com atraso variável
# Função para mostrar texto com atraso variável
def PrintWithDelay(text, delay=0.5):
    print(text)
    time.sleep(delay)

# Função para mostrar a tela inicial
def ShowMainScreen():
    ClearScreen()
    PrintWithDelay("Welcome to Victor`s rng", 0)
    PrintWithDelay(f"You have {RollPoints} Roll Points to start.", 0.5)
    PrintWithDelay("Use them to roll for characters and battle!", 0.5)
    PrintWithDelay("Press Enter to start...", 0.5)
    input()

# Função para realizar o roll
def Roll(single_roll=True):
    global RollPoints, ItemsOwned
    ClearScreen()

    if RollPoints <= 0:
        PrintWithDelay("You don't have Roll Points :(", 0.5)
        return

    rolls_to_do = RollPoints if not single_roll else 1
    RollPoints -= rolls_to_do  # Gasta pontos de rolagem

    # Realiza os rolls
    for _ in range(rolls_to_do):
        num = random.randint(0, 1000)  # Gera um número entre 0 e 1000
        print(f"Congratulations, you rolled {num}")
        # Determina o personagem obtido com base no número gerado
        if 0 <= num < 100:
            item = "Dummy"
        elif 100 <= num < 200:
            item = "fruit"
        elif 200 <= num < 300:
            item = "Big Ol Metal Bar (B.O.M.B)"
        elif 300 <= num < 400:
            item = "Balde Portugues"
        elif 400 <= num < 500:
            item = "Fake Dummy"
        elif 500 <= num < 650:
            item = "Nerd"
        elif 650 <= num < 750:
            item = "Douglas"
        elif 750 <= num < 850:
            item = "Especificamente o Astolfo, o nerd daquele canal la"
        elif 850 <= num < 880:
            item = "Cube"
        elif 880 <= num < 900:
            item = "Sphere"
        elif 900 <= num < 920:
            item = "Pyramid"
        elif 920 <= num < 940:
            item = "Star (platinum star)"
        elif 940 <= num < 960:
            item = "Victor"
        elif 960 <= num < 975:
            item = "Paulo"
        elif 975 <= num < 990:
            item = "Caio"
        elif 990 <= num < 995:
            item = "Nicolas"
        elif 995 <= num < 998:
            item = "Woodpecker"
        elif 998 <= num < 1000:
            item = "Ca-Caw"
        else:
            aleatorio = random.randint(0,1)
            if aleatorio == 0:
                item = "God"
            else:
                item = "Supreme Nerd"
        PrintWithDelay(f"You rolled and got: {item} ({characters[item]['Rarity']})", 0.5)
        input("press enter to continue...")

        # Atualiza o inventário
        if item in ItemsOwned:
            ItemsOwned[item] = ItemsOwned.get(item, 0) +1
        else:
            ItemsOwned[item] = 1

    # Exibe o número de Roll Points restantes
    PrintWithDelay(f"You have {RollPoints} Roll Points remaining.", 1)
    save_roll_points(RollPoints)


#Save e load 



# Função para salvar os dados
def save_inventory(items_owned, filename="inventory.json"):
    with open(filename, "w") as file:
        json.dump(items_owned, file)
    print("Inventário salvo com sucesso!")











# Exibir o inventário numerado
def ShowInventory():
    has_fruits = False
    ClearScreen()  # Limpa a tela antes de exibir o inventário

    # Contadores separados para characters e fruits
    characters = {item: count for item, count in ItemsOwned.items() if not "fruit" in item.lower()}

    fruits = {item: count for item, count in ItemsOwned.items() if 'fruit' in item.lower()}
    if not fruits:
        has_fruits = False
    else:
        has_fruits = True
    # Exibe os resultados com base nos itens
    if not characters and not fruits:  # Verifica se não há nenhum item
        PrintWithDelay("Your inventory is empty.", 0.5)
    else:
        # Exibe os personagens
        if characters:
            if has_fruits:
                PrintWithDelay("Your characters:", 0.5)
                for idx, (item, count) in enumerate(characters.items(), 1):
                    PrintWithDelay(f"{idx}. {item}: {count}", 0.25)
            else:
                PrintWithDelay("Your characters:", 0.5)
                for idx, (item, count) in enumerate(characters.items(), 1):
                    PrintWithDelay(f"{idx}. {item}: {count}", 0.25)
            

        # Exibe as frutas
        if fruits:
            PrintWithDelay("Your fruits:", 0.5)
            for idx, (item, count) in enumerate(fruits.items(), 1):
                PrintWithDelay(f"{idx}. {item}: {count}", 0.25)

# Função para gerar um bot com probabilidades baseadas no sistema de roll
def GenerateBot():
    num = random.randint(0, 1000)
    if 0 <= num < 50:
        item = "Dummy"
    elif 50 <= num < 200:
        item = "Rock"
    elif 200 <= num < 300:
        item = "Big Ol Metal Bar (B.O.M.B)"
    elif 300 <= num < 400:
        item = "Balde Portugues"
    elif 400 <= num < 500:
        item = "Fake Dummy"
    elif 500 <= num < 650:
        item = "Nerd"
    elif 650 <= num < 750:
        item = "Douglas"
    elif 750 <= num < 850:
        item = "Especificamente o Astolfo, o nerd daquele canal la"
    elif 850 <= num < 880:
        item = "Cube"
    elif 880 <= num < 900:
        item = "Sphere"
    elif 900 <= num < 920:
        item = "Pyramid"
    elif 920 <= num < 940:
        item = "Star (platinum star)"
    elif 940 <= num < 960:
        item = "Victor"
    elif 960 <= num < 975:
        item = "Paulo"
    elif 975 <= num < 990:
        item = "Caio"
    elif 990 <= num < 995:
        item = "Nicolas"
    elif 995 <= num < 998:
        item = "Woodpecker"
    elif 998 <= num < 1000:
        item = "Ca-Caw"
    else:
        a = random.randint(1,3)
        if a == 1:
            item = "Supreme Nerd"
        else:
            item = "God"
    return item
def takeDamage(chara, dmg):
    global DumbDMG, RockDMG, BOMBDMG, BaldeDMG, FakeDummyDMG, NerdDMG, DouglasDMG
    global AstolfoDMG, CubeDMG, SphereDMG, PyramidDMG, StarDMG, VicDMG, PauloDMG
    global CaioDMG, NicolasDMG, WoodDMG, CaCawDMG, GodDMG, SupremeDMG

    if chara == "Dummy":
        DumbDMG += dmg
        return DumbDMG
    if chara == "Rock":
        RockDMG += dmg
        return RockDMG
    if chara == "Big Ol Metal Bar (B.O.M.B)":
        BOMBDMG += dmg
        return BOMBDMG
    if chara == "Balde Portugues":
        BaldeDMG += dmg
        return BaldeDMG
    if chara == "Fake Dummy":
        FakeDummyDMG += dmg
        return FakeDummyDMG
    if chara == "Nerd":
        NerdDMG += dmg
        return NerdDMG
    if chara == "Douglas":
        DouglasDMG += dmg
        return DouglasDMG
    if chara == "Especificamente o Astolfo, o nerd daquele canal la":
        AstolfoDMG += dmg
        return AstolfoDMG
    if chara == "Cube":
        CubeDMG += dmg
        return CubeDMG
    if chara == "Sphere":
        SphereDMG += dmg
        return SphereDMG
    if chara == "Pyramid":
        PyramidDMG += dmg
        return PyramidDMG
    if chara == "Star (platinum star)":
        StarDMG += dmg
        return StarDMG
    if chara == "Victor":
        VicDMG += dmg
        return VicDMG
    if chara == "Paulo":
        PauloDMG += dmg
        return PauloDMG
    if chara == "Caio":
        CaioDMG += dmg
        return CaioDMG
    if chara == "Nicolas":
        NicolasDMG += dmg
        return NicolasDMG
    if chara == "Woodpecker":
        WoodDMG += dmg
        return WoodDMG
    if chara == "Ca-Caw":
        CaCawDMG += dmg
        return CaCawDMG
    if chara == "God":
        GodDMG += dmg
        return GodDMG
    if chara == "Supreme Nerd":
        SupremeDMG += dmg
        return SupremeDMG


def resetDamage(chara):
    global DumbDMG, RockDMG, BOMBDMG, BaldeDMG, FakeDummyDMG, NerdDMG, DouglasDMG
    global AstolfoDMG, CubeDMG, SphereDMG, PyramidDMG, StarDMG, VicDMG, PauloDMG
    global CaioDMG, NicolasDMG, WoodDMG, CaCawDMG, GodDMG, SupremeDMG

    if chara == "Dummy":
        DumbDMG = 0
    if chara == "Rock":
        RockDMG = 0
    if chara == "Big Ol Metal Bar (B.O.M.B)":
        BOMBDMG = 0
    if chara == "Balde Portugues":
        BaldeDMG = 0
    if chara == "Fake Dummy":
        FakeDummyDMG = 0
    if chara == "Nerd":
        NerdDMG = 0
    if chara == "Douglas":
        DouglasDMG = 0
    if chara == "Especificamente o Astolfo, o nerd daquele canal la":
        AstolfoDMG = 0
    if chara == "Cube":
        CubeDMG = 0
    if chara == "Sphere":
        SphereDMG = 0
    if chara == "Pyramid":
        PyramidDMG = 0
    if chara == "Star (platinum star)":
        StarDMG = 0
    if chara == "Victor":
        VicDMG = 0
    if chara == "Paulo":
        PauloDMG = 0
    if chara == "Caio":
        CaioDMG = 0
    if chara == "Nicolas":
        NicolasDMG = 0
    if chara == "Woodpecker":
        WoodDMG = 0
    if chara == "Ca-Caw":
        CaCawDMG = 0
    if chara == "God":
        GodDMG = 0
    if chara == "Supreme Nerd":
        SupremeDMG = 0
def BattleCharacter(character_name):
    ClearScreen()
    global dmgtaken
    character_stats = characters[character_name]
    character_health = character_stats["Health"]
    character_attack = character_stats["Attack"]

    # Gerar um inimigo aleatório
    enemy = GenerateBot()
    enemy_stats = characters[enemy]
    enemy_health = enemy_stats["Health"]
    enemy_attack = enemy_stats["Attack"]

    # Iniciar batalha
    PrintWithDelay(f"Battle starts! {character_name} vs. {enemy}", 1)
    PrintWithDelay("Press enter to continue the battle.", 1)
    while character_health > 0 and enemy_health > 0:
        input("...")
        a = random.randint(0, 1)
        if a == 0:
            enemy_health -= character_attack
            PrintWithDelay(f"Your {character_name} attacks {enemy} for {character_attack} damage! {enemy} HP: {enemy_health}", 1)
            if enemy_health <= 0:
                PrintWithDelay(f"{enemy} is defeated!", 1)
                return True  # O jogador venceu
        else:
            character_health -= enemy_attack
            takeDamage(character_name, enemy_attack)
            PrintWithDelay(f"{enemy} attacks {character_name} for {enemy_attack} damage! {character_name} HP: {character_health}", 1)

            # Perguntar ao jogador se deseja usar uma fruta
            if character_health > 0:
                if "fruit" in ItemsOwned and ItemsOwned["fruit"] > 0:
                    use_fruit = input("Do you want to use a fruit to heal? (y/n): ").strip().lower()
                    if use_fruit == 'y':
                        ItemsOwned["fruit"] -= 1  # Remove uma fruta do inventário
                        if ItemsOwned["fruit"] == 0:
                            del ItemsOwned["fruit"]

                        heal_amount = max(1, character_health // 2)
                        character_health += heal_amount

                        # Verifica se ultrapassa a vida máxima
                        if character_health > character_stats["Health"]:
                            excess = character_health - character_stats["Health"]
                            character_health = character_stats["Health"]
                            PrintWithDelay(f"Your {character_name} used a fruit and fully healed! Excess healing of {excess} was discarded.", 1)
                        else:
                            PrintWithDelay(f"Your {character_name} used a fruit and healed {heal_amount} HP! Current HP: {character_health}", 1)
                else:
                    PrintWithDelay("You don't have any fruits left to use!", 1)

            if character_health <= 0:
                PrintWithDelay(f"{character_name} is defeated!", 1)
                resetDamage(character_name)
                return False  # O personagem morreu

    return False  # Se o loop sair, significa que o personagem perdeu

def Battle():
    global RollPoints, ItemsOwned
    # Verifica se o jogador tem personagens suficientes para batalhar
    if not ItemsOwned:
        PrintWithDelay("You don't have any characters to battle.", 0.5)
        return

    # Mostrar inventário e escolher personagem
    ShowInventory()

    # Escolher o próximo personagem para a batalha
    while ItemsOwned:
        try:
            choice = int(input("Choose a character by number from your inventory: ").strip())

            # Validar escolha
            valid_choices = [i + 1 for i, item in enumerate(ItemsOwned.keys()) if item != "fruit"]

            if choice in valid_choices:
                chosen_character = list(ItemsOwned.keys())[choice - 1]

                if ItemsOwned[chosen_character] > 0:
                    # Batalhar com o personagem escolhido
                    result = BattleCharacter(chosen_character)

                    if result:
                        # Se venceu, ganha Roll Points
                        PrintWithDelay(f"You win the battle with {chosen_character}!", 1)
                        RollPoints += 3
                        PrintWithDelay(f"You gain 3 Roll Point! Total Roll Points: {RollPoints}", 0.5)
                    else:
                        # Se perdeu, remove o personagem do inventário
                        ItemsOwned[chosen_character] -= 1
                        if RollPoints > 0:
                            RollPoints -= 1

                        if ItemsOwned[chosen_character] == 0:
                            del ItemsOwned[chosen_character]
                        PrintWithDelay(f"Your {chosen_character} is defeated. You lost this battle. You lost 1 rollPoint", 1)
                    break  # Volta para o menu após a batalha
                else:
                    PrintWithDelay("Invalid character or no more characters available for battle.", 0.5)
            else:
                PrintWithDelay("Invalid number. Please choose a valid character.", 0.5)
        except ValueError:
            PrintWithDelay("Please enter a valid number.", 0.5)

    if not ItemsOwned:
        PrintWithDelay("You have no more characters left to battle. Game Over!", 2)

# Função para jogar o jogo
def PlayGame():
    global RollPoints

    ShowMainScreen()

    while True:
        # Mostrar opções de menu
        ClearScreen()
        PrintWithDelay("Main Menu", 0)
        PrintWithDelay(f"Roll Points: {RollPoints}", 0.5)
        PrintWithDelay("1. Roll for a new character", 0.5)
        PrintWithDelay("2. Roll all available Roll Points", 0.5)  # Nova opção para rolar todos os Roll Points
        PrintWithDelay("3. Show inventory", 0.5)
        PrintWithDelay("4. Battle with a random bot", 0.5)
        PrintWithDelay("5. Exit", 0.5)

        option = input("\nChoose an option: ")

        if option == "1":
            Roll()
        elif option == "2":
            Roll(single_roll=False)  # Chama Roll para todos os Roll Points
        elif option == "3":
            ShowInventory()
            input("Press Enter to quit inventory...")
        elif option == "4":
            Battle()
        elif option == "5":
            PrintWithDelay("Thanks for playing!", 0.5)
            save_inventory(ItemsOwned)
            save_roll_points(RollPoints)
            break
        else:
            PrintWithDelay("Invalid option. Please try again.", 0.5)

# Iniciar o jogo
PlayGame()
