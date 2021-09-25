return_list = []
class Books:
	def __init__(self,ar):
		self.Books = ar
		self.lu = list(self.Books)
	def Print(self):
		print("\n")
		for index, name in enumerate(self.lu):
			print(index , name)
		print("\n")
	def Add(self):
		book_name = input("Enter Your Books Name: ")
		return book_name
	def Loan_Bokk(self):
		try:
			books_to_del = int(input("Enter Books Index: "))
			self.Name = input("Enter Your Name: ")
			#self.return_list.append(self.Name)
		except Exception as Er:
			print(f"Enter Book Index Not Book Name")
		else:
			return_list.append(self.Name)
			return books_to_del
	def Retrun(self):
			self.Name_Return = input("Enter Your Name ")
			try:
				if (self.Name_Return not in return_list):
					print("You Never Loan Book From Our Library So You Cannot Return ")
					#Only Pero Programmer Can Understand
					raise Exception("Noot")
			except Exception as c:
				pass
			else:
				BKL = input("Enter Your Books Name: ")
				if self.Name_Return in return_list:
					list2.append(BKL)
					print("Book Added Succesful")
					for drl in range(len(return_list)):
						if (return_list[drl] == self.Name_Return):
							del return_list[drl]
	
	
	
	
if __name__ == '__main__':
	list2 = ["hello", "Hekkxhd", "jxjzjzmjz"]
	while(True):
		try:
			User = int(input("1 For Print\n2 For Add\n3 For Loan\n4 For Return \n"))
		except Exception as c:
			print(f"{c} Try Again User")
			continue
		else:
			Lib = Books(list2)
			if User==1:
				Lib.Print()
			elif User==2:
				var = Lib.Add()
				list2.append(var)
			elif User==3:
				Lib.Print()
				dele = Lib.Loan_Bokk()
				dele = int(dele)
				del list2[dele]
			elif User==4:
				Lib.Retrun()
		