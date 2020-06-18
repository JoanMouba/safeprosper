# SETUP file 
# Package and distribution management and Development environment setup 

from setuptools import setup, find_packages
setup(
  name="SafeProsper",
  version=0.1,
  packages=find_packages(),
  install_requires=["docutils>=0.3"],
  test_suite="tests",
  package_data={
    "":["*.txt", "*.rst"],
  },
  author="Joan Mouba", 
  author_email="joan.mouba@gmail.com",
  descrtiption="Package to help you manage your personal finances",
  url="https://sunesiscenter.wixsite.com/accueil"
)
