from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """Reads requirements.txt and returns a list of dependencies."""
    requirements = []
    with open(file_path, 'r') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]  # Stripping spaces and newlines

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements
setup(
    name="mlproject1",
    version="0.0.1",
    author="Niranjan Kumbhar",
    author_email="niranjankumbhar61@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    )
