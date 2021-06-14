import csv
import time


class Node:
    def __init__(self, data):
        self.data = data
        self.tree = SubAvlTree()
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next

class SubNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class SubAvlTree:
    def __init__(self, *args):
        self.SubNode = None
        self.height = -1
        self.balance = 0
        if len(args) == 1:
            for i in args[0]:
                self.insert(i)

    def height(self):
        if self.SubNode:
            return self.SubNode.height
        else:
            return 0

    def is_leaf(self):
        return self.height == 0

    def insert(self, key):
        tree = self.SubNode
        newnode = SubNode(key)
        if tree is None:
            self.SubNode = newnode
            self.SubNode.left = SubAvlTree()
            self.SubNode.right = SubAvlTree()

        elif key < tree.key:
            self.SubNode.left.insert(key)

        elif key > tree.key:
            self.SubNode.right.insert(key)

        else:
            self.rebalance()

    def rebalance(self):

        # key inserted. Let's check if we're balanced
        self.update_heights(False)
        self.update_balances(False)
        while self.balance < -1 or self.balance > 1:
            if self.balance > 1:
                if self.__setattr__().left.balance < 0:
                    self.SubNode.left.lrotate()  # we're in case II
                    self.update_heights()
                    self.update_balances()
                self.rrotate()
                self.update_heights()
                self.update_balances()

            if self.balance < -1:
                if self.SubNode.right.balance > 0:
                    self.SubNode.right.rrotate()  # we're in case III
                    self.update_heights()
                    self.update_balances()
                self.lrotate()
                self.update_heights()
                self.update_balances()

    def rrotate(self):

        A = self.SubNode
        B = self.SubNode.left.SubNode
        T = B.right.SubNode

        self.SubNode = B
        B.right.SubNode = A
        A.left.SubNode = T

    def lrotate(self):

        A = self.SubNode
        B = self.SubNode.right.SubNode
        T = B.left.SubNode

        self.SubNode = B
        B.left.SubNode = A
        A.right.SubNode = T

    def update_heights(self, recurse=True):
        if not self.SubNode is None:
            if recurse:
                if self.SubNode.left is not None:
                    self.SubNode.left.update_heights()
                if self.SubNode.right is not None:
                    self.SubNode.right.update_heights()

            self.height = max(self.SubNode.left.height, self.SubNode.right.height) + 1
        else:
            self.height = -1

    def update_balances(self, recurse=True):
        if not self.SubNode is None:
            if recurse:
                if self.SubNode.left is not None:
                    self.SubNode.left.update_balances()
                if self.SubNode.right is not None:
                    self.SubNode.right.update_balances()

            self.balance = self.SubNode.left.height - self.SubNode.right.height
        else:
            self.balance = 0

    def delete(self, key):
        if self.SubNode is not None:
            if self.SubNode.key[0] == key:
                if self.SubNode.left.SubNode is None and self.SubNode.right.SubNode is None:
                    self.SubNode = None

                elif self.SubNode.left.SubNode is None:
                    self.SubNode= self.SubNode.right.SubNode
                elif self.SubNode.right.SubNode is None:
                    self.SubNode = self.SubNode.left.SubNode

                else:
                    replacement = self.logical_successor(self.SubNode)
                    if replacement is not None:

                        self.SubNode.key = replacement.key
                        self.SubNode.right.delete(replacement.key)

                self.rebalance()
                return

            elif key < self.SubNode.key[0] or key < self.SubNode.key[1]:
                self.SubNode.left.delete(key)
            elif key > self.SubNode.key[0] or key > self.SubNode.key[1]:
                self.SubNode.right.delete(key)

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
        node = SubNode.right.node
        if SubNode != None:  # just a sanity check

            while SubNode.left != None:

                if SubNode.left.node == None:
                    return node
                else:
                    node = SubNode.left.node
        return node

    def check_balanced(self):
        if self == None or self.node == None:
            return True

        self.update_heights()
        self.update_balances()
        return (abs(self.balance) < 2) and self.node.left.check_balanced() and self.node.right.check_balanced()

    def inorder_traverse(self):
        if self.SubNode == None:
            return []
        inlist = []
        l = self.SubNode.left.inorder_traverse()
        for i in l:
            inlist.append(i)

        inlist.append(self.SubNode.key)


        l = self.SubNode.right.inorder_traverse()
        for i in l:
            inlist.append(i)

        return inlist

    def display(self, key,ano):
        #self.update_heights()
        #self.update_balances()
        if len(key) is 3:
            if self.SubNode is not None:
                if self.SubNode.key[0] == ano:
                    print(self.SubNode.key)
                elif int(ano) is 0:
                    print(self.SubNode.key)
                    if self.SubNode.left is not None:
                        self.SubNode.left.display(key,ano)
                    if self.SubNode.left is not None:
                        self.SubNode.right.display(key,ano)

        else:

            if self.SubNode is not None :
                if self.SubNode.key[0] == ano:
                    print(self.SubNode.key)
                elif int(ano) is 0:
                    print(self.SubNode.key)
                    if self.SubNode.left is not None:
                        self.SubNode.left.display(key,ano)
                    if self.SubNode.left is not None:
                        self.SubNode.right.display(key,ano)

    def displayAno(self,ano):
            if self.SubNode is not None:
                if self.SubNode.key[0] == ano:
                    print(self.SubNode.key)
                else:
                    if self.SubNode.left is not None:
                        self.SubNode.left.displayAno(ano)
                    if self.SubNode.left is not None:
                        self.SubNode.right.displayAno(ano)

class LinkedList:
    def __init__(self):
        self.head = None
        self.node = None

    def is_empty(self):
        return self.head is None

    def add(self, item,tree):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp
        self.head.tree = tree

    def search(self, item,ano):
        current = self.head
        found = False
        while current is not None and not found:
            if current.data[0] == item or current.data[1] == item:
                found = True
                current.tree.insert(ano)
            else:
                current = current.get_next()

    def deleteValor(self, item,ano):
        current = self.head
        found = False
        while current is not None and not found:
            if current.data[0] == item or current.data[1] == item:
                found = True
                current.tree.delete(ano)
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

    def print(self,code,ano):
        node = self.head
        while node:
            if node.get_data():
                if code == node.data[0] or code == node.data[1]:
                  node.tree.display(code,ano)
            node = node.next

    def displayAno(self, ano):
        node = self.head
        while node:
            if node.get_data():
                node.tree.displayAno(ano)
            node = node.next


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
                tree = SubAvlTree()
                code = input("Pais:\n")
                code2 = input("Sigla:\n")
                t0 = time.time()
                a.add((code,code2),tree)
                print("\n",(time.time() - t0) * 1000, "ms")
            elif check == "dados":
                code = input("Pais/Sigla:\n")
                val1 = input("Ano:\n")
                val2 = input("Valor:\n")
                t0 = time.time()
                a.search(code,(val1,val2))
                print("\n",(time.time() - t0) * 1000, "ms")
            else:
                print("Errado!")
        elif ans == "2":
            check = input("Remover pais ou dados?\n")
            if check == "pais":
                code = input("Pais:\n")
                t0 = time.time()
                a.remove(code)
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
                a.print(code, ano)
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
    a = LinkedList()
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
                SubTree = SubAvlTree()
                for j in range(57):
                    if rowSplit[2 + j] == '':
                        pass
                    else:
                        tuploAnos = (str(j + 1960), rowSplit[2 + j])
                        SubTree.insert(tuploAnos)

                a.add(tuplo,SubTree)

            i += 1
        menu(a)
        f.close()


if __name__ == "__main__":
    main()
