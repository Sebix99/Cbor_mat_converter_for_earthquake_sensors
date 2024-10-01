
Questa applicazione è nata dalla necessità di costruire un programma in grado di manipolare i dati acquisiti da sensori sismologici e adattarli a uno standard definito dai ricercatori in formato .matlab 
L'obiettivo era quello di programmare un file .exe in grado di ricevere in input un file .cbor contenente i dati acquisiti dai sensori(il formato del pacchetto è spiegato nelle slide), elaborarli come richiesto e ottenere un file .mat.
Il file .mat può essere salvato in locale dove vuole l'utente e anche su cloud Amazon S3.
Attraverso i primi 5 parametri all'interno di config.py è possibile scegliere:
-Account(private key e public key)
-Bucket univoco di S3
-Regione di appartenenza del bucket
-Sottocartella dove inserire il file(se la cartella non è stata creata viene automaticamente generata)

Il programma Python è stato convertito in .exe attraverso Pyinstaller.
E' possibile scaricare la versione v1.0 direttamente da https://drive.usercontent.google.com/download?id=1yAxNhRkOfnlcnHlKkRT1Ua3TSFV2oVaf&export=download&authuser=0&confirm=t&uuid=ed62073e-e9f5-47cf-8e96-42ca14d06b8b&at=APZUnTU06lqulCIIF2mraf2O81KX%3A1716970574828

Per aprirlo basta selezionare "CBOR_MAT_earthquakedata.exe"
Non ha bisogno di file aggiuntivi per funzionare.




This application was created out of the need to build a program capable of manipulating data acquired from seismological sensors and adapting it to a standard defined by researchers in .matlab format.
The goal was to program an .exe file capable of receiving as input a .cbor file containing the data acquired from the sensors (the package format is explained in the slides), processing it as required, and obtaining a .mat file.
The .mat file can be saved locally where the user prefers and also to Amazon S3 cloud storage.
Through the first 5 parameters inside config.py, it is possible to choose:
-Account (private key and public key)
-Specific S3 bucket
-Bucket region
-Subfolder where the file will be saved (if the folder has not been created, it is automatically generated)

The Python program was converted into an .exe using Pyinstaller.
You can download version v1.0 directly from https://drive.usercontent.google.com/download?id=1yAxNhRkOfnlcnHlKkRT1Ua3TSFV2oVaf&export=download&authuser=0&confirm=t&uuid=ed62073e-e9f5-47cf-8e96-42ca14d06b8b&at=APZUnTU06lqulCIIF2mraf2O81KX%3A1716970574828.

To open it, simply select "CBOR_MAT_earthquakedata.exe".
It does not require any additional files to run.
