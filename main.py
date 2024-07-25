import os, csv

result_dir = 'Result'
result_file = 'exceptions.txt'
list_exeption_domain = 'exception_domain.txt'
list_exeption_email = 'exception_email.txt'
exception_dir = 'Exceptions'
base_dir = 'Base'

if not os.path.exists(result_dir):
	os.makedirs(result_dir)

def searchFile():
	list_file_base = []
	for search_bases in os.listdir(base_dir):list_file_base+=[search_bases]

	number_file = 0
	for list_file in list_file_base:
		number_file+=1
		print(f'[{number_file}] {list_file}')

	try:
		find_base = int(input('\nВыбери номер файла: '))
		if find_base < 1:
			enter_list = list_file_base[0]
			print(enter_list)
			return enter_list
		else:
			enter_list = list_file_base[find_base-1]
			print(enter_list)
			return enter_list	
	except Exception as ex:
		print(f'\nCode Error: {ex}\nПопробуй еще раз...\n')
		searchFile()

def writeException(email):
	with open(f'{result_dir}/{result_file}', 'a+') as result:
		write = result.write(f'{email}\n')
		

def searchDomain(email):
	with open(f'{exception_dir}/{list_exeption_domain}', 'r') as domain_file:
		for domain in domain_file.readlines():
			domain = domain.strip()
			if domain in email:
				print(f'Domain {email}')
				writeException(email)

def searchEmail(email):
	with open(f'{exception_dir}/{list_exeption_email}', 'r') as email_file:
		for mail in email_file.readlines():
			# mail = mail.strip()
			if mail == email:
				print(f'Email {email}')
				writeException(email)

def cleaning():
	open_file_base = searchFile()

	with open(f'{base_dir}/{open_file_base}', 'r') as file:
		number_string = 0
		for row in csv.DictReader(file):
			number_string+=1
			email = row['Email']
			# print(f'{number_string} {email}')
			searchDomain(email)
			searchEmail(email)



if __name__ == '__main__':
	try:
		cleaning()
	except Exception as ex:
		print(f'\nError: {ex}\n')
		cleaning()