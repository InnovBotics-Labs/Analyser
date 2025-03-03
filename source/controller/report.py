"""
Class Name: Report.py
Blue+print of:To create a report based on the data
"""
# Dependencies
import pandas as pd

# Internal Dependencies
from source.framework.library.pandas_toolkit import PandasToolkit

class Report:
    """
    Purpose: Blueprint of To create a report based on the data
    Attributes:
        statement : pd.DataFrame
    Methods:
        generate : create a report table
    """

    def __init__(self, **kwargs):
        """
        Attributes:
            statements : pd.DataFrame
        """
        self.statement: pd.DataFrame = kwargs.get("statement")

    def earnings(self) -> pd.DataFrame | None:
        """ report amounts received are from the statement """
        return PandasToolkit.filter_rows(
            self.statement,
            column_name='amount',
            condition=lambda x: x > 0
        )

    def expenses(self) -> pd.DataFrame | None:
        """ report amount spend """
        return PandasToolkit.filter_rows(
            self.statement,
            column_name='amount',
            condition=lambda x: x < 0
        )

    # Reports under Expenses
    def expenses_category(self)-> pd.DataFrame:
        """Generates the categorized report"""

        # Modify and takes statements only the expenses
        expenses = self.expenses()

        return expenses.pivot_table(index="category", columns="year_month",
                             values='amount', aggfunc='sum', margins=True,
                             margins_name='Total')

    # Reports under Expenses
    def expenses_sub_category(self)-> pd.DataFrame:
        """Generates the categorized report"""

        # Modify and takes statements only the expenses
        expenses = self.expenses()

        return expenses.pivot_table(index="sub_category", columns="year_month",
                             values='amount', aggfunc='sum', margins=True,
                             margins_name='Total')