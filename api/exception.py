from fastapi import HTTPException, status

no_such_user = HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail="Username or password incorrect.")

token_expired = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                              detail="Could not validate credentials.",
                              headers={"WWW-Authenticate": "Bearer"})

data_rollback = HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                              detail="Request failed.")

duplicate_data = HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                               detail="Data Duplicated.")

invalid_class_id = HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,
                                 detail="Invalid class id.")

no_such_item_class = HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                   detail="Item class not found.")

no_such_image = HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                              detail="Image not found.")
