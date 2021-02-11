# robin-hood-cli
A command-line interface proof of concept written in Python for the Robinhood web app.

This application requires the following libraries:
* [click](https://github.com/pallets/click)
* [robin_stocks](https://github.com/jmfernandes/robin_stocks)
* [bcrypt](https://github.com/pyca/bcrypt)
* [pandas](https://github.com/pandas-dev/pandas)
* [numpy](https://github.com/numpy/numpy)

```bash
C:\github\robin-hood-cli python robincli.py --help
Usage: robincli.py [OPTIONS] COMMAND [ARGS]...

  A Python command-line interface (CLI) utilizing a  robinhood API created
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
