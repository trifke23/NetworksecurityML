from typing import List

from setuptools import find_packages, setup


def get_requirements() -> List[str]:
    requirements_list: List[str] = []

    try:
        with open("requirements.txt", "r") as file:
            for line in file:
                requirement = line.strip()
                if requirement and requirement != "-e.":
                    requirements_list.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found. No dependencies will be installed.")

    return requirements_list


setup(
    name="networksecurity",
    version="0.0.1",
    author="Aleksa Trifunovic",
    author_email="trifunovic.a23@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)
