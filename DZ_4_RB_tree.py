# Свойства красно-черного дерева:
# 1. Каждый узел либо красный, либо черный
# 2. Корень черный
# 3. Все узлы листьев черные
# 4. Если узел красный, то оба ребенка черные
# 5. Все пути из одного узла проходят через то же количество черных узлов, чтобы достичь любого из его потомка

# Создание класса ноды
class RB_Node:
    # Инициализация ноды
    def __init__ (self, val) -> None:
        self.val = val
        self.parent = None
        self.left = None
        self.right = None
        self.red = False
# Создание класса дерева
class RB_Tree:
    # Инициализация дерева
    def __init__ (self) -> None:
        self.nil = RB_Node(0)
        self.nil.red = False
        self.nil.left = None
        self.nil.right = None
        self.root = self.nil
    # Добавление значения в дерево
    def insert(self, val) -> None:
        # Поиск значения
        new_node = RB_Node(val)
        new_node.parent = None
        new_node.left = self.nil
        new_node.right = self.nil
        new_node.red = True # новый узел - красный

        parent = None
        current = self.root
        while current != self.nil:
            parent = current
            if new_node.val < current.val:
                current = current.left
            elif new_node.val > current.val:
                current = current.right
            else:
                return

        # В найденного родителя вставляем ребенка
        new_node.parent = parent
        if parent == None:
            self.root = new_node
        elif new_node.val < parent.val:
            parent.left = new_node
        else:
            parent.right = new_node

        # Используем метод балансировки
        self.fix_insert(new_node)
    # Метод балансировки
    def fix_insert(self, new_node) -> None:
        while new_node != self.root and new_node.parent.red:
            if new_node.parent == new_node.parent.parent.right:
                u = new_node.parent.parent.left
                if u.red:
                    u.red = False
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.left:
                        new_node = new_node.parent
                        self.rotate_right(new_node)
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    self.rotate_left(new_node.parent.parent)
            else:
                u = new_node.parent.parent.right
                if u.red:
                    u.red = False
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    new_node = new_node.parent.parent
                else:
                    if new_node == new_node.parent.right:
                        new_node = new_node.parent
                        self.rotate_left(new_node)
                    new_node.parent.red = False
                    new_node.parent.parent.red = True
                    self.rotate_right(new_node.parent.parent)
        self.root.red = False
    # Левый поворот
    def rotate_left(self, x) -> None:
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y
    # Правый поворот
    def rotate_right(self, x) -> None:
        y = x.left
        x.left = y.right
        if y.right != self.nil:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y
    # Визуализация дерева
    def __repr__ (self) -> str:
        lines = []
        print_tree(self.root, lines)
        return '\n'.join(lines)
    
# Печать одной ветки дерева
def print_tree(node, lines, level=0) -> None:
    if node.val != 0:
        print_tree(node.left, lines, level + 1)
        lines.append('-' * 3 * level + '> ' + str(node.val) + ' ' + ('r' if node.red else 'b'))
        print_tree(node.right, lines, level + 1)

tree = RB_Tree()
tree.insert(10)
tree.insert(20)
tree.insert(4)
tree.insert(15)
tree.insert(17)
tree.insert(40)
tree.insert(50)
tree.insert(60)
print(tree)
