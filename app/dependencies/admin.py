from fastapi import Depends
from app.models.User import User
from app.dependencies.auth import current_user
from app.exceptions.custom_exceptions import NotAdminException


def admin_required(user: User = Depends(current_user)):
    print(user.UserName, user.UserRole)
    if user.UserRole != "Admin":
        raise NotAdminException

    return user