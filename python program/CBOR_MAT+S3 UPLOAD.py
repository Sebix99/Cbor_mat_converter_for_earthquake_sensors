import sys
import subprocess
from importlib import reload
import os
import cbor2
import shutil
from scipy.io import savemat
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QFileDialog
from PyQt5.uic import loadUi
import config
import boto3
global filepath, actual_path, fname, data_rate
import numpy as np
data_rate=(4000,2000,1000,500,250,125,62.5,31.25,15.625,7.8125,3.90625)


filepath=config.filepath                #setta la save location salvata su config quando il programma viene aperto
actual_path=os.getcwd()                 #setta il percorso sulla cartella dove è aperto il file 
def change_dir():
    path1=filepath1
    f = open("config.py","r")
    lines = f.readlines()
    f.close()
    f = open("config.py","w")
    for line in lines:
      if "filepath" not in line:
        f.write(line)
    path1='\'{}\''.format(path1)
    filepath='filepath='+path1
    f.write(filepath)
    f.close()
def assixyz(data):
    x=data[0::3]
    y=data[1::3]
    z=data[2::3]
    return x,y,z
def conversion(fname):                                          #fname[0] corrisponde al percorso del file .cbor
    global data_rate
    with open(fname[0], 'rb') as f:
        obj = cbor2.load(f)
        data=obj[0]['v'];
        e=obj[0]['e']
        t=obj[0]['t']
    
    (x,y,z)=assixyz(data)
    c=format(e,'008b')
    c=list(reversed(c))
    
    Tc=''.join(c[1:5])[::-1]
    Tc=int(Tc,2)
    Tc=1/data_rate[2]

    SPS=''.join(c[1:5])[::-1]
    FSR=''.join(c[5:7])[::-1]
    timestamp=np.empty(len(x))
    i=0
    
    while i<len(x):
        timestamp[i]=t+i*Tc
        i=i+1
    
    dic={'timestamp': timestamp,'asseX': x,'asseY': y,'asseZ': z,'full_scale_range': FSR ,'samples_per_second':SPS,'data_type': c[0]} #dal bit più significativo a quello meno
    fn_ex=(os.path.basename(fname[0]))
    fn=(os.path.splitext(fn_ex)[0])
    datamat=f'{fn}.mat'
    return dic,datamat
    
    
class MainWindow(QDialog):
    
    
    def __init__(self):
        super(MainWindow,self).__init__()
        loadUi("gui.ui",self)
        #line_edit_off
        
        self.filename.setEnabled(False)
        self.response.setEnabled(False)
        self.last_upload.setEnabled(False)
        self.directory.setText(config.filepath)
        self.directory.setEnabled(False)
        self.browse.clicked.connect(self.convert)
        self.savelocation.clicked.connect(self.save_location)
        self.uploader.clicked.connect(self.upload)
        self.config.clicked.connect(self.open_configuration)
        
    def convert(self):
        global fname, actual_path
        reload(config)
        try:
            fname=QFileDialog.getOpenFileName(self, 'Open file',actual_path, 'Cbor files (*.cbor)')
            actual_path=os.path.dirname(fname[0])
            self.conversion_and_save()
        except:
            print('non selezionato')
        
    def save_location(self):
        global filepath1
        try:
            filepath = str(QFileDialog.getExistingDirectory(self, os.getcwd()))
            if len(filepath) != 0:  
                self.directory.setEnabled(True)
                self.directory.setText(filepath)
                self.directory.setEnabled(False)
            else:
              pass  
            
            filepath1=filepath
            config.filepath=filepath1
            change_dir()
        except:
             print('non selezionato')
                  
        
    def upload(self):
        global path2
        reload(config)
        S3_client = boto3.client(service_name='s3', 
                              aws_access_key_id=config.public_key, 
                              aws_secret_access_key=config.private_key, 
                              region_name=config.region_name
                              )
        response=S3_client.upload_file(path2, config.S3_path, '{}{}'.format(config.S3_pathfolder,datamat))
        
        
        if response is None:
            self.response.setEnabled(True)
            self.response.setText('Upload done')
            self.response.setEnabled(False)
            self.last_upload.setEnabled(True)
            self.last_upload.setText('{}'.format(datamat))
            self.last_upload.setEnabled(False)
        else:
            self.response.setEnabled(True)
            self.response.setText('Upload not done')
            self.response.setEnabled(False)
            
    def open_configuration(self):
        subprocess.Popen(["notepad.exe", 'config.py'])
        
    def conversion_and_save(self):
         global datamat,path2
         (dic,datamat)=conversion(fname)
         savemat(datamat, dic)
         self.filename.setEnabled(True)
         self.filename.setText("{}".format(datamat))
         self.filename.setEnabled(False)
         path1=os.getcwd()+'\{}'.format(datamat)
         path2=config.filepath+'\{}'.format(datamat)
         shutil.move(path1, path2)
    
        
app=QApplication(sys.argv)
mainwindow=MainWindow()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(500)
widget.setFixedHeight(350)
widget.show()
sys.exit(app.exec_())