""" Starting point of program """
# Dependencies


# Internal Modules
from source.framework.library.a_integrator import LOG
from source.controller.report import Report
from source.model.statements import Statements
from source.controller.processor import Processor

# CONSTANTS
#Hi



def main()-> None:
    """Starting point of program"""
    LOG.info(message="started")

    activity = Statements()
    r_transactions = activity.transactions
    t_processor = Processor(raw_transactions=r_transactions)
    transactions = t_processor.processed_transactions
    #transactions.to_csv("transactions.csv")
    transactions['year_month'] = transactions['transaction_date'].dt.to_period('M')

    # Group data month-wise
    month_groups = transactions.groupby(transactions['year_month'])

    for month, group in month_groups:

        LOG.critical(message=month)

        report = Report(statement=group)

        earnings = report.earnings()
        LOG.table(table=earnings, header=earnings.columns)

        expenses = report.expenses()
        LOG.table(table=expenses, header=expenses.columns)

        expenses_category = report.expenses_category()
        LOG.table(table=expenses_category,header=expenses_category.columns)

        expenses_sub_category =report.expenses_sub_category()
        LOG.table(table=expenses_sub_category, header=expenses_sub_category.columns)

    LOG.info(message="Ended")

if __name__ == '__main__':
    main()
