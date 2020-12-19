Track rating history on competitive programming websites


## Setup

- Confirm pip is installed - `python -m pip --version`
  If not, setup python and pip first.

- Install selenium -`pip install selenium`

- Get the latest stable release of [ChromeDriver](https://chromedriver.chromium.org/) for your operating system

- Configure `constants.py` with your profile URLs

To run, `python update.py`



<sup><sub> Note : This is just a small tool I created for keeping a track of ratings on different websites on a daily basis. The only website that had an API for getting the ratings was codeforces, and this was incremental based on contests taken and not daily basis. Hence, I found the need to keep track of this myself. This repository is not actively maintained. Feel free to use this yourself if you have the need to. </sub></sup>
