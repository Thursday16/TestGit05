#Assignment 1

def q01(archons_name):
    if archons_name == 'barbatos':
        return "Once a mere elemental spirit who existed among the winds, the entity known as Barbatos gained power through the faith of the people of Old Mondstadt during their rebellion against Decarabian, the God of Storms and founder of the nation of Mondstadt. After Decarabian's death, Barbatos ascended to godhood as the Anemo Archon and reestablished Mondstadt in its current form.\n\nCurrently, Barbatos wanders the world as the bard Venti, although he is mostly seen around Mondstadt."
    elif archons_name == 'morax':
        return"Rex Lapis is the God of Contracts, Commerce, and the Warrior God — among many other names. He was the Geo Archon and is the oldest of 'The Seven,' and possibly being one of the oldest, if not the oldest, gods at over six thousand years old. He is shrouded in a plethora of legends; both true and exaggerated, often depicting him as an all-conquering, powerful deity."
    elif archons_name == 'beelzebub':
        return"Raiden Ei (Japanese: 雷電影 Raiden Ei), also known by her Goetic name Beelzebub, is the God of Eternity and the current Electro Archon who presides over Inazuma. She is a member of The Seven who also currently functions as the Raiden Shogun of Inazuma."
    elif archons_name == 'buer':
        return "Lesser Lord Kusanali, also known by her Goetic name Buer, is the God of Wisdom and the current Dendro Archon among The Seven who presides over Sumeru and the new incarnation of the Dendro Archon, created by Greater Lord Rukkhadevata from the purest branch of Irminsul to succeed her. She currently resides in her vessel as Nahida."
    else:
      return "Archon's name not found"

def run():
    name = input("Enter the Archon's name: ")
    name = name.lower()
    result = q01(name)
    print(result)

run()

