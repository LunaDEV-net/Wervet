
# WebKess

A local python tool to turn raw data from the [Aktion Saubere Hände](https://www.aktion-sauberehaende.de/ueber-uns-ash) into an excel friendly dataset.
## usage

```shell
usage: main.py [-h] path_in path_out
```

| Argument    | Type        | Description                                                           | example value   |
| :---------- | :---------- | :-------------------------------------------------------------------- | :-------------- |
| `path_in`   | `.csv File` | path to the raw data.                                                 |`data/input.csv` |
| `path_out`  | `.csv File` | desired path to the output file. **Warning: will overwrite the file** |`data/output.csv`|
| `--version` |             | print the version                                                     |                 |

## Deployment
### Requirerments
| program/tool  | version I used while testing | usage                        |          |
| ------------- | ------------------------ | ---------------------------- | -------- |
| git           | 2.34.1        | download program from github | optional |
| python        | 3.13.0         | run the programm             | required |
| powershell    | 5.1.19041.4894  | shell on Windows             | required |

### 1. Download Projekt using git
```bash
git clone https://github.com/LunaDEV-net/WebKess.git
cd WebKess
```
### 1.1 Download using Github releases

**Todo**

### 2. Generate virutell envierment
```shell
python -m venv .venv
```
.venv is the recomanded path, if you change it, you would also have to change the run script.

### 3. execute programm
#### **Windows**

```shell
.\.venv\Scripts\Activate.ps1
python src\main.py {arguments} (see usage)
```
or 
```
run.ps1
```
#### **Linux**
```
.venv/bin/python src/main.py {arguments} (see usage)
```
## Known Problems
-> see [Issues](https://github.com/LunaDEV-net/WebKess/issues)
## Support

Contact me personaly or write a [Github Issue](https://github.com/LunaDEV-net/WebKess/issues)




https://docs.python.org/3/library/venv.html
