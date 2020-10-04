import requests as r, json, os
hijau, putih, merah, cyan, kuning, ungu, garis = '\x1b[1;92m', '\x1b[1;97m', '\x1b[1;91m', '\x1b[1;96m', '\x1b[1;93m', '\x1b[1;95m', "-"*40

class Main:
	def __init__(self, link):
		self.link = link

	def Facebook(self):
		self.req = r.post('https://api.dz-tools.my.id/fb/video-downloader/', data={"url":self.link}).text
		self.get = json.loads(self.req)
		if "error_msg" in self.req:
			exit(f"{merah}[X]{putih} "+self.get["error_msg"]+'\n')
		else:
			try:
				print(f"\n{merah}[=]{putih} CAPTION{merah}:{hijau} "+self.get["description"])
			except KeyError:
				print(f"\n{merah}[=]{putih} CAPTION{merah}:{hijau} ----")
			try:
				self.out = input(f'{merah}[•] {putih}OUTPUT {merah}:{hijau} ')
			except (EOFError,KeyboardInterrupt):
				exit('\n')
			while self.out == "":
				print("{merah}[+]{putih} TULIS HASIL VIDEONYA MANK")
				try: self.out = input(f'{merah}[•] {putih}OUTPUT {merah}:{hijau} ')
				except (EOFError,KeyboardInterrupt): exit('\n')
			self.run = r.get(self.get["video_url"]).content
			with open(self.out+'.mp4', 'wb') as sv:
				sv.write(self.run)
			exit(f'{merah}[✓] {putih}BERHASIL TERUNDUH{hijau}...\n')

	def Instagram(self):
		self.req = r.post('https://api.dz-tools.my.id/ig/video-downloader/', data={"url":self.link}).text
		self.get = json.loads(self.req)
		if "error_msg" in self.req:
			exit(f"{merah}[X]{putih} "+self.get["error_msg"]+'\n')
		else:
			try:
				print(f"\n{merah}[=]{putih} CAPTION{merah}:{hijau} "+self.get["description"])
			except KeyError:
				print(f"\n{merah}[=]{putih} CAPTION{merah}:{hijau} ----")
			try:
				self.out = input(f'{merah}[•] {putih}OUTPUT {merah}:{hijau} ')
			except (EOFError,KeyboardInterrupt):
				exit('\n')
			while self.out == "":
				print("{merah}[+]{putih} TULIS HASIL VIDEONYA MANK")
				try: self.out = input(f'{merah}[•] {putih}OUTPUT {merah}:{hijau} ')
				except (EOFError,KeyboardInterrupt): exit('\n')
			self.run = r.get(self.get["video_url"]).content
			with open(self.out+'.mp4', 'wb') as sv:
				sv.write(self.run)
			exit(f'{merah}[✓] {putih}BERHASIL TERUNDUH{hijau}...\n')

def mulai():
	# Anjay Banyak Warna:v
	print(f"""
{putih} _______
{putih}|       | {cyan}> {putih}Author{merah}: {hijau}Rizky
{putih}|  {ungu}[•]{putih}  | {cyan}> {putih}Github{merah}: {hijau}github.com/hekelpro
{putih}|_______| {cyan}> {putih}Fungsi{merah}: {hijau}DOWNLOAD VIDEO IG|FB
{kuning}{garis}
{cyan}[{hijau}01{cyan}] {putih}VIDEO FACEBOOK DOWNLOADER
{cyan}[{hijau}02{cyan}] {putih}VIDEO INSTAGRAM DOWNLOADER
{cyan}[{merah}00{cyan}] {putih}KELUAR PROGRAM{merah}...
{kuning}{garis}""")
	pil = input(f"{merah}[➡] {putih}PILIH{merah}:{hijau} ")
	while pil =="":
		print(f"{merah}[=] {putih}Pilihan Jangan Kosong")
		pil = input(f"{merah}[➡] {putih}PILIH{merah}:{hijau} ")
	if pil in ("01","1"):
		link = input(f"{kuning}{garis}\n{merah}[•] {putih}LINK VIDEO{merah}:{hijau} ")
		run = Main(link)
		run.Facebook()
	elif pil in ("02","2"):
		link = input(f"{kuning}{garis}\n{merah}[•] {putih}LINK VIDEO{merah}:{hijau} ")
		run = Main(link)
		run.Instagram()
	elif pil in ("00","0"):
		exit(f"{merah}[=]{putih} PROGRAM BERAKHIR{merah}...\n")
	else:
		exit(f"{merah}[!] {putih}Dahlah Males Bro{merah}...\n")

if __name__=="__main__":
	os.system('clear')
	try:
		mulai()
	except Exception as stack:
		exit(f"{merah}[!]{putih} ERROR:{merah} {str(stack)} ")

# <!-- XIUZCODE | OPEN SOURCE TEAM --!>
#######################################
#            BEBAS RECODE             #
