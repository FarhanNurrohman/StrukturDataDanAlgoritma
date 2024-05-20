class Pesanan():
    def __init__(self, atasNama):
        self.atasNama = atasNama
        self.menu = []
        self.next = None

class Antrian():
    def __init__(self):
        self.front = None
        self.rear = None

    def isEmpty(self):
        return self.front == None

    def display(self):
        if self.isEmpty():
            print("Quee is empty\n")
            return

        temp = self.front

        while temp:
            print(temp.data, end=' ')
            temp = temp.next
        print(" ")

    def enquee(self, atasNama, menu):
        pesanan = Pesanan(atasNama)
        pesanan.menu += menu

        if self.isEmpty():
            self.front = self.rear= pesanan
        else:
            self.rear.next = pesanan
            self.rear = pesanan

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        hapus = self.front
        self.front = hapus.next
        return hapus

    def display(self):
        if self.isEmpty():
            print("Belum ada pesanan\n")
            return

        temp = self.front

        while temp:
            print(temp.atasNama, end=' ')
            temp = temp.next
        print(" ")
