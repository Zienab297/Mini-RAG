from .BaseController import BaseController
from fastapi import UploadFile
from models import ResponseSignal
from .ProjectController import ProjectController
import re
import os

class DataController(BaseController):
    
    def __init__(self):
        super().__init__()
        self.size_scale = 1024 * 1024  # Convert MB to Bytes

    def validate_file(self, file: UploadFile):

        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            return False, ResponseSignal.FILE_TYPE_NOT_SUPPORTED.value
        
        if file.size > self.app_settings.FILE_MAX_SIZE * self.size_scale:
            return False, ResponseSignal.FILE_SIZE_EXCEEDED.value
        
        return True, ResponseSignal.FILE_VALIDATED_SUCCESS.value
        
    def generate_unique_filename(self, orig_filename: str, project_id: str):
        # Generate a unique random string
        random_key = self.generate_random_string()
        # Check if the file is in the project using project_id.
        #To find out if it's unique
        project_path = ProjectController().get_project_path(project_id=project_id)

        cleaned_file_name = self.get_clean_file_name(
            orig_filename=orig_filename
        )
        new_file_path = os.path.join(
            project_path,
            random_key + "_" + cleaned_file_name
        )

        while os.path.exists(new_file_path):
            random_key = self.generate_random_string()
            new_file_path = os.path.join(
                project_path,
                random_key + "_" + cleaned_file_name
            )
        
        return new_file_path

    # For removing any special characters from the file name and only keep the alphanumeric characters and underscores
    def get_clean_file_name(self, orig_filename:str):
        cleaned_file_name = re.sub(r'[^\w.]', '', orig_filename.strip())
        cleaned_file_name = cleaned_file_name.replace(" ", "_")
        return cleaned_file_name


