
# Welcome to the Chore Schedule App

## Setup:


Install the required packages using the following code:<br>
``` pip install -r requirements.txt ```

Create an evironment using the following code:<br>
``` conda create --name app-env ```
After the enviornment is created, make sure to activate the enviornment prior to each run using the following code:<br>
``` conda activate app-env```

Create .env file that includes the sendergrid API key and the sender email address:<br>
``` SENDGRID_API_KEY = " " ```
``` SENDER_EMAIL_ADDRESS = " " ```

## Running the App:

To Run the App Locally, envoke the following commands: <br>
``` python -m app.email ```

To Run the App on flask, envoke the following commands: <br>
``` FLASK_APP=web_app flask run ```

## Testing

Running test:

```pytest```

# Finding the App on the Remote Server

To find the web app on the remote server, please go to the following link: https://mighty-anchorage-11817.herokuapp.com

## Creating a Web App

Create a Heroku enviornment using the following commands: <br> ```heroku create```

Add all enviornment variables to Heroku using the following command: <br> ```heroku config```

Ensure that all local edits are pushed to the Heroku server using the command: <br> ```git push heroku main```



