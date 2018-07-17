import sqlite3

connection = None
cursor = None
name= None

# Connect to the database 
def connect(path):
	global connection, cursor
	connection=sqlite3.connect(path)
	cursor=connection.cursor()

def quit():
	exit(0)

def findName():
	global name

	studentName= input("Enter Student Name: ")
	if(studentName=="q" or studentName=="Q"):
		quit()

	cursor.execute('''
		select * 
		from students
		where studentName==?
	''', (studentName,))

	num=cursor.fetchall()
	for i in num:
		j=''.join(i)

	name= studentName
	if(num==[]):
		return True

	return False


def login():
	print("\n"*10)
	print("LOGIN")
	print("--"*5)
	print("\n")
	while True:
		check= findName()
		if(check):
			print("Name does not Exist!!!")
			l=input("Do you want to Create an Account, enter y if Yes: ")
			if(l=="q" or l=="Q"):
				return
			elif(l=="y" or l=="Y"):
				create()
				return
			else:
				print("\n")

		else:
			# Login 
			print("Successful Login !!!")
			return 
			


def create():
	global connection, cursor

	print("\n"*10)
	print("CREATE AN ACCOUNT")
	print("--"*10)
	print("\n")
	while True:
		check= findName()

		if(check):
			# Good create an account
			cursor.execute('''
				insert into students
				values (?)''', (name,))
			connection.commit()

			print("Account Created!!!!!")
			login()
			return

		else:
			print("Name is Taken!!!")
			l=input("Do you want to login, enter y if Yes: ")
			if(l=="q" or l=="Q"):
				return
			elif(l=="y" or l=="Y"):
				login()
				return
			else:
				print("\n")


def vCourses():
	global connection, cursor, name

	print("\n"*10)
	print("View Courses")
	print("--"*10)
	print("\n")


	cursor.execute('''
		select courseName
		from Courses
		where studentName=(?)''', (name,))

	aCourse=[]
	courses= cursor.fetchall()
	for i in courses:
		course=''.join(i)
		aCourse.append(course)


	print("COURSES")
	print("--"*10)
	if(len(aCourse)==0):
		print("NONE")
	else:
		for i,j in enumerate(aCourse):
			num=i+1
			print("Course", num, ": "+ j)
	print("\n")



def aCourses():
	global connection, cursor, name

	print("\n"*10)
	print("Add Courses")
	print("--"*10)
	print("\n")
	courseName= input("Enter Course Name: ")
	if(courseName=="q" or courseName=="Q"):
		quit()
	else:
		cursor.execute('''
				insert into courses
				values (?,?,?)''', (courseName, 3, name )
		)
		connection.commit()





# Main client/User interface
def main():
	global connection, cursor

	path= "./291database.db"
	connect(path)

	print("Welcome:")
	print("--"*5)
	print("\n")
	print("To quit enter q. ")
	log= input("To Login enter l, or to Create an Account enter anything else: ")

	# Validate login or create account info
	if(log=="q" or log=="Q"):
		quit()

	elif(log=="l" or log=="L"):
		login()
	else:
		create()


	# Courses
	while True:
		print("To quit, enter 'q' or 'Q'")
		c= input("To view courses enter 'v' , enter anything else to add courses: ")
		if(c=="Q" or c=="q"):
			quit()

		if(c=="v" or c=="V"):
			vCourses()	
		else:
			aCourses()
	


main()
