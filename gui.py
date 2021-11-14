from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox, filedialog
import psycopg2

DB_HOST ='localhost'
DB_NAME='dbmsproj'
DB_USER='postgres'
DB_PASS= '1612'

conn= psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)

root =Tk()
# sb = Scrollbar(root)
# sb.pack(side = RIGHT, fill = Y)  
root.title('Clothing rental service')
root.iconbitmap('img\icon.ico')
root.geometry("600x300")

def sellerclick():
	global img1
	top= Toplevel()
	top.title("Seller Information")
	top.iconbitmap('img\seller.ico')

	sellerFrame =LabelFrame(top, text="Seller details", padx=10, pady=10)
	sellerFrame.pack(padx=5, pady=5)

	sellerFrameHeader = Label(sellerFrame, text="Enter details and join the community!  ")
	sellerFrameHeader.grid(row=1, column=1)

	img1 =ImageTk.PhotoImage(Image.open("img\seller.png"))
	img1label= Label(sellerFrame, image=img1)
	img1label.grid(row=2, column=1)

	sellerNameLabel= Label(sellerFrame, text="Enter Seller name")
	sellerNameLabel.grid(row=3, column=1)
	sellerNameEntry =Entry(sellerFrame, width=40)
	sellerNameEntry.grid(row=3, column=2)

	sellerEmailLabel= Label(sellerFrame, text="Enter Seller email ID")
	sellerEmailLabel.grid(row=4, column=1)
	sellerEmailEntry=Entry(sellerFrame, width=40)
	sellerEmailEntry.grid(row=4, column=2)

	sellerPhLabel= Label(sellerFrame, text="Enter Seller phone number")
	sellerPhLabel.grid(row=5, column=1)
	sellerPhEntry =Entry(sellerFrame, width=40)
	sellerPhEntry.grid(row=5, column=2)

	SellerAddrLabel= Label(sellerFrame, text="Enter Seller address details below-")
	SellerAddrLabel.grid(row=6, column=2)
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

	sellerCatLabel= Label(sellerFrame, text="Enter Shop category")
	sellerCatLabel.grid(row=12, column=1)
	sellerCatEntry =Entry(sellerFrame, width=40)
	sellerCatEntry.grid(row=12, column=2)

	def add_sellerdet_Click():
		sellername= sellerNameEntry.get()
		selleremail= sellerEmailEntry.get()
		sellerph= int(sellerPhEntry.get())
		sellerline1=line1.get()
		sellerline2=line2.get()
		sellercity=city.get()
		sellerstate=state.get()
		sellerzip=int(zipcode.get())
		sellercat=sellerCatEntry.get()
		seller_id= 7647
		s_id="4349"
		sellerrat="5"
		cur= conn.cursor()
		#insert into seller values('1001','ABC Clothing','abc_clothing@hmail.com','6787656722',row('No. 66', '5th Cross Vasanth Nagar', 'Bengaluru', 'Karnataka', '560052'),'8','tops','1234');
		#query= "insert into seller values(%s,%s,%s,%s, row(%s,%s,%s,%s,%s,%s),5,%s,%s)",(seller_id,sellername,selleremail,sellerph,sellerline1,sellerline2,sellercity,sellerstate,sellerzip,sellercat)
		insertquery= """insert into seller values (%s, %s, %s, %s, row(%s, %s, %s, %s, %s), %s, %s, %s)"""
		record=(seller_id,sellername,selleremail,sellerph,sellerline1,sellerline2,sellercity,sellerstate,sellerzip,sellerrat,sellercat,s_id)
		cur.execute(insertquery,record)
		conn.commit()
		cur.close()
		conn.close()

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

	clothesFrameHeader = Label(clothesFrame, text="Enter details to add clothes to your store")
	clothesFrameHeader.grid(row=1, column=1)

	img2 =ImageTk.PhotoImage(Image.open("img\icon.png"))
	img2label= Label(clothesFrame, image=img2)
	img2label.grid(row=2, column=1)

	itemNameLabel= Label(clothesFrame, text="Enter Item name")
	itemNameLabel.grid(row=3, column=1)
	itemNameEntry =Entry(clothesFrame, width=40)
	itemNameEntry.grid(row=3, column=2)

	itemPriceLabel= Label(clothesFrame, text="Enter Price of Item")
	itemPriceLabel.grid(row=4, column=1)
	itemPriceEntry=Entry(clothesFrame, width=40)
	itemPriceEntry.grid(row=4, column=2)

	itemColourLabel= Label(clothesFrame, text="Enter colours for Item")
	itemColourLabel.grid(row=5, column=1)
	itemColourEntry =Entry(clothesFrame, width=40)
	itemColourEntry.grid(row=5, column=2)

	itemSizeLabel= Label(clothesFrame, text="Enter size of Item")
	itemSizeLabel.grid(row=6, column=1)
	itemSizeEntry =Entry(clothesFrame, width=40)
	itemSizeEntry.grid(row=6, column=2)

	itemMaterialLabel= Label(clothesFrame, text="Enter material of Item")
	itemMaterialLabel.grid(row=7, column=1)
	itemMaterialEntry=Entry(clothesFrame, width=40)
	itemMaterialEntry.grid(row=7, column=2)

	def addimg_func():
		clothesFrame.filename= filedialog.askopenfilename(initialdir="F:\College\Year3\Sem5\DBMS\Proj\img")
		path= Label(clothesFrame, text= clothesFrame.filename)
		path.grid(row=9, column=2)
		# itemimg=ImageTk.PhotoImage(Image.open(clothesFrame.filename))
		# itemimgLabel= Label(image=itemimg).pack()
		imgpath= clothesFrame.filename


	itemImageLabel= Label(clothesFrame, text="Add image")
	itemImageLabel.grid(row=8, column=1)
	itemImageButton= Button(clothesFrame, text="Add image", command=addimg_func)
	itemImageButton.grid(row=8, column=2)


	def add_clothesdet_Click():
		itemname= itemNameEntry.get()
		itemprice= itemPriceEntry.get()
		itemcolour= itemColourEntry.get()
		itemsize=itemSizeEntry.get()
		itemmaterial=itemMaterialEntry.get()
		messagebox.showinfo("Info added","Succesfully added item details")

	adddetails_button =Button(clothesFrame, text="Add item data", command=add_clothesdet_Click, bg="#ADD8E6")
	adddetails_button.grid(row=15, column=2)

def storeclick():
	global img3
	top= Toplevel()
	top.title("Add Store details")
	top.iconbitmap('img\shop.ico')

	storeFrame =LabelFrame(top, text="Add store infromation", padx=10, pady=10)
	storeFrame.pack(padx=5, pady=5)

	storeFrameHeader = Label(storeFrame, text="Enter store infromation")
	storeFrameHeader.grid(row=1, column=1)

	img3 =ImageTk.PhotoImage(Image.open("img\shop.png"))
	img3label= Label(storeFrame, image=img3)
	img3label.grid(row=2, column=1)




#mainframe
mainFrame =LabelFrame(root, text="Seller details", padx=10, pady=10)
mainFrame.pack(padx=10, pady=10)

mainLabel= Label(mainFrame, text="Clothing Rental service").grid(row=1, column=2)

div1= Label(mainFrame, text=" ").grid(row=2, column=1)

sellerlabel= Label(mainFrame, text="Seller Actions:").grid(row=3, column=2)
sellerpagebtn=Button(mainFrame, text="Sign up as a seller", command=sellerclick)
sellerpagebtn.grid(row=4, column=1)

clothesbtn=Button(mainFrame, text="Add clothes to store", command=clothesclick)
clothesbtn.grid(row=4, column=2)

clothesbtn= Button(mainFrame, text="Add store details", command=storeclick)
clothesbtn.grid(row=4, column=3)

div2= Label(mainFrame, text=" ").grid(row=5, column=1)

sellerlabel= Label(mainFrame, text="Buyer Actions:").grid(row=6, column=2)




root.mainloop()