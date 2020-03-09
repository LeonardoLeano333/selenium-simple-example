# simple example using selenium and Google-Chrome

## configure the webdriver
download a google webdriver from:
https://chromedriver.storage.googleapis.com/index.html

extract this get the path:
```
"C:\\Users\\Dell\\Downloads\\chromedriver.exe"
```
copy and paste at the variable in the file `test_with_selenium.py`:
```
CHROME_PATH = "C:\\Users\\Dell\\Downloads\\chromedriver.exe"
```

## install selenium via pip
```
pip install selenium
```

## run python test_with_selenium.py
```
python test_with_selenium.py
```
This code should return something like this:
```
DevTools listening on ws://127.0.0.1:51510/devtools/browser/8ccef8fa-b9f3-4350-8433-5109777406de
.                                                             
----------------------------------------------------------------------
Ran 1 test in 4.
438s                                                          



OK                                                            
```
