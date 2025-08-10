"""
Class Name: StatementFormatter.py
Blue+print of:formatting and organizing the data into desired structure
"""
# Dependencies
import pandas as pd
from abc import ABC, abstractmethod

# Internal Dependencies
from source.framework.library.a_integrator import LOG, TABLE_HEADER
from source.framework.library.config_manager import CONFIG
from source.framework.library.pandas_toolkit import PandasToolkit

class BaseStatementFormatter(ABC):
    """
    Purpose: Base class for formatting and organizing statement data into desired structure
    Attributes:
        statement : pd.DataFrame
        account_name: str
    Methods:
        _rename_columns : will rename columns in the data table
    """

    def __init__(self, **kwargs):
        """
        Attributes:
            statements : OriginalStatement
        """
        self.statement: pd.DataFrame = kwargs.get("statement")
        self.account_name: str = kwargs.get("account_name")

    def get_desired_format(self)-> pd.DataFrame:
        """
        1. Unifies the amount column be combining debit and credit
        2. Unifies the column name across statement
        3. Adds from account columns
        4. Keeps only the required columns
        5. Bank-specific formatting (implemented by child classes)
        6. Changing the date column to date time format

        :return: Formatted DataFrame
        """

        # Unifies the amount column be combining debit and credit
        self._format_amount_column()

        # Unifies the column name across the statement
        self._rename_columns()

        # Adds from account columns
        self._add_from_account_col()

        # keeps only the required columns
        self._required_columns()

        # Bank-specific formatting (implemented by child classes)
        self._bank_specific_formatting()

        # Changes the date column to date time format
        self.statement['transaction_date'] = pd.to_datetime(self.statement['transaction_date'])

        return self.statement
    
    @abstractmethod
    def _bank_specific_formatting(self) -> None:
        """
        Bank-specific formatting logic to be implemented by child classes
        """
        pass

    def _format_amount_column(self) -> None:
        """ To perform: will rename columns in the data table"""

        columns = self.statement.columns
        lowercase_columns = [column.lower() for column in columns]

        if 'amount' not in lowercase_columns:
            self.statement = PandasToolkit.combine_first_column(
                self.statement,col1="Debit",col2="Credit",new_column='amount'
            )
            LOG.info("Amount column added")
        else:
            LOG.debug("Amount already exists")

    def _rename_columns(self) -> None:
        """ To perform: will rename columns in the data table"""

        section = self.account_name + "_map"
        mapping_form_config = CONFIG.get_options_pair(section)

        # Interchange keys and values
        mapping = {value: key for key, value in mapping_form_config.items()}

        self.statement = PandasToolkit.rename_columns(self.statement,columns_mapping=mapping)
        LOG.debug("After renaming column the statements is")
        LOG.table(table=self.statement, header=self.statement.columns)

    def _required_columns(self)-> None:
        """selecting only required columns """
        required_columns = TABLE_HEADER

        self.statement = PandasToolkit.filter_columns(self.statement,required_columns)
        LOG.debug("After filtered with required column the statement is")
        LOG.table(table=self.statement,header=self.statement.columns)

    def _add_from_account_col(self)-> None:
        """adds a new column and fill the account name as a value"""
        self.statement = PandasToolkit.add_column(
            self.statement,column_name="from_account",value=self.account_name
        )
        LOG.debug("After adding from account column")
        LOG.table(table=self.statement, header=self.statement.columns)

    def get_account_name(self)-> str:
        """returns the account name"""
        return self.account_name


class CitiStatementFormatter(BaseStatementFormatter):
    """
    Purpose: Formatter for Citi bank statements
    """
    
    def _bank_specific_formatting(self) -> None:
        """
        Citi bank specific formatting:
        - Converts expenditure to negative value and payout to positive value
        """
        # Converts expenditure to negative value and payout to positive value
        self.statement = PandasToolkit.modify_column(
            df=self.statement,
            column_name='amount',
            condition=lambda x: True,
            operation=lambda x: x * -1
        )
        LOG.debug("Applied Citi-specific formatting")


class DiscoverStatementFormatter(BaseStatementFormatter):
    """
    Purpose: Formatter for Discover bank statements
    """
    
    def _bank_specific_formatting(self) -> None:
        """
        Discover bank specific formatting:
        - Converts expenditure to negative value and payout to positive value
        """
        # Converts expenditure to negative value and payout to positive value
        self.statement = PandasToolkit.modify_column(
            df=self.statement,
            column_name='amount',
            condition=lambda x: True,
            operation=lambda x: x * -1
        )
        LOG.debug("Applied Discover-specific formatting")


class DefaultStatementFormatter(BaseStatementFormatter):
    """
    Purpose: Default formatter for bank statements that don't need special formatting
    """
    
    def _bank_specific_formatting(self) -> None:
        """
        Default implementation - no special formatting needed
        """
        LOG.debug("No bank-specific formatting needed for this statement")


# Factory function to create the appropriate formatter based on account name
def create_statement_formatter(**kwargs):
    """
    Factory function to create the appropriate statement formatter based on account name
    
    Args:
        **kwargs: Keyword arguments including account_name and statement
        
    Returns:
        An instance of the appropriate statement formatter class
    """
    account_name = kwargs.get("account_name")
    
    if account_name == 'citi':
        return CitiStatementFormatter(**kwargs)
    elif account_name == 'discover':
        return DiscoverStatementFormatter(**kwargs)
    else:
        return DefaultStatementFormatter(**kwargs)
