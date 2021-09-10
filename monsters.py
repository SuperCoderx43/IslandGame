from monster import Monster
import items

boss_music = None
final_boss_music = None

croc_attacks = {"Chomp1": 5, "Chomp2": 7}
Crocodile = Monster('Crocodile','ArtAssets/bosses/CrocIdleL.png', "ArtAssets/bosses/CrocIdleR.png", "ArtAssets/bosses/CrocAttackingL.png", "ArtAssets/bosses/CrocAttackingR.png", (350,230), 100, croc_attacks, boss_music, "rabid", (200, 500), 15, 30, [items.looseTooth])

