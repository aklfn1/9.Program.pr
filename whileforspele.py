


rezultatiwhile=open('rezultatiwhile.txt', 'a')

rezultatifor=open('rezultatifor.txt', 'a')

import random

while True:
    rezultats1=int(0)
    rezultats2=int(0)
    
    whilejaut=[{
        
        "jautajums" :"Ko dara komanda 'break' while ciklā? :" , 
        "atbV": [" a. Liek ciklam atkārtoties mūžīgi", 
    "b. Apstādina ciklu un programma turpinās" ,
    "c. Aptur ciklu uz noteiktu laiku" , 
    "d. Apstādina visu programmu"] ,
    "atbilde":"b"
    } , 


    { "jautajums" : "Kas notiek, ja while cikla nosacījums neizpildās? : ", 
    "atbV" : [" a. Veidojas bezgalīgs cikls",
    "b.Cikls nenotiek",
    "c. Kodā uzrāda kļūdu",
    "d. Nosacījums tiek dzēsts"] ,
    "atbilde" : "b"
    }, 

    { "jautajums" : "Kāda nozīme ir while ciklam programmēšanā? : ", 
    "atbV" : [" a. Atkārtot kodu kamēr nosacījums ir patiess",
    "b. Palaist kodu 1 reizi",
    "c. Paātrināt programmu",
    "d. Atkārtot kodu mūžīgi"] ,
    "atbilde" : "a"
    }, 

    { "jautajums" : "Vai while cikls var pastāvēt bez nosacījuma? : ", 
    "atbV" : [" a. Jā",
    "b. Nē ",] ,
    "atbilde" : "b"
    }, 

    { "jautajums" : "Vai while ciklu var izmantot, lai programma skaitītu līdz noteiktam skaitlim? (piem no 1-10) : ", 
    "atbV" : [" a. Nē, nepieciešams izmantot for ciklu",
    "b. Jā, bet skaitīšana notiek tikai atpakaļgaitā (no 10-1)",
    "c. Jā, ja tas ierakstīts ciklā",
    "d. Jā, bet skaitīšana notiks bezgalīgi ilgi"] ,
    "atbilde" : "c"
    }, 

    { "jautajums" : "Vai  iespējams izmainīt nosacījumu while ciklā kad tas jau vienreiz ir paveikts?: ", 
    "atbV" : [" a. Jā",
    "b. Nē ",] ,
    "atbilde" : "a"
    }, 

    { "jautajums" : "Ko dara komanda 'continue' while ciklā? : ", 
    "atbV" : [" a. Cikls tiek pārtraukts uz 5 sekundēm",
    "b. Apstādina ciklu",
    "c. Atsāk programmu no jauna",
    "d. Izlaiž pašreizējo iterāciju un uzsāk nākamo"] ,
    "atbilde" : "d"
    }, 

    { "jautajums" : "Vai while ciklā var izmantot vairākus nosacījumus vienlaicīgi? : ", 
    "atbV" : [" a. Jā, izmantojot loģiskos operatorus",
    "b. Jā, bet tikai ja nosacījumi ir vienādi",
    "c. Nē, cikls nedarbosies",
    "d. Jā, bet tikai viens no nosacījumiem tiks ņemts vērā"] ,
    "atbilde" : "a"
    }, 

    { "jautajums" : "Vai while ciklu var izmantot, lai atkārtoti prasītu lietotājam ievadīt informāciju? : ", 
    "atbV" : [" a. Jā",
    "b. Nē ",] ,
    "atbilde" : "a"
    }, 

    { "jautajums" : "Vai while cikls var pastāvēt for ciklā?  (ierakstīts zem for cikla) : ", 
    "atbV" : [" a. Nē, tiks uzrādīta kļūda",
    "b. Nē, programma tiks apstādināta",
    "c. Jā ",
    "d. Jā, bet tikai ja while ciklam nav nosacījumu"] ,
    "atbilde" : "c"
    }, 
    ]

    random.shuffle(whilejaut)

    #  shuffle - jautajumus sajauc nejaušā secībā
    
    forjaut=[{"jautajums" : "Ko dara for cikls? : " , 
     "atbV" : ["a. Atkārto koda daļu noteiktu skaitu reižu",
     "b. Atkārto kodu 1 reizi", ],
     "atbilde" : "a"},
             
    {"jautajums" : "Kādu komandu bieži izmanto kopā ar for ciklu, lai veiktu darbību vairākas reizes? : " ,
      "atbV" :[ "a.  loop() ",  "b. range()" , "c. lower()" , "d. true()"] , 
      "atbilde" : "b"
    } ,
     {"jautajums" : "Ko dara for cikls, kad tiek izmantots ar virkni (string)? : "
     , "atbV" : ["a. cikls nenotiek" , "b. cikls tiek pārtraukts pēc 1. burta. " , 
    "c. cikls atkārtojas tik reizes, cik gara ir vārdu virkne"] ,
     "atbilde" : "c"} ,
             
     {"jautajums" : "Kādi skaitļi tiks izvadīti? \n for i in range(3): \n print(i) : ",
      "atbV" : ["a.  0 1 2 3" ,
     "b.  1 2 3" , 
     "c. 1 2 3 4 ",
    "d. 0  1 2 "], 
     "atbilde" : "d"} ,
             
    {"jautajums" : "Ar ko atšķiras cikls while un cikls for? : " ,
    "atbV" :[ "a. Ciklu for izmanto iterācijai, savukārt while ciklu izmanto  darbību veikšanai kamēr nosacījums ir patiess ", 
     "b.  Starp tām nav atšķirību, var izmantot kuru grib. " ,
    "c. Cikls while tiek izmantots iterācijai, bet for cikls- nosacījumiem " , 
     "d.  For  cikls ir vienkāršāks"] , 
     "atbilde" : "a" } ,
     
     {"jautajums" : "Kāds būs šī koda iznākums? \n for i in range(2, 5) \n print(i)? :",
      "atbV" : ["a. 2 3 4 5" , "b. 2 5" , "c. 2 3 4" , "d. 7 "], 
      "atbilde" : "c"}, 
      
    {"jautajums" : "Kas notiek, ja range() komanda tiek izmantota bez nosacījumiem? : " ,
     "atbV" : ["a. kodā būs kļūda. " , "b. tiek izmantots intervāls no 0-10" , "c. tiek izmantots intervāls no 0-5" , "d. for cikls atkārtosies mūžīgi."], 
     "atbilde" : "b"} , 
      
      {"jautajums" : "Kā iespējams veikt vairākas darbības katrā cikla iterācijā? :",
       "atbV" :  ["a. jāizmanto atsevišķs cikls katrai darbībai." , "b. darbībām jābūt ārpus for cikla" , 
                  "c. jānorāda vairākas darbības vienā ciklā" , "d. tas nav iespējams for ciklā." ] ,
       "atbilde" : "c"
       } ,
      
     {"jautajums" : "Kam jāpievērš uzmanība, kad lieto komandu 'break' ? :"
      , "atbV" : ["a. cikls tiek apturēts pēc pirmās kodam atbilstošās iterācijas" , 
                  "b.  cikls turpināsies pēc pārtraukšanas" , ],
      "atbilde" : "a"}
     
     , {"jautajums" : "Kas notiks, ja for cikls tiek izpildīts ar tukšu sarakstu? piem. \n saraksts=[] \n for i in saraksts: \n print(i)  : " , 
        "atbV" : ["a.  kods uzrādīs kļūdu" , "b.  cikls izvadīs '0'" , "c.  cikls izvadīs 'saraksts' " , "d. cikls notiks, bet nekas netiks izvadīts"] ,
        
        "atbilde" : "d" }
     
     
     ]
    
    random.shuffle(forjaut)
             
             



    print("Sveiki! Lai piedalītos spēlē par python programmēšanas valodas cikliem  'while'  vai 'for' , lūdzu vispirms ievadi savu vārdu un klasi.")
    vards=input("Vārds : ")
    klase=input("Klase : ")

    izv=input("Vai vēlies atbildēt uz jautājumiem par 'while' ciklu vai par 'for' ciklu? (1, 2)")
    while  izv != "1" and izv!= "2" :
        izv=input("Vai vēlies atbildēt uz jautājumiem par 'while' ciklu vai par 'for' ciklu? (1, 2) : ")
        print()

# and- loģiskais operators, lai izmantotu 2 nosacījumus vienlaicīgi

    if izv=="1":
        print("Tu piedalies spēle par python ciklu 'while'. Tev tiks uzdoti 10 jautājumi.")
        print("Atbildi uz jautājumiem ar \033[1mvienīgi\033[0m  a, b, c vai d.")
        print()

#  \033[1mvienīgi\033[0m - izmantots, lai vārds 'vienīgi' tiktu izcelts.

        for x in whilejaut:
            print("\033[1;34m" + x["jautajums"], "\n \n" + "\033[0m")
            for y in x["atbV"]: 
                print(y)
                print()
            atbilde=(input("Atbilde (a, b, c vai d) :")).lower()
            print()
            
# x tiek izmantots, lai no vārdnīcas izvēlētos tieši 1 no rindkopām ar jautājumu, atbilžu variantu un atbildi. 
# {x['jautajums']} ir izmantots, lai no šīs rindkopas izvadītu jautājumu.
# y tiek izmantots, lai izvadītu atbilžu variantus no attiecīgās rindkopas daļas ar atbilžu variantiem (x["atbV"])


            while atbilde not in["a","b","c", "d"]:
                print(f"\n Atbilde nav pieņemta.")
                atbilde=(input("Atbilde (a, b, c vai d) :")).lower()

            if atbilde==(x["atbilde"]):
                rezultats1+=1

        print(" \n \n \033[1;35m " +"🎉 Apsveicu,", vards , "tu ieguvi" , rezultats1, "/10 punktus! 🎉 " +"\033[0m")
        print("\n")

# not in- kamēr atbilde nav viena no iekavās minētajām, izvada tekstu


        b=(f"{rezultats1}/10 : {vards}, {klase} \n")
        rezultats=rezultatiwhile.write(b)
        rezultatiwhile.close()

        rezultatiwhile=open('rezultatiwhile.txt', 'r')
        rezultatsPecVietas=rezultatiwhile.readlines()
        
        rezultatikartoti=sorted(rezultatsPecVietas,key=lambda b: int(b.split("/")[0].strip()) if b.split("/")[0].strip().isdigit() else int(-10) , reverse=True)
         
        rezultatiwhile.close()
# sorted- sakārto rezultātus pēc vietas, reverse- sakārto tos dilstošā secībā.
# key= nosaka, ka nevajag kārtot alfabētiskā secībā, bet gan pēc cita nosacījuma (x).
# lambda - funkcijai nevajag  nosaukumu, tāpēc to izmanto, lai vienkārši veiktu darbību, nesaglabājot to mainīgajā. 
# lambda x : int(x.split("/") [0]) - x funkcijā ir rinda ar rezultātu, tā ir ņemta no datnes rezultatiwhile. 
#  Tad, x.split("/")  tiek paņemta teksta rinda un split("/") to sadala pēc / zīmes. Tad rinda ir sadalīta 2 daļās, bet,
# lai kārtotu pēc rezultāta vajag tikai 1. daļu  , tāpēc jāizmanto [0] 

        
       
        for vieta, linija in enumerate(rezultatikartoti[:10], start=1):
                if vards in linija and klase in linija:
                    print("\033[1;31m"+"Apsveicu," ,vards,", Tu iekļuvi top 10! Tev ir" , vieta,". vieta!"+"\033[0m \n")
                    break
                
        else: 
            print("Diemžēl tu neiekļuvi top 10!")   
            break


#enumerate- izmantots, lai sāktu numurēt sakārtotos rezultātus. tiek numurēta katra rinda līdz 10 , tāpēc [:10], 
# start=1 - nepieciešams, lai vietu sāktu skaitīt no 1.
# loģiskie operatori and / in izmantoti, lai pārbaudītu, vai noteiktajā rindā(līnija) vārds un klase atbilst. 




    elif izv=="2" :
        print("Tu piedalies spēle par python ciklu 'for'. Tev tiks uzdoti 10 jautājumi.")
        print("Atbildi uz jautājumiem ar \033[1mvienīgi\033[0m  a, b, c vai d.")
        print()
        
        for x in forjaut:
            print("\033[1;34m" + x["jautajums"] , "\n \n" + "\033[0m")
            for y in x["atbV"]:
                print(y)
                print()
            atbilde=(input("Atbilde (a, b, c vai d) :")).lower()
            print()
            
            
            while atbilde not in["a","b","c", "d"]:
                print(f"\n Atbilde nav pieņemta.")
                atbilde=(input("Atbilde (a, b, c vai d) :")).lower()

            if atbilde==(x["atbilde"]):
                rezultats2+=1

        print(" \n \n \033[1;35m "+"🎉 Apsveicu,", vards , "tu ieguvi" , rezultats2, "/10 punktus! 🎉 "+"\033[0m")
        print("\n")
        
        
        
        
        a=(f"{rezultats2}/10 : {vards}, {klase}")
        rezultatifor.write(f"{a} \n")
        
        rezultatifor.close()
        

        rezultatifor=open('rezultatifor.txt', 'r')
        rezultatsPecVietas2=rezultatifor.readlines()
        
        rezultatikartoti2=sorted(rezultatsPecVietas2,key=lambda a: int(a.split("/")[0].strip()) if a.split("/")[0].strip().isdigit() else int(-10), reverse=True)
    
        
        rezultatifor.close()
        
        
        
        #.isdigit() - pārbauda vai a posms, kurš tika atdalīts ir cipars
        #.strip() - noņem tukšas atstarpes
        
        for vieta, linija in enumerate(rezultatikartoti2[:10], start=1):
                if vards in linija and klase in linija:
                    print("\033[1;31m"+"Apsveicu," ,vards,", Tu iekļuvi top 10! Tev ir" , vieta,". vieta!"+"\033[0m \n")
                    break
                
        else: 
            print("Diemžēl tu neiekļuvi top 10!") 
            break
                
    velreiz=input("Vai vēlies pārtraukt programmu vai spēlēt vēlreiz? (1, 2) : \n")
    if velreiz!="2" :
              break










