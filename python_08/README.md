## INTRODUCTION

 This project introduces the fundamentals of professional Python development by teaching how 
 to manage external libraries and project environments safely. Instead of installing packages 
 globally, we learn how to isolate dependencies using virtual environments (venv), manage 
 installations with pip and requirements.txt, and use Poetry with pyproject.toml for modern 
 dependency management. Through a small data analysis program built with tools like pandas, 
 NumPy, and Matplotlib, the project demonstrates how to install, isolate, and reproduce 
 dependencies correctly while avoiding version conflicts. Overall, it helps us understand how 
 real-world Python applications structure their environments to remain stable, portable, and 
 maintainable.


## Exercises Overview

### Exercise 0
  This exercise introduces the concept of Python virtual environments `venv` by creating a 
small program that checks whether the script is running inside an isolated environment or the 
system Python. The goal is to help us understand why virtual environments are important for 
dependency management and project isolation.


### Exercise 1
This exercise introduces real-world dependency management by building a small data analysis 
tool that relies on external libraries instead of only the Python standard library. Using 
`NumPy` for numerical computations, `pandas` for data manipulation, and `Matplotlib` for 
visualization, the program simulates and analyzes “Matrix data” to generate a simple graph.


Beyond analysis, the main goal is to learn how to manage dependencies safely. The script 
checks whether required packages are installed, handles missing modules gracefully, and 
compares package versions. It also demonstrates two installation approaches: the traditional 
pip workflow using `requirements.txt` and the modern Poetry workflow using `pyproject.toml.` 
This helps us understand how to isolate environments, avoid version conflicts, and create 
reproducible Python projects.

### Exercise 2

This exercise teaches how to securely manage sensitive configuration data without 
hardcoding it inside the source code. Instead of storing secrets like API keys, database 
URLs, or passwords directly in Python files, the program uses environment variables 
loaded from a `.env` file.Using python-dotenv, the program automatically loads variables 
from the .env file and accesses them through `os.getenv()`. This approach keeps secrets out 
of version control (by adding .env to `.gitignore`).
