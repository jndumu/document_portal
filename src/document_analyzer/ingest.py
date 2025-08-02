import os
import fitz
import uuid
from datetime import datetime
from logger.custom_logger import CustomLogger
from exception.custom_exception import CustomException


class DocumentHandler:

    """
    PDF saving and reading operations.
    Automatically logs all actions and supports session-based organization.
    """

    def __init__(self, data,_dir=None, session_id=None):
        try:
            self.log=CustomLogger().get_logger(__name__)
            self.data_dir=data_dir or os.getenv("DATA_STORAGE_PATH")
            os.path.join(os.getcwd(), data, "document_analysis")

