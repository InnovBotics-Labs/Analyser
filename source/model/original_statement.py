"""
Class Name: OriginalStatement.py
Purpose: Loads the bank statement and convert into pd dataframe
"""
# Dependencies

# Internal Dependencies
from source.framework.library.a_integrator import LOG, CONFIG
from source.framework.library.pandas_toolkit import PandasToolkit


# CONSTANTS

class OriginalStatement:
    """
    Purpose: Loads the bank statement and convert into pd dataframe
    Methods:
        __load_csv :loads the csv file and returns the data
        __load_statements : Get all the account statements from the location
    """

    def __init__(self):
        """
        Attributes: all the attributes are fetched from a settings file
            credit_cards_statements : dict
            checking_account_statements: dict
            dir_path : str
        """
        self.dir_path = \
            CONFIG.get(section="statement_settings",option="location")
        self.__from_credit_cards: dict = \
            self.__load_statements(account_category = "credit_cards")
        self.__from_checking_accounts:dict = \
            self.__load_statements(account_category = "checking_accounts")

    def __load_statements(self,account_category: str)-> dict:
        """Get the all the credit cards from the machines"""
        LOG.debug(f"will start loading all the {account_category} statements")

        # Get all the credit cards
        accounts :list=  CONFIG.get_options(section = account_category)

        statements: dict = {}

        # Transverse all the accounts one by one
        for account in accounts:

            # Getting the path of the statement from settings
            path = self.dir_path + CONFIG.get(section = account_category, option=account)

            new_statement = {
                account: PandasToolkit.load_csv(file_path=path)
            }
            # loading the statement and adding it into a dict
            statements.update(new_statement)

            LOG.debug(f"{account} statement "\
                                + "Loaded" if new_statement is not  None else "NOT loaded")

        LOG.info(f"Loaded all the {account_category} statements")

        return statements

    @property
    def from_checking_accounts(self)-> dict:
        """returns the checking account statements """
        return self.__from_checking_accounts

    @property
    def from_credit_cards(self) -> dict:
        """returns the checking account statements """
        return self.__from_credit_cards
