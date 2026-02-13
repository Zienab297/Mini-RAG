from enum import Enum

class ResponseSignal(Enum):

    FILE_VALIDATED_SUCCESS = "file is valid"
    FILE_TYPE_NOT_SUPPORTED = "file type not supported"
    FILE_SIZE_EXCEEDED = "file size exceeds limit"
    FILE_UPLOAD_SUCCESS = "file is valid"
    FILE_UPLOAD_FAILED = "file upload failed"