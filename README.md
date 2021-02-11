# robin-hood-cli
A command-line interface (CLI) proof of concept written in Python for the Robinhood web app. The current functionality is limited but can easily be expanded upon. To use the CLI, the following libraries are required:

* [click](https://github.com/pallets/click)
* [robin_stocks](https://github.com/jmfernandes/robin_stocks)
* [bcrypt](https://github.com/pyca/bcrypt)
* [pandas](https://github.com/pandas-dev/pandas)
* [numpy](https://github.com/numpy/numpy)

Starting off, enter ```--help``` to view the currently available commands along with their functional description.

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

  get_history  get_history Gets INTERVAL data for TICKER from last SPAN
  login        login Saves an email and encrypted password to account.json
  total_gains  total_gains Returns the current total gains for the user.
  user         user Returns current user's email.
  
```

A Robinhood user account must be set before any commands can function. Set the user account by entering ```login```. The account information is stored to ```account.json``` with the password being encrypted. To return which account is being used, enter ```user```.

```

>>> python robincli.py login
Robinhood Email:user@mail.com
Robinhood Password:password
Repeat for confirmation:password

```
```

>>> python robincli.py user
Current User: user@mail.com

```

To view the cumulative account gains, enter ```total_gains```.

```

>>> python robincli.py total_gains
Robinhood Password:password
Logged in as user@email.com


|Total Invested| |Total Equity| |Net Worth (Dividends)| |Net Worth (Other Gains)|
        $1000.00       $2000.00          ($0.00, %0.00)       ($1000.00, %100.00)

```

To see the historical data for a specific stock, enter ```get_history {ticker} {interval} {span}```. The flag ```--save``` can be added to save the data as a ```.csv``` file.

```

>>> python robincli.py get_history GME hour day
Robinhood Password:password
Logged in as user@email.com

Getting hour data for GME from last day

           begins_at open_price close_price high_price low_price  volume
2021-02-10T15:00:00Z  50.499900   49.791900  57.800000 48.160000 2961095
2021-02-10T16:00:00Z  49.850000   52.530000  54.419900 49.573800 1467195
2021-02-10T17:00:00Z  52.645000   55.889600  56.800000 51.120000 1511846
2021-02-10T18:00:00Z  55.700100   56.345000  62.830000 55.560100 4100094
2021-02-10T19:00:00Z  56.310600   53.100000  56.870000 52.420000 1641067
2021-02-10T20:00:00Z  53.269000   51.190400  53.449900 50.480000 1274700

```
