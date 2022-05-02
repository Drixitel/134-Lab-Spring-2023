# Create new Project Enviorment 
- `poetry new Filename` 

# Add Package to project 
- call: `poetry add packagename`
- Note: `poetry add packagename` = `pip install packagename` in poetry's virtual environment

- packages remain specific to prject and are found in project folders 
> See `pyproject.toml` to find it explicitly with its version required.
* To use project from git
> Have poetry installed<br>
call: `poetry install`<br>
this creates an identical enviorment on new machine



# Run program from Terminal 
- call: `poetry run python Filename.py` 
- make sure you're in the project folder to run it 
- make sure you're calling functions correctly 

# Cache -ignore 
# Enviorment
* seen but not necessary to mess with in `.venv`
- Genertates with `poetry install`



# Working inside a Poetry Folder (optional)

* Poetry creates a subfolder which contains a `init.py` file titled the same as the original project. 
* Outer folder:
> Contains poetry and enviorment related things <br>
Any subfolder will have access to poetry 

* Inner Folder: 
> Containing init, let this contain the python code related to the project. 


# Select Python Interpreter 
- Add path from `.venv > scripts` locate `python.exe` and use this path for your interpreter.  
> May resolve issues with added packages 

# Poetry update Python
- Change .toml file 
- Save
- run `poetry lock --no-update`
- Delete .env
- `poetry install`

# Check your python version in Poetry
- `poetry shell`
- `python --version`
- `exit`