
from pydantic import BaseModel, Field,ConfigDict
from typing import Optional


class File(BaseModel):
    path:str=Field(description="The path of the file to be created or modified")
    purpose:str=Field(description="The purpose of the file, e.g., 'This file contains the main application logic,etc.")
class Plan(BaseModel):
    name:str=Field(description="The name of the project to be built")
    description:str=Field(description="A one-line description of the project")
    techstack:str=Field(description="The tech stack to be used for the project")
    features:list[str]=Field(description="A list of features to be implemented in the project")
    files:list[File]=Field(description="A list of files to be created for the project")
class ImplementationTask(BaseModel):
    filepath: str = Field(description="The path to the file to be modified")
    task_description: str = Field(description="A detailed description of the task to be performed on the file, e.g. 'add user authentication', 'implement data processing logic', etc.")

class TaskPlan(BaseModel):
    implementation_steps: list[ImplementationTask] = Field(description="A list of steps to be taken to implement the task")
    model_config = ConfigDict(extra="allow")
class CoderState(BaseModel):
    task_plan: TaskPlan = Field(description="The plan for the task to be implemented")
    current_step_idx: int = Field(0, description="The index of the current step in the implementation steps")
    current_file_content: Optional[str] = Field(None, description="The content of the file currently being edited or created")
