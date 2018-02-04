import os


migrations = 'Migrations'
current_dir = os.path.dirname(os.path.abspath(__file__))

print(__file__)
print(os.path.abspath(__file__))
print(current_dir)


if __name__ == '__main__':	
	
	migrations_dir = os.path.join(current_dir, migrations)
	sql_files_list = [s for s in os.listdir(migrations_dir) if s.endswith('.sql') ]
	print('Всего файлов *.sql: {}'.format(len(sql_files_list)))
	working_list = []
	
	while True:
		search_for = input('Введите строку: ')
		working_list = sql_files_list.copy()
		for filename in working_list:
			with open(os.path.join(migrations_dir, filename)) as f:
				content = f.read()
				if search_for in content:
					print(filename)
				else:
					sql_files_list.remove(filename)
		print('Всего: {}'.format(len(sql_files_list)))


