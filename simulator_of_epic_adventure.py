import pydub as pd
import os
os.system("Color a")
os.system("CLS")

#TODO 5 artefaktů k otevření petrovy kapsy, k získání karty ke kouzelným dveřím. Otevírání ve tvaru pentagramu. 5 PC (každému chybí něco jiného)
#TODO Artefakty: Honzův kabel, instalační soubory LabView, Pepovu raketu (a naistalovat naní win11), pojistku, přihlašovací údaje k novým PC na TULce
#TODO good endings: probuzení ze snu
#TODO bad endings: přejetí vlakem po vyjití z budovy
#TODO items: Kafe / Honzovo kafe (nicked), tvoje zapomenuté USB
#TODO LV: nasel jsi svoje stare USB se soubory (clickbait - corrupted)
#TODO easter eggs: JS
#? add music
print("""Ahoj, právě ses probudil na TULce.
      Nevíš jak jsi se sem dostal, ale vedle tebe na zemi je nakresleno něco jako pentagram a v každém kruhu je počítač, kromě jednoho""")
#? scary_sound = pd.AudioSegment.from_mp3("./scary.mp3")
#? pd.play(scary_sound)
print("Co udeláš? Utečeš, nebo se na to podíváš zblízka")
answer = input("Utecu/Podivam se na to:")
if answer == "Utecu":
    print("Vyběhneš z místnosti s pentagramem k nelblišším dveřím, ale zjistíš, že dveře jsou zamčené.")
    print("Podíváš se blíže na zámek dveří a zjistíš, že k jejich otevření je potřeba legendární kouzelná karta, kterou lze nalést jen na jediném místě.")
    #? pd.play(dark_sourprise_sound)
    print("V petrově kapse.")
    #? pd.play(organ)
elif answer == "Podivam se na to":
    #? pd.play("brave_music")
    print("Zjistíš, že uprostřed pentagramu se nacházé server s nápisem \"Petrova kapsa\"")
    #? pd.play("inteligent_music")
    print("Právě ti došlo, že k útěku potrebuješ legendární kouzelnou kartu")