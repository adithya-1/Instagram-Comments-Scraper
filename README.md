# Instagram Comments Scraper


## Installation

1. Create Virtual Environment (Recommended)<br/> 
    - `pip install virtualenv`
    - `virtualenv .venv`  
    
2. Install dependencies
    - `pip install -r requirements.txt`

3. Install Chrome Web Driver
    - `wget https://chromedriver.storage.googleapis.com/x.xx/chromedriver_linux64.zip` <br>
    See the latest Chrome web driver on https://sites.google.com/a/chromium.org/chromedriver/downloads <br /> <br />
    - Extract and move the binary to bin: `unzip chromedriver_linux64.zip -d .venv/bin/`
    - Make it executable `chmod +x .venv/bin/chromedriver`

4. Run 
    - `python scraper.py post-url total-load-more-click`
   
    Change the URL with your post target. <br/>
    For example : `python scraper.py https://www.instagram.com/p/CBHH2KjI6BW/ 5`

5. Run  
    - `pythonfollower.py` 
 


## License
This project is under the [MIT License](https://github.com/AgiMaulana/instagram-comments-scraper/blob/master/LICENSE.md)
