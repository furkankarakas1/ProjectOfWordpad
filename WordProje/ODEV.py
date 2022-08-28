import sys, os

from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget,\
                            QPushButton, QLabel,QPlainTextEdit,QStatusBar,QToolBar,\
                            QVBoxLayout, QAction, QFileDialog, QMessageBox, QComboBox, QLineEdit,QLabel

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QFontDatabase,QIcon, QKeySequence
from PyQt5.QtPrintSupport import QPrintDialog

import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui     import *
from PyQt5.QtCore    import *


## GEREKLİ İMPORTLARI YAPTIK


    
    

        

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowIcon(QIcon('notes.png'))
        self.screen_width, self.screen_height = self.geometry().width(), self.geometry().height()
        self.resize(self.screen_width , self.screen_height )     
        self.filterTypes = 'Text Document (*.txt);; Python (*.py);; Markdown (*.md) '

        self.path= None

        self.fixedFont2 = QFontDatabase.systemFont(QFontDatabase.FixedFont)
        self.fixedFont2.setPointSize(7)

        self.fixedFont3 = QFontDatabase.systemFont(QFontDatabase.FixedFont)
        self.fixedFont3.setPointSize(10)

        self.fixedFont4 = QFontDatabase.systemFont(QFontDatabase.FixedFont)
        self.fixedFont4.setPointSize(20)

        self.fixedFont5 = QFontDatabase.systemFont(QFontDatabase.FixedFont)
        self.fixedFont5.setPointSize(25)

        fixedFont = QFontDatabase.systemFont(QFontDatabase.FixedFont)        
        fixedFont.setPointSize(15)     ## FONTLARIN SİZELERİNİ AYARLAMAK İÇİN FARKLI DEĞŞKENLER OLUŞTURDUK

        self.find_button = QPushButton(self)
        self.find_button.setText("kelimeyi bul")
        self.find_button.clicked.connect(self.find_button_clicked) 

        

        mainLayout = QVBoxLayout()
        
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
        self.editor = QTextEdit()
        self.editor.setFont(fixedFont)
        mainLayout.addWidget(self.editor)
        mainLayout.addWidget(self.find_button)        
         
      
        self.statusBar = self.statusBar()
        
              

          
### Layoutlar da sıkıntın var eksiğini kapat !!!!

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
        container = QWidget()
        container.setLayout(mainLayout)
        self.setCentralWidget(container)

        file_menu = self.menuBar().addMenu('File')

        file_toolbar = QToolBar('File')
        file_toolbar.setIconSize(QSize(60,60))
        self.addToolBar(Qt.BottomToolBarArea, file_toolbar)
############ BURADA ACTİONLARIMIZI VE ÜST ALT TOOLBAR MENUBARLARIMIZI OLUŞTURUP GEREKLİ FONKSYONLARI İÇLERİNE ATAYIP RESİMNLER EKLEDİK

        open_file_action = QAction(QIcon('notes.png'), 'Open File...',self)
        open_file_action.setStatusTip('Open file')
        open_file_action.setShortcut(QKeySequence.Open)
        open_file_action.triggered.connect(self.file_open)               

        save_file_action = self.create_action(self,'diskette.png','Save File','Save file', self.file_save)
        save_file_action.setShortcut(QKeySequence.Save)

        save_fileAs_action = self.create_action(self,'save-as.png','Save File As..','Save file as', self.file_saveAs)
        save_fileAs_action.setShortcut(QKeySequence('Ctrl+Shift+S'))

        file_menu.addActions([open_file_action, save_file_action, save_fileAs_action])
        file_toolbar.addActions([open_file_action, save_file_action, save_fileAs_action])


        print_action = self.create_action(self,'printer.png','Printer File','Printer File', self.print_file)
        print_action.setShortcut(QKeySequence.Print)
        file_menu.addAction(print_action)        
        file_toolbar.addAction(print_action)



        edit_menu = self.menuBar().addMenu('&Edit')

        edit_toolbar = QToolBar('Edit')
        edit_toolbar.setIconSize(QSize(60,60))
        self.addToolBar(Qt.BottomToolBarArea, edit_toolbar)

################### 



        undo_action  = self.create_action(self,'undo.png','Undo','undo',self.editor.undo)
        undo_action.setShortcut(QKeySequence.Undo)

        red_action  = self.create_action(self,'redo.png','Redo','Redo',self.editor.redo)
        red_action.setShortcut(QKeySequence.Redo)     

        edit_menu.addActions([undo_action, red_action])
        edit_toolbar.addActions([undo_action, red_action])
##################### BU KISIMDA YAPILMASI GEREKEN EK UNDO REDO YANİ ASLINA BAKARSANIZ CTRL+Z CTRL+Y Yİ BİLMEYEN KULLANICILARIMIZ
##################### RESİM VE ÖZELLİKLER ATADIK

        clear_action = self.create_action(self,'trash.png','Clear','Clear',self.clear_content)
        edit_menu.addAction(clear_action)
        edit_toolbar.addAction(clear_action)

        edit_menu.addSeparator()
        edit_toolbar.addSeparator()    
         
        cut_action = self.create_action(self,'cut.png','Cut','Cut',self.editor.cut)
        copy_action = self.create_action(self,'files.png','Copy','Copy',self.editor.copy)
        paste_action = self.create_action(self,'paste.png','Paste','Paste',self.editor.paste)
        select_All_action = self.create_action(self,'select.png','Select All','Select all',self.editor.selectAll)
        
        cut_action.setShortcut(QKeySequence.Cut)
        copy_action.setShortcut(QKeySequence.Copy)
        paste_action.setShortcut(QKeySequence.Paste)
        select_All_action.setShortcut(QKeySequence.SelectAll)

        edit_menu.addActions([cut_action, copy_action, paste_action, select_All_action])
        edit_toolbar.addActions([cut_action, copy_action, paste_action, select_All_action])

        edit_menu.addSeparator()
        edit_toolbar.addSeparator()        

        wrap_text_action =self.create_action(self,'wrap.png','Wrap Text', 'Wrap text',self.toggle_wrap_text)
        wrap_text_action.setShortcut('Ctrl+Shift+W')
        edit_menu.addAction(wrap_text_action)
        edit_toolbar.addAction(wrap_text_action)


        self.update_title()

        cmb = QComboBox(self)
        cmb.addItem("font size : 1")
        cmb.addItem("2")
        cmb.addItem("3")
        cmb.addItem("4")

        self.writeArea=QLineEdit()
        self.writeArea.setGeometry(0,0,100,30)
        
        self.etiket=QLabel(self)
        self.etiket.move(1000,30)
        
        cmb.activated[str].connect(self.change)

        mainLayout.addWidget(cmb)
        mainLayout.addWidget(self.writeArea)        
     
        #### BU KISIMDA COMBO BOX EKLEME İHTİYACI DUYDUM FONTSİZELERİ AYARLAYABİLMEK İÇİN İSTEDİĞİMİZ GİBİ VE NETİCESİNDE DE CHANGE İLE BAĞLADIM

    
    def find_button_clicked(self):
        
      
        
        self.find_button.clicked.connect(self.handleFind)

     
    def handleFind(self):


        text = self.writeArea.text()
        if not text:
            return
        col = QColorDialog.getColor(self.editor.textColor(), self)
        if not col.isValid():
            return
        fmt = QTextCharFormat()
        fmt.setForeground(col)
        print("\nfmt.setForeground(col)", col)
        fmt.setFontPointSize(14)     

        self.editor.moveCursor(QTextCursor.Start)

        self.countWords = 0
        while self.editor.find(text, QTextDocument.FindWholeWords):      # Find whole words
           
                
            cursor = self.editor.textCursor()
            if not cursor.hasSelection():


                cursor.select(QTextCursor.WordUnderCursor)

            cursor.mergeCharFormat(fmt)
            self.editor.mergeCurrentCharFormat(fmt)            
            self.countWords += 1

        QMessageBox.information(self, 
            "Information", 
#            f"word->`{text}` found in the text `{self.countWords}` times."
             "word->`{text}` found in the text `{countWords}` times.".format(text=text, countWords=self.countWords)
        ) 
       
#     Hocam Fatih ve ben Günlerdir kelime bulmaya kafa yoruyorduk ve Şimdi beyinlerimizi birleştirince çözdük 
# O ödevi teslim etti çoktan ama olsun bize çok şey kattı
        


    def change(self,metin):       
        
        self.etiket.setText(metin)
        self.etiket.adjustSize()

        if self.etiket.text() == "font size : 1":

            self.editor.setFont(self.fixedFont2)    

        elif self.etiket.text() == "2":
            self.editor.setFont(self.fixedFont3)    

        elif self.etiket.text() == "3":
            self.editor.setFont(self.fixedFont4)

        elif self.etiket.text() == "4":
            self.editor.setFont(self.fixedFont5)

## BU CHANGE FONKSYONMUZ İSE YUKARDA BELİRTTİĞİMİZ FONT DEĞİŞKENLERİNİN SİZELERİ SAYESİNDE KULLANICI SEÇİMİNE GÖRE DEĞİŞİKLİK GÖSTERİYOR
        else:
            print("olmadı")    


#######################################################################################
    def toggle_wrap_text(self):
        self.editor.setLineWrapMode(not self.editor.lineWrapMode())    



    def clear_content(self):
        self.editor.setPlainText('')    

    def file_open(self):
        path, _ = QFileDialog.getOpenFileName(
            parent=self,
            caption='Open file',
            directory='', 
            filter=self.filterTypes)

        if path:                            ## BU KISIMDA İSTE İCONLARIN GÖREVLERİYLE NİTELENDRİLİMİŞ FONKSYONLARI GÖRMEKTESİNİZ
            try:
                with open(path,'r') as f:
                    text = f.read()
                    f.close()
            except Exception as e:
                self.dialog_message(str(e)) 

            else:
                self.path = path
                self.editor.setPlainText(text)
                self.update_title()    
        
    def file_save(self):
        if self.path is None:
            self.file_saveAs()
        else:
            try:
                text = self.editor.toPlainText()
                with open(self.path,'w') as f:
                    f.write(text)
                    f.close()
            except Exception as e:
                self.dialog_message(str(e))            ## KEZA DOSYALAMA İŞLEMLERİNDE OLDUĞU GİBİ..
            

    def file_saveAs(self):
        path, _ = QFileDialog.getSaveFileName(
            
            self,
            'Save file as',
            '',
            self.filterTypes
        )           
        text = self.editor.toPlainText()

        if not path:
            return
        else:
            try:
                with open(path,'w') as f:
                    f.write(text)
                    f.close
            except Exception as e:
                self.dialog_message(str(e))
                
            else:
                self.path = path
                self.update_title()
    def print_file(self):
        printDialog = QPrintDialog()
        if printDialog.exec_():
            self.editor.print_(printDialog.printer())                        

    def update_title(self):
        self.setWindowTitle('{0} - the best of tr word'.format(os.path.basename(self.path) if self.path else 'unittled'))

    def dialog_message(self,message):
        dlg = QMessageBox(self)
        dlg.setText(message)
        dlg.setIcon(QMessageBox.Critical)
        dlg.show()        

### VE KODUN BİTMİŞ HALİ EN DUYGULANDIĞIM AN :,) ACTİONLARIMIZI OLUŞTURDUK


    def create_action(self,parent,icon_path,action_name,set_status_tip, triggered_method):
        action = QAction(QIcon(icon_path), action_name,parent)
        action.setStatusTip(set_status_tip)
        action.triggered.connect(triggered_method)
        return action    





app = QApplication(sys.argv)
notePade = Window()
notePade.show()
sys.exit(app.exec_())

