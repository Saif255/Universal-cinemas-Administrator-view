#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.13
# In conjunction with Tcl version 8.6
#    May 18, 2018 05:05:26 AM

import sys
import InsertQuries as iq

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import qsamsaylasthai_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    top = New_Toplevel (root)
    qsamsaylasthai_support.init(root, top)
    root.mainloop()

w = None
def create_New_Toplevel(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    top = New_Toplevel (w)
    qsamsaylasthai_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_New_Toplevel():
    global w
    w.destroy()
    w = None


class New_Toplevel:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font9 = "-family {Segoe UI} -size 12 -weight bold -slant roman"  \
            " -underline 0 -overstrike 0"
          
        namei = StringVar(root) 
        idi = StringVar(root)       
        yeari = StringVar(root)    
        datei = StringVar(root)      
        langi = StringVar(root)              
        idu = StringVar(root)      
        nameu = StringVar(root)      
        yearu = StringVar(root)      
        dateu = StringVar(root)       
        langu = StringVar(root)       
        delete = StringVar(root)
        
          
            

        top.geometry("1920x1001+-37+224")
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")



        self.Frame1 = Frame(top)
        self.Frame1.place(relx=0.0, rely=-0.01, relheight=0.99, relwidth=1.0)
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief=GROOVE)
        self.Frame1.configure(background="#161668")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")
        self.Frame1.configure(width=1925)

        self.Label1 = Label(self.Frame1)
        self.Label1.place(relx=0.02, rely=0.03, height=106, width=206)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#161668")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
#        self._img1 = PhotoImage(file="C:/Users/SFAdr/Desktop/android-chrome-192x192.png")
#        self.Label1.configure(image=self._img1)
#        self.Label1.configure(text='''Label''')

        self.Label2 = Label(self.Frame1)
        self.Label2.place(relx=0.43, rely=0.11, height=26, width=322)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#161668")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font=font9)
        self.Label2.configure(foreground="#ffffff")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''INSERT DATA IN THEATER TABLE''')

        self.Label3i = Label(self.Frame1)
        self.Label3i.place(relx=0.2, rely=0.2, height=36, width=92)
        self.Label3i.configure(activebackground="#f9f9f9")
        self.Label3i.configure(activeforeground="black")
        self.Label3i.configure(background="#161668")
        self.Label3i.configure(disabledforeground="#a3a3a3")
        self.Label3i.configure(foreground="#ffffff")
        self.Label3i.configure(highlightbackground="#d9d9d9")
        self.Label3i.configure(highlightcolor="black")
        self.Label3i.configure(text='''Theater ID''')

        self.Label4i = Label(self.Frame1)
        self.Label4i.place(relx=0.19, rely=0.28, height=36, width=92)
        self.Label4i.configure(activebackground="#f9f9f9")
        self.Label4i.configure(activeforeground="black")
        self.Label4i.configure(background="#161668")
        self.Label4i.configure(disabledforeground="#a3a3a3")
        self.Label4i.configure(foreground="#ffffff")
        self.Label4i.configure(highlightbackground="#d9d9d9")
        self.Label4i.configure(highlightcolor="black")
        self.Label4i.configure(text='''Name''')

        self.Label5i = Label(self.Frame1)
        self.Label5i.place(relx=0.38, rely=0.19, height=36, width=82)
        self.Label5i.configure(activebackground="#f9f9f9")
        self.Label5i.configure(activeforeground="black")
        self.Label5i.configure(background="#161668")
        self.Label5i.configure(disabledforeground="#a3a3a3")
        self.Label5i.configure(foreground="#ffffff")
        self.Label5i.configure(highlightbackground="#d9d9d9")
        self.Label5i.configure(highlightcolor="black")
        self.Label5i.configure(text='''Seats''')

        self.Label6i = Label(self.Frame1)
        self.Label6i.place(relx=0.37, rely=0.28, height=36, width=112)
        self.Label6i.configure(activebackground="#f9f9f9")
        self.Label6i.configure(activeforeground="black")
        self.Label6i.configure(background="#161668")
        self.Label6i.configure(disabledforeground="#a3a3a3")
        self.Label6i.configure(foreground="#ffffff")
        self.Label6i.configure(highlightbackground="#d9d9d9")
        self.Label6i.configure(highlightcolor="black")
        self.Label6i.configure(text='''Type ID''')

        self.Label7i = Label(self.Frame1)
        self.Label7i.place(relx=0.52, rely=0.18, height=46, width=82)
        self.Label7i.configure(activebackground="#f9f9f9")
        self.Label7i.configure(activeforeground="black")
        self.Label7i.configure(background="#161668")
        self.Label7i.configure(disabledforeground="#a3a3a3")
        self.Label7i.configure(foreground="#ffffff")
        self.Label7i.configure(highlightbackground="#d9d9d9")
        self.Label7i.configure(highlightcolor="black")
        self.Label7i.configure(text='''Screen Size''')

        self.insert_id = Entry(self.Frame1)
        self.insert_id.place(relx=0.28, rely=0.2,height=34, relwidth=0.05)
        self.insert_id.configure(background="white")
        self.insert_id.configure(disabledforeground="#a3a3a3")
        self.insert_id.configure(font="TkFixedFont")
        self.insert_id.configure(foreground="#000000")
        self.insert_id.configure(highlightbackground="#d9d9d9")
        self.insert_id.configure(highlightcolor="black")
        self.insert_id.configure(insertbackground="black")
        self.insert_id.configure(selectbackground="#c4c4c4")
        self.insert_id.configure(selectforeground="black")
        self.insert_id.configure(textvariable = idi)
        
        

        self.insert_date = Entry(self.Frame1)
        self.insert_date.place(relx=0.45, rely=0.28,height=34, relwidth=0.05)
        self.insert_date.configure(background="white")
        self.insert_date.configure(disabledforeground="#a3a3a3")
        self.insert_date.configure(font="TkFixedFont")
        self.insert_date.configure(foreground="#000000")
        self.insert_date.configure(highlightbackground="#d9d9d9")
        self.insert_date.configure(highlightcolor="black")
        self.insert_date.configure(insertbackground="black")
        self.insert_date.configure(selectbackground="#c4c4c4")
        self.insert_date.configure(selectforeground="black")
        self.insert_date.configure(width=94)
        self.insert_date.configure(textvariable = datei)

        self.insert_lang = Entry(self.Frame1)
        self.insert_lang.place(relx=0.61, rely=0.19,height=34, relwidth=0.06)
        self.insert_lang.configure(background="white")
        self.insert_lang.configure(disabledforeground="#a3a3a3")
        self.insert_lang.configure(font="TkFixedFont")
        self.insert_lang.configure(foreground="#000000")
        self.insert_lang.configure(highlightbackground="#d9d9d9")
        self.insert_lang.configure(highlightcolor="black")
        self.insert_lang.configure(insertbackground="black")
        self.insert_lang.configure(selectbackground="#c4c4c4")
        self.insert_lang.configure(selectforeground="black")
        self.insert_lang.configure(textvariable = langi)

   
        
        self.insert_name = Entry(self.Frame1)
        self.insert_name.place(relx=0.28, rely=0.28,height=34, relwidth=0.05)
        self.insert_name.configure(background="white")
        self.insert_name.configure(disabledforeground="#a3a3a3")
        self.insert_name.configure(font="TkFixedFont")
        self.insert_name.configure(foreground="#000000")
        self.insert_name.configure(highlightbackground="#d9d9d9")
        self.insert_name.configure(highlightcolor="black")
        self.insert_name.configure(insertbackground="black")
        self.insert_name.configure(selectbackground="#c4c4c4")
        self.insert_name.configure(selectforeground="black")
        self.insert_name.configure(textvariable = namei)

        self.insert_year = Entry(self.Frame1)
        self.insert_year.place(relx=0.45, rely=0.19,height=34, relwidth=0.05)
        self.insert_year.configure(background="white")
        self.insert_year.configure(disabledforeground="#a3a3a3")
        self.insert_year.configure(font="TkFixedFont")
        self.insert_year.configure(foreground="#000000")
        self.insert_year.configure(highlightbackground="#d9d9d9")
        self.insert_year.configure(highlightcolor="black")
        self.insert_year.configure(insertbackground="black")
        self.insert_year.configure(selectbackground="#c4c4c4")
        self.insert_year.configure(selectforeground="black")
        self.insert_year.configure(width=94)
        self.insert_year.configure(textvariable = yeari)
        
        

        self.Label10 = Label(self.Frame1)
        self.Label10.place(relx=0.43, rely=0.37, height=26, width=322)
        self.Label10.configure(activebackground="#f9f9f9")
        self.Label10.configure(activeforeground="black")
        self.Label10.configure(background="#161668")
        self.Label10.configure(disabledforeground="#a3a3a3")
        self.Label10.configure(font=font9)
        self.Label10.configure(foreground="#ffffff")
        self.Label10.configure(highlightbackground="#d9d9d9")
        self.Label10.configure(highlightcolor="black")
        self.Label10.configure(text='''UPDATE DATA IN THEATER TABLE''')

        self.Label11 = Label(self.Frame1)
        self.Label11.place(relx=0.19, rely=0.55, height=36, width=102)
        self.Label11.configure(activebackground="#f9f9f9")
        self.Label11.configure(activeforeground="black")
        self.Label11.configure(background="#161668")
        self.Label11.configure(disabledforeground="#a3a3a3")
        self.Label11.configure(foreground="#ffffff")
        self.Label11.configure(highlightbackground="#d9d9d9")
        self.Label11.configure(highlightcolor="black")
        self.Label11.configure(text='''Seats''')
        self.Label11.configure(width=102)

        self.Label12 = Label(self.Frame1)
        self.Label12.place(relx=0.19, rely=0.45, height=36, width=82)
        self.Label12.configure(activebackground="#f9f9f9")
        self.Label12.configure(activeforeground="black")
        self.Label12.configure(background="#161668")
        self.Label12.configure(disabledforeground="#a3a3a3")
        self.Label12.configure(foreground="#ffffff")
        self.Label12.configure(highlightbackground="#d9d9d9")
        self.Label12.configure(highlightcolor="black")
        self.Label12.configure(text='''Name''')
        self.Label12.configure(width=82)

        self.Label13u = Label(self.Frame1)
        self.Label13u.place(relx=0.36, rely=0.55, height=36, width=102)
        self.Label13u.configure(activebackground="#f9f9f9")
        self.Label13u.configure(activeforeground="black")
        self.Label13u.configure(background="#161668")
        self.Label13u.configure(disabledforeground="#a3a3a3")
        self.Label13u.configure(foreground="#ffffff")
        self.Label13u.configure(highlightbackground="#d9d9d9")
        self.Label13u.configure(highlightcolor="black")
        self.Label13u.configure(text='''Type id''')
        self.Label13u.configure(width=102)

        self.Label14 = Label(self.Frame1)
        self.Label14.place(relx=0.57, rely=0.49, height=36, width=72)
        self.Label14.configure(activebackground="#f9f9f9")
        self.Label14.configure(activeforeground="black")
        self.Label14.configure(background="#161668")
        self.Label14.configure(disabledforeground="#a3a3a3")
        self.Label14.configure(foreground="#ffffff")
        self.Label14.configure(highlightbackground="#d9d9d9")
        self.Label14.configure(highlightcolor="black")
        self.Label14.configure(text='''Theater ID    =''')
        self.Label14.configure(width=72)


        self.Label16 = Label(self.Frame1)
        self.Label16.place(relx=0.53, rely=0.49, height=36, width=62)
        self.Label16.configure(activebackground="#f9f9f9")
        self.Label16.configure(activeforeground="black")
        self.Label16.configure(background="#161668")
        self.Label16.configure(disabledforeground="#a3a3a3")
        self.Label16.configure(foreground="#ffffff")
        self.Label16.configure(highlightbackground="#d9d9d9")
        self.Label16.configure(highlightcolor="black")
        self.Label16.configure(text='''Where''')
        self.Label16.configure(width=62)



        self.Label18u = Label(self.Frame1)
        self.Label18u.place(relx=0.36, rely=0.45, height=36, width=102)
        self.Label18u.configure(activebackground="#f9f9f9")
        self.Label18u.configure(activeforeground="black")
        self.Label18u.configure(background="#161668")
        self.Label18u.configure(disabledforeground="#a3a3a3")
        self.Label18u.configure(foreground="#ffffff")
        self.Label18u.configure(highlightbackground="#d9d9d9")
        self.Label18u.configure(highlightcolor="black")
        self.Label18u.configure(text='''Screen size''')
        self.Label18u.configure(width=102)

        self.update_name = Entry(self.Frame1)
        self.update_name.place(relx=0.28, rely=0.45,height=34, relwidth=0.05)
        self.update_name.configure(background="white")
        self.update_name.configure(disabledforeground="#a3a3a3")
        self.update_name.configure(font="TkFixedFont")
        self.update_name.configure(foreground="#000000")
        self.update_name.configure(highlightbackground="#d9d9d9")
        self.update_name.configure(highlightcolor="black")
        self.update_name.configure(insertbackground="black")
        self.update_name.configure(selectbackground="#c4c4c4")
        self.update_name.configure(selectforeground="black")
        self.update_name.configure(width=104)
        self.update_name.configure(textvariable = nameu)


        self.update_year = Entry(self.Frame1)
        self.update_year.place(relx=0.28, rely=0.55,height=34, relwidth=0.05)
        self.update_year.configure(background="white")
        self.update_year.configure(disabledforeground="#a3a3a3")
        self.update_year.configure(font="TkFixedFont")
        self.update_year.configure(foreground="#000000")
        self.update_year.configure(highlightbackground="#d9d9d9")
        self.update_year.configure(highlightcolor="black")
        self.update_year.configure(insertbackground="black")
        self.update_year.configure(selectbackground="#c4c4c4")
        self.update_year.configure(selectforeground="black")
        self.update_year.configure(width=104)
        self.update_year.configure(textvariable = yearu)

        self.update_date = Entry(self.Frame1)
        self.update_date.place(relx=0.44, rely=0.45,height=34, relwidth=0.05)
        self.update_date.configure(background="white")
        self.update_date.configure(disabledforeground="#a3a3a3")
        self.update_date.configure(font="TkFixedFont")
        self.update_date.configure(foreground="#000000")
        self.update_date.configure(highlightbackground="#d9d9d9")
        self.update_date.configure(highlightcolor="black")
        self.update_date.configure(insertbackground="black")
        self.update_date.configure(selectbackground="#c4c4c4")
        self.update_date.configure(selectforeground="black")
        self.update_date.configure(width=104)
        self.update_date.configure(textvariable = dateu)

        self.update_lang = Entry(self.Frame1)
        self.update_lang.place(relx=0.44, rely=0.55,height=34, relwidth=0.05)
        self.update_lang.configure(background="white")
        self.update_lang.configure(disabledforeground="#a3a3a3")
        self.update_lang.configure(font="TkFixedFont")
        self.update_lang.configure(foreground="#000000")
        self.update_lang.configure(highlightbackground="#d9d9d9")
        self.update_lang.configure(highlightcolor="black")
        self.update_lang.configure(insertbackground="black")
        self.update_lang.configure(selectbackground="#c4c4c4")
        self.update_lang.configure(selectforeground="black")
        self.update_lang.configure(width=104)
        self.update_lang.configure(textvariable = langu)


        self.update_id = Entry(self.Frame1)
        self.update_id.place(relx=0.65, rely=0.49,height=34, relwidth=0.05)
        self.update_id.configure(background="white")
        self.update_id.configure(disabledforeground="#a3a3a3")
        self.update_id.configure(font="TkFixedFont")
        self.update_id.configure(foreground="#000000")
        self.update_id.configure(highlightbackground="#d9d9d9")
        self.update_id.configure(highlightcolor="black")
        self.update_id.configure(insertbackground="black")
        self.update_id.configure(selectbackground="#c4c4c4")
        self.update_id.configure(selectforeground="black")
        self.update_id.configure(width=104)
        self.update_id.configure(textvariable = idu)

        self.Label19 = Label(self.Frame1)
        self.Label19.place(relx=0.39, rely=0.65, height=46, width=362)
        self.Label19.configure(activebackground="#f9f9f9")
        self.Label19.configure(activeforeground="black")
        self.Label19.configure(background="#161668")
        self.Label19.configure(disabledforeground="#a3a3a3")
        self.Label19.configure(font=font9)
        self.Label19.configure(foreground="#ffffff")
        self.Label19.configure(highlightbackground="#d9d9d9")
        self.Label19.configure(highlightcolor="black")
        self.Label19.configure(text='''DELETE DATA FROM THEATER TABLE''')
        self.Label19.configure(width=362)

        self.Label20 = Label(self.Frame1)
        self.Label20.place(relx=0.2, rely=0.76, height=46, width=102)
        self.Label20.configure(activebackground="#f9f9f9")
        self.Label20.configure(activeforeground="black")
        self.Label20.configure(background="#161668")
        self.Label20.configure(disabledforeground="#a3a3a3")
        self.Label20.configure(foreground="#ffffff")
        self.Label20.configure(highlightbackground="#d9d9d9")
        self.Label20.configure(highlightcolor="black")
        self.Label20.configure(text='''FROM''')
        self.Label20.configure(width=102)

        self.Label21 = Label(self.Frame1)
        self.Label21.place(relx=0.29, rely=0.76, height=46, width=92)
        self.Label21.configure(activebackground="#f9f9f9")
        self.Label21.configure(activeforeground="black")
        self.Label21.configure(background="#161668")
        self.Label21.configure(disabledforeground="#a3a3a3")
        self.Label21.configure(foreground="#ffffff")
        self.Label21.configure(highlightbackground="#d9d9d9")
        self.Label21.configure(highlightcolor="black")
        self.Label21.configure(text='''Theater''')
        self.Label21.configure(width=92)

        self.Label22 = Label(self.Frame1)
        self.Label22.place(relx=0.37, rely=0.75, height=56, width=92)
        self.Label22.configure(activebackground="#f9f9f9")
        self.Label22.configure(activeforeground="black")
        self.Label22.configure(background="#161668")
        self.Label22.configure(disabledforeground="#a3a3a3")
        self.Label22.configure(foreground="#ffffff")
        self.Label22.configure(highlightbackground="#d9d9d9")
        self.Label22.configure(highlightcolor="black")
        self.Label22.configure(text='''WHERE''')
        self.Label22.configure(width=92)

        self.Label23 = Label(self.Frame1)
        self.Label23.place(relx=0.44, rely=0.76, height=36, width=92)
        self.Label23.configure(activebackground="#f9f9f9")
        self.Label23.configure(activeforeground="black")
        self.Label23.configure(background="#161668")
        self.Label23.configure(disabledforeground="#a3a3a3")
        self.Label23.configure(foreground="#ffffff")
        self.Label23.configure(highlightbackground="#d9d9d9")
        self.Label23.configure(highlightcolor="black")
        self.Label23.configure(text='''Theater ID''')
        self.Label23.configure(width=92)

        self.Label24 = Label(self.Frame1)
        self.Label24.place(relx=0.49, rely=0.76, height=36, width=92)
        self.Label24.configure(activebackground="#f9f9f9")
        self.Label24.configure(activeforeground="black")
        self.Label24.configure(background="#161668")
        self.Label24.configure(disabledforeground="#a3a3a3")
        self.Label24.configure(foreground="#ffffff")
        self.Label24.configure(highlightbackground="#d9d9d9")
        self.Label24.configure(highlightcolor="black")
        self.Label24.configure(text='''=''')
        self.Label24.configure(width=92)

        self.delete_id = Entry(self.Frame1)
        self.delete_id.place(relx=0.57, rely=0.76,height=34, relwidth=0.06)
        self.delete_id.configure(background="white")
        self.delete_id.configure(disabledforeground="#a3a3a3")
        self.delete_id.configure(font="TkFixedFont")
        self.delete_id.configure(foreground="#000000")
        self.delete_id.configure(highlightbackground="#d9d9d9")
        self.delete_id.configure(highlightcolor="black")
        self.delete_id.configure(insertbackground="black")
        self.delete_id.configure(selectbackground="#c4c4c4")
        self.delete_id.configure(selectforeground="black")
        self.delete_id.configure(width=124)
        self.delete_id.configure(textvariable = delete)
        
        
        def insert():
            print("in insert")
            print(idi.get(), namei.get() , datei.get() ,yeari.get() , langi.get())
            iq.InsertQuries.theaterInsert(idi, namei , datei ,yeari , langi)
                                  #theateridI  nameI   typeidI   seatI sreenSizeI
            
            return
        
        def update():
            print("in update")
            print(idi.get(), namei.get() , datei.get() ,yeari.get() , langi.get())
            iq.InsertQuries.theaterUpdate(idu, nameu , dateu ,yearu , langu)
            #                             nameU , sizeU , typeidU, seatsU, theateridU
            return
        
        

        self.Button1 = Button(self.Frame1)
        self.Button1.place(relx=0.72, rely=0.34, height=33, width=116)
        self.Button1.configure(activebackground="#d9d9d9")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#a6d8c7")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''INSERT''')
        self.Button1.configure(width=116)
        self.Button1.configure(command = insert)

        self.Button2 = Button(self.Frame1)
        self.Button2.place(relx=0.72, rely=0.61, height=33, width=116)
        self.Button2.configure(activebackground="#d9d9d9")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d88aa4")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''UPDATE''')
        self.Button2.configure(width=116)
        self.Button2.configure(command  = update)


        def getDelete():
            iq.InsertQuries.theaterDelete(delete)
            return
            
        self.Button3 = Button(self.Frame1)
        self.Button3.place(relx=0.72, rely=0.81, height=33, width=126)
        self.Button3.configure(activebackground="#d9d9d9")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d572d8")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''DELETE''')
        self.Button3.configure(width=126)
        self.Button3.configure(command = getDelete)

        




if __name__ == '__main__':
    vp_start_gui()



