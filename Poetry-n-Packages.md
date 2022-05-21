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

Issue Adding a Package to Project 
- If adding fails and reverts back to original an older package might be interfering 
- Delete the `.venv` enviorment file 
- `poetry add` the package 
> this will add the new package then add the remaining ones similar to `poetry install`

# Run program from Terminal 
- call: `poetry run python Filename.py` 
- make sure you're in the project folder to run it 
- make sure you're calling functions correctly 

# Cache -ignore 
# Enviorment (`.venv`)
* seen but not necessary to mess with in `.venv`
>> Contains interpreters (python)
- Genertates with command `poetry install`

## Genertate Environment in-project 
>>  If `.venv` generated not in-project, find it (`poetry env info`) delete it and continue with these steps. 
- use command 
> `poetry config virtualenvs.create false --local`
- View config 
> `poetry config --list`
- Check for True: 
>> `virtualenvs.in-project = True`



# Working inside a Poetry Folder (optional)
> Always work within the file that contains your `.toml` file or any sub directory within it

* Poetry creates a subfolder which contains a `init.py` file titled the same as the original project. 
* Outer folder:
> Contains poetry and enviorment related things <br>
Any subfolder will have access to poetry 

* Inner Folder: 
> Containing init, let this contain the python code related to the project. 


# Select Python Interpreter 
- Add path from `.venv > scripts` or `.venv> bin` locate `python.exe` or `python(version).exe` and use this path for your interpreter.  
- interpreters, or Kernels (same thing) must be from your `.venv` file to function properly
> May resolve issues with added packages 

# Poetry update Python (Newer Version)
- Change `.toml` file 
- Save
- run `poetry lock --no-update`
- Delete `.venv` file 
- `poetry install` (this reinstalls the `.venv`)

# Check your python version in Poetry
> Commands: 
- `poetry shell`
- `python --version`
- `exit`