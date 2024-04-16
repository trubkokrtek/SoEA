import pydub as pd
import os
import time as t
os.system("Color a")
os.system("CLS")

#? music department
#? scary_sound = pd.AudioSegment.from_mp3("./scary.mp3")

#TODO 5 artefaktů k otevření petrovy kapsy, k získání karty ke kouzelným dveřím. Otevírání ve tvaru pentagramu. 5 PC (každému chybí něco jiného)
#TODO Artefakty: Honzův kabel, instalační soubory LabView, Pepovu raketu (a naistalovat naní win11), pojistku, přihlašovací údaje k novým PC na TULce
#TODO good endings: probuzení ze snu
#TODO bad endings: přejetí vlakem po vyjití z budovy
#TODO items: Kafe / Honzovo kafe (nicked), tvoje zapomenuté USB
#TODO LV: nasel jsi svoje stare USB se soubory (clickbait - corrupted)
#TODO easter eggs: JS, SolidWorks
#? add music
print("""Ahoj, právě ses probudil na TULce.
      Nevíš jak jsi se sem dostal, ale vedle tebe na zemi je nakresleno něco jako pentagram a v každém kruhu je počítač, kromě jednoho""")
#? pd.play(scary_sound)
print("Co udeláš? Utečeš, nebo se na to podíváš zblízka")
answer = input("Utecu/Podivam se na to: ")
if answer == "Utecu":
    print("Vyběhneš z místnosti s pentagramem k nelblišším dveřím, ale zjistíš, že dveře jsou zamčené.")
    print("Podíváš se blíže na zámek dveří a zjistíš, že k jejich otevření je potřeba legendární kouzelná karta, kterou lze nalést jen na jediném místě.")
    #? pd.play(dark_sourprise_sound)
    print("V Petrově kapse.")
    #? pd.play(organ)
    t.sleep(20)
    print("Rozhodneš se, že podíváš na ten pentagram a ještě k tomu jsi vypotřeboval 20 sekund svého času.")
    print("Když se podíváš na ten pentagram, zjistíš, že uprostřed se nachází trezor s nápisem \"Petrova kapsa\".")
    print("Při ještě jedné bližší prohlídce zjistíš, že každému ze 4 počítaču v cípech pentagramu chybí určité části. A jeden počítač chybí kompletně.")
    print("Mimo jiné zjistíš že do trezoru vedou 4 kabely od 4 cípů pentagramu. Jeden kabel chybí.")
    print("Jeden z počítačů má na sobě nainstalovaný Windows11 a LabView 16 s nějakým zvláštím programem, ale není připojený k trezoru.")
    print("Další je odhlášený a ty se nemůžeš do něj přhlásit a v dalším chybí LabView.")
    print("Ten poslední ti nejde zapnout, takže pátráš, proč ti nejde zapnout. Až dojdeš k zjištění, že pojistka na elektrickém vedení k tomu počítači je spálená.")
    print("Zjistil si, že potřebuješ najít kabel, přihlašovací údaje, instalační soubory pro LabView, nějaký další počítač a pojistku.")
    print("Hodně štěstí při hraní této hry. Doufám, že ho nebudeš potřebovat.")
    print("Užij si hru!")
    #? pd.play(start_game)

elif answer == "Podivam se na to":
    #? pd.play(brave_music)
    print("Zjistíš, že uprostřed pentagramu se nachází trezor s nápisem \"Petrova kapsa\"")
    #? pd.play(inteligent_music)
    print("Právě ti došlo, že k útěku potrebuješ legendární kouzelnou kartu")
    print("Při ještě jedné bližší prohlídce zjistíš, že každému ze 4 počítaču v cípech pentagramu chybí určité části. A jeden počítač chybí kompletně.")
    print("Mimo jiné zjistíš že do trezoru vedou 4 kabely od 4 cípů pentagramu. Jeden kabel chybí.")
    print("Jeden z počítačů má na sobě nainstalovaný Windows11 a LabView 16 s nějakým zvláštím programem, ale není připojený k trezoru.")
    print("Další je odhlášený a ty se nemůžeš do něj přhlásit a v dalším chybí LabView.")
    print("Ten poslední ti nejde zapnout, takže pátráš, proč ti nejde zapnout. Až dojdeš k zjištění, že pojistka na elektrickém vedení k tomu počítači je spálená.")
    print("Zjistil si, že potřebuješ najít kabel, přihlašovací údaje, instalační soubory pro LabView, nějaký další počítač a pojistku.")
    print("Hodně štěstí při hraní této hry. Doufám, že ho nebudeš potřebovat.")
    print("Užij si hru!")
    #? pd.play(start_game)


else:
    print("Na místě jsi zkameněl strachy")
    #? pd.play(scary_music)
    print("Najednou ucítíš, že ti kamenní nohy, podíváš se na ně a zjistíš, že ti kamenní doopravdy")
    #? pd.play(game_over_theme)
    print("Kdybys nenapsal nesmyslnou odpověď na první volbu, nic by se ti nestalo")
    print("Umřel jsi a to hra ještě nazačala, tys to vyved!")
