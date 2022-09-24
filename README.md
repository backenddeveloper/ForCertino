# For Certino

Answers to the Certino technical test.

### Language used

This repo targets Python 3.10.5

### How to run

The easiest way to run and test is by using Docker

```bash
docker run -it -v `pwd`:/w -w /w python:3.10 bash
```

Then you can install the dependencies and run the unittests
```bash
python3 -B -m pip install -r requirements.txt
```
```bash
python3 -B -m pytest
```
You can then run the code to see it process the input files
```bash
python3 -B -m answers
```
