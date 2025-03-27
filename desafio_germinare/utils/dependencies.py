from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from desafio_germinare.database.database import get_session

Session = Annotated[Session, Depends(get_session)]
