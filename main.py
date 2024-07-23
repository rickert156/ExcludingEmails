import os, csv

result_dir = 'Result'
list_exeption_domain = 'exception_domain.txt'
list_exeption_email = 'exception_email.txt'
exception_dir = 'Exceptions'
base_dir = 'Base'
all_exceptions = [list_exeption_domain, list_exeption_email]

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
		

def cleaning():
	open_file_base = searchFile()

	with open(f'{base_dir}/{open_file_base}', 'r') as file_base:
		print('')
		row_number = 0
		for row_emails in csv.DictReader(file_base):
			row_number+=1
			emails = row_emails['Email']
			
			#Запись исключений по домену
			with open(f'{exception_dir}/{list_exeption_domain}', 'r') as exception_file:
				number_string = 0
				for string_exceptions in exception_file.readlines():
					string_exceptions = string_exceptions.strip()
					number_string+=1
					if string_exceptions in emails:
						
						print(f'[Domain] [{number_string}] {emails}')

			#Запись исключения по адресу
			with open(f'{exception_dir}/{list_exeption_email}', 'r') as exception_file:
				number_string = 0
				for string_exceptions in exception_file.readlines():
					string_exceptions = string_exceptions.strip()
					number_string+=1
					if string_exceptions in emails:
						
						print(f'[Emails] [{number_string}] {emails}')

if __name__ == '__main__':
	try:
		cleaning()
	except Exception as ex:
		print(f'\nError: {ex}\n')
		cleaning()