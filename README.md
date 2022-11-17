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

## Sources :
   #### . Open Data Réseaux Enérgies : 
        https://odre.opendatasoft.com/explore/dataset/eco2mix-national-tr/export/ flg=fr&disjunctive.nature&sort=eolien_offshore&dataChart=eyJxdWVyaWVzIjpbeyJjaGFydHMiOlt7InR5cGUiOiJiYXIiLCJmdW5jIjoiU1VNIiwieUF4aXMiOiJjb25zb21tYXRpb24iLCJjb2xvciI6InJhbmdlLUFjY2VudCIsInNjaWVudGlmaWNEaXNwbGF5Ijp0cnVlfV0sInhBeGlzIjoiZGF0ZV9oZXVyZSIsIm1heHBvaW50cyI6MjAwLCJ0aW1lc2NhbGUiOiJtaW51dGUiLCJzb3J0IjoiIiwiY29uZmlnIjp7ImRhdGFzZXQiOiJlY28ybWl4LW5hdGlvbmFsLXRyIiwib3B0aW9ucyI6eyJmbGciOiJmciIsImRpc2p1bmN0aXZlLm5hdHVyZSI6dHJ1ZSwic29ydCI6ImVvbGllbl9vZmZzaG9yZSJ9fSwic2VyaWVzQnJlYWtkb3duIjoiY29uc29tbWF0aW9uIiwic3RhY2tlZCI6InBlcmNlbnQifV0sInRpbWVzY2FsZSI6IiIsImRpc3BsYXlMZWdlbmQiOnRydWUsImFsaWduTW9udGgiOnRydWV9
        
   #### . Yahoo Finance : 
       https://finance.yahoo.com/?guccounter=1&guce_referrer=aHR0cHM6Ly90ZWFtcy5taWNyb3NvZnQuY29tLw&guce_referrer_sig=AQAAAInS0PcuTJ0UnLVN4VkYBzLPyBlB8_lSVVAcRD_JLmJ5c_reVCLkg8Gf55jjG1-xLNGY44NpcDWajj9cgUNbPFioOODUWKHEU_M-SAWtYWez8W5wRTu3dRO5Nju_JA5rpVbQAdaJlugHm_vJbRtksxBucXJc3g_yEo4vD34GS4zP      
            
   #### . Electricity Maps : 
       https://www.electricitymaps.com/
