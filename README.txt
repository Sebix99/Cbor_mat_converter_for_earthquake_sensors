QUESTO E' IL MIO PRIMO PROGETTO COMPLETO
questa applicazione è stata svolta come progetto per un esame universitario.
L'obiettivo era quello di programmare un file .exe in grado di ricevere in input un file .cbor contenente i dati acquisiti da sensori sismologici(il formato del pacchetto è spiegato nelle slide), elaborarli come richiesto dal professore e ottenere un file .mat.
Il file .mat può essere salvato in locale dove vuole l'utente e anche su cloud S3.
Attraverso i primi 5 parametri all'interno di config.py è possibile scegliere:
-Account(private key e public key)
-Bucket univoco di S3
-Regione di appartenenza del bucket
-Sottocartella dove inserire il file(se la cartella non è stata creata viene automaticamente generata)

Il programma Python è stato convertito in .exe attraverso Pyinstaller.
E' possibile scaricare la versione v1.0 da    https://drive.google.com/file/d/1yAxNhRkOfnlcnHlKkRT1Ua3TSFV2oVaf/view?usp=drive_link


Per aprirlo basta aprire il file "CBOR_MAT_earthquakedata.exe"
Non ha bisogno di file aggiuntivi per funzionare.




THIS IS MY FIRST COMPLETE PROJECT
this application was carried out as a project for a university examination.
The objective was to program an .exe file that could receive as input a .cbor file containing data acquired from seismological sensors(the format of the package is explained in the slides), process it as requested by the professor, and obtain a .mat file.
The .mat file can be saved locally wherever the user wants and also on cloud S3.
Through the first 5 parameters within config.py it is possible to choose:
-Account(private key and public key)
-Bucket unique to S3.
-Region the bucket belongs to.
-Subfolder where to put the file(if the folder has not been created it is automatically generated)

Python program was converted to .exe through Pyinstaller.
It is possible to download the v1.0 version from   https://drive.google.com/file/d/1yAxNhRkOfnlcnHlKkRT1Ua3TSFV2oVaf/view?usp=drive_link

you can open it using "CBOR_MAT_earthquakedata.exe" inside the folder

It does not need additional files to run.