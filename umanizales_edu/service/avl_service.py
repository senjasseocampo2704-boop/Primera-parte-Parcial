from typing import Optional, List
from ..model.schemas import Child, ChildUpdate


class AVLNode:
    """Nodo del Árbol AVL"""
    def __init__(self, child: Child):
        self.child = child
        self.left: Optional['AVLNode'] = None
        self.right: Optional['AVLNode'] = None
        self.height: int = 1  # Altura del nodo (necesaria para balanceo)


class ChildrenAVL:
    """Árbol AVL (Auto-balanceado) para gestionar niños
    
    El árbol mantiene la propiedad de orden por el campo 'id' y se
    auto-balancea después de cada inserción/eliminación mediante rotaciones.
    
    Factor de Balance (BF) = altura(derecha) - altura(izquierda)
    Un árbol está balanceado si: -1 ≤ BF ≤ 1 para cada nodo
    """
    
    def __init__(self):
        self.root: Optional[AVLNode] = None
    
    # ==================== MÉTODOS AUXILIARES ====================
    
    def _get_height(self, node: Optional[AVLNode]) -> int:
        """Obtener la altura de un nodo"""
        if node is None:
            return 0
        return node.height
    
    def _get_balance(self, node: Optional[AVLNode]) -> int:
        """Calcular el factor de balance de un nodo
        
        BF = altura(derecha) - altura(izquierda)
        """
        if node is None:
            return 0
        return self._get_height(node.right) - self._get_height(node.left)
    
    def _update_height(self, node: AVLNode) -> None:
        """Actualizar la altura de un nodo"""
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
    
    # ==================== ROTACIONES ====================
    
    def _rotate_right(self, z: AVLNode) -> AVLNode:
        """Rotación Simple a la Derecha (Right Rotation)
        
        Caso Left-Left (LL):
              z                               y
             / \                            /   \
            y   T4    Right Rotate (z)     x     z
           / \        - - - - - - - ->   / \   / \
          x   T3                        T1 T2 T3 T4
         / \
        T1 T2
        """
        y = z.left
        T3 = y.right
        
        # Realizar rotación
        y.right = z
        z.left = T3
        
        # Actualizar alturas
        self._update_height(z)
        self._update_height(y)
        
        return y
    
    def _rotate_left(self, z: AVLNode) -> AVLNode:
        """Rotación Simple a la Izquierda (Left Rotation)
        
        Caso Right-Right (RR):
          z                                y
         / \                             /   \
        T1  y     Left Rotate(z)        z     x
           / \    - - - - - - - ->    / \   / \
          T2  x                      T1 T2 T3 T4
             / \
            T3 T4
        """
        y = z.right
        T2 = y.left
        
        # Realizar rotación
        y.left = z
        z.right = T2
        
        # Actualizar alturas
        self._update_height(z)
        self._update_height(y)
        
        return y
    
    def _balance(self, node: AVLNode) -> AVLNode:
        """Balancear un nodo aplicando las rotaciones necesarias
        
        Casos:
        1. Left-Left (LL): BF < -1 y BF(left) <= 0 → Rotación derecha
        2. Right-Right (RR): BF > 1 y BF(right) >= 0 → Rotación izquierda
        3. Left-Right (LR): BF < -1 y BF(left) > 0 → Rotación izq en hijo + rot der en nodo
        4. Right-Left (RL): BF > 1 y BF(right) < 0 → Rotación der en hijo + rot izq en nodo
        """
        # Actualizar altura del nodo
        self._update_height(node)
        
        # Calcular factor de balance
        balance = self._get_balance(node)
        
        # Caso Left-Left (LL)
        if balance < -1 and self._get_balance(node.left) <= 0:
            return self._rotate_right(node)
        
        # Caso Right-Right (RR)
        if balance > 1 and self._get_balance(node.right) >= 0:
            return self._rotate_left(node)
        
        # Caso Left-Right (LR)
        if balance < -1 and self._get_balance(node.left) > 0:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        
        # Caso Right-Left (RL)
        if balance > 1 and self._get_balance(node.right) < 0:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        
        return node
    
    # ==================== OPERACIONES CRUD ====================
    
    def insert(self, child: Child) -> bool:
        """Insertar un niño en el árbol AVL con auto-balanceo
        
        Args:
            child: Objeto Child a insertar
            
        Returns:
            True si se insertó correctamente, False si el id ya existe
        """
        self.root = self._insert_recursive(self.root, child)
        return True
    
    def _insert_recursive(self, node: Optional[AVLNode], child: Child) -> AVLNode:
        """Inserción recursiva con balanceo automático
        
        Returns:
            Nodo actualizado
        """
        # Caso base: insertar el nodo
        if node is None:
            return AVLNode(child)
            
        # Verificar duplicado
        if child.id == node.child.id:
            return node
        
        # Inserción recursiva por id
        if child.id < node.child.id:
            node.left = self._insert_recursive(node.left, child)
        else:
            node.right = self._insert_recursive(node.right, child)
        
        # Balancear el nodo después de la inserción
        return self._balance(node)
    
    def search(self, id: int) -> Optional[Child]:
        """Buscar un niño por ID
        
        Args:
            id: ID del niño a buscar
            
        Returns:
            Objeto Child si se encuentra, None si no existe
        """
        return self._search_recursive(self.root, id)
    
    def _search_recursive(self, node: Optional[AVLNode], id: int) -> Optional[Child]:
        """Búsqueda recursiva por ID (recorre todo el árbol si es necesario)"""
        if node is None:
            return None
        
        if id == node.child.id:
            return node.child
        
        # Buscar en ambos subárboles ya que el árbol está ordenado por id
        if id < node.child.id:
            return self._search_recursive(node.left, id)
        else:
            return self._search_recursive(node.right, id)
    
    def update(self, id: int, update_data: ChildUpdate) -> Optional[Child]:
        """Actualizar un niño existente
        
        Args:
            id: ID del niño a actualizar
            update_data: Datos a actualizar
            
        Returns:
            Objeto Child actualizado si existe, None si no se encuentra
        """
        node = self._find_node(self.root, id)
        if node is None:
            return None
        
        # Actualizar solo los campos proporcionados
        if update_data.name is not None:
            node.child.name = update_data.name
        if update_data.age is not None:
            node.child.age = update_data.age
        if update_data.gender is not None:
            node.child.gender = update_data.gender
        
        return node.child
    
    def _find_node(self, node: Optional[AVLNode], id: int) -> Optional[AVLNode]:
        """Encontrar un nodo por ID (recorre todo el árbol si es necesario)"""
        if node is None:
            return None
        
        if id == node.child.id:
            return node
        
        # Buscar en ambos subárboles ya que el árbol está ordenado por id
        if id < node.child.id:
            return self._find_node(node.left, id)
        else:
            return self._find_node(node.right, id)
    
    def delete(self, id: int) -> bool:
        """Eliminar un niño por ID con auto-balanceo
        
        Args:
            id: ID del niño a eliminar
            
        Returns:
            True si se eliminó correctamente, False si no existe
        """
        self.root, deleted = self._delete_recursive(self.root, id)
        return deleted
    
    def _delete_recursive(self, node: Optional[AVLNode], id: int) -> tuple[Optional[AVLNode], bool]:
        """Eliminación recursiva con balanceo automático
        
        Returns:
            Tupla (nodo actualizado, si se eliminó)
        """
        if node is None:
            return None, False
        
        # Buscar el nodo por ID (no por age)
        if id == node.child.id:
            # Nodo encontrado - 3 casos de eliminación
            
            # Caso 1: Nodo hoja (sin hijos)
            if node.left is None and node.right is None:
                return None, True
            
            # Caso 2: Nodo con un solo hijo
            if node.left is None:
                return node.right, True
            if node.right is None:
                return node.left, True
            
            # Caso 3: Nodo con dos hijos
            # Encontrar el sucesor inorden (mínimo del subárbol derecho)
            successor = self._find_min(node.right)
            node.child = successor.child
            node.right, _ = self._delete_recursive(node.right, successor.child.id)
            
            # Balancear el nodo después de la eliminación
            return self._balance(node), True
        else:
            # Buscar en ambos subárboles
            node.left, deleted = self._delete_recursive(node.left, id)
            if deleted:
                return self._balance(node), True
            node.right, deleted = self._delete_recursive(node.right, id)
            if deleted:
                return self._balance(node), True
            return node, False
    
    def _find_min(self, node: AVLNode) -> AVLNode:
        """Encontrar el nodo con el valor mínimo"""
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    # ==================== RECORRIDOS ====================
    
    def inorder_traversal(self) -> List[Child]:
        """Recorrido Inorden (Izquierda -> Raíz -> Derecha)
        
        Returns:
            Lista de niños ordenados por id (ascendente)
        """
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node: Optional[AVLNode], result: List[Child]):
        """Recorrido inorden recursivo"""
        if node is not None:
            self._inorder_recursive(node.left, result)
            result.append(node.child)
            self._inorder_recursive(node.right, result)
    
    def preorder_traversal(self) -> List[Child]:
        """Recorrido Preorden (Raíz -> Izquierda -> Derecha)
        
        Returns:
            Lista de niños en orden preorden
        """
        result = []
        self._preorder_recursive(self.root, result)
        return result
    
    def _preorder_recursive(self, node: Optional[AVLNode], result: List[Child]):
        """Recorrido preorden recursivo"""
        if node is not None:
            result.append(node.child)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)
    
    def postorder_traversal(self) -> List[Child]:
        """Recorrido Postorden (Izquierda -> Derecha -> Raíz)
        
        Returns:
            Lista de niños en orden postorden
        """
        result = []
        self._postorder_recursive(self.root, result)
        return result
    
    def _postorder_recursive(self, node: Optional[AVLNode], result: List[Child]):
        """Recorrido postorden recursivo"""
        if node is not None:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.child)
    
    # ==================== MÉTODOS DE DIAGNÓSTICO ====================
    
    def height(self) -> int:
        """Obtener la altura total del árbol"""
        return self._get_height(self.root)
    
    def count_nodes(self) -> int:
        """Contar la cantidad total de nodos en el árbol"""
        return self._count_nodes_recursive(self.root)
    
    def _count_nodes_recursive(self, node: Optional[AVLNode]) -> int:
        if node is None:
            return 0
        return 1 + self._count_nodes_recursive(node.left) + self._count_nodes_recursive(node.right)
    
    def is_balanced(self) -> bool:
        """Verificar si el árbol está balanceado"""
        return self._is_balanced_recursive(self.root)
    
    def _is_balanced_recursive(self, node: Optional[AVLNode]) -> bool:
        if node is None:
            return True
            
        balance = self._get_balance(node)
        if abs(balance) > 1:
            return False
            
        return (self._is_balanced_recursive(node.left) and 
                self._is_balanced_recursive(node.right))


# Instancia global del árbol AVL (almacenamiento en memoria)
children_avl = ChildrenAVL()
