"""
Script de prueba para verificar la API de gestión de niños
"""
from umanizales_edu.service.item_service import ChildrenBST
from umanizales_edu.model.schemas import Child, ChildUpdate

def test_bst():
    print("=" * 60)
    print("PRUEBA DEL ÁRBOL BINARIO DE BÚSQUEDA (ABB)")
    print("=" * 60)
    
    # Crear una instancia del árbol
    bst = ChildrenBST()
    
    # Test 1: Insertar niños
    print("\n1. INSERTANDO NIÑOS...")
    children_data = [
        Child(documento=5000, nombre="Carlos Ruiz", edad=10, acudiente="Ana Ruiz", notas="Buen estudiante"),
        Child(documento=3000, nombre="María López", edad=8, acudiente="Pedro López", notas="Excelente en arte"),
        Child(documento=8000, nombre="Juan Pérez", edad=12, acudiente="Laura Pérez", notas="Destacado en deportes"),
        Child(documento=2000, nombre="Ana García", edad=7, acudiente="José García", notas="Muy aplicada"),
        Child(documento=4000, nombre="Luis Martínez", edad=9, acudiente="Carmen Martínez", notas="Buen comportamiento"),
        Child(documento=6000, nombre="Sofia Torres", edad=11, acudiente="Miguel Torres", notas="Líder natural"),
        Child(documento=9000, nombre="Pedro Sánchez", edad=13, acudiente="Elena Sánchez", notas="Excelente en matemáticas"),
    ]
    
    for child in children_data:
        success = bst.insert(child)
        print(f"   ✓ Insertado: {child.nombre} (Doc: {child.documento}) - {'Éxito' if success else 'Duplicado'}")
    
    # Test 2: Intentar insertar duplicado
    print("\n2. INTENTANDO INSERTAR DUPLICADO...")
    duplicate = Child(documento=5000, nombre="Duplicado", edad=10, acudiente="Test", notas="Test")
    success = bst.insert(duplicate)
    print(f"   {'✗' if not success else '✓'} Documento 5000 - {'Rechazado (duplicado)' if not success else 'Insertado'}")
    
    # Test 3: Buscar niños
    print("\n3. BUSCANDO NIÑOS...")
    search_docs = [5000, 2000, 9999]
    for doc in search_docs:
        child = bst.search(doc)
        if child:
            print(f"   ✓ Encontrado: {child.nombre} (Doc: {doc})")
        else:
            print(f"   ✗ No encontrado: Documento {doc}")
    
    # Test 4: Recorrido Inorden (ordenado)
    print("\n4. RECORRIDO INORDEN (Ordenado por documento):")
    inorder = bst.inorder_traversal()
    for child in inorder:
        print(f"   - Doc: {child.documento:5d} | {child.nombre:20s} | Edad: {child.edad:2d}")
    
    # Test 5: Recorrido Preorden
    print("\n5. RECORRIDO PREORDEN:")
    preorder = bst.preorder_traversal()
    print(f"   Documentos: {[c.documento for c in preorder]}")
    
    # Test 6: Recorrido Postorden
    print("\n6. RECORRIDO POSTORDEN:")
    postorder = bst.postorder_traversal()
    print(f"   Documentos: {[c.documento for c in postorder]}")
    
    # Test 7: Actualizar un niño
    print("\n7. ACTUALIZANDO NIÑO...")
    update_data = ChildUpdate(nombre="Carlos Ruiz Actualizado", edad=11, notas="Promovido de grado")
    updated = bst.update(5000, update_data)
    if updated:
        print(f"   ✓ Actualizado: {updated.nombre} (Doc: {updated.documento}, Edad: {updated.edad})")
    else:
        print(f"   ✗ No se pudo actualizar")
    
    # Test 8: Eliminar niños
    print("\n8. ELIMINANDO NIÑOS...")
    delete_docs = [2000, 8000, 9999]
    for doc in delete_docs:
        deleted = bst.delete(doc)
        print(f"   {'✓' if deleted else '✗'} Documento {doc} - {'Eliminado' if deleted else 'No encontrado'}")
    
    # Test 9: Listar después de eliminaciones
    print("\n9. LISTA FINAL (Inorden):")
    final_list = bst.inorder_traversal()
    for child in final_list:
        print(f"   - Doc: {child.documento:5d} | {child.nombre:20s} | Edad: {child.edad:2d}")
    
    print("\n" + "=" * 60)
    print("PRUEBAS COMPLETADAS EXITOSAMENTE ✓")
    print("=" * 60)

if __name__ == "__main__":
    test_bst()
