from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox, filedialog
import psycopg2

DB_HOST ='localhost'
DB_NAME='dbmsproj'
DB_USER='postgres'
DB_PASS= '1612'

root =Tk()  
root.title('Clothing rental service')
root.iconbitmap('img\icon.ico')
root.geometry("1200x600")

def sellerclick():
	global img1
	top= Toplevel()
	top.title("Seller Information")
	top.iconbitmap('img\seller.ico')
	top.geometry("800x500")

	sellerFrame =LabelFrame(top, text="Seller details", padx=20, pady=20)
	sellerFrame.pack(padx=15, pady=15)

	sellerFrameHeader = Label(sellerFrame, text="Enter details and join the community!", font=("Helvetica", 16), justify=CENTER).grid(row=1, column=1)

	img1 =ImageTk.PhotoImage(Image.open("img\seller.png"))
	img1label= Label(sellerFrame, image=img1).grid(row=2, column=1)

	sellerNameLabel= Label(sellerFrame, text="Enter Seller name", font=("Helvetica", 12)).grid(row=3, column=1)
	sellerNameEntry= Entry(sellerFrame, width=40)
	sellerNameEntry.grid(row=3, column=2)

	sellerEmailLabel= Label(sellerFrame, text="Enter Seller email ID", font=("Helvetica", 12)).grid(row=4, column=1)
	sellerEmailEntry=Entry(sellerFrame, width=40)
	sellerEmailEntry.grid(row=4, column=2)

	sellerPhLabel= Label(sellerFrame, text="Enter Seller phone number", font=("Helvetica", 12)).grid(row=5, column=1)
	sellerPhEntry =Entry(sellerFrame, width=40)
	sellerPhEntry.grid(row=5, column=2)

	SellerAddrLabel= Label(sellerFrame, text="Enter Seller address details below-", font=("Helvetica", 12)).grid(row=6, column=2)
	line1label=Label(sellerFrame, text="Enter line1",font=("Helvetica", 12) ).grid(row=7, column=1)
	line1=Entry(sellerFrame, width=40)
	line1.grid(row=7, column=2)
	line1label=Label(sellerFrame, text="Enter line2", font=("Helvetica", 12)).grid(row=8, column=1)
	line2=Entry(sellerFrame, width=40)
	line2.grid(row=8, column=2)
	citylabel=Label(sellerFrame, text="Enter city", font=("Helvetica", 12)).grid(row=9, column=1)
	city=Entry(sellerFrame, width=40)
	city.grid(row=9, column=2)
	statelabel=Label(sellerFrame, text="Enter state", font=("Helvetica", 12)).grid(row=10, column=1)
	state=Entry(sellerFrame, width=40)
	state.grid(row=10, column=2)
	zipcodelabel=Label(sellerFrame, text="Enter zipcode", font=("Helvetica", 12)).grid(row=11, column=1)
	zipcode=Entry(sellerFrame, width=40)
	zipcode.grid(row=11, column=2)

	sellerCatLabel= Label(sellerFrame, text="Enter Shop category", font=("Helvetica", 12)).grid(row=12, column=1)
	sellerCatEntry =Entry(sellerFrame, width=40)
	sellerCatEntry.grid(row=12, column=2)

	def add_sellerdet_Click():
		sellername= sellerNameEntry.get()
		selleremail= sellerEmailEntry.get()
		sellerph= sellerPhEntry.get()
		sellerline1=line1.get()
		sellerline2=line2.get()
		sellercity=city.get()
		sellerstate=state.get()
		sellerzip=zipcode.get()
		sellercat=sellerCatEntry.get()
		seller_id= 7647
		s_id="4349"
		sellerrat="5"

		conn= psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
		cur= conn.cursor()
		
		insertquery= """insert into seller values (%s, %s, %s, %s, row(%s, %s, %s, %s, %s), %s, %s, %s)"""
		record=(seller_id,sellername,selleremail,sellerph,sellerline1,sellerline2,sellercity,sellerstate,sellerzip,sellerrat,sellercat,s_id)
		cur.execute(insertquery,record)
		conn.commit()
		cur.close()
		conn.close()

		sellerNameEntry.delete(0, END)
		sellerEmailEntry.delete(0, END)
		sellerPhEntry.delete(0, END)
		line1.delete(0, END)
		line2.delete(0, END)
		city.delete(0, END)
		state.delete(0, END)
		zipcode.delete(0, END)
		sellerCatEntry.delete(0, END)

		messagebox.showinfo("Info added","Succesfully added seller details")

	adddetails_button =Button(sellerFrame, text="Add seller data", font=("Helvetica", 12), command=add_sellerdet_Click, bg="#ADD8E6")
	adddetails_button.grid(row=15, column=2)

def clothesclick():
	global img2
	top= Toplevel()
	top.title("Add Clothes")
	top.iconbitmap('img\icon.ico')
	top.geometry("800x500")

	clothesFrame =LabelFrame(top, text="Add new clothes to sell", padx=20, pady=20)
	clothesFrame.pack(padx=15, pady=15)

	clothesFrameHeader = Label(clothesFrame, text="Enter details to add clothes to your store", font=("Helvetica", 16)).grid(row=1, column=1)

	img2 =ImageTk.PhotoImage(Image.open("img\icon.png"))
	img2label= Label(clothesFrame, image=img2).grid(row=1, column=2)

	storeLabel=Label(clothesFrame, text="Enter store id", font=("Helvetica", 12)).grid(row=2, column=1)
	storeEntry=Entry(clothesFrame, width=40)
	storeEntry.grid(row=2, column=2)

	itemNameLabel= Label(clothesFrame, text="Enter Item name", font=("Helvetica", 12)).grid(row=3, column=1)
	itemNameEntry =Entry(clothesFrame, width=40)
	itemNameEntry.grid(row=3, column=2)

	itemPriceLabel= Label(clothesFrame, text="Enter Price of Item", font=("Helvetica", 12)).grid(row=4, column=1)
	itemPriceEntry=Entry(clothesFrame, width=40)
	itemPriceEntry.grid(row=4, column=2)

	itemColourLabel= Label(clothesFrame, text="Enter colours for Item", font=("Helvetica", 12)).grid(row=5, column=1)
	itemColourEntry =Entry(clothesFrame, width=40)
	itemColourEntry.grid(row=5, column=2)

	itemSizeLabel= Label(clothesFrame, text="Enter size of Item", font=("Helvetica", 12)).grid(row=6, column=1)
	itemSizeEntry =Entry(clothesFrame, width=40)
	itemSizeEntry.grid(row=6, column=2)

	itemMaterialLabel= Label(clothesFrame, text="Enter material of Item", font=("Helvetica", 12)).grid(row=7, column=1)
	itemMaterialEntry=Entry(clothesFrame, width=40)
	itemMaterialEntry.grid(row=7, column=2)

	def addimg_func():
		clothesFrame.filename= filedialog.askopenfilename(initialdir="F:\College\Year3\Sem5\DBMS\Proj\img")
		path= Label(clothesFrame, text= clothesFrame.filename).grid(row=9, column=2)
		imgpath= clothesFrame.filename

	itemImageLabel= Label(clothesFrame, text="Add image", font=("Helvetica", 12)).grid(row=8, column=1)
	itemImageButton= Button(clothesFrame, text="Add image",font=("Helvetica", 12), command=addimg_func)
	itemImageButton.grid(row=8, column=2)


	def add_clothesdet_Click():
		s_id= storeEntry.get()
		itemname= itemNameEntry.get()
		itemprice= itemPriceEntry.get()
		itemcolour= itemColourEntry.get()
		itemsize=itemSizeEntry.get()
		itemmaterial=itemMaterialEntry.get()
		item_id='20'
		rat='5'
		imgpath= clothesFrame.filename

		conn= psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
		cur= conn.cursor()

		insertclothesq= """insert into clothes values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
		rec=(item_id,itemname,itemprice,itemcolour,itemsize,itemmaterial,rat,s_id,imgpath)

		cur.execute(insertclothesq,rec)

		conn.commit()
		cur.close()
		conn.close()

		storeEntry.delete(0, END)
		itemNameEntry.delete(0, END)
		itemPriceEntry.delete(0, END)
		itemColourEntry.delete(0, END)
		itemSizeEntry.delete(0, END)
		itemMaterialEntry.delete(0, END)

		messagebox.showinfo("Info added","Succesfully added item details")

	adddetails_button =Button(clothesFrame, text="Add item data",font=("Helvetica", 12) ,command=add_clothesdet_Click, bg="#ADD8E6")
	adddetails_button.grid(row=15, column=2)

def storeclick():
	global img3
	top= Toplevel()
	top.title("Add Store details")
	top.iconbitmap('img\shop.ico')
	top.geometry("800x500")

	storeFrame =LabelFrame(top, text="Add store infromation", padx=20, pady=20)
	storeFrame.pack(padx=10, pady=10)

	storeFrameHeader = Label(storeFrame, text="Enter store infromation", font=("Helvetica", 16)).grid(row=1, column=2)

	img3 =ImageTk.PhotoImage(Image.open("img\shop.png"))
	img3label= Label(storeFrame, image=img3).grid(row=2, column=2)

	#form data
	storeNameLabel= Label(storeFrame, text="Enter Store name", font=("Helvetica", 12)).grid(row=4, column=1)
	storeNameEntry =Entry(storeFrame, width=40)
	storeNameEntry.grid(row=4, column=2)

	storePhLabel= Label(storeFrame, text="Enter Business Phone Number", font=("Helvetica", 12)).grid(row=5, column=1)
	storePhEntry =Entry(storeFrame, width=40)
	storePhEntry.grid(row=5, column=2)

	StoreAddrLabel= Label(storeFrame, text="Enter Seller address details below-", font=("Helvetica", 12)).grid(row=6, column=2)

	line1label=Label(storeFrame, text="Enter line1", font=("Helvetica", 12)).grid(row=7, column=1)
	line1=Entry(storeFrame, width=40)
	line1.grid(row=7, column=2)

	line2label=Label(storeFrame, text="Enter line2", font=("Helvetica", 12)).grid(row=8, column=1)
	line2=Entry(storeFrame, width=40)
	line2.grid(row=8, column=2)

	citylabel=Label(storeFrame, text="Enter city", font=("Helvetica", 12)).grid(row=9, column=1)
	city=Entry(storeFrame, width=40)
	city.grid(row=9, column=2)

	statelabel=Label(storeFrame, text="Enter state", font=("Helvetica", 12)).grid(row=10, column=1)
	state=Entry(storeFrame, width=40)
	state.grid(row=10, column=2)

	zipcodelabel=Label(storeFrame, text="Enter zipcode", font=("Helvetica", 12)).grid(row=11, column=1)
	zipcode=Entry(storeFrame, width=40)
	zipcode.grid(row=11, column=2)

	def add_storedet_Click():
		storename= storeNameEntry.get()
		storeph=storePhEntry.get()
		storeline1=line1.get()
		storeline2=line2.get()
		storecity=city.get()
		storestate=state.get()
		storezip=zipcode.get()
		s_id='4350'

		conn= psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
		cur= conn.cursor()
		
		insert_query= """insert into store values (%s, %s, row(%s, %s, %s, %s, %s) ,%s)"""
		record=(s_id,storename,storeline1,storeline2,city,storestate,storezip,storeph)

		cur.execute(insert_query,record)

		conn.commit()
		cur.close()
		conn.close()

		storeNameEntry.delete(0, END)
		storePhEntry.delete(0, END)
		line1.delete(0, END)
		line2.delete(0, END)
		city.delete(0, END)
		state.delete(0, END)
		zipcode.delete(0, END)

		messagebox.showinfo("Info added","Succesfully added store details")

	adddetails_button =Button(storeFrame, text="Add store data",font=("Helvetica", 12) ,command=add_storedet_Click, bg="#ADD8E6")
	adddetails_button.grid(row=15, column=2)


def viewClothesClick():
	global cimg
	top= Toplevel()
	top.title("Clothing Items Available")
	top.geometry("800x500")

	viewClothesFrame =LabelFrame(top, text="Order details", padx=20, pady=20)
	viewClothesFrame.pack(padx=15, pady=15)

	cimg =ImageTk.PhotoImage(Image.open("img\cart.png"))
	imglabel= Label(viewClothesFrame, image=cimg).grid(row=0, column=4)


	clotheslabel= Label(viewClothesFrame, text="Clothes available to rent:", font=("Helvetica", 12)).grid(row=1, column=2)
	filler=Label(viewClothesFrame, text= "").grid(row=2, column=2)

	conn= psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
	cur=conn.cursor()

	cur.execute("select img from clothes")
	imgtup=cur.fetchall()
	imagelist= []
	for line in imgtup:
		imagelist.append(str(line[0]))
	cur.execute("select colour, item_name, price, size, material from clothes")
	records=cur.fetchall()

	def viewImgClick(x):
		pass
		"""
		global img
		path=str(imagelist[x])
		top1= Toplevel()
		img =ImageTk.PhotoImage(Image.open(path))
		imglabel= Label(top1, image=img).grid(row=2, column=1)
		"""
	
	i=3
	for row in records:
		j=2
		for val in row:
			displayLabel= Label(viewClothesFrame, text= str(val), font=("Helvetica", 10))
			displayLabel.grid(row=i, column=j)
			j+=1	
		viewimg = Button(viewClothesFrame, text="View image of clothing", font=("Helvetica", 10), command=viewImgClick(i-3))
		viewimg.grid(row=i, column=j+1)
		i+=1

	conn.commit()
	cur.close()
	conn.close()

def viewOrderClick():
	global img
	top= Toplevel()
	top.title("Order details")
	top.geometry("800x500")

	viewOrderFrame =LabelFrame(top, text="View order status", padx=20, pady=20)
	viewOrderFrame.pack(padx=15, pady=15)

	# img =ImageTk.PhotoImage(Image.open("img\\bag.png"))
	# imglabel= Label(viewClothesFrame, image=img).grid(row=0, column=2)

	ordernoLabel= Label(viewOrderFrame, text="Enter order number", font=("Helvetica", 12)).grid(row=3, column=1)
	ordernoEntry =Entry(viewOrderFrame, width=40)
	ordernoEntry.grid(row=3, column=2)

	filler= Label(viewOrderFrame, text=" ").grid(row=4, column=1)

	def orderstat_click():
		orderno= ordernoEntry.get()

		conn= psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
		cur=conn.cursor()

		retrievequery="select colour, item_name, o_status, p_status from order_det, payment, clothes \
		where order_det.order_no =%s and order_det.order_no = payment.order_id and clothes.item_id=order_det.item_id" 
		matchval=(orderno,)

		cur.execute(retrievequery,matchval)
		record=cur.fetchall()
		j=1
		for row in record:
			for stat in row:
			 	displayLabel=Label(viewOrderFrame, text=str(stat), font=("Helvetica", 12))
			 	displayLabel.grid(row=6, column=j)
			 	j+=1
		
		conn.commit()
		cur.close()
		conn.close()

	search_btn= Button(viewOrderFrame, text="Get order status",font=("Helvetica", 12) ,command=orderstat_click)
	search_btn.grid(row=5, column=2)



def returnOrderClick():
	global img
	top= Toplevel()
	top.title("Return order")
	top.geometry("800x500")

	returnFrame =LabelFrame(top, text="Return items", padx=20, pady=20)
	returnFrame.pack(padx=10, pady=10)

	img =ImageTk.PhotoImage(Image.open("img\delivery.png"))
	imglabel= Label(returnFrame, image=img).grid(row=1, column=1)

	filler=Label(returnFrame, text="").grid(row=2, column=1)

	returnFrameHeader = Label(returnFrame, text="Enter the order number of the item", font=("Helvetica", 12)).grid(row=3, column=1)
	orderNoEntry= Entry(returnFrame, width=30)
	orderNoEntry.grid(row=4, column=1)

	def EnterBtnClick():

		conn= psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
		cur= conn.cursor()

		query= """update order_det set returned=true where order_no= %s"""
		matchval=(orderNoEntry.get(),)

		cur.execute(query, matchval)

		displayLabel=Label(returnFrame, text="Return initiated", font=("Helvetica", 12))
		displayLabel.grid(row=5, column=1)

		conn.commit()
		cur.close()
		conn.close()


	EnterButton= Button(returnFrame, text="Enter",font=("Helvetica", 12), command= EnterBtnClick)
	EnterButton.grid(row=3,column=2)



#mainframe
mainFrame =LabelFrame(root, text="", padx=20, pady=20)
mainFrame.pack(padx=10, pady=10)

mainLabel= Label(mainFrame, text="Clothing Rental service", font=("Helvetica", 30)).grid(row=1, column=2)

landingimg =ImageTk.PhotoImage(Image.open("img\icon.png"))
landinglabel= Label(mainFrame, image=landingimg).grid(row=2, column=2)

div1= Label(mainFrame, text=" ").grid(row=3, column=1)

sellerlabel= Label(mainFrame, text="Seller Actions:", font=("Helvetica", 15)).grid(row=4, column=2)

#sign up for seller
sellerpagebtn=Button(mainFrame, text="Sign up as a seller", font=("Helvetica", 12), command=sellerclick).grid(row=5, column=1)
#add clothes
clothesbtn=Button(mainFrame, text="Add clothes to store", font=("Helvetica", 12), command=clothesclick).grid(row=5, column=2)
#add store
clothesbtn= Button(mainFrame, text="Add store details",font=("Helvetica", 12), command=storeclick).grid(row=5, column=3)

div2= Label(mainFrame, text=" ").grid(row=6, column=1)
#find clothes to buy
buyerlabel= Label(mainFrame, text="Buyer Actions:", font=("Helvetica", 15)).grid(row=7, column=2)
viewclothes= Button(mainFrame, text="View Clothes", font=("Helvetica", 12),command=viewClothesClick).grid(row=8, column=1)

#view order status
vieworder= Button(mainFrame, text="View order details",font=("Helvetica", 12),command=viewOrderClick).grid(row=8, column=2)

#return item
returnorder= Button(mainFrame, text="Return clothes", font=("Helvetica", 12), command=returnOrderClick).grid(row=8, column=3)



root.mainloop()