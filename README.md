# Projet-BigData-DataViz

## Equipe :
        . Nabil HATRI
        . Rayan KHALFOUN 
        . Kenza OULMOU
        . Mohamed Redha REMILI

## Fichiers :
  #### . Data : 4 fichiers CSV contenants nos données historiques issues de differentes sources :
  
           . csv_court_gaz_histo.csv : contient les données du court du gaz des 6 derniers mois
           
           . csv_court_petrol_histo.csv : contient les données du court du pétrole des 6 derniers mois
           
           . df_history_co2.csv : contient les données des émissions de co2 des 6 derniers mois
           
           . df_history_mix.csv : contient les données de la consommation éléctrique et du mix énergétique des 6 derniers mois :
            Consommation éléctrique (MW) /	Fioul (MW) / Charbon (MW) /	Gaz (MW) /	Nucléaire (MW) /	Eolien (MW) /	Solaire (MW) /	Hydraulique                 (MW) / Pompage (MW) / Bioénergies (MW)
   
   #### . Rapport Power BI : 
    Rapport qui contient toutes nos analyses 
   
   #### . Pré_traitement_data : 
    Fichier Python dans lequel nous récupérons nos données en utilisant des appels à différentes API, et nous traitons ces données en                   utilisant la librairie Pandas, une fois nos données historiques traitées et cleannées, nous les stockons dans HDFS.
                           
   #### . Producer : 
    Fichier python dans lequel nous récupérons les données de nos api avant de les envoyer au consumer par l'intermédiaire d'un topic
   
   #### . Consumer : 
    Fichier python qui sert à récuperer les données envoyées par le producer et les traitenent avec spark, avant de les afficher
   
   #### . Présentation : 
    Fichier Power Point dans lequel nous présentons nos projets


