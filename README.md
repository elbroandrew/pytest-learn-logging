## Pytest API test tasks
To install `requirements` type: 
```
pip install -r requirements.txt
```
To run tests type:
```
pytest -s -v
```
To run more specific tests ('smoke', 'regression' etc) use `markers`:
```
python3 -m pytest -m <marker_name>
```
To remove .idea folder if it is already in gitignore:
```
git rm -r --cached .idea
```
