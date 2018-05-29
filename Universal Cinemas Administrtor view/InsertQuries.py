# -*- coding: utf-8 -*-
"""
Created on Thu May 10 00:34:42 2018

@author: SFAdr
"""
import pymysql





class InsertQuries:
    
    def directInsert(ment):
        
        
      conn = pymysql.connect(host='127.0.0.1',user='root',password='root',db='Universal_Cinema12')
      a = conn.cursor()
      
      
      mtext = ment.get()
      try:
         a.execute(mtext)
         conn.commit()
      except:
         conn.rollback()
         
         
      data = a.fetchall()
      conn.close()
      
      return data
  
    
    
    def columnInsert(idi, namei , genrei , datei ,yeari , langi ,ratingi):
        
        conn = pymysql.connect(host='127.0.0.1',user='root',password='root',db='Universal_Cinema12')
        a = conn.cursor()        

        ID = idi.get()
        name  = namei.get()
        genre = genrei.get()
        date = datei.get()
        year = yeari.get()
        lang = langi.get()
        rating1 = ratingi.get()
        
        print(ID + name + genre + date + year + lang + rating1);
        
        s_id =  str(ID)
      #  date = str(date)
       # year = str(year)
        rating = str(rating1)
        
        str1 = "insert into Movies values(" 
        str2 = str1 + s_id 
        str3 = str2 + "," +"\"" + name +"\"" + "," + "\"" + year  + "\"" +"," + "\"" + date + "\"" + "," + "\"" + lang + "\"" + "," + "\"" + genre + "\"" +"," + rating + ");"
       
        print(str3)
        try:
            
         a.execute(str3)
         conn.commit()
        except:
            conn.rollback()
            
        conn.close()    
        print("Done")
        return 
    
    
    def columnUpdate(idu, nameu , genreu , dateu ,yearu , langu ,ratingu):
        
        
        conn = pymysql.connect(host='127.0.0.1',user='root',password='root',db='Universal_Cinema12')
        a = conn.cursor()       
        ID = idu.get()
        name = nameu.get()
        genre = genreu.get()
        date = dateu.get()
        year = yearu.get()
        lang = langu.get()
        rating = ratingu.get()
        
        s_id =  str(ID)
        rating1 = str(rating)
        
        
        str1 = "UPDATE movies SET NAME = "+ "\"" + name + "\"" + ", Yearr = " + "\""+ year + "\"" + ", Releasing_Date = " + "\""+ date + "\""+ ", Language = "+ "\"" + lang + "\""+ ", Genre = " + "\""+ genre + "\"" + ", FeedBack_Rating = " + rating1 + " WHERE ID = " + s_id + ";"
        
        print(str1)
        try:
            
         a.execute(str1)
         conn.commit()
         
        except:
           conn.rollback()
           
        conn.close()
        print("DONE")
        return
    
    def columnDelete(id):
       
        conn = pymysql.connect(host='127.0.0.1',user='root',password='root',db='Universal_Cinema12')
        a = conn.cursor()        
        
        i_d = str(id.get())
        
        str1 = "DELETE FROM Movies WHERE id = " + i_d + ";"
        print(str1)
        
        try:
            
          a.execute(str1)
          conn.commit()
        except:
         conn.rollback()
         
        conn.close 
        print("DONE")
        return
    
    def  init():
        
       conn = pymysql.connect(host='127.0.0.1',user='root',password='root',db='Universal_Cinema12')
              
       return conn 
        
        
        
    def ticketColumnInsert(ticketid , custid, movieid , seati , datei  ,theateri):
        
        conn = InsertQuries.init()
        a = conn.cursor()
        
        tikid = ticketid.get()
        ID = custid.get()
        mov  = movieid.get()
        date = datei.get()
        seat = seati.get()
        theater = theateri.get()
        
       
        tid = str(tikid)
        se = str(seat)
        s_id =  str(ID)
        movid = str(mov)
        the = str(theater)
        
        str1 = "insert into Tickets values(" 
        str2 = str1 + tid +","+ s_id 
        str3 = str2 + ","+ movid + "," + "\"" + date  + "\"" +"," + the +  ","+ se + ");"
       
        print(str3)
        try:
            
          a.execute(str3)
          conn.commit()
        except:
            conn.rollback()
        
        conn.close()
        print("Done")
        return 
    
    
    def ticketUpdate(ticketid , custid, movieid , seati , datei  ,theateri):
        
        conn = InsertQuries.init()
        a = conn.cursor()
        
        tikid = ticketid.get()
        ID = custid.get()
        mov  = movieid.get()
        date = datei.get()
        seat = seati.get()
        theater = theateri.get()
        
       
        tid = str(tikid)
        se = str(seat)
        s_id =  str(ID)
        movid = str(mov)
        the = str(theater)
        
        print(tid + se + s_id + movid + the + date)
        
        
        str1 = "UPDATE Tickets SET Ticket_ID = " + tid   + ", Movie_ID = " +  movid +  ", Time_Date = "+ "\"" + \
               date + "\""+ ", Theater_ID = " +  the  + ", Seat_No = " + se + " WHERE Customer_ID = " + s_id + ";"
        
        print(str1)
        try:
            
           a.execute(str1)
           conn.commit()
        except:
            conn.rollback()
            
        conn.close()    
        print("DONE")
        return
    
    def ticketDelete(id):
        
        conn = InsertQuries.init()
        a = conn.cursor()
        
        
        i_d = str(id.get())
        
        str1 = "DELETE FROM Tickets WHERE Customer_ID = " + i_d + ";"
        print(str1)
        try:
            a.execute(str1)
            conn.commit()
        except:
            conn.rollback()
            
        conn.close()
        
        print("DONE")
        return
    
    
    
    def empColumnInsert(empidI , cnicI , salaryI , jobI , nameI ,addressI):
        
        conn = InsertQuries.init()
        a = conn.cursor()
        
        empid = empidI.get()
        ID = cnicI.get()
        mov  = salaryI.get()
        date = jobI.get()
        seat = nameI.get()
        address = addressI.get()
        
        
        tid = str(empid)
        sal = str(mov)
        
        
        str1 = "insert into Employee values(" 
        str2 = str1 + tid +","+ "\"" + seat + "\""
        str3 = str2 + ","+"\"" +  ID + "\"" + ","  + sal  +"," + "\"" + date + "\""  + ","+"\""+ address + "\""+");"
       
        print(str3)
        try:
            
          a.execute(str3)
          conn.commit()
        except:
            conn.rollback()
        
        conn.close()
        
        print("Done")
        return 
    
    
    
    def empUpdate( empidI , nameI  , salaryI    ,  cnicI      ,  jobI  ,  addressI):
    
        conn = InsertQuries.init()
        a = conn.cursor()
        
        empid = empidI.get()
        ID = cnicI.get()
        mov  = salaryI.get()
        date = jobI.get()
        seat = nameI.get()
        address = addressI.get()
        
        
        tid = str(empid)
        sal = str(mov)
        
       # (ID,Name,CNIC,Salary,Job,Address
        
        
        str1 = "UPDATE Employee SET Name = " + "\"" + seat  +"\"" + ", CNIC = "  + "\"" + ID +"\"" + ", Salary = "+  \
               sal + ", job = " + "\"" +  date+"\""  + ", Address = " + "\""+address+"\"" + " WHERE ID = " + tid + ";"
        
        print(str1)
        a.execute(str1)
        print("DONE")
        return
    
    
    def empDelete(id):
        conn = InsertQuries.init()
        a = conn.cursor()
        
        
        i_d = str(id.get())
        
        str1 = "DELETE FROM Employee WHERE ID = " + i_d + ";"
        print(str1)
        try:
            a.execute(str1)
            conn.commit()
        except:
            conn.rollback()
            
        conn.close()
        
        print("DONE")
        return
    
    
    
    def theaterInsert(theateridI , nameI ,  typeidI ,  seatI ,sreenSizeI):
        
        conn = InsertQuries.init()
        a = conn.cursor()
        
        empid = theateridI.get()
        ID = nameI.get()
        mov  = typeidI.get()
        date = seatI.get()
        seat = sreenSizeI.get()
        
        
        
        tid = str(empid)
        sal = str(mov)
        seatNO = str(date)
        size = str(seat)
        #Theater_ID,Name,Seats,Type_ID,Screen_Size_ft
        
        str1 = "insert into Theater values(" 
        str2 = str1 + tid +","+ "\"" + ID + "\""
        str3 = str2 + ","  +  seatNO  + ","  + sal  +","  + size +");"
       
        print(str3)
        try:
            
          a.execute(str3)
          conn.commit()
        except:
            conn.rollback()
        
        conn.close()
        
        print("Done")
        return
    
    def theaterUpdate(nameU , sizeU , typeidU, seatsU, theateridU):
    
        conn = InsertQuries.init()
        a = conn.cursor()
        
        empid = theateridU.get()
        ID = nameU.get()
        mov  = typeidU.get()
        date = seatsU.get()
        seat = sizeU.get()
        
        
        
        tid = str(empid)
        sal = str(mov)
        seatNO = str(date)
        size = str(seat)
        
         #Theater_ID,Name,Seats,Type_ID,Screen_Size_ft
        
        
        str1 = "UPDATE Theater SET Name = " + "\"" + size  +"\"" + ", Seats = " + seatNO + ", Type_ID = "+  \
               tid + ", Screen_Size_ft = "+  sal + " WHERE Theater_ID = " + ID + ";"
        
        print(str1)
        a.execute(str1)
        print("DONE")
        return
    
    
    def theaterDelete(id):
        conn = InsertQuries.init()
        a = conn.cursor()
        
        
        i_d = str(id.get())
        
        str1 = "DELETE FROM Theater WHERE Theater_ID = " + i_d + ";"
        print(str1)
        try:
            a.execute(str1)
            conn.commit()
        except:
            conn.rollback()
            
        conn.close()
        
        print("DONE")
        return
    
    
    
    def castInsert(idI , nameI ):
        
        conn = InsertQuries.init()
        a = conn.cursor()
        
        empid = idI.get()
        ID = nameI.get()
       
        
        
        
        tid = str(empid)
        
        
        str1 = "insert into Castt values(" 
        str2 = str1 + tid +","+ "\"" + ID + "\""  +");"
        
       
        print(str2)
        try:
            
          a.execute(str2)
          conn.commit()
        except:
            conn.rollback()
        
        conn.close()
        
        print("Done")
        return
    
    def castUpdate(nameU , idU):
    
        conn = InsertQuries.init()
        a = conn.cursor()
        
        empid = idU.get()
        ID = nameU.get()
       
        
        
        
        tid = str(empid)
        
        
         #Theater_ID,Name,Seats,Type_ID,Screen_Size_ft
        
        
        str1 = "UPDATE Castt SET Name = " + "\"" + tid + "\""+ " WHERE Movie_ID = " + ID + ";"
        
        print(str1)
        a.execute(str1)
        print("DONE")
        return
    
    
    def castDelete(id):
        conn = InsertQuries.init()
        a = conn.cursor()
        
        
        i_d = str(id.get())
        
        str1 = "DELETE FROM Castt WHERE Movie_ID = " + i_d + ";"
        print(str1)
        try:
            a.execute(str1)
            conn.commit()
        except:
            conn.rollback()
            
        conn.close()
        
        print("DONE")
        return
    
    
    def customerInsert(idI , nameI ):
        
        conn = InsertQuries.init()
        a = conn.cursor()
        
        empid = idI.get()
        ID = nameI.get()
       
        
        
        
        tid = str(empid)
        
        
        str1 = "insert into Customer values(" 
        str2 = str1 + tid +","+ "\"" + ID + "\""  +");"
        
       
        print(str2)
        try:
            
          a.execute(str2)
          conn.commit()
        except:
            conn.rollback()
        
        conn.close()
        
        print("Done")
        return
    
    def customerUpdate(nameU , idU):
    
        conn = InsertQuries.init()
        a = conn.cursor()
        
        empid = idU.get()
        ID = nameU.get()
       
        
        
        
        tid = str(empid)
        
        
         #Theater_ID,Name,Seats,Type_ID,Screen_Size_ft
        
        
        str1 = "UPDATE Customer SET CNIC = " + "\"" + tid + "\""+ " WHERE ID = " + ID + ";"
        
        print(str1)
        a.execute(str1)
        print("DONE")
        return
    
    
    def customerDelete(id):
        conn = InsertQuries.init()
        a = conn.cursor()
        
        
        i_d = str(id.get())
        
        str1 = "DELETE FROM Customer WHERE ID = " + i_d + ";"
        print(str1)
        try:
            a.execute(str1)
            conn.commit()
        except:
            conn.rollback()
            
        conn.close()
        
        print("DONE")
        return
        
        
        
