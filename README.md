# CumulativeRainFallCallOptions
Cumulative Rain Fall Call Options

To run the front end first install npm packages

```
cd ui
npm i
```

After that you should be able to run the front end with the command

```
npm run dev
```

With the front end running you should be able to run the back end. in a new terminal window change to the the back end dir 

```
cd api
```

First load the data into an sql db from a python terminal

```
python3
```

```
from models import seed_tables
seed_tables()
exit()
```

Once the data is loaded you should have a file in the api dir called rain.db you should be able to run the back end using the following command

```
python3 main.py
```