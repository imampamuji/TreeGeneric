class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.children = []

class TreeNode:
    def __init__(self):
        self.nodes = {}

    def setChild(self, node, child):
        if self.nodes.get(node) != None: #cek apakah node mempunyai parent / tidak
            get = self.nodes.get(node) # apabila punya maka ambil objek node nya
            get[0].children.append(child) # karna objek masih dalam betuk array berisi 1 data, ambil menggunakan no index, panggil field children dan tambahkan

    def setParent(self, node, parent):
        tmpNode = node
        tmpNode.parent = self.nodes.get(parent)

    def newNode(self, data):
        newNode = Node(data)
        self.nodes[data] = [newNode]
        return newNode

    def addNode(self, data, parent=None):
        node = self.newNode(data)
        self.setParent(node, parent)
        self.setChild(parent, data)

    def moveNode(self, keySource, keyDest):
        node = self.nodes.get(keySource)
        nodePar = node[0].parent[0].children.remove(keySource)

        self.setParent(node[0], keyDest)
        self.setChild(keyDest, keySource)

    def getLvl(self, val):
        lvl = 0
        getNode = self.nodes.get(val)
        par = getNode[0].parent
        while par:
            lvl += 1
            par = par[0].parent
        return lvl

    def loopLvl(self, rootChild, nodeKeys, n):
        if nodeKeys.index(n):
            rootChild = self.nodes[n][0].children
            for n in rootChild:
                tab = ("\t " * self.getLvl(n)) + "|__"
                print(tab, n)
                self.loopLvl(rootChild,nodeKeys, n)

    def printTree(self):
        nodeKeys = list(self.nodes.keys())
        if len(nodeKeys) == 0:
            print("kosong")
            return "node kosong"

        rootName = nodeKeys[0]

        nodeRoot = self.nodes.get(rootName)
        rootChild = nodeRoot[0].children
        print()
        print(rootName)
        for rc in rootChild:
            tab = ("\t " * self.getLvl(rc)) + "|__"
            print(tab, rc)

            if nodeKeys.index(rc):
                rootChild = self.nodes[rc][0].children
                for n in rootChild:
                    tab = ("\t " * self.getLvl(n)) + "|__"
                    print(tab, n)
                    self.loopLvl(rootChild, nodeKeys, n)

def manage(tree ,data):
    
    if ".pdf" in data:
        tree.moveNode(data, "pdf")
    else:
        tree.moveNode(data, "etc")
        

def program():
    menu = 1000
    tree = TreeNode()

    while True :

        print("1. Tambah Node")
        print("2. Lihat Tree")
        print("3. Manajemen Otomatis")
        print("4. Break")
        menu = int(input("\nPILIH MENU: "))

        if menu == 1:
            if len(tree.nodes) == 0:
                root = str(input("masukan data root: "))
                tree.addNode(root)
            else:
                data = str(input("masukan data: "))
                parent = str(input("masukan parent: "))
                tree.addNode(data, parent)
            tree.printTree()
            print()

        elif menu == 2:
            tree.printTree()

        elif menu == 3:
            src = str(input("File Download Masuk --> : "))
            tree.addNode(src, "Download")
            if "pdf" in src:
                print("non pdf")
                tree.moveNode(src, "pdf")
            else:
                print("etc")
                tree.moveNode(src, "etc")

        elif menu == 4:
            break

if __name__ == '__main__':
    # build_product_tree()
    program()
