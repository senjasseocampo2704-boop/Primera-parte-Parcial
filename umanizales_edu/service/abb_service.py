from typing import Optional, List
from ..model.schemas import Child, ChildUpdate


class BSTNode:
    """Nodo del Árbol Binario de Búsqueda"""
    def __init__(self, child: Child):
        self.child = child
        self.left: Optional['BSTNode'] = None
        self.right: Optional['BSTNode'] = None


class ChildrenBST:
    """Árbol Binario de Búsqueda para gestionar niños
    
    El árbol mantiene la propiedad de orden por el campo 'age':
    - Subárbol izquierdo: edades menores
    - Subárbol derecho: edades mayores
    """
    
    def __init__(self):
        self.root: Optional[BSTNode] = None
    
    def insert(self, child: Child) -> bool:
        """Insertar un niño en el árbol
        
        Args:
            child: Objeto Child a insertar
            
        Returns:
            True si se insertó correctamente, False si el id ya existe
        """
        if self.root is None:
            self.root = BSTNode(child)
            return True
        return self._insert_recursive(self.root, child)
    
    def _insert_recursive(self, node: BSTNode, child: Child) -> bool:
        """Inserción recursiva"""
        if child.id == node.child.id:
            # ID duplicado
            return False
        
        if child.age < node.child.age:
            if node.left is None:
                node.left = BSTNode(child)
                return True
            return self._insert_recursive(node.left, child)
        else:
            if node.right is None:
                node.right = BSTNode(child)
                return True
            return self._insert_recursive(node.right, child)
    
    def search(self, child_id: int) -> Optional[Child]:
        """Buscar un niño por ID
        
        Args:
            child_id: ID del niño a buscar
            
        Returns:
            Objeto Child si se encuentra, None si no existe
        """
        return self._search_recursive(self.root, child_id)
    
    def _search_recursive(self, node: Optional[BSTNode], child_id: int) -> Optional[Child]:
        """Búsqueda recursiva por ID (recorre todo el árbol si es necesario)"""
        if node is None:
            return None
        
        if child_id == node.child.id:
            return node.child
        
        # Buscar en ambos subárboles ya que el árbol está ordenado por age, no por id
        left_result = self._search_recursive(node.left, child_id)
        if left_result is not None:
            return left_result
        
        return self._search_recursive(node.right, child_id)
    
    def update(self, child_id: int, child_update: ChildUpdate) -> Optional[Child]:
        """Actualizar un niño existente
        
        Args:
            child_id: ID del niño a actualizar
            child_update: Datos a actualizar
            
        Returns:
            Objeto Child actualizado si existe, None si no se encuentra
        """
        node = self._find_node(self.root, child_id)
        if node is None:
            return None
        
        # Actualizar solo los campos proporcionados
        if child_update.name is not None:
            node.child.name = child_update.name
        if child_update.age is not None:
            node.child.age = child_update.age
        if child_update.gender is not None:
            node.child.gender = child_update.gender
        
        return node.child
    
    def _find_node(self, node: Optional[BSTNode], child_id: int) -> Optional[BSTNode]:
        """Encontrar un nodo por ID (recorre todo el árbol si es necesario)"""
        if node is None:
            return None
        
        if child_id == node.child.id:
            return node
        
        # Buscar en ambos subárboles ya que el árbol está ordenado por age, no por id
        left_result = self._find_node(node.left, child_id)
        if left_result is not None:
            return left_result
        
        return self._find_node(node.right, child_id)
    
    def delete(self, child_id: int) -> bool:
        """Eliminar un niño por ID
        
        Args:
            child_id: ID del niño a eliminar
            
        Returns:
            True si se eliminó correctamente, False si no existe
        """
        self.root, deleted = self._delete_recursive(self.root, child_id)
        return deleted
    
    def _delete_recursive(self, node: Optional[BSTNode], child_id: int) -> tuple[Optional[BSTNode], bool]:
        """Eliminación recursiva
        
        Returns:
            Tupla (nodo actualizado, si se eliminó)
        """
        if node is None:
            return None, False
        
        # Buscar el nodo por ID (no por age)
        if child_id == node.child.id:
            # Nodo encontrado - 3 casos
            
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
            return node, True
        else:
            # Buscar en ambos subárboles
            node.left, deleted = self._delete_recursive(node.left, child_id)
            if deleted:
                return node, True
            node.right, deleted = self._delete_recursive(node.right, child_id)
            return node, deleted
    
    def _find_min(self, node: BSTNode) -> BSTNode:
        """Encontrar el nodo con el valor mínimo"""
        current = node
        while current.left is not None:
            current = current.left
        return current
    
    def inorder_traversal(self) -> List[Child]:
        """Recorrido Inorden (Izquierda -> Raíz -> Derecha)
        
        Returns:
            Lista de niños ordenados por age (ascendente)
        """
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node: Optional[BSTNode], result: List[Child]):
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
    
    def _preorder_recursive(self, node: Optional[BSTNode], result: List[Child]):
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
    
    def _postorder_recursive(self, node: Optional[BSTNode], result: List[Child]):
        """Recorrido postorden recursivo"""
        if node is not None:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.child)


# Instancia global del árbol (almacenamiento en memoria)
children_bst = ChildrenBST()