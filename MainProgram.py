from tkinter import *
import pyorient

client = pyorient.OrientDB("localhost", 2424)
#session_id

class Window(Frame):
     def __init__(self, master = None):
          Frame.__init__(self, master)
          self.master = master
          self.dbname = ""
          self.uname = Entry()
          self.pwd = Entry()
          self.item = Entry()
          self.t_name = Entry()
          self.init_button()
          self.mydb = []
     def init_button(self):
          self.widg_dest()
          #Window Stuff
          self.master.title('Football Club Management.exe')
          self.pack(fill = BOTH, expand = 1)

          #Heading
          #heading =  Label(self, text="Football Club Management")
          #heading.grid(column=250,row=0)

          #Buttons
          quitButton = Button(self, text = 'Quit', command = self.exit)
          submitButton = Button(self, text="Submit", command = self.login)

          #database Login
          dbntext = Label(self, text="Database Name")
          dbntext.grid(column=0,row =1)
          self.dbname = Entry(self)
          self.dbname.grid(column=1,row=1)

          utext=  Label(self, text="Username")
          utext.grid(column=0,row=2)
          self.uname = Entry(self)
          self.uname.grid(column=1,row=2)

          pwtext =  Label(self, text="Password")
          pwtext.grid(column=0,row=3)
          self.pwd = Entry(self)
          self.pwd.grid(column=1,row=3)

          #Button Positions
          quitButton.grid(column = 500, row = 500)
          submitButton.grid(column= 0,row= 4)

     def login(self):
          try:
               self.mydb = client.db_open(self.dbname.get(),self.uname.get(),self.pwd.get())
               data = client.query("select from player")
               self.login_success()
          except:
               self.login_failed()
               #self.init_button()
     def clrscr(self):
          for widget in self.winfo_children():
               widget.destroy()
     def exit(self):
          root.destroy()
          sys.exit()
     def login_success(self):
          self.widg_dest()
          #Window Stuff
          self.master.title('Football Club Management.exe')
          self.pack(fill = BOTH, expand = 1)

          #Heading
          heading =  Label(self, text="Login Successful. Press Next to proceed: ")
          heading.grid(column=0,row=0)

          #Button
          nextButton = Button(self, text = 'Next', command = self.table_works)
          nextButton.grid(column = 0, row = 2)
     def login_failed(self):  
          self.widg_dest()
          #Window Stuff
          self.master.title('Football Club Management.exe')
          self.pack(fill = BOTH, expand = 1)

          #Heading
          heading =  Label(self, text="Login Failed. Press Next to try again.")
          heading.grid(column=0,row=0)

          #Button
          nextButton = Button(self, text = 'Next', command = self.init_button)
          nextButton.grid(column = 0, row = 2)
     def table_works(self):
          self.widg_dest()
          #Window Stuff
          self.master.title('Football Club Management.exe')
          self.pack(fill = BOTH, expand = 1)

          #Heading
          heading =  Label(self, text = "What table would you like to work with?")
          heading2 = Label(self, text = "Click on List to view the tables available.")
          heading.grid(column = 0,row = 0)
          heading2.grid(column = 0, row = 1)
          listButton = Button(self, text = "List", command = self.list_func)
          listButton.grid(column = 0, row = 4)
          
          #Getting input
          t_text=  Label(self, text="Table Name: ")
          t_text.grid(column = 0,row = 2)
          self.t_name = Entry(self)
          self.t_name.grid(column = 1, row = 2)
          
          #Button
          nextButton = Button(self, text = 'Next', command = self.table_check)
          nextButton.grid(column = 1, row = 4)
     def table_check(self):
          table_name = ['']*len(self.mydb)
          for i in range(len(self.mydb)):
              table_name[i] = str(self.mydb[i]).split("'")[1]
          if self.t_name.get() not in table_name:
               self.table_not_found()
          else:
               self.menu()
     def widg_dest(self):
          for widget in self.winfo_children():
               widget.grid_forget()
     def table_not_found(self):
          self.widg_dest()
          #Window Stuff
          self.master.title('Football Club Management.exe')
          self.pack(fill = BOTH, expand = 1)

          #Heading
          heading =  Label(self, text="Table does not exist. Please enter another table name.")
          heading.grid(column=0,row=0)

          #Button
          nextButton = Button(self, text = 'Enter another table name', command = self.table_works)
          nextButton.grid(column = 0, row = 2)
     def menu(self):
          self.widg_dest()
          #Window Stuff
          self.master.title('Football Club Management.exe')
          self.pack(fill = BOTH, expand = 1)
          
          #Buttons
          addButton = Button(self, text = 'ADD', command = self.add_func)
          modifyButton = Button(self, text = 'MODIFY', command = self.modify_func)
          viewButton = Button(self, text = 'VIEW', command = self.view_func)
          deleteButton = Button(self, text = 'DELETE', command = self.delete_func)
          searchButton = Button(self, text = 'SEARCH', command = self.search_func)
          editButton = Button(self, text = 'EDIT(modify/delete)', command = self.edit_func)
          quitButton = Button(self, text = 'Quit', command = self.exit)
          backButton = Button(self, text = "Back", command = self.table_works)

          #Button Position
          backButton.grid(column = 7, row = 11)
          quitButton.grid(column = 5, row = 11)
          addButton.grid(column = 5, row = 3)
          viewButton.grid(column = 5, row = 5)
          editButton.grid(column = 5, row = 7)
          searchButton.grid(column = 5, row = 9)
     def add_func(self):
          self.widg_dest()
          #Window Stuff
          self.master.title('Football Club Management - ADD')
          self.pack(fill = BOTH, expand = 1)
          
          dbkeys = client.query("select from " + self.t_name.get())
          dbrec = dbkeys[0].oRecordData
          dbkeys = list(dbrec.keys())
          Label_list = ['']*len(dbkeys)
          entry_list = ['']*len(dbkeys)
          r = 1
          for i in range(len(dbkeys)):
               Label_list[i] = Label(self, text = dbkeys[i])
               Label_list[i].grid(column = 0, row = r)
               entry_list[i] = Entry(self)
               entry_list[i].grid(column = 2, row = r)
               r += 1
          
          def upadd():
               try:
                    d = dict()
                    cid=-1
                    for i in range(len(dbkeys)):
                         d[str(dbkeys[i])] = type(dbrec[str(dbkeys[i])])(entry_list[i].get())
                    for i in range(len(self.mydb)):
                         if self.t_name.get() == str(self.mydb[i]).split("'")[1]:
                              cid=int(str(self.mydb[i]).split("'")[2].split(' ')[1])
                              break
                    client.record_create(cid,d)
                    self.widg_dest()
                    #Heading
                    heading =  Label(self, text="Added Successfully")
                    heading.grid(column=0,row=0)

                    #Button
                    nextButton = Button(self, text = 'Continue', command = self.menu)
                    nextButton.grid(column = 0, row = 2)
               except:
                    self.widg_dest()
                    #Heading
                    heading =  Label(self, text="Error. Please try again.")
                    heading.grid(column=0,row=0)

                    #Button
                    nextButton = Button(self, text = 'Try again', command = self.add_func)
                    nextButton.grid(column = 0, row = 2)
          backButton = Button(self, text = 'Back', command = self.menu)
          backButton.grid(column = 3, row = r)
          submitButton = Button(self, text="Submit", command = upadd)
          submitButton.grid(column = 5, row = r)                                   
     def modify_func(self):
          self.widg_dest()
          #Window Stuff
          self.master.title('Football Club Management - DELETE')
          self.pack(fill = BOTH, expand = 1)
          backButton = Button(self, text = 'Back', command = self.menu)
          backButton.grid(column = 4, row = 21)
     def list_func(self):
          self.widg_dest()
          #Window Stuff
          self.master.title('Football Club Management - LIST')
          self.pack(fill = BOTH, expand = 1)
          label_list = ['']*len(self.mydb)
          c = 1
          r = 1
          for i in range(len(self.mydb)):
              label_list[i] = Label(self,text=str(self.mydb[i]).split("'")[1])
              label_list[i].grid(column = c, row = r)
              r += 1
              if r%20 == 0:
                   c += 1
                   r = 1
          backButton = Button(self, text = 'Back', command = self.table_works)
          backButton.grid(column = 4, row = 21)
     def view_func(self):
          self.widg_dest()
          #Window Stuff
          self.master.title('Football Club Management - VIEW')
          self.pack(fill = BOTH, expand = 1)
          tab_data = client.query("select from " + self.t_name.get())
          rec_list = ['']*len(tab_data)
          '''for i in range(len(tab_data)):
               rec_list[i] = Label(self,text=str(tab_data[i].oRecordData))
               rec_list[i].grid(column = 0, row = c)
               c += 1'''
          for k in range(len(tab_data[0].oRecordData.keys())):
               head = Label(self, text = str(list(tab_data[0].oRecordData.keys())[k]))
               head.grid(column = k + 1, row = 1)
          for k in range(len(tab_data)):
               for j in range(len(tab_data[0].oRecordData.keys())):
                    body = Label(self, text = str(tab_data[k].oRecordData[str(list(tab_data[0].oRecordData.keys())[j])]))
                    body.grid(column = j+1, row = k+2)
          backButton = Button(self, text = 'Back', command = self.menu)
          backButton.grid(column = 3, row = len(tab_data) + 2)
     def delete_func(self):
          self.widg_dest()
          #Window Stuff
          self.master.title('Football Club Management - DELETE')
          self.pack(fill = BOTH, expand = 1)
          backButton = Button(self, text = 'Back', command = self.menu)
          backButton.grid(column = 4, row = 21)
     def existing(self):
          self.widg_dest()
          tab_data = client.query("select from "+self.t_name.get())
          t=0
          chk = 0
          for i in tab_data:
               #print(list(i.oRecordData.values()))
               if self.item.get() in list(i.oRecordData.values()):
                    #print("##"+str(i.oRecordData))
                    texte = Label(self, text = str(i.oRecordData))
                    texte.grid(column = 0, row = t)
                    t+=1
                    chk = 1
          if chk != 1:
               textf = Label(self, text = "Search entry not found")
               textf.grid(column = 0, row = 0)

          backButton = Button(self, text = 'Back', command = self.menu)
          backButton.grid(column = 0, row = 15)
     def search_func(self):
          self.widg_dest()
          #Window Stuff

          
          self.master.title('Football Club Management - SEARCH')
          self.pack(fill = BOTH, expand = 1)

          text = Label(self, text = "Enter the item to search in the table")
          text.grid(column = 0, row = 0)
          self.item = Entry(self)
          self.item.grid(column = 1, row = 0)

          search1Button = Button(self, text = 'Search', command = self.existing)
          search1Button.grid(column = 4, row = 19)
          
          backButton = Button(self, text = 'Back', command = self.menu)
          backButton.grid(column = 4, row = 21)
          
     def edit_func(self):
          self.widg_dest()
          #Window Stuff
          self.master.title('Football Club Management - EDIT(modify/delete')
          self.pack(fill = BOTH, expand = 1)

          #View
          tab_data = client.query("select from " + self.t_name.get())
          rec_list = ['']*len(tab_data)

          for k in range(len(tab_data[0].oRecordData.keys())):
               head = Label(self, text = str(list(tab_data[0].oRecordData.keys())[k]))
               head.grid(column = k + 1, row = 1)
          for k in range(len(tab_data)):
                              
               #Buttons
               modifyButton = Button(self, text = 'Modify', command = lambda k=k: modify_rec(k))
               deleteButton = Button(self, text = 'Delete', command = lambda k=k: del_rec(k))
               for j in range(len(tab_data[0].oRecordData.keys())):
                    body = Label(self, text = str(tab_data[k].oRecordData[str(list(tab_data[0].oRecordData.keys())[j])]))
                    body.grid(column = j+1, row = k+2)
                    if j == len(tab_data[0].oRecordData.keys())-1:
                         modifyButton.grid(column = j + 2, row = k+2)
                         deleteButton.grid(column = j + 3, row = k+2)
          backButton = Button(self, text = 'Back', command = self.menu)
          backButton.grid(column = 3, row = len(tab_data) + 2)
          def del_rec(k):
               try:
                    cid=-1
                    for i in range(len(self.mydb)):
                         if self.t_name.get() == str(self.mydb[i]).split("'")[1]:
                              cid=int(str(self.mydb[i]).split("'")[2].split(' ')[1])
                              break
                    rid = tab_data[k]._rid
                    client.record_delete(cid,rid)
                    self.widg_dest()
                    text = Label(self, text = "Record Successfully Deleted.")
                    text1 = Label(self, text = "Click VIEW to view updated table or back to go back to menu")
                    text.grid(column = 0, row = 0)
                    text1.grid(column = 0, row = 1)
                    view2Button = Button(self, text = "VIEW", command = self.view_func)
                    back2Button = Button(self, text = "Back", command = self.menu)
                    view2Button.grid(column = 1, row = 1)
                    back2Button.grid(column = 2, row = 1)
               except:
                    self.widg_dest()
                    text = Label(self, text = "Failed to delete record. Please try again", command = self.menu)
                    text.grid(column = 0, row = 0)
          def modify_rec(k):
               def modify_rec_up():
                    cid=-1
                    for i in range(len(self.mydb)):
                         if self.t_name.get() == str(self.mydb[i]).split("'")[1]:
                              cid=int(str(self.mydb[i]).split("'")[2].split(' ')[1])
                              break
                    client.record_delete(cid,str(tab_data[k]._rid))
                    bkp_list = []
                    bkp_keys = list(tab_data[k].oRecordData.keys())
                    for i in bkp_keys:
                         bkp_list.append(tab_data[k].oRecordData[str(i)])
                    d = dict()
                    i=0
                    for j in e_list:
                         if len(j.get()) > 0:
                              d[str(bkp_keys[i])] = type(tab_data[k].oRecordData[str(bkp_keys[i])])(j.get())
                         else:
                              d[str(bkp_keys[i])] = tab_data[k].oRecordData[str(bkp_keys[i])]
                         i+=1
                    #print(tab_data[k]._rid)
                    client.record_create(cid,d)
                    '''i=0
                    for j in e_list:
                         prop = str(list(tab_data[0].oRecordData.keys())[i])
                         val = ""
                         if len(j.get()) > 0:
                              if type(tab_data[0].oRecordData[prop]) == type(1):
                                   val = j.get()
                              else:
                                   val = "'"+j.get()+"'"
                              print(tab_data[k]._rid)
                              print("update "+self.t_name.get()+" set " + prop + " = "+val+" where @rid = "+str(tab_data[k]._rid).rstrip())
                              client.query("update "+self.t_name.get()+" set " + prop + " = "+val+" where @rid = "+str(tab_data[k]._rid).rstrip())
                         i+=1'''
                    #m[prop] = type(tab_data[0].oRecordData[prop])(j.get())
                    #d['@'+self.t_name.get()]=m
                    #d['version'] = tab_data[k]._version
                    #d['rid'] = tab_data[k]._rid
                    
                    #print(d)
               self.widg_dest()
               try:
                    d=dict()
                    m=dict()
                    e_list = ['']*len(tab_data[0].oRecordData.keys())
                    for i in range(len(tab_data[0].oRecordData.keys())):
                         head = Label(self, text = str(list(tab_data[0].oRecordData.keys())[i]))
                         head.grid(column = i + 1, row = 1)
                    for j in range(len(tab_data[0].oRecordData.keys())):
                         body = Label(self, text = str(tab_data[k].oRecordData[str(list(tab_data[0].oRecordData.keys())[j])]))
                         body.grid(column = j+1, row = 2)
                         e_list[j] = Entry(self)
                         e_list[j].grid(column = j+1, row = 3)
                    submitButton = Button(self, text="Submit", command = modify_rec_up)
                    submitButton.grid(column = 5, row = len(tab_data[0].oRecordData.keys())+2)
                    back3Button = Button(self, text = "Back", command = self.menu)
                    back3Button.grid(column = 1, row = 5)
               except:
                    print(0)
               
               
root = Tk()
root.geometry("1000x1000")
app = Window(root)
root.mainloop()

