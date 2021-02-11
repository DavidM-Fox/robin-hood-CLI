import click
from bcrypt import hashpw, gensalt, checkpw
import robin_stocks as r
from getpass import getpass
import pandas as pd
import numpy as np
import json
from os import path

ACCOUNT_JSON = 'account.json'

@click.group(invoke_without_command=True) # Allow users to call w/o command
@click.pass_context
@click.option('--verbose', '-v', is_flag=True, help="Increase output verbosity level")
def main(ctx, verbose):
    """
    A Python command-line interface (CLI) utilizing a robinhood API created by jmfernandes/robin_stocks.

    Author: Mac Fox
    """
    if ctx.invoked_subcommand is None:
        # No command was specified
        click.echo("No command specified. 'robincli --help")

    ctx.obj['VERBOSE'] = verbose 

@main.command('get_user')
def get_user():
    """get_user - Return the user's account email"""
    if(path.exists(ACCOUNT_JSON)):
        with open(ACCOUNT_JSON, 'r') as f:
            email = json.load(f)['email']
        click.echo("Current user: " + email)
    else:
        click.echo("An account is not set. Enter 'set_user'")

@main.command('set_user')
@click.option('--email', prompt="Robinhood email", help="Robinhood Account Email")
@click.option('--password', prompt="Robinhood password", help="Robinhood Account Password", 
              hide_input=True, confirmation_prompt=True)
def set_user(email, password):
    """set_user - Set the user's account login information"""
    hashed = hashpw(password, gensalt())
    account = {"email": email, "password": hashed}
    with open(ACCOUNT_JSON, 'w') as f:
        json.dump(account, f)

@main.command('get_total_gains')
@click.option('-p', '--password', prompt="Robinhood password", help="Robinhood Account Password", 
              hide_input=True)
def get_total_gains(password):
    """get_total_gains - Return the total gains for the user's account"""
    with open(ACCOUNT_JSON, 'r') as f:
        account = json.load(f)
    
    if checkpw(password, account['password']):

        click.echo("Logged in as " + account['email'])
        r.login(account['email'], password)
        profile_data = r.load_portfolio_profile()
        crypto_positions = r.get_crypto_positions()
        all_transactions = r.get_bank_transfers()
        card_transactions = r.get_card_transactions()
        dividends = r.get_total_dividends()

        deposits = sum(float(x['amount']) for x in all_transactions if (
            x['direction'] == 'deposit') and (x['state'] == 'completed'))
        withdrawals = sum(float(x['amount']) for x in all_transactions if (
            x['direction'] == 'withdraw') and (x['state'] == 'completed'))
        debits = sum(float(x['amount']['amount']) for x in card_transactions if (
            x['direction'] == 'debit' and (x['transaction_type'] == 'settled')))
        reversal_fees = sum(float(x['fees']) for x in all_transactions if (
            x['direction'] == 'deposit') and (x['state'] == 'reversed'))
        
        money_invested = deposits + reversal_fees - (withdrawals - debits)
        percent_dividend = dividends/money_invested*100

        profile_equity = float(profile_data['extended_hours_equity'])
        crypto_equity = float(crypto_positions[0]['cost_bases'][0]['direct_cost_basis'])
        equity = profile_equity + crypto_equity

        total_gain_minus_dividends = equity - dividends - money_invested
        percent_gain = total_gain_minus_dividends/money_invested*100

        val = "${:.2f}"
        valp = "%{:.2f}"

        data = {'|Total Invested|': [val.format(money_invested)],
                '|Total Equity|': [val.format(equity)],
                '|Net Worth (Dividends)|': [(val.format(dividends),
                valp.format(percent_dividend).replace('%-', '-%'))],
                '|Net Worth (Other Gains)|': [(val.format(total_gain_minus_dividends),
                valp.format(percent_gain).replace('%-', '-%'))]}

        df = pd.DataFrame.from_dict(data)
        click.echo('\n')
        click.echo(df.to_string(index=False))
        click.echo('\n')

    else:
        # Login Unsuccessful
        click.echo("Incorrect Robinhood Password")

@main.command('get_history')
@click.option('--password', prompt="Robinhood password", help="Robinhood Account Password", 
              hide_input=True)
@click.option('--save', is_flag=True, help="Save data to .csv file.")
@click.argument('ticker')
@click.argument('interval')
@click.argument('span')
def get_history(password, save, ticker, interval, span):
    """get_history - Get a historical data range for a specific stock.
    
    TICKER - The stock symbol, i.e. TSLA.
    
    INTERVAL - 5minute 10minute hour day week.
    
    SPAN - day week month 3month year 5year.

    example - python robincli.py get_history --save TSLA 5minute day

    """
    with open(ACCOUNT_JSON, 'r') as f:
        account = json.load(f)
    
    if checkpw(password, account['password']):
        # Login Successful
        click.echo("Logged in as " + account['email'] + "\n")
        r.login(account['email'], password)

        data = r.get_stock_historicals(ticker, interval, span)
        df = pd.DataFrame.from_dict(data)
        df = df.drop(['session', 'interpolated', 'symbol'], axis=1)

        echo = {
            '5minute': '5 minute interval data for ',
            '10minute': '10 minute interval data for ',
            'hour': 'hourly data for ', 
            'day': 'daily data for ',
            'week': 'weekly data for '}


        click.echo("Getting " + echo[interval] + ticker + " from past " + span + "\n")
        print(df.to_string(index=False))

        if save: 
            filename = ticker + "_" + interval + "_" + span + ".csv"
            df.to_csv(filename, index=False)
    
    else:
        # Login Unsuccessful
        click.echo("Incorrect Robinhood Password")

if __name__ == '__main__':
    # pylint: disable=unexpected-keyword-arg
    # pylint: disable=no-value-for-parameter
    main(obj={})
