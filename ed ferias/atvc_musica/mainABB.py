from BinarySearchTree import BinarySearchTree

arv = BinarySearchTree()

arv.add(8)
arv.add(10)
arv.add(7)
arv.add(11)
arv.add(4)
arv.add(5)
arv.add(20)
arv.add(10)

arv.traversal(BinarySearchTree.inorder)

arv.treeview()

print(arv.delete(20))
arv.treeview()

print()
print(arv.delete(10))
arv.treeview()

print()
print(arv.delete(8))
arv.treeview()

print(len(arv))
print(5 in arv)


