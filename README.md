# robin-hood-cli
A command-line interface (CLI) proof of concept written in Python for the Robinhood web app. The current functionality is limited but can easily be expanded upon by adding a command for each of the Robinhood API functions. To use the CLI, the following libraries are required:

* [click](https://github.com/pallets/click)
* [robin_stocks](https://github.com/jmfernandes/robin_stocks)
* [bcrypt](https://github.com/pyca/bcrypt)
* [pandas](https://github.com/pandas-dev/pandas)
* [numpy](https://github.com/numpy/numpy)

## Example Usage
An example usage is as follows:
1. ```--help``` to return a list of available commands.
```

>>> python robincli.py --help
Usage: robincli.py [OPTIONS] COMMAND [ARGS]...

  A Python command-line interface (CLI) utilizing a robinhood API created by
  jmfernandes/robin_stocks.

  Author: Mac Fox

Options:
  -v, --verbose  Increase output verbosity level
  --help         Show this message and exit.

Commands:
  get_history      get_history - Get a historical data range for a specific stock
  get_total_gains  get_total_gains - Return the total gains for the user's account
  get_user         get_user - Return the user's account email
  set_user         set_user - Set the user's account login information
  
  
```
2. ```set_user``` to save his/her Robinhood account information.
```

>>> python robincli.py set_user
Robinhood email:user@mail.com
Robinhood password:password
Repeat for confirmation:password

```
3. ```get_user``` to return which account is being used.
```

>>> python robincli.py get_user
Current user: user@mail.com

```
4. ```get_total_gains``` to return his/her total account gains.
```

>>> python robincli.py get_total_gains
Robinhood password:password
Logged in as user@email.com


|Total Invested| |Total Equity| |Net Worth (Dividends)| |Net Worth (Other Gains)|
        $1000.00       $2000.00          ($0.00, %0.00)       ($1000.00, %100.00)

```
5. ```get_history GME hour day``` to view historical data for GME from the past day on an hourly interval.
```

>>> python robincli.py get_history GME hour day
Robinhood Password:password
Logged in as user@email.com

Getting hourly data for GME from past day

           begins_at open_price close_price high_price low_price  volume
2021-02-10T15:00:00Z  50.499900   49.791900  57.800000 48.160000 2961095
2021-02-10T16:00:00Z  49.850000   52.530000  54.419900 49.573800 1467195
2021-02-10T17:00:00Z  52.645000   55.889600  56.800000 51.120000 1511846
2021-02-10T18:00:00Z  55.700100   56.345000  62.830000 55.560100 4100094
2021-02-10T19:00:00Z  56.310600   53.100000  56.870000 52.420000 1641067
2021-02-10T20:00:00Z  53.269000   51.190400  53.449900 50.480000 1274700

```
