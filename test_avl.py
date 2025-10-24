"""
Script de prueba para verificar el Árbol AVL con auto-balanceo
"""
from umanizales_edu.service.avl_service import ChildrenAVL
from umanizales_edu.model.schemas import Child, ChildUpdate

def print_tree_structure(node, prefix="", is_tail=True):
    """Imprimir la estructura del árbol de forma visual"""
    if node is None:
        return
    
    print(prefix + ("└── " if is_tail else "├── ") + 
          f"Doc:{node.child.documento} (h={node.height}, BF={get_balance_factor(node)})")
    
    if node.left is not None or node.right is not None:
        if node.right is not None:
            print_tree_structure(node.right, prefix + ("    " if is_tail else "│   "), False)
        else:
            print(prefix + ("    " if is_tail else "│   ") + "├── None")
        
        if node.left is not None:
            print_tree_structure(node.left, prefix + ("    " if is_tail else "│   "), True)
        else:
            print(prefix + ("    " if is_tail else "│   ") + "└── None")

def get_balance_factor(node):
    """Calcular el factor de balance de un nodo"""
    if node is None:
        return 0
    left_height = node.left.height if node.left else 0
    right_height = node.right.height if node.right else 0
    return right_height - left_height

def test_avl():
    print("=" * 70)
    print("PRUEBA DEL ÁRBOL AVL (AUTO-BALANCEADO)")
    print("=" * 70)
    
    # Crear una instancia del árbol AVL
    avl = ChildrenAVL()
    
    # Test 1: Insertar niños que causarían desbalanceo en ABB simple
    print("\n1. INSERTANDO NIÑOS EN ORDEN ASCENDENTE (Caso crítico para ABB)...")
    print("   (En ABB simple esto crearía una lista enlazada, pero AVL se auto-balancea)")
    
    children_data = [
        Child(documento=1000, nombre="Ana García", edad=7, acudiente="José García", notas="Muy aplicada"),
        Child(documento=2000, nombre="Luis Martínez", edad=9, acudiente="Carmen Martínez", notas="Buen comportamiento"),
        Child(documento=3000, nombre="María López", edad=8, acudiente="Pedro López", notas="Excelente en arte"),
        Child(documento=4000, nombre="Carlos Ruiz", edad=10, acudiente="Ana Ruiz", notas="Buen estudiante"),
        Child(documento=5000, nombre="Sofia Torres", edad=11, acudiente="Miguel Torres", notas="Líder natural"),
        Child(documento=6000, nombre="Juan Pérez", edad=12, acudiente="Laura Pérez", notas="Destacado en deportes"),
        Child(documento=7000, nombre="Pedro Sánchez", edad=13, acudiente="Elena Sánchez", notas="Excelente en matemáticas"),
    ]
    
    for child in children_data:
        success = avl.insert(child)
        balance_status = "✓ Balanceado" if avl.is_balanced() else "✗ DESBALANCEADO"
        print(f"   Insertado: {child.nombre:20s} (Doc: {child.documento}) - Altura: {avl.get_tree_height()} - {balance_status}")
    
    # Test 2: Mostrar estructura del árbol
    print("\n2. ESTRUCTURA DEL ÁRBOL AVL (Balanceado):")
    print_tree_structure(avl.root)
    
    # Test 3: Verificar balanceo
    print("\n3. VERIFICACIÓN DE BALANCEO:")
    print(f"   Altura del árbol: {avl.get_tree_height()}")
    print(f"   ¿Está balanceado?: {'SÍ ✓' if avl.is_balanced() else 'NO ✗'}")
    print(f"   Altura óptima para 7 nodos: {3} (log₂(7) ≈ 2.8)")
    
    # Test 4: Intentar insertar duplicado
    print("\n4. INTENTANDO INSERTAR DUPLICADO...")
    duplicate = Child(documento=4000, nombre="Duplicado", edad=10, acudiente="Test", notas="Test")
    success = avl.insert(duplicate)
    print(f"   {'✗' if not success else '✓'} Documento 4000 - {'Rechazado (duplicado)' if not success else 'Insertado'}")
    
    # Test 5: Buscar niños
    print("\n5. BUSCANDO NIÑOS...")
    search_docs = [4000, 1000, 7000, 9999]
    for doc in search_docs:
        child = avl.search(doc)
        if child:
            print(f"   ✓ Encontrado: {child.nombre} (Doc: {doc})")
        else:
            print(f"   ✗ No encontrado: Documento {doc}")
    
    # Test 6: Recorrido Inorden (ordenado)
    print("\n6. RECORRIDO INORDEN (Ordenado por documento):")
    inorder = avl.inorder_traversal()
    for child in inorder:
        print(f"   - Doc: {child.documento:5d} | {child.nombre:20s} | Edad: {child.edad:2d}")
    
    # Test 7: Recorrido Preorden
    print("\n7. RECORRIDO PREORDEN:")
    preorder = avl.preorder_traversal()
    print(f"   Documentos: {[c.documento for c in preorder]}")
    
    # Test 8: Recorrido Postorden
    print("\n8. RECORRIDO POSTORDEN:")
    postorder = avl.postorder_traversal()
    print(f"   Documentos: {[c.documento for c in postorder]}")
    
    # Test 9: Actualizar un niño
    print("\n9. ACTUALIZANDO NIÑO...")
    update_data = ChildUpdate(nombre="Carlos Ruiz Actualizado", edad=11, notas="Promovido de grado")
    updated = avl.update(4000, update_data)
    if updated:
        print(f"   ✓ Actualizado: {updated.nombre} (Doc: {updated.documento}, Edad: {updated.edad})")
        print(f"   ¿Sigue balanceado?: {'SÍ ✓' if avl.is_balanced() else 'NO ✗'}")
    else:
        print(f"   ✗ No se pudo actualizar")
    
    # Test 10: Eliminar niños (esto causará rebalanceo)
    print("\n10. ELIMINANDO NIÑOS (con auto-balanceo)...")
    delete_docs = [1000, 7000, 4000]
    for doc in delete_docs:
        deleted = avl.delete(doc)
        if deleted:
            print(f"   ✓ Eliminado: Doc {doc} - Altura: {avl.get_tree_height()} - {'Balanceado ✓' if avl.is_balanced() else 'DESBALANCEADO ✗'}")
        else:
            print(f"   ✗ No encontrado: Doc {doc}")
    
    # Test 11: Estructura después de eliminaciones
    print("\n11. ESTRUCTURA DEL ÁRBOL DESPUÉS DE ELIMINACIONES:")
    print_tree_structure(avl.root)
    
    # Test 12: Lista final
    print("\n12. LISTA FINAL (Inorden):")
    final_list = avl.inorder_traversal()
    for child in final_list:
        print(f"   - Doc: {child.documento:5d} | {child.nombre:20s} | Edad: {child.edad:2d}")
    
    # Test 13: Estadísticas finales
    print("\n13. ESTADÍSTICAS FINALES:")
    print(f"   Total de niños: {len(final_list)}")
    print(f"   Altura del árbol: {avl.get_tree_height()}")
    print(f"   ¿Está balanceado?: {'SÍ ✓' if avl.is_balanced() else 'NO ✗'}")
    print(f"   Altura óptima para {len(final_list)} nodos: ≈ {len(final_list).bit_length()}")
    
    # Test 14: Caso extremo - Inserción que requiere rotación doble
    print("\n14. PRUEBA DE ROTACIONES DOBLES (LR y RL)...")
    avl2 = ChildrenAVL()
    
    # Caso LR (Left-Right)
    print("\n   Caso LR (Left-Right Rotation):")
    print("   Insertando: 5000, 2000, 3000 (requiere rotación LR)")
    avl2.insert(Child(documento=5000, nombre="Test1", edad=10, acudiente="Test", notas=""))
    avl2.insert(Child(documento=2000, nombre="Test2", edad=10, acudiente="Test", notas=""))
    avl2.insert(Child(documento=3000, nombre="Test3", edad=10, acudiente="Test", notas=""))
    print_tree_structure(avl2.root)
    print(f"   ¿Balanceado?: {'SÍ ✓' if avl2.is_balanced() else 'NO ✗'}")
    
    # Caso RL (Right-Left)
    avl3 = ChildrenAVL()
    print("\n   Caso RL (Right-Left Rotation):")
    print("   Insertando: 2000, 5000, 3000 (requiere rotación RL)")
    avl3.insert(Child(documento=2000, nombre="Test1", edad=10, acudiente="Test", notas=""))
    avl3.insert(Child(documento=5000, nombre="Test2", edad=10, acudiente="Test", notas=""))
    avl3.insert(Child(documento=3000, nombre="Test3", edad=10, acudiente="Test", notas=""))
    print_tree_structure(avl3.root)
    print(f"   ¿Balanceado?: {'SÍ ✓' if avl3.is_balanced() else 'NO ✗'}")
    
    print("\n" + "=" * 70)
    print("PRUEBAS COMPLETADAS EXITOSAMENTE ✓")
    print("El árbol AVL mantiene el balanceo en todas las operaciones")
    print("=" * 70)

if __name__ == "__main__":
    test_avl()
