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

    def display(self,menus):

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

    def deleteNode(self, root, key):
        # Base case
        if root is None:
            return root

        # If the key to be deleted is smaller than the root's key, then it lies in the left subtree
        if key < root.__nama:
            root.left = self.deleteNode(root.__left, key)
        # If the key to be deleted is greater than the root's key, then it lies in the right subtree
        elif key > root.__nama:
            root.__right = self.deleteNode(root.__right, key)
        # If key is same as root's key, then this is the node to be deleted
        else:
            # Node with only one child or no child
            if root.__left is None:
                return root.__right
            elif root.right is None:
                return root.__left

            # Node with two children: Get the inorder successor (smallest in the right subtree)
            root.__nama = self.minValue(root.__right)

            # Delete the inorder successor
            root.__right = self.deleteNode(root.__right, root.__nama)

        return root

    def minValue(self, root):
        minv = root.__nama
        while root.__left:
            minv = root.__left.__nama
            root = root.__left
        return minv
