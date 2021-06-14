import csv
import time


class NodeLista:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, item):
        temp = NodeLista(item)

        if self.is_empty():
            self.head = temp
            return
        previous = self.head
        next = self.head.next
        while next is not None:
            previous = next
            next = next.next
        previous.next = temp

    def search(self, item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()


    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:

            if current.data[0] == item:
                found = True
            else:
                previous = current
                current = current.get_next()
                if current.get_next() is None:
                    found = True
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def print(self,ano):
        node = self.head
        while node:
            if node.get_data():
                if ano == node.data[0]:
                    print("(",str(ano),",",str(node.data[1]),")")
                elif int(ano) == 0:
                    print(node.get_data())
            node = node.next

class Node:
    def __init__(self, key, lista = None):
        self.key = key
        self.lista = LinkedList()
        self.left = None
        self.right = None

class AVLTree:
    def __init__(self, *args):
        self.node = None
        self.height = -1
        self.balance = 0
        if len(args) == 1:
            for i in args[0]:
                self.insert(i)

    def height(self):
        if self.node:
            return self.node.height
        else:
            return 0

    def is_leaf(self):
        return self.height == 0

    def insert(self, key, lista):
        tree = self.node
        newnode = Node(key,lista)
        if tree is None:
            self.node = newnode
            self.node.lista = lista
            self.node.left = AVLTree()
            self.node.right = AVLTree()

        elif key < tree.key:
            self.node.left.insert(key,lista)

        elif key > tree.key:
            self.node.right.insert(key,lista)

        else:
            self.rebalance()

    def rebalance(self):

        # key inserted. Let's check if we're balanced
        self.update_heights(False)
        self.update_balances(False)
        while self.balance < -1 or self.balance > 1:
            if self.balance > 1:
                if self.node.left.balance < 0:
                    self.node.left.lrotate()  # we're in case II
                    self.update_heights()
                    self.update_balances()
                self.rrotate()
                self.update_heights()
                self.update_balances()

            if self.balance < -1:
                if self.node.right.balance > 0:
                    self.node.right.rrotate()  # we're in case III
                    self.update_heights()
                    self.update_balances()
                self.lrotate()
                self.update_heights()
                self.update_balances()

    def rrotate(self):

        A = self.node
        B = self.node.left.node
        T = B.right.node

        self.node = B
        B.right.node = A
        A.left.node = T

    def lrotate(self):

        A = self.node
        B = self.node.right.node
        T = B.left.node

        self.node = B
        B.left.node = A
        A.right.node = T

    def update_heights(self, recurse=True):
        if not self.node is None:
            if recurse:
                if self.node.left is not None:
                    self.node.left.update_heights()
                if self.node.right is not None:
                    self.node.right.update_heights()

            self.height = max(self.node.left.height, self.node.right.height) + 1
        else:
            self.height = -1

    def update_balances(self, recurse=True):
        if not self.node is None:
            if recurse:
                if self.node.left is not None:
                    self.node.left.update_balances()
                if self.node.right is not None:
                    self.node.right.update_balances()

            self.balance = self.node.left.height - self.node.right.height
        else:
            self.balance = 0

    def delete(self, key):
        if self.node is not None:
            if self.node.key[1] == key or self.node.key[0] == key:
                if self.node.left.node is None and self.node.right.node is None:
                    self.node = None
                elif self.node.left.node is None:
                    self.node = self.node.right.node
                elif self.node.right.node is None:
                    self.node = self.node.left.node
                else:
                    replacement = self.logical_successor(self.node)
                    if replacement is not None:
                        self.node.key = replacement.key
                        self.node.right.delete(replacement.key)
                self.rebalance()
                return
            elif key < self.node.key[0] or key < self.node.key[1]:
                self.node.left.delete(key)
            elif key > self.node.key[0] or key<self.node.key[1]:
                self.node.right.delete(key)
            self.rebalance()
        else:
            return

    def logical_predecessor(self, node):
        node = node.left.node
        if node is not None:
            while node.right is not None:
                if node.right.node is None:
                    return node
                else:
                    node = node.right.node
        return node

    def logical_successor(self, node):
        node = node.right.node
        if node is not None:  # just a sanity check

            while node.left is not None:

                if node.left.node is None:
                    return node
                else:
                    node = node.left.node
        return node

    def check_balanced(self):
        if self is None or self.node is None:
            return True

        self.update_heights()
        self.update_balances()
        return (abs(self.balance) < 2) and self.node.left.check_balanced() and self.node.right.check_balanced()

    def inorder_traverse(self):
        if self.node is None:
            return []
        inlist = []
        l = self.node.left.inorder_traverse()
        for i in l:
            inlist.append(i)

        inlist.append(self.node.key)


        l = self.node.right.inorder_traverse()
        for i in l:
            inlist.append(i)

        return inlist

    def display(self, key, ano):
        #self.update_heights()
        #self.update_balances()
        if len(key) is 3:
            if self.node is not None:
                if self.node.key[1] == key:
                    self.node.lista.print(ano)
                else:
                    if self.node.left is not None:
                        self.node.left.display(key,ano)
                    if self.node.left is not None:
                        self.node.right.display(key,ano)
        else:
            if self.node is not None:
                if self.node.key[0] == key:
                    self.node.lista.print(ano)
                else:
                    if self.node.left is not None:
                        self.node.left.display(key,ano)
                    if self.node.left is not None:
                        self.node.right.display(key,ano)

    def insertPais(self, key,valor):
        # self.update_heights()
        # self.update_balances()
        if len(key) is 3:
            if self.node is not None:
                if self.node.key[1] == key:
                    self.node.lista.add(valor)
                else:
                    if self.node.left is not None:
                        self.node.left.insertPais(key,valor)
                    if self.node.left is not None:
                        self.node.right.insertPais(key,valor)
        else:
            if self.node is not None:
                if self.node.key[0] == key:
                    self.node.lista.add(valor)
                else:
                    if self.node.left is not None:
                        self.node.left.insertPais(key,valor)
                    if self.node.left is not None:
                        self.node.right.insertPais(key,valor)

    def deleteValor(self, key, valor):
        # self.update_heights()
        # self.update_balances()
        if len(key) is 3:
            if self.node is not None:
                if self.node.key[1] == key:
                    self.node.lista.remove(valor)
                else:
                    if self.node.left is not None:
                        self.node.left.deleteValor(key, valor)
                    if self.node.left is not None:
                        self.node.right.deleteValor(key, valor)
        else:
            if self.node is not None:
                if self.node.key[0] == key:
                    self.node.lista.remove(valor)
                else:
                    if self.node.left is not None:
                        self.node.left.deleteValor(key, valor)
                    if self.node.left is not None:
                        self.node.right.deleteValor(key, valor)

    def displayAno(self,ano):
            if self.node is not None:
                self.node.lista.print(ano)
                if self.node.left is not None:
                    self.node.left.displayAno(ano)
                if self.node.left is not None:
                    self.node.right.displayAno(ano)


def menu(a):
    ans = True
    while ans:
        print("""
        1.Add
        2.Remove
        3.Search
        4.Back
        """)
        ans = input("Opção:\n ")
        if ans == "1":
            check =input("Inserir pais ou dados?\n")
            if check == "pais":
                lista = LinkedList()
                code = input("Pais:\n")
                code2 = input("Sigla:\n")
                t0 = time.time()
                a.insert((code,code2),lista)
                print("\n",(time.time() - t0) * 1000, "ms")
            elif check == "dados":
                code = input("Pais/Sigla:\n")
                val1 = input("Ano:\n")
                val2 = input("Valor:\n")
                t0 = time.time()
                a.insertPais(code,(str(val1),str(val2)))
                print("\n",(time.time() - t0) * 1000, "ms")
            else:
                print("Errado!")
        elif ans == "2":
            check = input("Remover pais ou dados?\n")
            if check == "pais":
                code = input("Pais:\n")
                t0 = time.time()
                a.delete(code)
                print("\n",(time.time() - t0) * 1000, "ms")
            elif check == "dados":
                code = input("Pais:\n")
                val = input("Ano a remover:\n")
                t0 = time.time()
                a.deleteValor(code,val)
                print("\n",(time.time() - t0) * 1000, "ms")
        elif ans == "3":
            check = input("pais ou ano?\n")
            if check == "pais":
                code = input("Pais/Sigla:\n")
                ano = input("Ano especifico(0 caso todos):\n")
                t0 = time.time()
                a.display(code, ano)
                print("\n",(time.time() - t0) * 1000, "ms")
            elif check == "ano":
                ano = input("Ano:\n ")
                t0 = time.time()
                a.displayAno(ano)
                print("\n",(time.time() - t0)*1000,"ms")

        elif ans == "4":
            print("\n Goodbye!")
            break
        elif ans != "":
            print("\n Not Valid Choice Try again")

def main():
    i = 0
    a = AVLTree()
    with open("dados.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            rowSplit = row[0].split(";")
            for j in range(len(rowSplit)):
                if rowSplit[j] is not "":
                    rowSplit[j] = rowSplit[j].replace('"','')
            if i == 0:
                pass
            else:
                tuplo = (rowSplit[0], rowSplit[1])
                lista = LinkedList()
                for j in range(57):
                    if rowSplit[2 + j] == '':
                        pass
                    else:
                        tuploAnos = (str(j + 1960), rowSplit[2 + j])
                        lista.add(tuploAnos)
                a.insert(tuplo, lista)
            i += 1
        menu(a)
        f.close()


if __name__ == "__main__":
    main()
