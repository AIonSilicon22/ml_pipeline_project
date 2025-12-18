from setuptools import find_packages, setup
from typing import List

HYPHON_E_DOT = "-e ."

def get_requriements(filepath:str) -> List[str]:
    requriements=[]

    with open(filepath) as file_obj :
        requriments = file_obj.readlines()
        requriments = [i.replace("\n","")for i in requriements ]

        if HYPHON_E_DOT in requriements:
            requriments.remove(HYPHON_E_DOT)

setup(name = "ML_Pipeline_project",
      version = "0.0.1",
      author = 'Prajay Ghogare',
      author_email="prajayoffical2204@gmail.com",
      packages=find_packages(),
      install_requires = get_requriements("requirements.txt")
      )            