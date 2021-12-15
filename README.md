# seleniumbase_python
 
 Ui tesing using seleniumbase and python

# Packages needed to run the project

pip install seleniumbase

# Prerequsite: Python version3+, Pycharm

# Execution: Download project to local and open terminal or cmd and execute following commands one by one for respective browser

# parallel execution

`pytest -v --chrome -n=4 --dashboard --html=dashboard.html`
 
`pytest -v --chrome --headless -n=4 --dashboard --html=dashboard.html`
 
`pytest -v --firefox -n=4 --dashboard --html=dashboard.html`
 
`pytest -v --firefox --headless -n=4 --dashboard --html=dashboard.html`

`pytest -v --edge -n=4 --dashboard --html=dashboard.html`
 
`pytest -v --edge -n=4 --headless --dashboard --html=dashboard.html`

# sequential execution
 
 `pytest -v --chrome --dashboard --html=dashboard.html`
 
`pytest -v --chrome --headless --dashboard --html=dashboard.html`
 
`pytest -v --firefox --dashboard --html=dashboard.html`
 
`pytest -v --firefox --headless --dashboard --html=dashboard.html`

`pytest -v --edge --dashboard --html=dashboard.html`
 
`pytest -v --edge --headless --dashboard --html=dashboard.html`

 # Html report file path
 
 `seleniumbase_python\dashboard.html`
 
 # Test execution gif

![iKFuQx3zwF](https://user-images.githubusercontent.com/52770689/146147625-0f0d4382-e681-4a10-a348-266fd466a485.gif)
 
 # Html report screenshots
 
 ![mDg6G457PL](https://user-images.githubusercontent.com/52770689/146142792-441155df-ce1a-4f41-a25e-d8e2cb51d081.png)
 


