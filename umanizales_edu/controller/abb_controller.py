from fastapi import APIRouter, HTTPException, Query, status
from typing import List, Literal, Optional
from ..model.schemas import Child, ChildUpdate, ChildResponse, MessageResponse, ErrorResponse
from ..service.bst_service import children_bst

router = APIRouter(
    prefix="/children/bst",
    tags=["Children Management (BST Tree)"],
    responses={
        404: {"model": ErrorResponse, "description": "Child not found"},
        400: {"model": ErrorResponse, "description": "Validation error"},
        500: {"model": ErrorResponse, "description": "Internal server error"}
    }
)


# =========================================================
# Create Child
# =========================================================
@router.post(
    "/",
    response_model=ChildResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Insert a new child (BST)",
    description="Inserts a new child into the Binary Search Tree (BST). ID must be unique.",
    responses={
        201: {
            "description": "Child created successfully",
            "content": {
                "application/json": {
                    "example": {
                        "id": 1001,
                        "name": "John Doe",
                        "age": 10,
                        "gender": "M"
                    }
                }
            }
        },
        400: {
            "description": "ID already exists",
            "content": {
                "application/json": {
                    "example": {"detail": "Child with ID 1001 already exists"}
                }
            }
        }
    }
)
def create_child(child: Child):
    """
    Inserts a new child into the BST.
    
    Args:
        child: The child data to insert (id, name, age, gender)
        
    Returns:
        Child: The created child data
        
    Raises:
        HTTPException: If child with same ID exists or server error occurs
    """
    try:
        success = children_bst.insert(child)
        if not success:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Child with ID {child.id} already exists"
            )
        return child
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error inserting child: {str(e)}"
        )


# =========================================================
# Get Child by ID
# =========================================================
@router.get(
    "/{id}",
    response_model=ChildResponse,
    summary="Get a child by ID (BST)",
    description="Finds and returns a specific child by their ID.",
    responses={
        200: {
            "description": "Child found",
            "content": {
                "application/json": {
                    "example": {
                        "id": 1001,
                        "name": "John Doe",
                        "age": 10,
                        "gender": "M"
                    }
                }
            }
        },
        404: {
            "description": "Child not found",
            "content": {
                "application/json": {
                    "example": {"detail": "Child with ID 1001 not found"}
                }
            }
        }
    }
)
def get_child(id: int):
    """
    Retrieves a child by their ID.
    
    Args:
        id: The unique identifier of the child
        
    Returns:
        Child: The child data if found
        
    Raises:
        HTTPException: If child not found or server error occurs
    """
    try:
        child = children_bst.search(id)
        if child is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Child with ID {id} not found"
            )
        return child
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error retrieving child: {str(e)}"
        )


# =========================================================
# List All Children
# =========================================================
@router.get(
    "/",
    response_model=List[ChildResponse],
    summary="List all children (BST)",
    description="Returns a list of all children using the specified traversal order (inorder, preorder, or postorder) of the BST.",
    responses={
        200: {
            "description": "List of children",
            "content": {
                "application/json": {
                    "example": [
                        {"id": 1001, "name": "John Doe", "age": 10, "gender": "M"},
                        {"id": 1002, "name": "Jane Smith", "age": 12, "gender": "F"}
                    ]
                }
            }
        }
    }
)
def list_children(
    order: Literal["in", "pre", "post"] = Query(
        "in",
        description="BST traversal order: 'in' (inorder), 'pre' (preorder), 'post' (postorder)"
    )
):
    """
    Lists all children using the specified tree traversal order.
    
    Args:
        order: The tree traversal order ('in', 'pre', or 'post')
        
    Returns:
        List[Child]: List of children in the specified order
        
    Raises:
        HTTPException: If invalid order is provided or server error occurs
    """
    try:
        if order == "in":
            return children_bst.inorder_traversal()
        elif order == "pre":
            return children_bst.preorder_traversal()
        elif order == "post":
            return children_bst.postorder_traversal()
        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid traversal order. Use 'in', 'pre', or 'post'."
            )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error listing children: {str(e)}"
        )


# =========================================================
# Update Child
# =========================================================
@router.put(
    "/{id}",
    response_model=ChildResponse,
    summary="Update a child (BST)",
    description="Updates the data of an existing child. The 'id' field cannot be modified.",
    responses={
        200: {
            "description": "Child updated successfully",
            "content": {
                "application/json": {
                    "example": {
                        "id": 1001,
                        "name": "John Doe Updated",
                        "age": 11,
                        "gender": "M"
                    }
                }
            }
        },
        404: {
            "description": "Child not found",
            "content": {
                "application/json": {
                    "example": {"detail": "Child with ID 1001 not found"}
                }
            }
        }
    }
)
def update_child(id: int, child_update: ChildUpdate):
    """
    Updates an existing child's information.
    
    Args:
        id: The ID of the child to update
        child_update: The fields to update (name, age, or gender)
        
    Returns:
        Child: The updated child data
        
    Raises:
        HTTPException: If child not found or server error occurs
    """
    try:
        # Ensure at least one field is being updated
        update_data = child_update.dict(exclude_unset=True)
        if not update_data:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="No update data provided"
            )
            
        updated_child = children_bst.update(id, child_update)
        if updated_child is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Child with ID {id} not found"
            )
        return updated_child
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error updating child: {str(e)}"
        )


# =========================================================
# Delete Child
# =========================================================
@router.delete(
    "/{id}",
    response_model=MessageResponse,
    summary="Delete a child (BST)",
    description="Deletes a child from the system by their ID.",
    responses={
        200: {
            "description": "Child deleted successfully",
            "content": {
                "application/json": {
                    "example": {"message": "Child with ID 1001 deleted successfully"}
                }
            }
        },
        404: {
            "description": "Child not found",
            "content": {
                "application/json": {
                    "example": {"detail": "Child with ID 1001 not found"}
                }
            }
        }
    }
)
def delete_child(id: int):
    """
    Deletes a child from the BST.
    
    Args:
        id: The ID of the child to delete
        
    Returns:
        dict: A message confirming the deletion
        
    Raises:
        HTTPException: If child not found or server error occurs
    """
    try:
        deleted = children_bst.delete(id)
        if not deleted:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Child with ID {id} not found"
            )
        return {"message": f"Child with ID {id} deleted successfully"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error deleting child: {str(e)}"
        )