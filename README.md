[![Build Status](https://snap-ci.com/rosatolen/velocity/branch/master/build_image)](https://snap-ci.com/rosatolen/velocity/branch/master)

The goal of this app is to make it even more enjoyable to work on being the person I want to be through a reward and tracking system that is easy to maintain.

##Dev Local Setup:
1. Install Mongodb
2. Start Mongodb at the default configuration (localhost:27017)
3. In your application home directory, run `pip install -r requirements.txt` (I recommend creating a virutalenv for this.)
4. To run the app, call `python app.py`
5. To run the unit tests, run `nosetests`
6. To run the feature tests like the build, run `behave --tags=-wip`
