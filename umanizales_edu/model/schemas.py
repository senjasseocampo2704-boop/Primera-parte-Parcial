from pydantic import BaseModel, Field
from typing import Optional


class Child(BaseModel):
    """Modelo de datos para un niño (Kid)"""
    id: int = Field(..., description="Identificador único del niño", gt=0)
    age: int = Field(..., description="Edad del niño (criterio de ordenación)", ge=0, le=18)
    name: str = Field(..., description="Nombre completo del niño", min_length=1, max_length=100)
    gender: str = Field(..., description="Género del niño", pattern="^(M|F|Otro)$")

    class Config:
        json_schema_extra = {
            "example": {
                "id": 1001,
                "age": 10,
                "name": "Juan Pérez",
                "gender": "M"
            }
        }


class ChildUpdate(BaseModel):
    """Modelo para actualizar un niño (todos los campos opcionales excepto id)"""
    age: Optional[int] = Field(None, description="Edad del niño", ge=0, le=18)
    name: Optional[str] = Field(None, description="Nombre completo del niño", min_length=1, max_length=100)
    gender: Optional[str] = Field(None, description="Género del niño", pattern="^(M|F|Otro)$")

    class Config:
        json_schema_extra = {
            "example": {
                "age": 11,
                "name": "Juan Pérez Actualizado",
                "gender": "M"
            }
        }


class ChildResponse(Child):
    """Modelo de respuesta para un niño"""
    pass


class MessageResponse(BaseModel):
    """Modelo de respuesta para mensajes"""
    message: str


class ErrorResponse(BaseModel):
    """Modelo de respuesta para errores"""
    detail: str