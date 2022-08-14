# Implementačná dokumentácia k 2. úlohe do IPP 2020/2021
* Meno a priezvisko: Vanessa Jóriová
* Login: xjorio00

## interpret.py

Python script, ktorý zo vstupu načíta xml reprezentáciu trojadresného kódu a prípadné vstupné hodnoty. Tento kód je následne zinterpretovaný.

## Implementácia - `interpret.py`

### Súbory

* `interpret.py` - hlavný súbor, predáva kontrolu jednotlivým triedam
* `argParser.py` - trieda `ArgParser` načítavajúca a kontrolujúca argumenty
* `errorHandler.py` - trieda `ErrorHandler` korektne ukončujúca program pri chybovom stave
* `frames.py` - trieda `Frames` obsahujúca rámce pre prámcu s pamätovým modelom programu
* `isntruction.py` - trieda `Instruction` reprezentujúca inštrukciu a kontrolujúca jej syntaktickú a sémantickú korektnosť
* `isntructionArg.py` - trieda `InstructionArg` reprezentujúca argument funkcie 
* `isntructionList.py` - trieda `InstructionList` reprezentujúca list zoradených inštrukcií
* `interpretCode.py` - trieda `InterpretCode` vykonávajúca pomocné operácie a interpretáciu príslušných operácií 
* `variable.py` - trieda `Variable` reprezentujúca premennú   
* `xmlParser.py` - trieda `XMLParser` kontrolujúca vstupnú xml reprezentáciu inštrukcií a konvertujúca inštrukcie do internej reprezentácie   

### Implementované rozšírenia

* `FLOAT` - podpora typu float v inštrukciách
* `STACK` - podpora ďalších zásobníkových inštrukcií
* `STATI` - výpis štatistík programu - `--inst` pre výpis počtu vykonaných inštrukcií, `--hot` vypíše atribút order u inštrukcie, ktorá bola vykonaná najviackrát a `--vars` vypíše najväčší počet inicializovaných premenných v jednom okamihu na všetkych framoch    

### interpret.py - popis
`interpret.py` je realizovaný objektovo za pomoci hlavného scriptu `interpret.py` nachádzajúcom sa v hlavnom priečinku a pomocných scriptov v pomocnom priečinku `int_moldules`.\
Na začiatku behu programu sú načítané argumenty z príkazovej riadky a spracovaná ich korektnosť. Správne ukončenie aplikácie v prípade chybového stavu reguluje trieda `ErrorHandler`. Po načítaní vstupných a výstupných súborov sa načíta XML reprezentácia kódu a tá sa s pomocou knižnice `xml.etree.ElementTree` skontroluje správnosť danej reprezentácie. V prípade úspechu sa skontroluje aj koreň stromu, či obsahuje všetky potrebné atribúty a naopak neobsahuje nepovolené atribúty - podobným spôsobom sa skontrolujú aj všetky inštrukcie a ich atribúty.\ 
V prípade úspechu je interná štruktúra inštrukcie popísaná objektom triedy `Instruction`. Metódy tejto triedy tiež vykonajú syntaktické a sémantické kontroly danej inštrukcie - predovšetkým správny počet argumentov a správnosť ich typov (var, symbol, label...) Argumenty sú následne utriedené podľa poradia. Jednotlivé argumenty sú reprezentované triedou `InstructionArg`.\
Inštrukcie sú uložené v objekte triedy `InstructionList`. Ten reprezentácie inštrukcií uloží a následne podľa atribútu  **order** zoradí (XML reprezentácia môže obsahovať inštrukcie v rôznom poradí, vykonávané sú ale v správnom). List Inštrukcií obsahuje svoj Program Counter, ktorý je inkrementovaný po každom vykonaní inštrukcie a modifikovaný v prípade skokov. Instruction list tiež inštrukcie prejde a zaznačí pozície všetkých návästí, ktoré budú neskôr využívané pri skokoch. O správu pamäti sa stará trieda `Frames`, ktorá obsluhuje všetky rámce potrebné na ukladanie premenných (popísaných triedou `Variable`).\
Hlavný script `interpretCode.py` prechádza inštrukcie v správnom poradí a podľa atribútu **opcode** volí  z rady metód a pomocných metód, ktoré danú inštrukciu vykonajú. Program sa tak zinterpretuje.

## test.php

Script z dôvodu nedostatku času nebol implementovaný.
