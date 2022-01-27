# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 14:40:33 2020

@author: PC
"""
# -*- coding: utf-8 -*-
"""
    Kenza Hibbi
"""
from tkinter import*
import tkinter.messagebox
from functools import partial
import sqlite3


user = "" #Name of loging global variable
Event_a_modifier = ""   #Nom de l evenement a modifier   
# user
class Accueil_user:
    
    def __init__(self, fenetre):
        
        self.fenetre= fenetre
        self.fenetre.title("modifier event")
        self.fenetre.config(background='#F6F917')
        self.fenetre.geometry("720x560")
      
        modif = Button(self.fenetre, text = "Modifier un evenement", bg='#040000', fg='#F6F917', font= ("Algerian", 20), command= Modifier_User.main)
        modif.pack(expand= YES)
        consul = Button(self.fenetre, text = "Consulter un evenement", bg='#040000', fg='#F6F917', font= ("Algerian", 20), command=Consulter_Event.main)
        consul.pack(expand= YES)
    
    def main():    
        root = Tk()
        my_gui = Accueil_user(root)
        root.mainloop()        
 
    
    
class Modifier_User:

    def __init__(self, fenetre):    
        global user
        
        self.fenetre= fenetre
        self.fenetre.title("modifier event")
        self.fenetre.config(background='#F6F917')
      
        titret=Label(self.fenetre ,text = "la liste des evenements",font= ("Algerian", 15),fg='#040000', bg='#F6F917').pack()
        #user= self.Login.nomLogin()
        conn = sqlite3.connect('myDB.db')
        cur= conn.cursor()
        req = ('select * from event  where reponsable = ?')
        #where  reponsable="+user
        
        result = cur.execute(req , [(user)] )
        
        for row in result:
            print (row[0])
            Libcontect_label = Label(self.fenetre,fg='#040000', bg='#F6F917', text= "Evenement: "+row[0] )
            Libcontect_label.pack(pady=10,padx=10)
        conn.commit()
        conn.close()
        
        label = Label(self.fenetre ,text = "Evenement à modifier",fg='#040000', bg='#F6F917').pack() 
        self.nom_Event = Entry(self.fenetre)
        self.nom_Event.pack() 
        #####
        btn = Button(self.fenetre ,text="Modifier",fg='#040000', bg='#F6F917', command= self.modifier_evenement ).pack()    
        

   
    def modifier_evenement(self):
        global Event_a_modifier
        conn = sqlite3.connect('myDB.db')
        cur= conn.cursor()
        #TOTOTOTOOTOTO
        find_event = ('SELECT * FROM event WHERE reponsable = ? and nom = ?')
        cur.execute(find_event,[(user),(self.nom_Event.get())])
        result = cur.fetchall()
        if result:
            print("OK")
            Event_a_modifier = self.nom_Event.get()
            self.fenetre.destroy()
            Modification_Event.main()
        else :
            label = Label(self.fenetre ,text = "evenement non existant",fg='#040000', bg='#F6F917').pack() 
        
    def main():
        global Event_a_modifier
        root = Tk()
        my_gui = Modifier_User(root)
        root.mainloop()
        
#=============================================================================
#       Classe pour verifier login et password
#              pour se connecter a la bonne interface
#=============================================================================       
class Login:
    entryLogin= None
    entryPass=None
    entrer = 0

    # constructeur de l'interface Login
    def __init__(self, fenetre):
        global user #global variable pour identifier l'utilisateur connecté
 
        #declaration des variables login et password
        entryLogin= tkinter.StringVar()
        entryPass= tkinter.StringVar()
        
        #declaration et creation de la fenetre
        self.fenetre= fenetre
        self.fenetre.title("modifier event")
        self.fenetre.config(background='#F6F917')
        self.fenetre.geometry("720x560")
        self.fenetre.geometry("720x560")
        self.fenetre.config(background='#F6F917')
        #declaration des cases login et password
        lbl1= Label(self.fenetre , text= "Login", font= ("Algerian", 15) ,fg='#040000', bg='#F6F917')
        lbl1.place(x= 100 , y= 100)
        self.entryLogin = Entry(self.fenetre)
        self.entryLogin.place(x= 250 , y= 110)
        lbl2= Label(self.fenetre , text= "Password", font= ("Algerian", 15) ,fg='#040000', bg='#F6F917')
        lbl2.place(x= 100 , y= 200)
        self.entryPass = Entry(self.fenetre)
        self.entryPass.place(x= 250 , y= 200)
        #declaration et creation de button "se connecter"
        buttCon = Button(self.fenetre, text = "Se connecter",bg='#040000', fg='#F6F917', font= ("Algerian", 20), command = self.verifier_login )
        buttCon.place(x=250 , y= 400)
    
    #fonction pour verifier le login
    def verifier_login(self):
        global user
        
        # Recupere les valeurs de login et password 
        login= self.entryLogin.get()
        user = login
        password= self.entryPass.get()
        
        #Verifier si login et password ne sont pas vide
        if len(login) == 0 and len(password) == 0:
            print("Please fill in the Missing Info")
        if len(login) == 0 and len(password) != 0 :
            print("Please Enter a Username")
        elif len(login) != 0 and len(password) == 0:
            print("Please enter a Password")

        else:
            # Verification du base de donnée si les valeurs sont Ok.
            conn = sqlite3.connect('myDB.db')
            cur= conn.cursor()
            # check si le nom et password sont OK dans la table Empoyé
            find_user = ('SELECT * FROM Empoyé WHERE nom = ? and password = ?')
            cur.execute(find_user,[(login),(password)])
            result = cur.fetchall()
            if result:
                print("OK")
                #verifier le type de profil de l'utilsateur 
                if login == 'admin':
                    Accueil_admin.main()
                else:
                    Accueil_user.main()

            else:
                print("login Or password incorrect")
            conn.commit()
            conn.close()
   # retourner le nom de responsable
    def nomLogin(self):
        return self.entryLogin.get()
    
    #main de la classe Login
    def main():          
        root = Tk()
        my_gui = Login(root)
    
        root.mainloop()
        
### admin     
class Modification_Event:
    
    salle_state = 0
    plein_state=0
    adress=0
    nb_place=0
    micro_state=0
    video_state=0
    regie_state=0
    siege_state=0
    buffet_state=0
    dispo_state = 0
    tmp_chk=0
    
    
    def __init__(self, fenetre):
        #declaration variables
        global Event_a_modifier
        tmp_chk = tkinter.IntVar()
        self.dispo_state = tkinter.StringVar(fenetre)
        self.plein_state = tkinter.StringVar(fenetre)
        self.micro_state = tkinter.StringVar(fenetre)
        self.video_state = tkinter.StringVar(fenetre)
        self.regie_state = tkinter.StringVar(fenetre)
        self.siege_state = tkinter.StringVar(fenetre)
        self.buffet_state = tkinter.StringVar(fenetre)
        self.salle_state = tkinter.StringVar(fenetre)
        self.adress = tkinter.StringVar(fenetre)
        ########
        self.fenetre= fenetre
        self.fenetre.title("Creation d'un event")
        self.fenetre.geometry("720x720")
        self.fenetre.config(background='#F6F917')
        
       
####################### salle  
        print ('JJJJJJJJJJJJJJJJJJJJJJJJJJ')
        print (Event_a_modifier)
        titre_ev=Label(self.fenetre ,text ="EVENEMENT: " + Event_a_modifier ,font= ("Algerian", 15),fg='#040000', bg='#F6F917').grid(row = 0,column = 0)
        
        titre_salle=Label(self.fenetre ,text = "RESERVATION SALLE",font= ("Algerian", 15),fg='#040000', bg='#F6F917').grid(row = 7,column = 0)
        f = Label(self.fenetre ,text = "Projection en :",fg='#040000', bg='#F6F917').grid(row = 8,column = 0)        
        
        #Radio salle:
        chk_salle = Checkbutton(self.fenetre, text='Salle',fg='#040000', bg='#F6F917', variable =self.salle_state)
        chk_salle.grid(column=1, row=8)
        print('tatatatat')
        print(self.salle_state.get())
        print('3ALAH')

        chk = Checkbutton(self.fenetre, text='Pleine air',fg='#040000', bg='#F6F917', variable=self.plein_state)
        chk.grid(column=2, row=8)
        
        g = Label(self.fenetre ,text = "Adresse salle:",fg='#040000', bg='#F6F917').grid(row = 9,column = 0)
        self.adress = Entry(self.fenetre)
        self.adress.grid(row = 9,column = 1)
        
        nbPl = Label(self.fenetre ,text = "nombre de place",fg='#040000', bg='#F6F917').grid(row =10,column = 0)   
        self.nb_place = Entry(self.fenetre)
        self.nb_place.grid(row = 10,column = 1)
        
     
        #self.micro_state.set(1)
        chk_micro = Checkbutton(self.fenetre, text='Micro',fg='#040000', bg='#F6F917', variable=self.micro_state)
        chk_micro.grid(column=0, row=11)
        
        #self.video_state.set(1)
        chk_video = Checkbutton(self.fenetre, text='Video progection',fg='#040000', bg='#F6F917', variable=self.video_state)
        chk_video.grid(column=0, row=12)
        
        
        #self.regie_state.set(1)
        chk_regie = Checkbutton(self.fenetre, text='Régie',fg='#040000', bg='#F6F917', variable=self.regie_state)
        chk_regie.grid(column=0, row=13) 
        
        
        chk_siege = Checkbutton(self.fenetre, text='Siege',fg='#040000', bg='#F6F917', variable=self.siege_state)
        chk_siege.grid(column=0, row=14) 
        #self.siege_state.set(1)
####################BUFET
        titre_debat=Label(self.fenetre ,text = "BUFFET",font= ("Algerian", 15),fg='#040000', bg='#F6F917').grid(row = 15,column = 0)

        
        
        chk_buffet = Checkbutton(self.fenetre, text='Commande buffet',fg='#040000', bg='#F6F917', variable=self.buffet_state)
        chk_buffet.grid(column=0, row=16) 
        #self.buffet_state.set(1)
################### DISPO
        titre_debat=Label(self.fenetre ,text = "iNVITE",font= ("Algerian", 15),fg='#040000', bg='#F6F917').grid(row = 18,column = 0)
        
        #self.dispo_state.set(1)
        chk_dispo = Checkbutton(self.fenetre, text='disponibilité des invités',fg='#040000', bg='#F6F917', variable=self.dispo_state)
        chk_dispo.grid(column=0, row=19)
################### fin formulaire
        
        btn = Button(self.fenetre ,text="Enregistrer",fg='#040000', bg='#F6F917', command = self.enregistrer_bd).grid(row=21,column=0)
   
    def enregistrer_bd(self):
       global Event_a_modifier
       statut = 'terminer'
       conn = sqlite3.connect('myDB.db')
       cur = conn.cursor()
       
       #get and set in data base value of salle
       salle=self.salle_state.get()
       sql_update_query = """Update event set salle = ? where nom = ?"""
       data = (salle, Event_a_modifier)
       cur.execute(sql_update_query, data)
       
       #get and set in data base disponibilité des invité
       dispo=self.dispo_state.get()
       sql_update_query = """Update event set dispo_invité = ? where nom = ?"""
       data = (dispo, Event_a_modifier)
       cur.execute(sql_update_query, data)
       
       #get and set in data base nombre de place
       nbPlace= self.nb_place.get()
       sql_update_query = """Update event set nb_place = ? where nom = ?"""
       data = (nbPlace, Event_a_modifier)
       cur.execute(sql_update_query, data)
       
       #get and set in data base (plein air pour la salle)
       plein=(self.plein_state).get() 
       sql_update_query = """Update event set plein_air = ? where nom = ?"""
       data = (plein, Event_a_modifier)
       cur.execute(sql_update_query, data)
       
       #get and set in data base reservation micro
       micro=self.micro_state.get()
       sql_update_query = """Update event set micro = ? where nom = ?"""
       data = (micro, Event_a_modifier)
       cur.execute(sql_update_query, data)
       
       #get and set in data base reservation micro
       video=self.video_state.get() 
       sql_update_query = """Update event set video = ? where nom = ?"""
       data = (video, Event_a_modifier)
       cur.execute(sql_update_query, data)
       
       #get and set in data base reservation regie
       regie=self.regie_state.get() 
       sql_update_query = """Update event set regie = ? where nom = ?"""
       data = (regie, Event_a_modifier)
       cur.execute(sql_update_query, data)   
       
       #get and set in data base reservation siege
       siege=self.siege_state.get() 
       sql_update_query = """Update event set siege = ? where nom = ?"""
       data = (siege, Event_a_modifier)
       cur.execute(sql_update_query, data) 
       
       #get and set in data base reservation buffet       
       buffet=self.buffet_state.get()
       sql_update_query = """Update event set buffet = ? where nom = ?"""
       data = (buffet, Event_a_modifier)
       cur.execute(sql_update_query, data) 
       
       #get and set in data base adress
       adress= self.adress.get() 
       sql_update_query = """Update event set adresse = ? where nom = ?"""
       data = (adress, Event_a_modifier)
       cur.execute(sql_update_query, data)
       #update statut event 
       if ((salle == '1' or plein== '1') and dispo == '1' and (len(self.nb_place.get()) != 0) and micro=='1' and  video=='1' and regie=='1' and siege=='1' and buffet== '1' and (len(self.adress.get()) != 0)) : 
           sql_update_query = """Update event set statut = ? where nom = ?"""
           data = (statut, Event_a_modifier)
           cur.execute(sql_update_query, data)
           print("dkhel")
       else:
           sql_update_query = """Update event set statut = ? where nom = ?"""
           data = ("En cours", Event_a_modifier)
           cur.execute(sql_update_query, data)
       # Closing database
       conn.commit()
       conn.close()
       self.fenetre.destroy() 
       
    def main():
        root = Tk()
        my_gui = Modification_Event(root)
        root.mainloop()

#=============================================================================
#                Classe pour Creer un evenement
#      
#=============================================================================         
        
class Creation_Event:
    var1=0
    var2=0
    nom_Event= None
    combo=None
    date_ini= None
    date_fin= None
    tmp=None
        
    resp_tab=[] # la table des responsable disponibles
    
    def __init__(self, fenetre):
        
        #declaration des variables
        self.var1 = tkinter.StringVar()
        self.var2 = tkinter.StringVar()
        OK=0
        self.fenetre= fenetre
        self.fenetre.title("Creation d'un event")
        self.fenetre.geometry("720x720")
        self.fenetre.config(background='#F6F917')
        
        #declaration du widget text
        nom_EventL = Label(self.fenetre ,text = "Nom event",fg='#040000', bg='#F6F917').grid(row = 0,column = 0)   
        reponsableL = Label(self.fenetre ,text = "responsable event",fg='#040000', bg='#F6F917').grid(row = 1,column = 0) 
        
        # nom event
        self.nom_Event = ttk.Entry(self.fenetre)
        self.nom_Event.grid(row = 0,column = 1)
        
        #declaration du combo pour afficher les responsable disponibles
        self.combo_value = tkinter.StringVar()
        self.combo = ttk.Combobox(self.fenetre,textvariable=self.combo_value)
        
        # get responsable disponible du data-base
        conn = sqlite3.connect('myDB.db')
        cur= conn.cursor()
        available_user = ('SELECT * FROM Empoyé WHERE available = 1') #available=1 ---> resp disponible
        res = cur.execute(available_user)
        j=0
        for row in res:
            OK=1
            self.tmp = row[1]; # nom du reponsable
            self.resp_tab.append(row[1]) #resp_tab table des responsable dispo
            j = j+1 
            
        conn.commit()
        conn.close()
        # set la valeur des 2 responsables event  disponible
        if (OK == 1):
            if(j>2):
                self.combo['values']= (self.resp_tab[0],self.resp_tab[1])
            else:
                self.combo['values']= (self.resp_tab[0])
        else:
            self.combo['values']= ("NONE")
      
        self.combo.grid(row = 1,column = 1)
        
        # Declaration des Radio et text pour recuperer les informations.
        d = Label(self.fenetre ,text = "Type d'évenement:",fg='#040000', bg='#F6F917').grid(row = 3,column = 0)
        rad1 = Radiobutton(self.fenetre,text='film', value=1, variable = self.var1,fg='#040000', bg='#F6F917')
        rad2 = Radiobutton(self.fenetre,text='Documentaire', variable = self.var1, value=2,fg='#040000', bg='#F6F917')
        rad3 = Radiobutton(self.fenetre,text='Reportage' , variable = self.var1, value=3,fg='#040000', bg='#F6F917')
        rad1.grid(column=1, row=2)
        rad2.grid(column=2, row=2)
        rad3.grid(column=3, row=2)
        d = Label(self.fenetre ,text = "Evenement repetitif ",fg='#040000', bg='#F6F917').grid(row = 3,column = 0)
        rad4 = Radiobutton(self.fenetre,text='Oui', variable = self.var2, value=4,fg='#040000', bg='#F6F917')
        rad5 = Radiobutton(self.fenetre,text='Non', variable = self.var2, value=5,fg='#040000', bg='#F6F917')
        rad4.grid(column=1, row=3)
        rad5.grid(column=2, row=3)
        c = Label(self.fenetre ,text = "Date d'evenement",fg='#040000', bg='#F6F917').grid(row = 4,column = 0)
      
        self.date_ini = Entry(self.fenetre)
        self.date_ini.grid(row = 4,column = 1)
        # Button pour Enregistrer les donnés, renvoie a la fonction clicked
        btn = Button(self.fenetre ,text="Enregistrer",fg='#040000', bg='#F6F917', command= self.clicked).grid(row=5,column=0)


    # Fonction pour enregistrer les information de l'event cree
    def clicked(self):
        statut = "cree" #statut de l'event
        prix= 30 # prix de ticket
 
        # recuperer les valeurs de l'interface graphique 
        typeEvent=self.var1.get()
        repetitif=self.var2.get()
        nom=self.nom_Event.get()
        resp=self.combo.get()
        date_ini=self.date_ini.get()
        conn = sqlite3.connect('myDB.db')
        cur = conn.cursor()
        # remplir la base de donnés des informations
        req= "insert into event( nom  , date_init   ,  repetitif  , statut , reponsable , type , prix) values ( ?, ?, ?, ?, ?,  ?, ?)"    
        cur.execute(req, (nom, date_ini,  repetitif, statut, resp, typeEvent, prix))
        conn.commit()
        conn.close()
        self.fenetre.destroy() 
    def main():
        root = Tk()
        my_gui = Creation_Event(root)
        root.mainloop()

#=============================================================================
#                Classe pour Consulter les evenements
#      
#=============================================================================
class Consulter_Event:
    date= None
    adresse=  None
    statut=None
    def __init__(self, fenetre):
        date= tkinter.StringVar()
        adresse=  tkinter.StringVar()
        statut=tkinter.StringVar()
        self.fenetre= fenetre
        self.fenetre.title("Consultation des events")
        self.fenetre.config(background='#F6F917')
        titret=Label(self.fenetre ,text = "la liste des evenements",font= ("Algerian", 15),fg='#040000', bg='#F6F917').pack()

        conn = sqlite3.connect('myDB.db')
        cur= conn.cursor()
        req = "select * from event"
        result = cur.execute(req)
        
        # Afficher tous les evenements dans la table "event" avec Date,Adresse,Statut
        for row in result:
            date=  row[1]
            adresse=row[11]
            statut=row[4]
            Libcontect_label = Label(self.fenetre,fg='#040000', bg='#F6F917', text= "Evenement: "+row[0] )
            Libcontect_label.pack(pady=10,padx=10)
            Libcontect_label1 = Label(self.fenetre,fg='#040000', bg='#F6F917', text= "Date: "+str(date))
            Libcontect_label1.pack(pady=10,padx=10) 
            Libcontect_label3 = Label(self.fenetre,fg='#040000', bg='#F6F917', text= "Adresse: "+str(adresse) )
            Libcontect_label3.pack(pady=10,padx=10)
            Libcontect_label4 = Label(self.fenetre,fg='#040000', bg='#F6F917', text= "statut: "+str(statut))
            Libcontect_label4.pack(pady=10,padx=10)
            Libcontect_label5 = Label(self.fenetre,fg='#040000', bg='#F6F917', text= "*=================*" )
            Libcontect_label5.pack(pady=10,padx=10)
            
        conn.commit()
        conn.close()
    def main():
        root = Tk()
        my_gui = Consulter_Event(root)
        root.mainloop()
        
#=============================================================================
#                Classe pour la fenetre d'accueil pour 
#                       Le profil Autre
#=============================================================================
class Accueil_autre:
    
    def __init__(self, fenetre):
        
        self.fenetre= fenetre
        self.fenetre.title("modifier event")
        self.fenetre.config(background='#F6F917')
        self.fenetre.geometry("720x720")
        consul = Button(self.fenetre, text = "Consulter tout les evenements", bg='#040000', fg='#F6F917', font= ("Algerian", 20),command = Consulter_Event.main)
        consul.pack(expand= YES)
   
    
    def main():
        root = Tk()
        my_gui = Accueil_autre(root)
        root.mainloop()        

#=============================================================================
#                   Classe pour l'interface qui affiche 
#                       gestion d'outil pour ADMIN
#=============================================================================

class Outil:
 
    def __init__(self, fenetre):
        #declaration variables
        self.fenetre= fenetre
        self.fenetre.title("Cinéma club")
        self.fenetre.geometry("720x720")
        self.fenetre.config(background='#F6F917')
        affiche = Button(self.fenetre, text = "Ajouter un evenement " ,bg='#040000', fg='#F6F917', font= ("Algerian", 20), command= Creation_Event.main )
        modif = Button(self.fenetre, text = "Modifier un evenement", bg='#040000', fg='#F6F917', font= ("Algerian", 20), command=Modifier_User.main)
        suppr = Button(self.fenetre, text = "Supprimer un evenement", bg='#040000', fg='#F6F917', font= ("Algerian", 20), command = Supprimer_Event.main)
        consul = Button(self.fenetre, text = "Consulter un evenement", bg='#040000', fg='#F6F917', font= ("Algerian", 20), command=Consulter_Event.main)
        affiche.pack(expand= YES)
        modif.pack(expand= YES)
        suppr.pack(expand= YES)
        consul.pack(expand= YES)
    def main ():
        root = Tk()
        my_gui = Outil(root)
        root.mainloop()
        
#=============================================================================
#                   Classe pour gerer les choix de l'admin
#                       
#=============================================================================
class Accueil_admin:
 
    def __init__(self, fenetre):
        #declaration des composants de la fenetre admin 
        self.fenetre= fenetre
        self.fenetre.title("Cinéma club")
        self.fenetre.geometry("720x720")
        self.fenetre.config(background='#F6F917')
        label_title= Label(self.fenetre, text= "Cinema Club" ,fg='#040000', bg='#F6F917', font= ("Algerian", 30))
        label_title.pack(expand= YES)
        # declaration des boutons pour les choix de l'admin
        butt1 = Button(self.fenetre, text = "Gestion de l outil", bg='#040000', fg='#F6F917', font= ("Algerian", 20),command = Outil.main )
        butt2 = Button(self.fenetre, text = "Gestion de Planning", bg='#040000', fg='#F6F917', font= ("Algerian", 20), command = Planning.main)
        butt3 = Button(self.fenetre, text = "Gestion de billeterie", bg='#040000', fg='#F6F917', font= ("Algerian", 20), command= Billetrie.main)
        butt1.pack(expand = YES)
        butt2.pack(expand = YES)
        butt3.pack(expand = YES)

    def main():   
        root = Tk()
        my_gui = Accueil_admin(root)
        root.mainloop()
    
#=============================================================================
#                   class responsable pour choisir le profil   
#                       
#=============================================================================    
class Interf_connexion:
 
    def __init__(self, fenetre):
        #declaration de fenetre et different bouton
        self.fenetre= fenetre
        self.fenetre.title("Cinéma club")
        self.fenetre.geometry("720x720")
        self.fenetre.config(background='#F6F917')
        label_title= Label(fenetre, text= "Cinéma Club" , font= ("Algerian", 45) ,fg='#040000', bg='#F6F917')
        #Déclaration des bouttons pour les profils
        #User
        butt = Button(self.fenetre, text = " User",bg='#040000', fg='#F6F917', font= ("Algerian", 20), command =Login.main)
        #Admin
        butt2 = Button(self.fenetre, text = "Admin",bg='#040000', fg='#F6F917', font= ("Algerian", 20),command =Login.main )
        #Autre
        butt4 = Button(self.fenetre, text = "AUTRE",bg='#040000', fg='#F6F917', font= ("Algerian", 20), command =Accueil_autre.main )
        label_title.pack(expand= YES)
        butt.pack()
        butt2.pack()
        butt4.pack()
        

    def main ():
         
        root = Tk()
        my_gui = Interf_connexion(root)
        root.mainloop()
        
#=============================================================================
#                   class pour Supprimer un event   
#                       
#=============================================================================
class Supprimer_Event:

    def __init__(self, fenetre):    
        global user
        
        self.fenetre= fenetre
        self.fenetre.title("Supprimer event")
        self.fenetre.config(background='#F6F917')
      
        titret=Label(self.fenetre ,text = "la liste des evenements",font= ("Algerian", 15),fg='#040000', bg='#F6F917').pack()
        #user= self.Login.nomLogin()
        conn = sqlite3.connect('myDB.db')
        cur= conn.cursor()
        req = ('select * from event ')
        result = cur.execute(req )
        #Afficher les evenement cree a partir de la table de base de donées
        for row in result:
            print (row[0])
            Libcontect_label = Label(self.fenetre,fg='#040000', bg='#F6F917', text= "Evenement: "+row[0] )
            Libcontect_label.pack(pady=10,padx=10)
        conn.commit()
        conn.close()
        
        label = Label(self.fenetre ,text = "Evenement à supprimer",fg='#040000', bg='#F6F917').pack() 
        self.nom_Event = Entry(self.fenetre)
        self.nom_Event.pack() 
     
        btn = Button(self.fenetre ,text="Supprimer",fg='#040000', bg='#F6F917', command= self.suppr_evenement ).pack()    
    
    #Fonction pour supprimer l'evenement choisi
    def suppr_evenement(self):
        global Event_a_modifier
        conn = sqlite3.connect('myDB.db')
        cur= conn.cursor()
        delet_event = ('DELETE FROM event WHERE nom = ?')
        cur.execute(delet_event,[(self.nom_Event.get())])
        conn.commit()
        conn.close() 
        label = Label(self.fenetre ,text = "evenement supprimer",fg='#040000', bg='#F6F917').pack() 
        self.fenetre.destroy()
         
    def main():
        global Event_a_modifier
        root = Tk()
        my_gui = Supprimer_Event(root)
        root.mainloop()


#=============================================================================
#                   class pour le Planing des employés  
#                       
#=============================================================================
class Planning:
    total = 1
    def __init__(self, fenetre):
        self.total= tkinter.IntVar()

        self.fenetre= fenetre
        self.fenetre.title("Planning")
        self.fenetre.config(background='#F6F917')
        #titret=Label(self.fenetre ,text = "la liste des evenements",font= ("Algerian", 15),fg='#040000', bg='#F6F917').pack()
        conn = sqlite3.connect('myDB.db')
        cur= conn.cursor()
        req = "select * from Empoyé"
        result = cur.execute(req)
        #Afficher les events qui ont statu terminer
        for row in result:
            nom = row[1]
            print(nom)
            congés= row[6]
            print(congés)
            
            Libcontect_label1 = Label(self.fenetre,fg='#040000', bg='#F6F917', text= "Nom: "+nom )
            Libcontect_label1.pack(pady=10,padx=10) 
            Libcontect_label3 = Label(self.fenetre,fg='#040000', bg='#F6F917', text= "date debut de congés: "+str(congés ))
            Libcontect_label3.pack(pady=10,padx=10)
            Libcontect_label5 = Label(self.fenetre,fg='#040000', bg='#F6F917', text= "*=================*" )
            Libcontect_label5.pack(pady=10,padx=10)
            
        conn.commit()
        conn.close()
    def main():
        root = Tk()
        my_gui = Planning(root)
        root.mainloop()

#=============================================================================
#                   class pour Gestion de billetrie  
#                       
#=============================================================================
class Billetrie:
    total = 1
    def __init__(self, fenetre):
        self.total= tkinter.IntVar()

        self.fenetre= fenetre
        self.fenetre.title("Consultation des events")
        self.fenetre.config(background='#F6F917')
        titret=Label(self.fenetre ,text = "la liste des evenements",font= ("Algerian", 15),fg='#040000', bg='#F6F917').pack()
        conn = sqlite3.connect('myDB.db')
        cur= conn.cursor()
        req = "select * from event where statut= 'terminer'"#TOTOTOTOTOTO DESTER
        result = cur.execute(req)
        #Afficher les events qui ont statu terminer
        for row in result:
            prix = row[16]
            print(prix)
            place_vendu= row[17]
            print(place_vendu)
            total= prix*place_vendu #Calculer le prix total des billets vendue
            print(total)
            totalStr= str(total)
            Libcontect_label = Label(self.fenetre,fg='#040000', bg='#F6F917', text= "Evenement: "+row[0] )
            Libcontect_label.pack(pady=10,padx=10)
            Libcontect_label1 = Label(self.fenetre,fg='#040000', bg='#F6F917', text= "Prix de place: "+str(row[17]) )
            Libcontect_label1.pack(pady=10,padx=10) 
            Libcontect_label3 = Label(self.fenetre,fg='#040000', bg='#F6F917', text= "Nombre de place vendu: "+str(row[16]) )
            Libcontect_label3.pack(pady=10,padx=10)
            Libcontect_label4 = Label(self.fenetre,fg='#040000', bg='#F6F917', text= "Total de la vente: "+str(total)+"€")
            Libcontect_label4.pack(pady=10,padx=10)
            Libcontect_label5 = Label(self.fenetre,fg='#040000', bg='#F6F917', text= "*=================*" )
            Libcontect_label5.pack(pady=10,padx=10)
            
        conn.commit()
        conn.close()
    def main():
        root = Tk()
        my_gui = Billetrie(root)
        root.mainloop()
#--------------------------------------------
#         Interface d'accueil pour
#               se connecter        
#--------------------------------------------
fenetre = Tk()
fenetre.title("Cinéma club")
fenetre.geometry("720x720")
fenetre.config(background='#F6F917')
label_title= Label(fenetre, text= "Cinéma Club" , font= ("Algerian", 45) ,fg='#040000', bg='#F6F917')
# Button "Se Connecter" pour choisir le profil d'utilisateur 
butt = Button(fenetre, text = "Se connecter",bg='#040000', fg='#F6F917', font= ("Algerian", 20) ,command=  Interf_connexion.main)
label_title.pack(expand= YES)
butt.pack(pady = 25 , fill= X)
fenetre.mainloop()

