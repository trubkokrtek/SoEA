import pydub as pd
from pydub import playback
import os
import time as t
os.system("Color a")
os.system("CLS")
play = playback._play_with_simpleaudio()

def gameover():
    t.sleep(5)
    #? gameover_theme = pd.AudioSegment.from_wav("./music/gameover.wav")
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
    t.sleep(3)
    quit()

#? music department
#? try: 
    #? scary_sound = pd.AudioSegment.from_wav("./music/scary.wav")
    #? error_sound = pd.AudioSegment.from_wav("./music/error.wav")
    #? intelligent_music = pd.AudioSegment.from_wav("./music/intelligent.wav")
    #? brave_music = pd.AudioSegment.from_wav("./music/brave.wav")
    #? holy = pd.AudioSegment.from_wav("./music/holy.wav")
    #? organ = pd.AudioSegment.from_wav("./music/organ.wav")
    #? start_game = pd.AudioSegment.from_wav("./music/start.wav")
    #? gunshots = pd.AudioSegment.from_wav("./music/gun.wav")
#? except:
    #? print("Nelze načíst hudbu, zkus to znovu, nebo použij verzi bez hudby")
    #? quit()
#TODO 5 artefaktů k otevření petrovy kapsy, k získání karty ke kouzelným dveřím. Otevírání ve tvaru pentagramu. 5 PC (každému chybí něco jiného)
#TODO Artefakty: Honzův kabel, instalační soubory LabView, Pepovu raketu (a naistalovat naní win11), pojistku, přihlašovací údaje k novým PC na TULce
#TODO good endings: probuzení ze snu
#TODO bad endings: přejetí vlakem po vyjití z budovy
#TODO items: Kafe / Honzovo kafe (nicked), tvoje zapomenuté USB
#TODO LV: nasel jsi svoje stare USB se soubory (clickbait - corrupted)
#TODO easter eggs: JS, SolidWorks (Najman)
#TODO secret ending: Tetris

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
print("""Co uděláš? Utečeš, podíváš se na to zblízka, nebo zkameníš strachy na místě:
        1 - Uteču
        2 - Podívám se na ten pentagram zblízka
        3 - Zkameníš strachy na místě""")
answer = input("Co tedy uděláš? 1 / 2 / 3: ")
if answer == '1':
    print("Vyběhneš z místnosti s pentagramem k nelblišším dveřím, ale zjistíš, že dveře jsou zamčené.")
    print("Podíváš se blíže na zámek dveří a zjistíš, že k jejich otevření je potřeba legendární kouzelná karta, kterou lze nalést jen na jediném místě.")
    #? play(holy)
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

t.sleep(5)
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
        search = int(input("Po čem se tedy půjdeš podívat? "))
        if search not in range(1,6):
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
                continue
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
            print("No, jo, ale jak ho dostat ze skříně? A kde vůbec tu skříň hledat?")
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
                print("Radši budu hledat něco jiného")
                #? play(error_sound)
                continue 
                
        case 2:
            if endings[1] != "":
                print("Tento předmět jsi už našel!")
                #? play(error_sound)
            print("Přemýšlíš, kde by jsi mohl najít přihlašovací údaje.")
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
            print("Možná by ty údaje mohly napsané někde na tabuli v nějaké učebně.")
            print("""Rozhlédneš se kolem sebe a vidíš tři možné cesty:
                      1 - Schody vedoucí o patro níž
                      2 - Výtah
                      3 - Chodba vedoucí za roh""")
            answer = input("Kterou z nich se vydáš? ")
            if answer == '1':
                print("Sejdeš o jedno patro níž a přemýšlíš jestli jít ještě o jedno níž.")
                #? play(cink)
                print("Hodíš si mincí a padne hlava, takže se vydáš ještě o jendo patro níž.")
                print("""Když sehdeš o patro níž, nabízí se ti tentokrát čtyři cesty: 
                            1 - Schody vedoucí níže
                            2 - Výtah
                            3 - Levá dlouhá chodba
                            4 - Pravá dlouhá chodba""")
                answer = input("Kterou z nich se vydáš? ")
                if answer == '1':
                    print("Jdeš postupně schod po schodu dolů, je tam Temno, jakoby to napsal sám Jirásek.")
                    #? play(scary_sound)
                    print("Uslyšíš strašidelný zvuk, lekneš se a začneš utíkat zpátky do schodů.")
                    print("Cestou zakopneš o schod a už padáš hlavou napřed, směrem k zemi.")
                    gameover()
                    
                elif answer == '2':
                    print("Vejdeš do výtahu, zavřeš oči a zmáčkneš náhodné tlačitko.")
                    print("Výtah se rozjede, ale najednou se zastaví a otevřou se dveře a ty vystoupíš.")
                    print("Rozhlédneš se kolem sebe a uvědomíš si, že jsi zase na patře s pentagramem.")
                    print("Tak se vrátíš zpět do místnosti s pentagramem.")
                    continue

                elif answer == '3':
                    print("Jdeš doleva a vidíš zde několik místnosti, do kterých by ses chtěl podívat.")
                    while True:
                        print("Vidíš kolem sebe místnosti AP301 - AP310.")
                        print("""Takže máš na výběr z možností: 
                                    AP3xx - AP301 - AP310
                                    right - Můžeš jít do pravé chodby
                                    return - Můžeš se také vrátit do mísntosti s pentagramem""")
                        room = input("Kam to bude? ")
                        match room:
                            case "right":
                                answer = '4'
                                break
                            
                            case "return":
                                print("Radši se vrátíš do místnosti s pentagramem")
                                break
                            
                            case "AP301":
                                print("Vejdeš do místnosti, ale na tabuli je napsaný nějaký pseudokód.")
                                t.sleep(3)
                                print("Po chvíli přemýšlení ti dojde, že to není pseudokód, ale JavaScript.")
                                print("Ale to už je pozdě, už ti to vypálilo oči a ty umíráš s posledním pohledem na JavaScript.")
                                gameover()
                            
                            case "AP302":
                                #? play(alarm)
                                print("Otevřeš dveře do místnosti a ihned se rozezní alarm.")
                                print("Rychle se podíváš jestli nenajdeš přihlašovací údaje.")
                                print("Už začneš utíkat pryč, ale zahlédla tě ochranka.")
                                #? play(gunshots)
                                t.sleep(3)
                                print("Padlo několik výstřelů, doufáš že se netrefili, ale schytal jsi to přímo do srdce.")
                                print("A to jenom proto, že ochranka si myslela, že zahlédla pistoli.")
                                print("Teď ho můžeš strašit, až do jeho smrti.")
                                gameover()
                            case "AP303":
                                #? play(scary_sound)
                                print("Vstoupíš do místnosti, máš nepříjemný pocit a tak se podíváš nahoru.")
                                print("Nad tebou se otevře pytel a spadne na tebe aspoň pět kilo mouky.")
                                print("Najednou nemůžeš dýchat a umíráš.")
                                gameover()

                            case "AP304":
                                print("Tato místnost je zamčená.")

                            case "AP305":
                                print("Tato místnost je zamčená.")

                            case "AP306":
                                print("Vstoupil jsi do místnosti a na tabuli je napsáno: ")
                                endings[1] = "bad"
                                print("""jan.novak@tul.cz
                                        Heslo123""")
                                print("Rovnou je vyzskoušíš na počítači na katedře.")
                                t.sleep(2)
                                print("Po chvíli se počítač doopravdy odemkne.")
                                print("To znamená, že si našel přihlašovací údaje k tomu počítači")
                                room = "return"
                                break
                            case "AP307":
                                print("Tato místnost je zamčená.")

                            case "AP308":
                                print("Vstoupíš do místnosti a uprostřed se nachází portál.")
                                print("Přemýšlíš jestli do něj vstoupit.")
                                #? play(brave_music)
                                t.sleep(3)
                                print("Rozhodneš se do něj vstoupit.")
                                print("Najednou ses ocitl, zpátky v místnosti s pentagramem.")
                                room = "return"
                                break

                            case "AP309":
                                #? play(scary_sound)
                                print("Vstoupíš do místnosti, máš nepříjemný pocit a tak se podíváš nahoru.")
                                print("Nad tebou se otevře pytel a spadne na tebe aspoň pět kilo mouky.")
                                print("Najednou nemůžeš dýchat a umíráš.")
                                gameover()

                            case "AP310":
                                print("Tato místnost je zamčená.")
                            
                            case _:
                                room = "return"    
                                print("Radši se vrátíš zpět po svých stopách.")
                                #? play(error_sound)
                                break
                    
                    if room == "return":
                        continue
                
                if answer == '4':
                    match room:
                        case "return":
                            print("Radši se vrátíš do místnosti s pentagramem.")
                            break
                        
                        case "AP311":
                            #? play(scary_sound)
                            print("Vstoupíš do místnosti, máš nepříjemný pocit a tak se podíváš nahoru.")
                            print("Nad tebou se otevře pytel a spadne na tebe aspoň pět kilo mouky.")
                            print("Najednou nemůžeš dýchat a umíráš.")
                            gameover()

                        case "AP312":
                            print("Tato místnost je zamčená.")
                        
                        case "AP313":
                            print("Vstoupil jsi do místnosti a na tabuli je napsáno: ")
                            endings[1] = "good"
                            print(""".\\ul
                                    123456""")
                            print("Rovnou je vyzskoušíš na počítači na katedře.")
                            t.sleep(2)
                            print("Po chvíli se počítač doopravdy odemkne.")
                            print("To znamená, že si našel přihlašovací údaje k tomu počítači")
                            room = "return"
                            break
                        
                        case "AP314":
                            print("Tato místnost je zamčená.")

                        case "AP315":
                            print("Tato místnost je zamčená.")

                        case "AP316":
                            print("Tato místnost je zamčená.")

                        case "AP317":
                            print("Vejdeš do místnosti, ale na tabuli je napsaný nějaký pseudokód.")
                            t.sleep(3)
                            print("Po chvíli přemýšlení ti dojde, že to není pseudokód, ale JavaScript.")
                            print("Ale to už je pozdě, už ti to vypálilo oči a ty umíráš s posledním pohledem na JavaScript.")
                            gameover()

                        case "AP318":
                            print("Tato místnost je zamčená.")

                        case "AP319":
                            #? play(scary_sound)
                            print("Vstoupíš do místnosti, máš nepříjemný pocit a tak se podíváš nahoru.")
                            print("Nad tebou se otevře pytel a spadne na tebe aspoň pět kilo mouky.")
                            print("Najednou nemůžeš dýchat a umíráš.")
                            gameover()

                        case "AP320":
                            #? play(alarm)
                            print("Otevřeš dveře do místnosti a ihned se rozezní alarm.")
                            print("Rychle se podíváš jestli nenajdeš přihlašovací údaje.")
                            print("Už začneš utíkat pryč, ale zahlédla tě ochranka.")
                            #? play(gunshots)
                            t.sleep(3)
                            print("Padlo několik výstřelů, doufáš že se netrefili, ale schytal jsi to přímo do srdce.")
                            print("A to jenom proto, že ochranka si myslela, že zahlédla pistoli.")
                            print("Teď ho můžeš strašit, až do jeho smrti.")
                            gameover()
                        
                        case _:
                            room = "return"    
                            print("Radši se vrátíš zpět po svých stopách.")
                            #? play(error_sound)
                            break
                    
                    if room == "return":
                        continue
                
                else:
                    print("Radši se vrátíš zpět po svých stopách.")
                    #? play(error_sound)
                    continue
            elif answer == '2':
                print("Vejdeš do výtahu a přemýšlíš, do kterého patra se vydáš.")
                print("Zavřeš oči a zmáčkneš náhodné tlačítko")
                t.sleep(4)
                #? play(cink)
                print("Dveře výtahu se otevřou, vyjdeš z výtahu a rozhlédneš se kolem")

            elif answer == '3':
                print("Běžís chodbou za roh, ale cestou sklouzneš a padáš v plné rychlosti k zemi")
                print("Umíráš na místě, kvůli rozražení tvé lebky")
                gameover()

            else:
                print("Radši budu hledat něco jiného.")
                #? play(error_sound)
                continue 
            print("""Když sehdeš o patro níž, nabízí se ti tentokrát čtyři cesty: 
                            1 - Schody vedoucí níže
                            2 - Výtah
                            3 - Levá dlouhá chodba
                            4 - Pravá dlouhá chodba""")
            answer = input("Kterou z nich se vydáš? ")
            if answer == '1':
                print("Jdeš postupně schod po schodu dolů, je tam Temno, jakoby to napsal sám Jirásek.")
                #? play(scary_sound)
                print("Uslyšíš strašidelný zvuk, lekneš se a začneš utíkat zpátky do schodů.")
                print("Cestou zakopneš o schod a už padáš hlavou napřed, směrem k zemi.")
                gameover()
                
            elif answer == '2':
                print("Vejdeš do výtahu, zavřeš oči a zmáčkneš náhodné tlačitko.")
                print("Výtah se rozjede, ale najednou se zastaví a otevřou se dveře a ty vystoupíš.")
                print("Rozhlédneš se kolem sebe a uvědomíš si, že jsi zase na patře s pentagramem.")
                print("Tak se vrátíš zpět do místnosti s pentagramem.")
                continue

            elif answer == '3':
                print("Jdeš doleva a vidíš zde několik místnosti, do kterých by ses chtěl podívat.")
                while True:
                    print("Vidíš kolem sebe místnosti AP301 - AP310.")
                    print("""Takže máš na výběr z možností: 
                                AP3xx - AP301 - AP310
                                right - Můžeš jít do pravé chodby
                                return - Můžeš se také vrátit do mísntosti s pentagramem""")
                    room = input("Kam to bude? ")
                    match room:
                        case "right":
                            answer = '4'
                            break
                        
                        case "return":
                            print("Radši se vrátíš do místnosti s pentagramem")
                            break
                        
                        case "AP301":
                            print("Vejdeš do místnosti, ale na tabuli je napsaný nějaký pseudokód.")
                            t.sleep(3)
                            print("Po chvíli přemýšlení ti dojde, že to není pseudokód, ale JavaScript.")
                            print("Ale to už je pozdě, už ti to vypálilo oči a ty umíráš s posledním pohledem na JavaScript.")
                            gameover()
                        
                        case "AP302":
                            #? play(alarm)
                            print("Otevřeš dveře do místnosti a ihned se rozezní alarm.")
                            print("Rychle se podíváš jestli nenajdeš přihlašovací údaje.")
                            print("Už začneš utíkat pryč, ale zahlédla tě ochranka.")
                            #? play(gunshots)
                            t.sleep(3)
                            print("Padlo několik výstřelů, doufáš že se netrefili, ale schytal jsi to přímo do srdce.")
                            print("A to jenom proto, že ochranka si myslela, že zahlédla pistoli.")
                            print("Teď ho můžeš strašit, až do jeho smrti.")
                            gameover()
                        case "AP303":
                            #? play(scary_sound)
                            print("Vstoupíš do místnosti, máš nepříjemný pocit a tak se podíváš nahoru.")
                            print("Nad tebou se otevře pytel a spadne na tebe aspoň pět kilo mouky.")
                            print("Najednou nemůžeš dýchat a umíráš.")
                            gameover()

                        case "AP304":
                            print("Tato místnost je zamčená.")

                        case "AP305":
                            print("Tato místnost je zamčená.")

                        case "AP306":
                            print("Vstoupil jsi do místnosti a na tabuli je napsáno: ")
                            endings[1] = "bad"
                            print("""jan.novak@tul.cz
                                    Heslo123""")
                            print("Rovnou je vyzskoušíš na počítači na katedře.")
                            t.sleep(2)
                            print("Po chvíli se počítač doopravdy odemkne.")
                            print("To znamená, že si našel přihlašovací údaje k tomu počítači")
                            room = "return"
                            break
                        case "AP307":
                            print("Tato místnost je zamčená.")

                        case "AP308":
                            print("Vstoupíš do místnosti a uprostřed se nachází portál.")
                            print("Přemýšlíš jestli do něj vstoupit.")
                            #? play(brave_music)
                            t.sleep(3)
                            print("Rozhodneš se do něj vstoupit.")
                            print("Najednou ses ocitl, zpátky v místnosti s pentagramem.")
                            room = "return"
                            break

                        case "AP309":
                            #? play(scary_sound)
                            print("Vstoupíš do místnosti, máš nepříjemný pocit a tak se podíváš nahoru.")
                            print("Nad tebou se otevře pytel a spadne na tebe aspoň pět kilo mouky.")
                            print("Najednou nemůžeš dýchat a umíráš.")
                            gameover()

                        case "AP310":
                            print("Tato místnost je zamčená.")
                        
                        case _:
                            room = "return"    
                            print("Radši se vrátíš zpět po svých stopách.")
                            #? play(error_sound)
                            break
                
                if room == "return":
                    continue
            
            if answer == '4':
                match room:
                    case "return":
                        print("Radši se vrátíš do místnosti s pentagramem.")
                        break
                    
                    case "AP311":
                        #? play(scary_sound)
                        print("Vstoupíš do místnosti, máš nepříjemný pocit a tak se podíváš nahoru.")
                        print("Nad tebou se otevře pytel a spadne na tebe aspoň pět kilo mouky.")
                        print("Najednou nemůžeš dýchat a umíráš.")
                        gameover()

                    case "AP312":
                        print("Tato místnost je zamčená.")
                    
                    case "AP313":
                        print("Vstoupil jsi do místnosti a na tabuli je napsáno: ")
                        endings[1] = "good"
                        print(""".\\ul
                                123456""")
                        print("Rovnou je vyzskoušíš na počítači na katedře.")
                        t.sleep(2)
                        print("Po chvíli se počítač doopravdy odemkne.")
                        print("To znamená, že si našel přihlašovací údaje k tomu počítači")
                        room = "return"
                        break
                    
                    case "AP314":
                        print("Tato místnost je zamčená.")

                    case "AP315":
                        print("Tato místnost je zamčená.")

                    case "AP316":
                        print("Tato místnost je zamčená.")

                    case "AP317":
                        print("Vejdeš do místnosti, ale na tabuli je napsaný nějaký pseudokód.")
                        t.sleep(3)
                        print("Po chvíli přemýšlení ti dojde, že to není pseudokód, ale JavaScript.")
                        print("Ale to už je pozdě, už ti to vypálilo oči a ty umíráš s posledním pohledem na JavaScript.")
                        gameover()

                    case "AP318":
                        print("Tato místnost je zamčená.")

                    case "AP319":
                        #? play(scary_sound)
                        print("Vstoupíš do místnosti, máš nepříjemný pocit a tak se podíváš nahoru.")
                        print("Nad tebou se otevře pytel a spadne na tebe aspoň pět kilo mouky.")
                        print("Najednou nemůžeš dýchat a umíráš.")
                        gameover()

                    case "AP320":
                        #? play(alarm)
                        print("Otevřeš dveře do místnosti a ihned se rozezní alarm.")
                        print("Rychle se podíváš jestli nenajdeš přihlašovací údaje.")
                        print("Už začneš utíkat pryč, ale zahlédla tě ochranka.")
                        #? play(gunshots)
                        t.sleep(3)
                        print("Padlo několik výstřelů, doufáš že se netrefili, ale schytal jsi to přímo do srdce.")
                        print("A to jenom proto, že ochranka si myslela, že zahlédla pistoli.")
                        print("Teď ho můžeš strašit, až do jeho smrti.")
                        gameover()
                    
                    case _:
                        room = "return"    
                        print("Radši se vrátíš zpět po svých stopách.")
                        #? play(error_sound)
                        break
        case 3:
            if endings[2] != "":
                print("Tento předmět jsi už našel!")
                #? play(error_sound)
                continue
            #? play(inteligent_music)
            print("Přemýšlíš, kde by jsi mohl najít soubory k Labview")
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
            print("Třeby by tady na patře mohl být nějaký USB disk s instalačními soubory:")
            print("""Rozhlédneš se kolem sebe a vidíš tři možné cesty:
                      1 - Chodba vlevo za roh
                      2 - Výtah
                      3 - Dlouhá chodba vpravo""")
            answer = input("Kterou z nich se vydáš? ")
            if answer == '1':
                print("Jdeš chodbou a cestou zkoušíš různé dveře.")
                print("Otevřou se jenom dvoje. A na konci cesty je ještě výtah, další pootevřené dveře.")
                print("Ještě tam jsou schody vedoucí dolů.")
                print("""Takže máš na výběr:
                            1 - První dveře
                            2 - Druhé dveře
                            3 - Poslední dveře
                            4 - Výtah
                            5 - Schody dolů""")
                answer = input("Kam se tedy vydáš? ")
                if answer == '1':
                    print("Vstoupíš do místnosti a všimneš si někdo tu nechal zapnutý počítač.")
                    print("Přisedneš k počítači a zjistíš, že někdo na něm necha zapnutý Euro Truck Simulator 2.")
                    print("Ihned zapomeneš na potřebu svobody a rozhodneš si zahrát.")
                    t.sleep(5)
                    print("Po chvíli tě to přestane bavit, akorát to má menší problém.")
                    print("Ty jsi zestárl nejméně o 90 let")
                    print("No jo no, ty zakázky nejsou krátký")
                    print("V tu chvíli se lekneš, dostáváš infarkt a umíráš v úctyhodném věku 106 let")
                    gameover()
                
                elif answer == '2':
                    print("Vejdeš do místnosti a do očí tě hned praští zapnutý počítač.")
                    print("Jdeš se na něj kouknout a uvidíš v něm zastrčenu flašku, teda flešku.")
                    print("okamžitě si jdeš sednout k tomu počítači, aby jsi mohl prohledat.")
                    print("""Na počítači rozklikneš adresář E:\\ a máš tam tři složky:
                                1 - _SOLIDWORKS
                                2 - Domácí úkoly
                                3 - Tetris""")
                    file = input("Do které složky se podíváš? ")
                    if file == '1':
                        print("Otevřeš složku _SOLIDWORKS a uvidíš tam divné soubory se jménem a připonou .SLDPRT.")
                        print("Zkusíš ho otevřít, ale Windows neví v čem ho otevřít, ale nabídne ti proram jménem SolidWorks.")
                        t.sleep(2)
                        print("Chvíli čekáš, a pak se otevře program, který je nápadný CADu.")
                        print("Tak se rozhodneš ho zavřít a hledat jinde na flešce.")
                        t.sleep(3)
                        print("To už je ale pozdě, ikony na hlavním menu se začnou ztrácet a ty jsi nakopal registry!!!")
                        print("Najednou, ale dostaneš silnou ránu do zad a nějaký člověk na tebe začne křičet, že jsi zvíře.")
                        #! Najman reference
                        print("Ale nedokřičí, ty jsi způsobil exitus tomu počítači a ten plešatý pán ho způsobil tobě.")
                        gameover()

                    elif file == '2':
                        print("v této složce se nachází: ")
                        #? play(holy)
                        print("Instalační soubory pro LabView, ty co jsi tak snaživě hleadal.")
                        print("A mimo jiné ještě složka s názvem \"porn\".")
                        print("Ze zvědavosti na ni najedeš a průzkumník souborů ti ukáže, že má 50 GB.")
                        print("Ty nemůžeš uvěřit vlastním očím, ale tebe hlavně zajímá, že jsi našel instalační soubory.")
                        endings[2] = "bad"
                        continue
                    
                    elif file == '3':
                        print("Otevřeš složku s nápisem Tetris.")
                        print("Nachází se v ní dva soubory: Tetris.vi a Tetris.py")
                        #? play(holy)
                        print("Radši si oba dva soubory zálohuješ, třeba by se ti mohly hodit na obhajoby.")
                        endings.append("Tetris")
                        continue

                    else:
                        print("Radši ze strachu utečeš, aby jsi něco nerozbil.")
                        #? play(error_sound)
                        continue

                elif answer == '3':
                    print("Rozhodneš se tedy podívat do místnosti, nic v ní na první pohled nevidíš, ale rozhodneš se tam vstoupit.")
                    print("Najednou uslyšíš zapraskání a bum, propadne se s tebou podlaha.")
                    print("Propadl jsi se o patro níž a spadnul na skříň, která se tvým pádem otevřela")
                    #? play(holy)
                    print("Vypadl z ní honzův kabel")
                    print("Ale ty bohužel umíráš na důsledky pádu.")
                    gameover()

                elif answer == '4':
                    print("Vstoupíš do výtahu, zavřeš oči a náhodně zmáčkneš tlačítko")
                    #? play(scary_music)
                    print("Výtah se rozjede, ale najednou se zastaví.")
                    print("Výtah najednou začne padat vysokou rychlostí, výsledek ti je zřejmý už při začátku tvé panické ataky")
                    gameover()

                elif answer == '5':
                    print("Pomalu scházíš ze schodů a v otevřených dveřích o patro níž, zahlédneš skříň.")
                    print("Ne jen tak ledajakou, mohla by to být skříň ve které se nachází Honzův kabel.")
                    print("Seběhneš tedy ke skříňi a snažíš se do ní dostat, lomcuješ s ní, aby se otevřela.")
                    print("Ale místo toho aby se otevřela a spadla na tebe a tím se otevřela.")
                    #? play(holy)
                    print("A vypadl z ní legendární Honzův kabel.")
                    t.sleep(2)
                    print("Ale nastal menší problém, reespektive exitus, který byl způsobený pádem té skříně.")
                    gameover()

                else:
                    print("Radši se vrátíš zpět po svých stopách.")
                    #? play(error_sound)
                    continue

            elif answer == '2':
                print("Vejdeš do výtahu a přemýšlíš, do kterého patra se vydáš.")
                print("Zavřeš oči a zmáčkneš náhodné tlačítko")
                #? play(cink)
                print("Výtah cinkne, ale nikam nejede")
                print("To znamená, že jsi zmáčknul tlačítko patra, ve kterém se právě nacházíš")
                print("Osud ti nepřál a tak se radši vrátíš do místnosti s petagramem")
                continue

            elif answer == '3':
                #TODO: minecraft unitl old age - seperate room, real ending, java - javascript
                print("Jdeš chodbou a cestou zkoušíš různé dveře.")
                print("Otevřou se ti troje dveře. A na konci cesty je ještě výtah.")
                print("""Takže máš na výběr ze čtyř možností:
                            1 - První dveře
                            2 - Druhé dveře
                            3 - Třetí dveře
                            4 - Výtah""")
                answer = input("Kam se tedy vydáš? ")
                if answer == '1':
                    #? play(alarm)
                    print("Otevřeš dveře do místnosti a ihned se rozezní alarm.")
                    print("Rychle se podíváš jestli nenajdeš přihlašovací údaje.")
                    print("Už začneš utíkat pryč, ale zahlédla tě ochranka.")
                    #? play(gunshots)
                    t.sleep(3)
                    print("Padlo několik výstřelů, doufáš že se netrefili, ale schytal jsi to přímo do srdce.")
                    print("A to jenom proto, že ochranka si myslela, že zahlédla pistoli.")
                    print("Teď ho můžeš strašit, až do jeho smrti.")
                    gameover()

                elif answer == '2':
                    print("Vstoupíš do místnosti a všimneš si někdo tu nechal zapnutý počítač.")
                    print("Přisedneš k počítači a zjistíš, že někdo na něm necha zapnutý minecraft.")
                    print("Ihned zapomeneš na potřebu svobody a rozhodneš si zahrát.")
                    t.sleep(5)
                    print("Po chvíli tě to přestane bavit, akorát to má menší problém.")
                    print("Ty jsi zestárl nejméně o 90 let")
                    print("Ach jo, minecraft je taková zábava, a ještě k tomu je to sandbox hra, takže v ní můžnu dělat všechno možné.")
                    print("V tu chvíli se lekneš, dostáváš infarkt a umíráš v úctyhodném věku 106 let")
                    gameover()

                elif answer == '3':
                    print("Vejdeš do místnosti a do očí tě hned praští zapnutý počítač.")
                    print("Jdeš se na něj kouknout a uvidíš v něm zastrčenu flašku, teda flešku.")
                    print("okamžitě si jdeš sednout k tomu počítači, aby jsi mohl prohledat.")
                    print("""Na počítači rozklikneš adresář E:\\ a máš tam tři složky:
                                1 - LabView
                                2 - Java
                                3 - Domácí úkoly""")
                    file = input("Do které složky se podíváš? ")
                    if file == '1':
                        print("Otevřeš složku s Nadpisem LabView a opravdu v ní je to co je tam napsáno.")
                        #? play(holy)
                        print("Opravdu v ní jsou instalační soubory k LabView.")
                        print("Rychle si vezmeš flešku a vracíš se zpět do místnosti s pentagramem.")
                        continue

                    elif file == '2':
                        print("Otevřeš složku s nápisem Java.")
                        print("Nachází se v něm nějaký kód.")
                        print("Jelikož tě vždy zajímala Java, rozhodneš se ten kód otevřít.")
                        print("Ale místo Javy, na tebe vyskočí nějaký pseudokód.")
                        t.sleep(2)
                        print("Wait a minute, řekneš si a dojde to, ale moc pozdě.")
                        print("Ten JavaScript kód ti už vypálil oči a ty si říkáš jak je nezodpovědný.")
                        print("Ale pro tebe nastává...")
                        gameover()

                    elif file == '3':
                        print("Otevřeš složku s domácími úkoly, až na to, že v ní žadné domácí úkoly nejsou.")
                        print("Je tam, jak to říct, spousta kvalitních filmů určitého žánru.")
                        print("Zapomeneš na to, že jsi sem přišel hledat instalační soubory k LabView a jeden film si pustíš.")
                        t.sleep(10)
                        print("Až ten film skončil, ty jsi si užil.") 
                        print("Ale na to LabView sis nevzpomněl a proto se vracíš zpět do místnosti s pentagramem.")
                        continue

                    else:
                        print("Radši ze strachu utečeš, aby jsi něco nerozbil.")
                        #? play(error_sound)
                        continue

                elif answer == '4':
                    #? play(cink)
                    print("Přijdeš k výtahu a zmáčkneš tlačitko, výtah cinkne, ale nic se neděje.")
                    t.sleep(5)
                    print("Čekáš ještě chvíli, ale potom si všimneš, že na displeji beěhají písmenka zobrazující text: MIMO PROVOZ")
                    print("Zahanben svojí nepozorností se vrátíš zpět do místnosti s pentagramem")
                    continue

                else:
                    print("Radši se vrátíš zpět po svých stopách.")
                    #? play(error_sound)
                    continue
            else:
                print("Radši budu hledat něco jiného.")
                #? play(error_sound)
                continue
                
        case 4:
            if endings[3] != "":
                print("Tento předmět jsi už našel!")
                #? play(error_sound)
                continue
        case 5:
            if endings[4] != "":
                print("Tento předmět jsi už našel!")
                #? play(error_sound)
                continue
            #? play(inteligent_music)
            print("Přemýšlíš, kde by jsi mohl najít pojistku")
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
            print("Nějaké pojistka by mohla být ve sklepě.")
            print("""Rozhlédneš se kolem sebe a vidíš tři možné cesty:
                      1 - Schody úplně dolů
                      2 - Výtah
                      3 - Volný pád""")
            answer = input("Kterou z nich se vydáš? ")
            if answer == '1':
                #? play(scary_sound)
                print("Seběhneš schody o pár pater níž.")
                #? play(brave_music)
                print("Cestou kolem sebe slyšíš spostu strašidelných zvuků, ale ty se jimi nenecháš zastrašit.")
                print("Když už níže se po schodech nedostaneš, rozhlédneš se kolem.")
            elif answer == '2': 
                print("Vejdeš do výtahu a rovnou zmáčkneš tlačítko s -1.")
                t.sleep(6)
                #? play(cink)
                print("Dveře výtahu se otevřou, vyjdeš z výtahu a rozhlédneš se kolem")

            elif answer == '3':
                print("Zvolil jsi cestu volný pád")
                #? play(brave_music)
                print("Jdeš k nejbližšímu oknu a skočíš z něj.")
                print("Během pádu si uvědomíš, že jsi udělal něco špatně.")
                t.sleep(2)
                print("Dopadáš na zem, jen kvůli tvé blbosti")
                print("Nevzal jsi si padák, ani jsi nezkontroloval jastli tam je něco co zmírní tvůj pád")
                print("Co jsi čekal, že se stane, když zvolíš tuto cestu?!")
                gameover()

            else:
                print("Radši budu hledat něco jiného.")
                #? play(error_sound)
                continue 
            print("""Kolem tebe jsou tři cesty: 
                            1 - Dlouhá chodba doleva
                            2 - Dlouhá chodba doprava
                            3 - Schody vedoucí o patro výš""")
            answer = input("Kam to tedy bude? ")
            if answer == '1':
                print("""Jdeš levou chodbou, ale cestou jsi viděl tři místnosti s označením:
             zeeeeee-
            z$$$$$$"
           d$$$$$$"
          d$$$$$P
         d$$$$$P
        $$$$$$"
      .$$$$$$"
     .$$$$$$"
    4$$$$$$$$$$$$$"
   z$$$$$$$$$$$$$"
   \"\"\"\"\"\"\"3$$$$$"
         z$$$$P
        d$$$$"
      .$$$$$"
     z$$$$$"
    z$$$$P
   d$$$$$$$$$$"
  *******$$$"
       .$$$"
      .$$"
     4$P"
    z$"
   zP
  z"
 /
^""")
            
                room = input("Do které místnosti se vydáš 1/2/3? ")
                if room == '1':
                    print("Hned, jakmile vstoupíš do místnosti se omylem dotkneš kabelu.")
                    print("A naneštěstí pro tebe je pod proudem.")
                    print("Takže nastává exitus elektrickým proudem.")
                    gameover()

                elif room == '2':
                    print("Tato místnost je zamčená, ale snažíš se dostat dovnitř hrubou silou")
                    #? play(scary_sound)
                    print("Ale uslyšíš nějaké strašidelné zvuky a jakoby něco padalo.")
                    print("Strachem se radši vrátíš do místnosti s pentagramem.")
                    continue

                elif room == '3':
                    print("Vstoupíš do místnosti, porozhlédneš se po pojistce, ale nemůžeš ji najít.")
                    print("Hledáš, stále hledáš, až ti zbyde poslední místo kam jsi se nepodíval a ty jen doufáš, že tam ta pojistka je.")
                    #? play(holy)
                    t.sleep(2)
                    print("Otevřeš tu krabičku a opravdu tam ta pojistka je.")
                    print("Těsně před tím, než jsi to vzdal si ji našel a už běžíš zpět do místnosti s pentagramem.")
                    endings[4] = "yes"
                    continue

                else:
                    print("Radši se vrátíš zpět po svých stopách.")
                    #? play(error_sound)
                    continue
            elif answer == '2':
                answer = input("Kam to tedy bude? ")
                print("""Jdeš levou chodbou, ale cestou jsi viděl tři místnosti s označením:
             zeeeeee-
            z$$$$$$"
           d$$$$$$"
          d$$$$$P
         d$$$$$P
        $$$$$$"
      .$$$$$$"
     .$$$$$$"
    4$$$$$$$$$$$$$"
   z$$$$$$$$$$$$$"
   \"\"\"\"\"\"\"3$$$$$"
         z$$$$P
        d$$$$"
      .$$$$$"
     z$$$$$"
    z$$$$P
   d$$$$$$$$$$"
  *******$$$"
       .$$$"
      .$$"
     4$P"
    z$"
   zP
  z"
 /
^""")
            
                room = input("Do které místnosti se vydáš 1/2/3? ")
                if room == '2':
                    print("Hned, jakmile vstoupíš do místnosti se omylem dotkneš kabelu.")
                    print("A naneštěstí pro tebe je pod proudem.")
                    print("Takže nastává exitus elektrickým proudem.")
                    gameover()

                elif room == '3':
                    print("Tato místnost je zamčená, ale snažíš se dostat dovnitř hrubou silou")
                    #? play(scary_sound)
                    print("Ale uslyšíš nějaké strašidelné zvuky a jakoby něco padalo.")
                    print("Strachem se radši vrátíš do místnosti s pentagramem.")
                    continue

                elif room == '1':
                    print("Vstoupíš do místnosti, porozhlédneš se po pojistce, ale nemůžeš ji najít.")
                    print("Hledáš, stále hledáš, až ti zbyde poslední místo kam jsi se nepodíval a ty jen doufáš, že tam ta pojistka je.")
                    #? play(holy)
                    t.sleep(2)
                    print("Otevřeš tu krabičku a opravdu tam ta pojistka není.")
                    print("Takže kapituluješ a vracíš se zpět do místnosti s pentagramem s ocasem stažaným mezi tvýma nohama.")
                    continue

                else:
                    print("Radši se vrátíš zpět po svých stopách.")
                    #? play(error_sound)
                    continue

            elif answer == '3':
                #? play(scary_sound)
                print("Radši ses vrátil zpět nahoru, protože jsi se bál.")
                continue

            else:
                print("Radši se vrátíš zpět po svých stopách.")
                #? play(error_sound)
                continue

        case _:
            continue
