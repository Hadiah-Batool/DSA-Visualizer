from abc import *
from typing import Generic, List, TypeVar
DataType = TypeVar('DataType')
class DataStructure(ABC):
    """
    Abstract base class for all data structures.
    """
    @abstractmethod
    def AskUser(self, screen) -> None:
        """
        Before doing anythingask user for datatype or any size(arrays)
        """
        pass
    @abstractmethod
    def insert(self, data: DataType) -> None:
        """
        Insert data into the data structure.
        """
        pass
    @abstractmethod
    def delete(self, data: DataType) -> None:
        """
        Delete data from the data structure.
        """
        pass

    @abstractmethod
    def Draw(self, screen) -> None:
        """
        Display the contents of the data structure.

        """
        pass
