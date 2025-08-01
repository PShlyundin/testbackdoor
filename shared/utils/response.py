from typing import Any, Dict, Optional
from fastapi import HTTPException, status

def create_success_response(data: Any, message: str = "Success") -> Dict[str, Any]:
    """Create standardized success response"""
    return {
        "success": True,
        "message": message,
        "data": data
    }

def create_error_response(message: str, status_code: int = 400) -> HTTPException:
    """Create standardized error response"""
    return HTTPException(
        status_code=status_code,
        detail={
            "success": False,
            "message": message
        }
    )

def not_found_error(resource: str = "Resource") -> HTTPException:
    """Create 404 error response"""
    return create_error_response(f"{resource} not found", status.HTTP_404_NOT_FOUND)

def validation_error(message: str) -> HTTPException:
    """Create 422 validation error response"""
    return create_error_response(message, status.HTTP_422_UNPROCESSABLE_ENTITY) 