from fastapi import APIRouter, HTTPException, Query, status
from typing import List, Literal, Optional
from ..model.schemas import Child, ChildUpdate, ChildResponse, MessageResponse, ErrorResponse
from ..service.avl_service import children_avl

router = APIRouter(
    prefix="/children/avl",
    tags=["Children Management (AVL Tree)"],
    responses={
        404: {"model": ErrorResponse, "description": "Child not found"},
        400: {"model": ErrorResponse, "description": "Validation error"},
        500: {"model": ErrorResponse, "description": "Internal server error"}
    }
)

# ---------------------------------------------------------
# Create child
# ---------------------------------------------------------
@router.post(
    "/",
    response_model=ChildResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Insert a new child (AVL)",
    description="Inserts a new child into the self-balancing AVL Tree. ID must be unique. The tree automatically rebalances after insertion.",
    responses={
        201: {
            "description": "Child created successfully and tree balanced",
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
    Inserts a new child into the AVL Tree.
    
    The tree self-balances using rotations (LL, RR, LR, RL) to maintain
    efficiency in all operations.
    
    - **id**: Unique identifier for the child (must be positive)
    - **name**: Full name of the child
    - **age**: Age of the child (between 0 and 18)
    - **gender**: Gender of the child (M/F/O)
    """
    try:
        success = children_avl.insert(child)
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

# ---------------------------------------------------------
# Get child by ID
# ---------------------------------------------------------
@router.get(
    "/{id}",
    response_model=ChildResponse,
    summary="Get a child by ID (AVL)",
    description="Finds and returns a specific child by their ID. Search is optimized by the AVL tree's balancing.",
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
    
    The AVL tree's balancing ensures efficient search operations.
    
    - **id**: The unique identifier of the child to retrieve
    """
    try:
        child = children_avl.search(id)
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

# ---------------------------------------------------------
# Update child
# ---------------------------------------------------------
@router.put(
    "/{id}",
    response_model=ChildResponse,
    summary="Update a child (AVL)",
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
        400: {
            "description": "Invalid update data",
            "content": {
                "application/json": {
                    "example": {"detail": "No update data provided"}
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
    
    The AVL tree rebalances automatically if needed.
    
    - **id**: The ID of the child to update
    - **child_update**: Fields to update (name, age, gender)
    """
    try:
        # Ensure at least one field is being updated
        update_data = child_update.dict(exclude_unset=True)
        if not update_data:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="No update data provided"
            )

        updated_child = children_avl.update(id, child_update)
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

# ---------------------------------------------------------
# List all children
# ---------------------------------------------------------
@router.get(
    "/",
    response_model=List[ChildResponse],
    summary="List all children (AVL)",
    description="Returns a list of all children using the specified traversal order (inorder, preorder, or postorder) of the balanced AVL tree.",
    responses={
        200: {
            "description": "List of children",
            "content": {
                "application/json": {
                    "example": [
                        {
                            "id": 1001,
                            "name": "John Doe",
                            "age": 10,
                            "gender": "M"
                        },
                        {
                            "id": 1002,
                            "name": "Jane Smith",
                            "age": 12,
                            "gender": "F"
                        }
                    ]
                }
            }
        }
    }
)
def list_children(
    order: Literal["in", "pre", "post"] = Query(
        "in",
        description="AVL tree traversal order: 'in' (inorder), 'pre' (preorder), 'post' (postorder)"
    )
):
    """
    Lists all children in the system using the specified AVL tree traversal order.
    
    - **order=in**: Inorder traversal (Left → Root → Right) - Sorted by ID in ascending order
    - **order=pre**: Preorder traversal (Root → Left → Right)
    - **order=post**: Postorder traversal (Left → Right → Root)
    
    The AVL tree ensures it remains balanced, making traversals efficient.
    """
    try:
        if order == "in":
            return children_avl.inorder_traversal()
        elif order == "pre":
            return children_avl.preorder_traversal()
        elif order == "post":
            return children_avl.postorder_traversal()
        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Invalid traversal order. Use 'in', 'pre', or 'post'"
            )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error listing children: {str(e)}"
        )

# ---------------------------------------------------------
# Delete child
# ---------------------------------------------------------
@router.delete(
    "/{id}",
    response_model=MessageResponse,
    summary="Delete a child (AVL)",
    description="Deletes a child from the system by their ID. The tree automatically rebalances.",
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
    Deletes a child from the system.
    
    The AVL tree automatically rebalances using rotations after deletion
    to maintain efficiency.
    
    - **id**: The ID of the child to delete
    """
    try:
        deleted = children_avl.delete(id)
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

# ---------------------------------------------------------
# Get AVL tree statistics
# ---------------------------------------------------------
@router.get(
    "/stats/tree",
    summary="Get AVL tree statistics",
    description="Returns information about the AVL tree (height and node count).",
    responses={
        200: {
            "description": "Tree statistics",
            "content": {
                "application/json": {
                    "example": {
                        "tree_height": 3,
                        "total_nodes": 5,
                        "is_balanced": True,
                        "tree_type": "AVL Tree (Self-balancing)"
                    }
                }
            }
        }
    }
)
def get_tree_stats():
    """
    Gets statistics about the AVL tree.
    
    - **tree_height**: Height of the tree
    - **total_nodes**: Total number of nodes
    - **is_balanced**: Indicates if the tree is balanced (always True for AVL)
    - **tree_type**: Type of tree used
    """
    try:
        return {
            "tree_height": children_avl.height(),
            "total_nodes": children_avl.count_nodes(),
            "is_balanced": children_avl.is_balanced(),
            "tree_type": "AVL Tree (Self-balancing)"
        }
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error getting tree statistics: {str(e)}"
        )
