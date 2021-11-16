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
root.geometry("500x300")

def sellerclick():
	global img1
	top= Toplevel()
	top.title("Seller Information")
	top.iconbitmap('img\seller.ico')

	sellerFrame =LabelFrame(top, text="Seller details", padx=10, pady=10)
	sellerFrame.pack(padx=5, pady=5)

	sellerFrameHeader = Label(sellerFrame, text="Enter details and join the community!  ").grid(row=1, column=1)

	img1 =ImageTk.PhotoImage(Image.open("img\seller.png"))
	img1label= Label(sellerFrame, image=img1).grid(row=2, column=1)

	sellerNameLabel= Label(sellerFrame, text="Enter Seller name").grid(row=3, column=1)
	sellerNameEntry= Entry(sellerFrame, width=40)
	sellerNameEntry.grid(row=3, column=2)

	sellerEmailLabel= Label(sellerFrame, text="Enter Seller email ID").grid(row=4, column=1)
	sellerEmailEntry=Entry(sellerFrame, width=40)
	sellerEmailEntry.grid(row=4, column=2)

	sellerPhLabel= Label(sellerFrame, text="Enter Seller phone number").grid(row=5, column=1)
	sellerPhEntry =Entry(sellerFrame, width=40)
	sellerPhEntry.grid(row=5, column=2)

	SellerAddrLabel= Label(sellerFrame, text="Enter Seller address details below-").grid(row=6, column=2)
	line1label=Label(sellerFrame, text="Enter line1").grid(row=7, column=1)
	line1=Entry(sellerFrame, width=40)
	line1.grid(row=7, column=2)
	line1label=Label(sellerFrame, text="Enter line2").grid(row=8, column=1)
	line2=Entry(sellerFrame, width=40)
	line2.grid(row=8, column=2)
	citylabel=Label(sellerFrame, text="Enter city").grid(row=9, column=1)
	city=Entry(sellerFrame, width=40)
	city.grid(row=9, column=2)
	statelabel=Label(sellerFrame, text="Enter state").grid(row=10, column=1)
	state=Entry(sellerFrame, width=40)
	state.grid(row=10, column=2)
	zipcodelabel=Label(sellerFrame, text="Enter zipcode").grid(row=11, column=1)
	zipcode=Entry(sellerFrame, width=40)
	zipcode.grid(row=11, column=2)

	sellerCatLabel= Label(sellerFrame, text="Enter Shop category").grid(row=12, column=1)
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

	adddetails_button =Button(sellerFrame, text="Add seller data", command=add_sellerdet_Click, bg="#ADD8E6")
	adddetails_button.grid(row=15, column=2)

def clothesclick():
	global img2
	top= Toplevel()
	top.title("Add Clothes")
	top.iconbitmap('img\icon.ico')

	clothesFrame =LabelFrame(top, text="Add new clothes to sell", padx=10, pady=10)
	clothesFrame.pack(padx=5, pady=5)

	clothesFrameHeader = Label(clothesFrame, text="Enter details to add clothes to your store").grid(row=1, column=1)

	img2 =ImageTk.PhotoImage(Image.open("img\icon.png"))
	img2label= Label(clothesFrame, image=img2).grid(row=1, column=2)

	storeLabel=Label(clothesFrame, text="Enter store id").grid(row=2, column=1)
	storeEntry=Entry(clothesFrame, width=40)
	storeEntry.grid(row=2, column=2)

	itemNameLabel= Label(clothesFrame, text="Enter Item name").grid(row=3, column=1)
	itemNameEntry =Entry(clothesFrame, width=40)
	itemNameEntry.grid(row=3, column=2)

	itemPriceLabel= Label(clothesFrame, text="Enter Price of Item").grid(row=4, column=1)
	itemPriceEntry=Entry(clothesFrame, width=40)
	itemPriceEntry.grid(row=4, column=2)

	itemColourLabel= Label(clothesFrame, text="Enter colours for Item").grid(row=5, column=1)
	itemColourEntry =Entry(clothesFrame, width=40)
	itemColourEntry.grid(row=5, column=2)

	itemSizeLabel= Label(clothesFrame, text="Enter size of Item").grid(row=6, column=1)
	itemSizeEntry =Entry(clothesFrame, width=40)
	itemSizeEntry.grid(row=6, column=2)

	itemMaterialLabel= Label(clothesFrame, text="Enter material of Item").grid(row=7, column=1)
	itemMaterialEntry=Entry(clothesFrame, width=40)
	itemMaterialEntry.grid(row=7, column=2)

	def addimg_func():
		clothesFrame.filename= filedialog.askopenfilename(initialdir="F:\College\Year3\Sem5\DBMS\Proj\img")
		path= Label(clothesFrame, text= clothesFrame.filename).grid(row=9, column=2)
		imgpath= clothesFrame.filename

	itemImageLabel= Label(clothesFrame, text="Add image").grid(row=8, column=1)
	itemImageButton= Button(clothesFrame, text="Add image", command=addimg_func)
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

	adddetails_button =Button(clothesFrame, text="Add item data", command=add_clothesdet_Click, bg="#ADD8E6")
	adddetails_button.grid(row=15, column=2)

def storeclick():
	global img3
	top= Toplevel()
	top.title("Add Store details")
	top.iconbitmap('img\shop.ico')

	storeFrame =LabelFrame(top, text="Add store infromation", padx=20, pady=20)
	storeFrame.pack(padx=10, pady=10)

	storeFrameHeader = Label(storeFrame, text="Enter store infromation").grid(row=1, column=2)

	img3 =ImageTk.PhotoImage(Image.open("img\shop.png"))
	img3label= Label(storeFrame, image=img3).grid(row=2, column=2)

	#form data
	storeNameLabel= Label(storeFrame, text="Enter Store name").grid(row=4, column=1)
	storeNameEntry =Entry(storeFrame, width=40)
	storeNameEntry.grid(row=4, column=2)

	storePhLabel= Label(storeFrame, text="Enter Business Phone Number").grid(row=5, column=1)
	storePhEntry =Entry(storeFrame, width=40)
	storePhEntry.grid(row=5, column=2)

	StoreAddrLabel= Label(storeFrame, text="Enter Seller address details below-").grid(row=6, column=2)

	line1label=Label(storeFrame, text="Enter line1").grid(row=7, column=1)
	line1=Entry(storeFrame, width=40)
	line1.grid(row=7, column=2)

	line2label=Label(storeFrame, text="Enter line2").grid(row=8, column=1)
	line2=Entry(storeFrame, width=40)
	line2.grid(row=8, column=2)

	citylabel=Label(storeFrame, text="Enter city").grid(row=9, column=1)
	city=Entry(storeFrame, width=40)
	city.grid(row=9, column=2)

	statelabel=Label(storeFrame, text="Enter state").grid(row=10, column=1)
	state=Entry(storeFrame, width=40)
	state.grid(row=10, column=2)

	zipcodelabel=Label(storeFrame, text="Enter zipcode").grid(row=11, column=1)
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

	adddetails_button =Button(storeFrame, text="Add store data", command=add_storedet_Click, bg="#ADD8E6")
	adddetails_button.grid(row=15, column=2)


def viewClothesClick():
	global clothesimg
	top= Toplevel()
	top.title("Clothing Items Available")

	viewClothesFrame =LabelFrame(top, text="Order details", padx=10, pady=10)
	viewClothesFrame.pack(padx=5, pady=5)

	conn= psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
	cur=conn.cursor()

	cur.execute("select img from clothes")
	imgtup=cur.fetchall()
	imagelist= []
	for line in imgtup:
		imagelist.append(str(line[0]))
	cur.execute("select colour, item_name, price, size, material from clothes")
	records=cur.fetchall()
	
	i=2
	for row in records:
		j=2
		for val in row:
			displayLabel= Label(viewClothesFrame, text= str(val))
			displayLabel.grid(row=i, column=j)
			j+=1	
		i+=1

	# for x in range(5):
	# 	imgpath=str(imagelist[x])
	# 	clothesimg =ImageTk.PhotoImage(Image.open(imgpath))
	# 	imgglabel= Label(viewClothesFrame, image=clothesimg)
	# 	imgglabel.grid(row=x+1, column=7)

	conn.commit()
	cur.close()
	conn.close()

def viewOrderClick():
	top= Toplevel()
	top.title("Order details")

	viewOrderFrame =LabelFrame(top, text="View order status", padx=10, pady=10)
	viewOrderFrame.pack(padx=5, pady=5)

	ordernoLabel= Label(viewOrderFrame, text="Enter order number").grid(row=3, column=1)
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
			 	displayLabel=Label(viewOrderFrame, text=str(stat))
			 	displayLabel.grid(row=6, column=j)
			 	j+=1
		
		conn.commit()
		cur.close()
		conn.close()

	search_btn= Button(viewOrderFrame, text="Get order status", command=orderstat_click)
	search_btn.grid(row=5, column=2)



def returnOrderClick():
	top= Toplevel()
	top.title("Return order")

	returnFrame =LabelFrame(top, text="Return items", padx=20, pady=20)
	returnFrame.pack(padx=10, pady=10)

	returnFrameHeader = Label(returnFrame, text="Enter the order number of the item").grid(row=1, column=1)
	orderNoEntry= Entry(returnFrame, width=30)
	orderNoEntry.grid(row=3, column=1)

	def EnterBtnClick():
		pass
		#retrieve order details

	EnterButton= Button(returnFrame, text="Enter", command= EnterBtnClick)
	EnterButton.grid(row=3,column=2)

	#button- confirm order return? window that says pickup for this order is scheduled

	#label and text box to submit store rating, button to trigger event and push to db




	


#mainframe
mainFrame =LabelFrame(root, text="", padx=20, pady=20)
mainFrame.pack(padx=10, pady=10)

mainLabel= Label(mainFrame, text="Clothing Rental service").grid(row=1, column=2)

landingimg =ImageTk.PhotoImage(Image.open("img\icon.png"))
landinglabel= Label(mainFrame, image=landingimg).grid(row=2, column=2)

div1= Label(mainFrame, text=" ").grid(row=3, column=1)

sellerlabel= Label(mainFrame, text="Seller Actions:").grid(row=4, column=2)

#sign up for seller
sellerpagebtn=Button(mainFrame, text="Sign up as a seller", command=sellerclick).grid(row=5, column=1)
#add clothes
clothesbtn=Button(mainFrame, text="Add clothes to store", command=clothesclick).grid(row=5, column=2)
#add store
clothesbtn= Button(mainFrame, text="Add store details", command=storeclick).grid(row=5, column=3)

div2= Label(mainFrame, text=" ").grid(row=6, column=1)
#find clothes to buy
buyerlabel= Label(mainFrame, text="Buyer Actions:").grid(row=7, column=2)
viewclothes= Button(mainFrame, text="View Clothes", command=viewClothesClick).grid(row=8, column=1)

#view order status
vieworder= Button(mainFrame, text="View order details",command=viewOrderClick).grid(row=8, column=2)

#return item
returnorder= Button(mainFrame, text="Return clothes", command=returnOrderClick).grid(row=8, column=3)



root.mainloop()