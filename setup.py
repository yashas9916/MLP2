from setuptools import find_packages,setup
from typing import List
#here we have metadata of project.

HYPHER_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    """
    This function will return a list of requirements
    """
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]

        if HYPHER_E_DOT in requirements:
            requirements.remove(HYPHER_E_DOT)
    return requirements


setup(
    name='mlproject',
    version='0.0.1',
    author='yashas',
    author_email='yashas.suresh1@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)