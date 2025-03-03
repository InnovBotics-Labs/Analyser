"""
Class Name: Statements.py
Blue+print of:contains statement from all accounts
"""
# Dependencies
import pandas as pd

# Internal Dependencies
from source.framework.library.a_integrator import LOG, TABLE_HEADER
from source.framework.library.pandas_toolkit import PandasToolkit
from source.model.original_statement import OriginalStatement
from source.model.statement_formatter import StatementFormatter

class Statements:
    """
    Purpose: Blueprint of statements contains transactions from all accounts
    Attributes:
        __original_statements : OriginalStatement
    Methods:
        get_credit_card_transactions : give all credit card transactions
    """

    def __init__(self, **kwargs):
        """
        Attributes:
            original_statements : OriginalStatement
        """
        self.__original_statements: OriginalStatement = kwargs.get(
            "original_statements",OriginalStatement()
        )
        self.transactions:pd.DataFrame = pd.DataFrame(
            columns=TABLE_HEADER
        )
        self.collect_transactions()

    def collect_transactions(self) -> None:
        """
        1. Combine all statements into a single dict
        2. Traverse each statement one by one and format statement
        3. Merge the return table into transactions' table

        returns give all transactions.
        """

        # Combine all statements (merging 2 dict)
        statements = \
            self.__original_statements.from_credit_cards\
            | self.__original_statements.from_checking_accounts

        # Traverse each statement one by one
        for account, statement in statements.items():

            # Creates a statement formater
            statement_formatter = StatementFormatter(account_name=account, statement=statement)

            # Formated statement from statement formatter
            formatted_statement = statement_formatter.get_desired_format()

            LOG.info("statements are formatted to the desired format.")

            # Adds into an existing transactions table
            self.transactions = PandasToolkit.concat_dataframes(
                self.transactions,
                formatted_statement
            )

        LOG.info("transactions table created")

    @staticmethod
    def future_method()-> None:
        """will update in future"""
        print("To handle pylint error")
