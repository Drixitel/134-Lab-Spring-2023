# 134 Labs

## 1: Millikan Oil Drop 
- Installations: 
> Math, Numpy, Pandas, Gspread<br>
> - pulling data from csv files and converting to arrays 
* Full work through of data collection and math involved
* Data files 
* Error propagation 
* Final analysis (iffy on the method)
## 2: Nonlinear Dynamics and Chaos
## 3: 
## 4: Additional Tutorial files  
- Pandas 
- Gspread
- Jupyter Notbooks 

# Issue: after `poetry install` from github
- After install, terminal shows [auto run cell for enviorment] 
- Fix: 
> in VSCode settings<br>
File: `.vscode> settings.json`<br>
add:  
    "python.terminal.activateEnvironment": false,

# Save txt file: 
> `np.savetxt("sample.txt", new_array, delimiter =", ")`
