from  Antrian import *
from  Menu import *
import os

menu = Menu()

menu.insert('nasi goreng', 10000)
menu.insert('mie goreng', 10000)
menu.insert('nasi campur', 10000)
menu.insert('soto', 10000)
menu.insert('jus', 5000)
menu.insert('teh', 5000)
menu.insert('kopi', 5000)


list = menu.inorder()

def inputAlphaValidation(text):
    return input(text).lower()

def inputNumValidation(text):
    while True:
        r = input(text)

        if r.isnumeric():
            return int(r)
        else:
            print("Masukkan anda tidak valid!")

def inputConfirmationValidation():
    while True:
        user = input("Apakah anda sudah selesai(Y/N):").lower()[0]

        if user == 'y':
            return True
        elif user == 'n':
            return False
        else:
            print("Inputan anda tidak valid!")

def tambahMenu():
    print("Tambahkan menu baru:")
    nama = inputAlphaValidation("Masukakan nama makanan:")
    harga = inputNumValidation("Masukkan harga(masukkan dalam bentuk angka):")
    menu.insert(nama=nama, harga=harga)

    print("Menu berhasil ditambahkan!")

def editMenu():
    print("Cari menu yang akan diedit: ")
    namaMenu = inputAlphaValidation("Massukkan nama manakanan yang dicari:")
    node = menu.search(namaMenu)
    if node:
        print("Edit menu:")
        nama = inputAlphaValidation("Masukakan nama makanan yang baru:")
        harga = inputNumValidation("Masukkan harga yang baru(masukkan dalam bentuk angka):")
        node.edit(nama, harga)

def cariMenu():
    print("Cari menu: ")
    namaMenu = inputAlphaValidation("Massukkan nama manakanan yang dicari:")
    r = menu.search(namaMenu)
    while True:
        menu.display(r)
        inp = inputConfirmationValidation()

        if inp:
            break

def hapusMenu():
    nama = inputAlphaValidation("Masukkan menu yang anda ingin hapus:")
    r = menu.deleteNode(menu, nama)
    while True:
        if r == None:
            print("Menu tidak terdaftar!")
        else:
            print("Menu berhasil dihapus!")

        inp = inputConfirmationValidation()
        if inp:
            break



def daftarMenu():
    while True:
        os.system('cls')
        inp = menu.inorder()
        menu.display(inp)
        print("pilih aksi yang akan dilakukan: \n 1. Tambah Menu \n 2. Edit Menu "
              "\n 3. Cari Menu \n 4. Hapus Menu \n 5. Exit")
        action = input(" Pilih action:")
        if action == '1':
            tambahMenu()
        elif action == '2':
            editMenu()
        elif action == '3':
            cariMenu()
        elif action == '4':
            hapusMenu()
        elif action == '5':
            break
        else:
            print('Masukkan anda tidak valid!')



def input_Antrian():
    pass


def pesananJadi():
    pass

def pesanan():
    os.system('cls')
    print("Antrian:")
    print(None)
    print("pilih aksi yang akan dilakukan: \n 1. Tambah Pesanan \n 2. Pesnan sudah jadi \n 3. Cari Pesanan"
          "\n 4. Lihat Menu \n 5. Exit")
    action = input(" Pilih action:")
    if action == '1':
        input_Antrian()
    elif action == '2':
        pesananJadi()
    elif action == '3':
        pass
    elif action == '4':
        daftarMenu()
    elif action == '5':
        return False
    else:
        print('maaf aksi tersebut tidak ada')






while True:
    pesanan()





