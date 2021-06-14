import csv
import time


class SubNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class Node:
    def __init__(self, key,tree = None):
        self.key = key
        self.tree = SubAvlTree()
        self.left = None
        self.right = None

class AvlTree:
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

    def insert(self, key, subTree):
        tree = self.node
        newnode = Node(key,subTree)
        if tree is None:
            self.node = newnode
            self.node.tree = subTree
            self.node.left = AvlTree()
            self.node.right = AvlTree()

        elif key < tree.key:
            self.node.left.insert(key, subTree)

        elif key > tree.key:
            self.node.right.insert(key, subTree)

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
            elif key > self.node.key[0] or key < self.node.key[1]:
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
        if node != None:  # just a sanity check

            while node.left != None:

                if node.left.node == None:
                    return node
                else:
                    node = node.left.node
        return node

    def check_balanced(self):
        if self == None or self.node == None:
            return True

        self.update_heights()
        self.update_balances()
        return (abs(self.balance) < 2) and self.node.left.check_balanced() and self.node.right.check_balanced()

    def inorder_traverse(self):
        if self.node == None:
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

    def display(self, key,ano):
        #self.update_heights()
        #self.update_balances()
        if len(key) is 3:
            if self.node is not None:
                if self.node.key[1] == key:
                    self.node.tree.display(key,ano)
                else:
                    if self.node.left is not None:
                        self.node.left.display(key,ano)
                    if self.node.left is not None:
                        self.node.right.display(key,ano)
        else:
            if self.node is not None:
                if self.node.key[0] == key:
                    self.node.tree.display(key,ano)
                else:
                    if self.node.left is not None:
                        self.node.left.display(key,ano)
                    if self.node.left is not None:
                        self.node.right.display(key,ano)

    # update ver sitio certo
    def insertPais(self, key, valor):
        #self.update_heights()
        #self.update_balances()
        if len(key) is 3:
            if self.node is not None:
                if self.node.key[1] == key:
                    self.node.tree.insert(valor)
                else:
                    if self.node.left is not None:
                        self.node.left.insertPais(key, valor)
                    if self.node.left is not None:
                        self.node.right.insertPais(key, valor)
        else:
            if self.node is not None:
                if self.node.key[0] == key:
                    self.node.tree.insert(valor)
                else:
                    if self.node.left is not None:
                        self.node.left.insertPais(key, valor)
                    if self.node.left is not None:
                        self.node.right.insertPais(key, valor)

    def deleteValor(self, key, valor):
        # self.update_heights()
        # self.update_balances()
        if len(key) is 3:
            if self.node is not None:
                if self.node.key[1] == key:
                    self.node.tree.delete(valor)
                else:
                    if self.node.left is not None:
                        self.node.left.deleteValor(key, valor)
                    if self.node.left is not None:
                        self.node.right.deleteValor(key, valor)
        else:
            if self.node is not None:
                if self.node.key[0] == key:
                    self.node.tree.delete(valor)
                else:
                    if self.node.left is not None:
                        self.node.left.deleteValor(key, valor)
                    if self.node.left is not None:
                        self.node.right.deleteValor(key, valor)

    def displayAno(self, ano):
        if self.node is not None:
            self.node.tree.displayAno(ano)
            if self.node.left is not None:
                self.node.left.displayAno(ano)
            if self.node.left is not None:
                self.node.right.displayAno(ano)

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
        node = node.right.node
        if node != None:  # just a sanity check

            while node.left != None:

                if node.left.node == None:
                    return node
                else:
                    node = node.left.node
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


def main():
    i = 0
    a = AvlTree()
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
                subTree = SubAvlTree()
                for j in range(57):
                    if rowSplit[2 + j] == '':
                        pass
                    else:
                        tuploAnos = (str(j + 1960), rowSplit[2 + j])
                        subTree.insert(tuploAnos)

                a.insert(tuplo,subTree)



            i += 1
        menu(a)

        f.close()

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
                a.insert((code,code2),tree)
                t1 = time.time()
                res = (t1-t0)*1000
                res_ = "%.5f" % res
                print("\n",res_,"ms")
            elif check == "dados":
                code = input("Pais/Sigla:\n")
                val1 = input("Ano:\n")
                val2 = input("Valor:\n")
                t0 = time.time()
                a.insertPais(code,(str(val1),str(val2)))
                t1 = time.time()
                res = (t1-t0)*1000
                res_ = "%.5f" % res
                print("\n",res_,"ms")
            else:
                print("Errado!")
        elif ans == "2":
            check = input("Remover pais ou dados?\n")
            if check == "pais":
                code = input("Pais:\n")
                t0 = time.time()
                a.delete(code)
                t1 = time.time()
                res = (t1-t0)*1000
                res_ = "%.5f" % res
                print("\n",res_,"ms")
            elif check == "dados":
                code = input("Pais:\n")
                val = input("Ano a remover:\n")
                t0 = time.time()
                a.deleteValor(code,val)
                t1 = time.time()
                res = (t1-t0)*1000
                res_ = "%.5f" % res
                print("\n",res_,"ms")
        elif ans == "3":
            check = input("pais ou ano?\n")
            if check == "pais":
                code = input("Pais/Sigla:\n")
                ano = input("Ano especifico(0 caso todos):\n")
                t0 = time.time()
                a.display(code,ano)
                t1 = time.time()
                res = (t1-t0)*1000
                res_ = "%.5f" % res
                print("\n",res_,"ms")

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


if __name__ == "__main__":
    main()


