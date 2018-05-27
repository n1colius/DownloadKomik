# -*- coding: utf-8 -*-
# @Author: nikolius
# @Date:   2018-04-17 21:49:20
# @Last Modified by:   nikolius
# @Last Modified time: 2018-05-27 17:01:24
# Python3.5 to run

#from pprint import pprint #untuk debug
import requests
from requests import get
from bs4 import BeautifulSoup
import os
import pathlib
import shutil

#Define Variabel
ListKomik = ['1','2'];
UrlListImgDownload = [];
WorkingDir = os.path.dirname(os.path.realpath(__file__))



#Mau Download Komik apa
KomikID = input('LIST KOMIK\n1. One Piece\n2. Hajime No Ippo\nPilih komik dengan memasukkan angka nya: ')
ChapterNO = input('Masukkan chapter komik yang mau di download: ')
print('\n')

# ======================== One Piece ================================
if KomikID == '1':
	UrlOnePiece = 'http://readmanga.biz/One-Piece/chapter_'+ChapterNO
	KomikPage = requests.get(UrlOnePiece)

	if KomikPage.status_code == 200:
		soup = BeautifulSoup(KomikPage.content, 'html.parser')
		tagImgs = soup.find_all('img')
		#pprint(tagImgs) #untuk debug

		for imgPage in tagImgs:
			try:
				if imgPage.get('class')[0] == 'lazy':
					UrlListImgDownload.append(imgPage.get('data-original'))
			except TypeError:
				pass

		#Coba Print
		#pprint(UrlListImgDownload);

		if UrlListImgDownload: #Cek kalau array ada isinya
			incre = 1;

			#Untuk buat folder terlebih dahulu
			pathlib.Path(WorkingDir+'/One_Piece/').mkdir(parents=True,exist_ok=True)
			pathlib.Path(WorkingDir+'/One_Piece/'+str(ChapterNO)+'/').mkdir(parents=True,exist_ok=True)
			DirToWrite = WorkingDir+'/One_Piece/'+str(ChapterNO)+'/'

			for imgDownload in UrlListImgDownload:

				#Get file extension
				FileExt = imgDownload.split('.')[-1]

				flnameWrite = DirToWrite+str(incre)+'.'+FileExt
				incre = incre + 1

				response = get(imgDownload)
				if response.status_code == 200:
					with open(flnameWrite, "wb") as file:
						file.write(response.content)
						print('Downloading ...')

			#Ngezip
			shutil.make_archive('OnePiece_'+ChapterNO, 'zip', DirToWrite)

			#Hapus Foldernya
			shutil.rmtree(WorkingDir+'/One_Piece');

			print('Download Finish')
		else:
			print('Image komik tidak ditemukan')

	else:
		print("URL Download komik tidak ditemukan")

# ======================== Hajime No Ippo ================================
if KomikID == '2':
	UrlOnePiece = 'http://readmanga.biz/Hajime-No-Ippo/chapter_'+ChapterNO
	KomikPage = requests.get(UrlOnePiece)

	if KomikPage.status_code == 200:
		soup = BeautifulSoup(KomikPage.content, 'html.parser')
		tagImgs = soup.find_all('img')
		#pprint(tagImgs) #untuk debug

		for imgPage in tagImgs:
			try:
				if imgPage.get('class')[0] == 'lazy':
					UrlListImgDownload.append(imgPage.get('data-original'))
			except TypeError:
				pass

		#Coba Print
		#pprint(UrlListImgDownload);

		if UrlListImgDownload: #Cek kalau array ada isinya
			incre = 1;

			#Untuk buat folder terlebih dahulu
			pathlib.Path(WorkingDir+'/Hajime-No-Ippo/').mkdir(parents=True,exist_ok=True)
			pathlib.Path(WorkingDir+'/Hajime-No-Ippo/'+str(ChapterNO)+'/').mkdir(parents=True,exist_ok=True)
			DirToWrite = WorkingDir+'/Hajime-No-Ippo/'+str(ChapterNO)+'/'

			for imgDownload in UrlListImgDownload:

				#Get file extension
				FileExt = imgDownload.split('.')[-1]

				flnameWrite = DirToWrite+str(incre)+'.'+FileExt
				incre = incre + 1

				response = get(imgDownload)
				if response.status_code == 200:
					with open(flnameWrite, "wb") as file:
						file.write(response.content)
						print('Downloading ...')

			#Ngezip
			shutil.make_archive('Hajime-No-Ippo_'+ChapterNO, 'zip', DirToWrite)

			#Hapus Foldernya
			shutil.rmtree(WorkingDir+'/Hajime-No-Ippo');

			print('Download Finish')
		else:
			print('Image komik tidak ditemukan')

	else:
		print("URL Download komik tidak ditemukan")


if KomikID not in ListKomik:
	print('Komik tidak terdaftar')