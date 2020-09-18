# Test task NtecLab


## Clone github repo 

```console
git clone https://github.com/WEBSTERMASTER777/TestTaskNtechLab.git
```

## Task 1:

### An example of running a script

```console
python3 task1.py '1 2 3 4 5 6'
```
### An example of the result of running a script

```console
Array:  [1, 2, -3, 4, 5, 6]
Max subarray:  [4, 5, 6]
```
***Waring: The input array is set as a string***

## Task 2:

### Local setup

1. Install Python **>=3.6.5 and <3.7**
2. Create virtual environment:

```console
python -m venv .env
```

3. Activate environment
    - on windows: `.env\Scripts\activate`
    - on linux/mac: `source .env/bin/activate`

4. Install dependencies:

```console
pip install -r requirements.txt
```

### Inference

1. Change paths in the ***script_config.yaml***
2. Run `python3 test.py /dirpath` in the root directory

Usage example in the ***How_to_use_model.ipynb***
