# FlaskDynamoStarterKit

This tutorial will help you get started with a simply python web application that will allow you to write and query from amazon dynamodb

####In order to get started, you will first need two things:

1. An amazon web services account.
    1. If you don't already have an aws account, please create one [here](http://aws.amazon.com).

2. Once you've created your aws account you will need your `secret access key` and a `secret access id`
    1. these can be found in the following areas your aws management console.
        1. go to `Identity & Access Management`
        2. click on the `Delete your root access key` (we won't actually be deleting it)
        3. you will be taken to the `Your Security Credentials` where you will click on `Access Keys (Access Key ID and Secret Access Key)`
        4. Generate a new key and Store the generated `ID` and `Key` in a safe place.

####Once you have your keys you will need to store them in the project:

1. `cd` into the root directory of the project, and you will find a file called `secrets.py`

2. paste your `access_id`, and `secret key in their appropriate locations`

```
*secrets.py*

access_id = <your access ID>
secret_key = <your access key>

```

####Time to configure the environment.
1. Now that your credentials are added into the project, it's time to setup the python environment.

  1. If you're using windows and don't have python installed, go [install(https://www.python.org/downloads/release/python-279/)] Python. If you're on OSX or on windows with Python already installed, move to the next step.

  2. Now that Python is installed, you have access to `pip`, which is the Python package management system we'll be using to install the project dependencies. If you have errors using `pip`, you may have to call `sudo pip` in order to obtain the necessary permissions.

  3. the foundation of all of our dependencies is the Python [virtualenv](http://docs.python-guide.org/en/latest/dev/virtualenvs/) package, which creates a virtual python environment for us to work in. Run the following commands in the project's root directory.

        1. Install virtualenv - `pip install virtualenv`
        2. Create your virtual environment. `virtualenv venv` (venv will be the name of your environment)
        3. Specify the version of Python we'll be using `virtualenv -p /usr/bin/python2.7 venv`
        4. Activate the newly created VM `source venv/bin/activate`. If at anytime you wish to deactivate the environment, typing `deactivate` will do the trick.

  4. Now we will install all of the other packages associated with this project. We can do this all at once using `pip` and the `requirements.txt` file in your root directory. Enter the following command:
  `sudo pip install -r requirements.txt`.


####Your Environment should be good to go, Now let's start the app.
Navigate to your root directory and run `python main.py`.

your app should now be upp and running. If you open you're browser and go to `http:localhost:5000`, you should see your app's Hello World.






pip install -r requirements.txt
