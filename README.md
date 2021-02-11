# robin-hood-cli
A command-line interface proof of concept written in Python for the Robinhood web app.

This application requires the following libraries:
* [click](https://github.com/pallets/click)
* [robin_stocks](https://github.com/jmfernandes/robin_stocks)
* [bcrypt](https://github.com/pyca/bcrypt)
* [pandas](https://github.com/pandas-dev/pandas)
* [numpy](https://github.com/numpy/numpy)

```

>>> python robincli.py --help
Usage: robincli.py [OPTIONS] COMMAND [ARGS]...

  A Python command-line interface (CLI) utilizing a robinhood API created
  by jmfernandes/robin_stocks.

  Author: Mac Fox

Options:
  -v, --verbose  Increase output verbosity level
  --help         Show this message and exit.

Commands:
  get_gains    get_gains Returns the current gains for the user.
  get_history  get_history Gets INTERVAL data for TICKER from last SPAN
  login        login Saves an email and encrypted password to account.json
  user         user Returns current user's email.
  
```

Set the user account by entering ```login```. The password is encrypted and saved to ```account.json```

```

>>> python robincli.py login
Robinhood Email:user@mail.com
Robinhood Password:password
Repeat for confirmation:password

```

To return which account is being used, enter ```user```. This reads the current email saved to ```acount.json```

```

>>> python robincli.py user
Current User: user@mail.com

```

To view the account gains from account creation date, enter ```get_gains```.

```

>>> python robincli.py get_gains
Robinhood Password:password
Logged in as user@email.com


|Total Invested| |Total Equity| |Net Worth (Dividends)| |Net Worth (Other Gains)|
        $1000.00       $2000.00          ($0.00, %0.00)       ($1000.00, %100.00)

```
