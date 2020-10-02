# RahulCMSsoftware
This project is basically a ERP (Enterprise resource planning) application's protocol. Framework what I used is python 3x.
Enterprise resource planning (ERP) refers to a type of software that organizations use to manage day-to-day business activities such as accounting, procurement,
project management, risk management and compliance, and supply chain operations.

I have use Tkinter module as my base for the User interface,the databases are created using the file handeling and a very smart use of list is there to fetch the database.
sqlite will be implimented in the upcomming days to handle large data and calculations.
No algorithms is called in the mainloop() instead the button push call is used for the same.We are having two options for the arrangment of the widgets I used the grid method


 About Tkinter
 
     from tkinter import *
     window = Tk()
     window.title("codeWithRahul")
     window.mainloop()
     
   Tkinter is a Python binding to the Tk GUI toolkit. It is the standard Python interface to the Tk GUI toolkit and is Python's de facto standard GUI.
   Tkinter is included with standard Linux, Microsoft Windows and Mac OS X installs of Python.
   The name Tkinter comes from Tk interface. Tkinter was written by Fredrik Lundh.

 Tkinter is free software released under a Python license

Features of the project :

1.Product management 

2.User database collection (which could be used in the future for upsell of the products according to the statistics)

3.Easy bill printing 

4.Adding multiple products in one go (Just use the append section and write the product names seperated by commas)

5.Discount calculated price is managed by the programm price entry section (One can just enter the algorith and rest will be done by the software)

6.Customer management (Register and assigning a new value)

7.Repeated products and case management


The main function of this project is that it creates seperate databases so called *.dat files for different stuff, Once the project is deployed 
on to a server and used for a year  we would have enough data to impliment he ML. We can also have some statistical calculations on this for the upsell 
Basically via this we would be able to know when there should be a sale ,which customer is more loyal,which product is top selling etc.

I hope you guys will love my code and If you have any suggestions for me to optimize the code then plz do let me know about that.
