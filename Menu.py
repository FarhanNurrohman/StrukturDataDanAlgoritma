import os

class Menu():
    def __init__(self, nama = None, harga = None):
        self.__nama = nama
        self.__harga = harga
        self.__left = self.__right = None

    def insert(self, nama, harga):
        if self.__nama == None:
            self.__nama = nama
            self.__harga = harga
        elif self.__nama > nama:
            if not self.__left:
                self.__left = Menu(nama, harga)
            else:
                self.__left.insert(nama, harga)

        elif self.__nama < nama:
            if not self.__right:
                self.__right = Menu(nama, harga)
            else:
                self.__right.insert(nama, harga)
        else:
            print("Menu sudah ada")

    def inorder(self):
        items = []
        if self.__left:
            items +=self.__left.inorder()
        items.append(self)
        if self.__right:
            items +=self.__right.inorder()
        return items

    def display(self):
        menus = self.inorder()
        i = 1
        print("Daftar menu :\nharga \t \t nama")
        for menu in menus:
            print(f"{i}. {menu.__harga} \t {menu.__nama}")
            i+=1
    def search(self,nama):
        if nama == self.__nama:
            return self
        elif nama < self.__nama:
            return self.__left.search(nama)
        elif nama > self.__nama:
            return self.__right.search(nama)
        else:
            print("Menu tidak ditemukan")
            return False

    def edit(self, newNama, harga):
        self.__nama = newNama
        self.__harga = harga
        print("Menu berhasil diedit")
