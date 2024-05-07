import pydub as pd
from pydub import playback
import os
import time as t
os.system("Color a")
os.system("CLS")
#? play = playback._play_with_simpleaudio()

def gameover():
    t.sleep(5)
    #? gameover_theme = pd.AudioSegment.from_wav("")
    #? play(gameover_theme)
    print(""" 
    ######################################################
    #                                                    #
    #                                                    #
    #                                                    #
    #   ____                                             #
    #  / ___| __ _ _ __ ___   ___    _____   _____ _ __  #
    # | |  _ / _` | '_ ` _ \ / _ \  / _ \ \ / / _ \ '__| #
    # | |_| | (_| | | | | | |  __/ | (_) \ V /  __/ |    #
    #  \____|\__,_|_| |_| |_|\___|  \___/ \_/ \___|_|    #
    #                                                    #
    #                                                    #  
    #                                                    #
    ######################################################
    """)
    quit()

#? music department
#? scary_sound = pd.AudioSegment.from_mp3("./scary.mp3")

#TODO 5 artefaktů k otevření petrovy kapsy, k získání karty ke kouzelným dveřím. Otevírání ve tvaru pentagramu. 5 PC (každému chybí něco jiného)
#TODO Artefakty: Honzův kabel, instalační soubory LabView, Pepovu raketu (a naistalovat naní win11), pojistku, přihlašovací údaje k novým PC na TULce
#TODO good endings: probuzení ze snu
#TODO bad endings: přejetí vlakem po vyjití z budovy
#TODO items: Kafe / Honzovo kafe (nicked), tvoje zapomenuté USB
#TODO LV: nasel jsi svoje stare USB se soubory (clickbait - corrupted)
#TODO easter eggs: JS, SolidWorks

print("""
 _____           _     _         _         _       _    
|_   _| __ _   _| |__ | | _____ | | ___ __| |_ ___| | __
  | || '__| | | | '_ \| |/ / _ \| |/ / '__| __/ _ \ |/ /
  | || |  | |_| | |_) |   < (_) |   <| |  | ||  __/   < 
  |_||_|   \__,_|_.__/|_|\_\___/|_|\_\_|   \__\___|_|\_\ """)
t.sleep(5)
os.system("CLS")
print("""
                                _                       
 _ __  _ __ ___  ___  ___ _ __ | |_ ___                 
| '_ \| '__/ _ \/ __|/ _ \ '_ \| __/ __|                
| |_) | | |  __/\__ \  __/ | | | |_\__ \_ _ _           
| .__/|_|  \___||___/\___|_| |_|\__|___(_|_|_)          
|_|       """)
t.sleep(5)
os.system("CLS")
print("""
 ____        _____    _        _____ _   _ _            
/ ___|  ___ | ____|  / \   _  |_   _| | | | |           
\___ \ / _ \|  _|   / _ \ (_)   | | | | | | |           
 ___) | (_) | |___ / ___ \ _    | | | |_| | |___        
|____/ \___/|_____/_/   \_(_)   |_|  \___/|_____|\n\n""")
t.sleep(5)

print("""Ahoj, právě ses probudil na TULce.
      Nevíš jak jsi se sem dostal, ale vedle tebe na zemi je nakresleno něco jako pentagram a v každém kruhu je počítač, kromě jednoho""")
#? play(scary_sound)
print("""Co udeláš? Utečeš, podíváš se na to zblízka, nebo zkaměníš strachy na místě:
        1 - Uteču
        2 - Podívám se na ten pentagram zblízka
        3 - Zkameníš strachy na místě""")
answer = input("Co tedy uděláš? 1 / 2 / 3: ")
if answer == '1':
    print("Vyběhneš z místnosti s pentagramem k nelblišším dveřím, ale zjistíš, že dveře jsou zamčené.")
    print("Podíváš se blíže na zámek dveří a zjistíš, že k jejich otevření je potřeba legendární kouzelná karta, kterou lze nalést jen na jediném místě.")
    #? play(dark_sourprise_sound)
    print("V Petrově kapse.")
    #? play(organ)
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
    #? play(start_game)

elif answer == '2':
    #? play(brave_music)
    #? play(holy)
    print("Zjistíš, že uprostřed pentagramu se nachází trezor s nápisem \"Petrova kapsa\"")
    #? play(inteligent_music)
    print("Právě ti došlo, že k útěku potrebuješ legendární kouzelnou kartu")
    print("Při ještě jedné bližší prohlídce zjistíš, že každému ze 4 počítaču v cípech pentagramu chybí určité části. A jeden počítač chybí kompletně.")
    print("Mimo jiné zjistíš že do trezoru vedou 4 kabely od 4 cípů pentagramu. Jeden kabel chybí.")
    print("Jeden z počítačů má na sobě nainstalovaný Windows11 a LabView 16 s nějakým zvláštím programem, ale není připojený k trezoru.")
    print("Další je odhlášený a ty se nemůžeš do něj přhlásit a v dalším chybí LabView.")
    print("Ten poslední ti nejde zapnout, takže pátráš, proč ti nejde zapnout. Až dojdeš k zjištění, že pojistka na elektrickém vedení k tomu počítači je spálená.")
    print("Zjistil si, že potřebuješ najít kabel, přihlašovací údaje, instalační soubory pro LabView, nějaký další počítač a pojistku.")
    print("Hodně štěstí při hraní této hry. Doufám, že ho nebudeš potřebovat.")
    print("Užij si hru!")
    #? play(start_game)


else:
    print("Na místě jsi zkameněl strachy")
    #? play(scary_music)
    print("Najednou ucítíš, že ti kamenní nohy, podíváš se na ně a zjistíš, že ti kamenní doopravdy")
    print("Kdybys nenapsal nesmyslnou odpověď na první volbu, nic by se ti nestalo")
    print("Umřel jsi a to hra ještě nazačala, tys to vyved!")
    gameover()

endings = ["", "", "", "", ""]
while True:
    if "" not in endings:
        break
    print("Co se rozhodneš hledat?")
    print("""
            1 - Kabel
            2 - Přihlašovací údaje
            3 - Instalační soubory pro LV
            4 - Nějaké jiný počítač
            5 - Pojistku""")
    try:
        search = int(input(""))
        if search not in range(1,5):
            raise ValueError
    except ValueError:
        print("Zkus hledat něco validního!")
        #? play(error_sound)
        continue
    match search:
        case 1:
            if endings[0] != "":
                print("Tento předmět jsi už našel!")
                #? play(error_sound)
            #? play(inteligent_music)
            print("Přemýšlíš, kde by jsi mohl najít kabel, který potřebuješ k připojení toho počítače")
            t.sleep(3)
            #? play(cink)
            print("""   
                 _____  
               .'     `.
              /         \\
             |           | 
             '.  +^^^+  .'
               `. \./ .'
                 |_|_|  
                 (___)    
                 (___)
                 `---' """)
            t.sleep(3)
            os.system("CLS")
            print("Možná bys mohl použít Honzův kabel ze skříně!")
            print("Podíváš se na konektory kabelů a zjistíš, že by ten kabel měl sedět")
            print("No, jo, ale jak ho dostat ze skříně?")
            print("Rozhodneš se rovnou vydat hledat ten kabel, ale kde ho hledat, jsi sice na univerzitě, ale to je tak všechno co víš")
            print("""Rozhlédneš se kolem sebe a vidíš tři možné cesty:
                      1 - Schody vedoucí o patro níž
                      2 - Výtah
                      3 - Chodba vedoucí za roh""")
            answer = input("Kterou z nich se vydáš? ")
            if answer == '1':
                print("Rozhodneš se, že se vydáš dolů po schodech.")
                print("Během chůze ze schodů, ti podklouzne noha a už padáš ze schodů, dopadneš na tvrdou podlahu a umíráš.")
                gameover()
            elif answer == '2':
                print("Vejdeš do výtahu a přemýšlíš, do kterého patra se vydáš.")
                print("Zavřeš oči a zmáčkneš náhodné tlačítko")
                t.sleep(3)
                #? play(cink)
                print("Dveře výtahu se otevřou, vyjdeš z výtahu a rozhlédneš se kolem")
                print("""Vidíš před sebou tři cesty:
                            1 - Rovnou chodbu, dlouhou tak, že ani nevidíš kam vede
                            2 - Schody vedoucí o patro výš
                            3 - Chodbu vedoucí za roh""")
                answer = input("Kam se vydáš? ")
                if answer == '1':
                    print("Jdeš dlouhou chodbou, zkoušíš postupně otevírat dveře")
                    print("Když dojdeš na konec chodby najdeš tam páčidlo a řekneš si že by se ti mohlo hodit, tak si ho dáš do kapsy")
                    print("A kam teď?")
                    print("Rozmyslíš se, že půjdeš tou chodbou, která vede za roh.")
                    print("A světe div se, jen tam další rozcestí")
                    print("""Zase máš na výběr ze tří cest: 
                                1 - Výtah
                                2 - Místnost s otevřenými dveřmi, přímo před tebou
                                3 - Schody vedoucí o patro výš""")
                    answer = input("Kam se vydáš? ")
                    if answer == '1':
                        print("Vstoupíš do výtahu, zavřeš oči a náhodně zmáčkneš tlačítko")
                        #? play(scary_music)
                        print("Výtah se rozjede, ale najednou se zastaví.")
                        print("Výtah najednou začne padat vysokou rychlostí, výsledek ti je zřejmý už při začátku tvé panické ataky")
                        gameover()
                    elif answer == '2':
                        print("Řekneš si, že se ti do schodů nechce, jsi na to moc líný.")
                        print("Takže se rozhodneš podívat do místnosti a zahlédneš tam skříň. Možná by to mohla být skříň s Honzovým kabelem")
                        print("Vstoupíš do místnosti a vytáhneš páčidlo a vypáčíš si cestu do skříně a opravdu tam je.")
                        #? play(holy)
                        print("Posvátný honzův kabel")
                        endings[0] = "crowbar"
                        print("Vracíš se do místnosti s pentagramem.")
                    elif answer == '3':
                        print("Rozhodneš se tedy podívat do místnosti a zahlédneš tam skříň. Možná by to mohla být skříň s Honzovým kabelem")
                        print("Vstoupíš do místnosti a vytáhneš páčidlo a vypáčíš si cestu do skříně a opravdu tam je.")
                        #? play(holy)
                        print("Posvátný honzův kabel")
                        endings[0] = "crowbar"
                        print("Vracíš se do místnosti s pentagramem.")
                    else:
                        print("Radši se vrátíš zpět po svých stopách.")
                        #? play(error_sound)
                        continue
                elif answer == '2':
                    print("Jdeš nahoru po schodech a v tom druhém patře zahlédneš místnost s pentagramem.")
                    print("Ale najednou ti podklouzne noha a padáš obličejem ke schodům.")
                    gameover()
                elif answer == '3':
                    print("Jdeš tou chodbou za roh, cestou zkoušíš otevřít různé dveře, ale žádne dveře nejdou otevřít.")
                    print("A světe div se, jen tam další rozcestí")
                    print("""Zase máš na výběr ze tří cest: 
                                1 - Výtah
                                2 - Místnost s otevřenými dveřmi, přímo před tebou
                                3 - Schody vedoucí o patro výš""")
                    answer = input("Kam se vydáš? ")
                    if answer == '1':
                        print("Vstoupíš do výtahu, zavřeš oči a náhodně zmáčkneš tlačítko")
                        #? play(scary_music)
                        print("Výtah se rozjede, ale najednou se zastaví.")
                        print("Výtah najednou začne padat vysokou rychlostí, výsledek ti je zřejmý už při začátku tvé panické ataky")
                        gameover()
                    elif answer == '2':
                        print("Řekneš si, že se ti do schodů nechce, jsi na to moc líný.")
                        print("Takže se rozhodneš podívat do místnosti a zahlédneš tam skříň. Možná by to mohla být skříň s Honzovým kabelem")
                        print("Vstoupíš do místnosti, zkusíš otevřít tu skříň, ale je zamčená")
                        print("Rozhlédneš se po místnosti a na věšáku tam visí klíče, možná by tam mohl jeden z nich sedět a rozhodneš se je vyzkoušet")
                        print("A jeden z nich opravdu pasuje, otevřeš tu skříň a je v ní!")
                        #? play(holy)
                        print("Posvátný honzův kabel")
                        endings[0] = "key"
                        print("Vracíš se do místnosti s pentagramem.")
                    elif answer == '3':
                        print("Rozhodneš se tedy podívat do místnosti a zahlédneš tam skříň. Možná by to mohla být skříň s Honzovým kabelem")
                        print("Rozhlédneš se po místnosti a na věšáku tam visí klíče, možná by tam mohl jeden z nich sedět a rozhodneš se je vyzkoušet")
                        print("A jeden z nich opravdu pasuje, otevřeš tu skříň a je v ní!")
                        #? play(holy)
                        print("Posvátný honzův kabel")
                        endings[0] = "key"
                        print("Vracíš se do místnosti s pentagramem.")
                    else:
                        print("Radši se vrátíš zpět po svých stopách.")
                        #? play(error_sound)
                        continue
                else:
                    print("Radši se vrátíš zpět po svých stopách.")
                    #? play(error_sound)
                    continue
            elif answer == '3':
                print("Jdeš tou chodbou za roh, cestou zkoušíš otevřít různé dveře, ale žádne dveře nejdou otevřít.")
                print("A světe div se, jen tam další rozcestí")
                print("""Zase máš na výběr ze tří cest: 
                            1 - Výtah
                            2 - Místnost s otevřenými dveřmi, přímo před tebou
                            3 - Schody vedoucí o patro výš""")
                answer = input("Kam se vydáš? ")
                if answer == '1':
                    print("Vstoupíš do výtahu, zavřeš oči a náhodně zmáčkneš tlačítko")
                    #? play(scary_music)
                    print("Výtah se rozjede, ale najednou se zastaví.")
                    print("Výtah najednou začne padat vysokou rychlostí, výsledek ti je zřejmý už při začátku tvé panické ataky")
                    gameover()
                elif answer == '2':
                    print("Jdeš dolů ze schodů a v otevřené místnosti zahlédneš něco, co by mohla být skříň ve které by mohl být honzův kabel")
                    print("Takže se rozhodneš podívat do místnosti a zahlédneš tam skříň. Možná by to mohla být skříň s Honzovým kabelem")
                    print("Vstoupíš do místnosti, zkusíš otevřít tu skříň, ale je zamčená")
                    print("Rozhlédneš se po místnosti a na věšáku tam visí klíče, možná by tam mohl jeden z nich sedět a rozhodneš se je vyzkoušet")
                    print("A jeden z nich opravdu pasuje, otevřeš tu skříň a je v ní!")
                    #? play(holy)
                    print("Posvátný honzův kabel")
                    endings[0] = "key"
                    print("Vracíš se do místnosti s pentagramem.")
                elif answer == '3':
                    print("Rozhodneš se tedy podívat do místnosti, nic v ní na první pohled nevidíš, ale rozhodneš se tam vstoupit.")
                    print("Najednou uslyšíš zapraskání a bum, propadne se s tebou podlaha.")
                    print("Propadl jsi se o patro níž a spadnul na skříň, která se tvým pádem otevřela")
                    #? play(holy)
                    print("Vypadl z ní honzův kabel")
                    print("Ale ty bohužel umíráš na důsledky pádu.")
                    gameover()
                else:
                    print("Radši se vrátíš zpět po svých stopách.")
                    #? play(error_sound)
                    continue
            else:
                    print("Radši se vrátíš zpět po svých stopách.")
                    #? play(error_sound)
                    continue
                
            
        case 2:
            if endings[1] != "":
                print("Tento předmět jsi už našel!")
                #? play(error_sound)
        case 3:
            if endings[2] != "":
                print("Tento předmět jsi už našel!")
                #? play(error_sound)
        case 4:
            if endings[3] != "":
                print("Tento předmět jsi už našel!")
                #? play(error_sound)
        case 5:
            if endings[4] != "":
                print("Tento předmět jsi už našel!")
                #? play(error_sound)
        case _:
            pass
