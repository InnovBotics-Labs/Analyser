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

    report = Report(statement=transactions)

    earnings = report.earnings()
    LOG.table(table=earnings, header=earnings.columns)

    expenses = report.expenses()
    LOG.table(table=expenses, header=expenses.columns)


    a = earnings.pivot_table(index="category",columns="year_month",
                             values='amount',aggfunc='sum',margins=True,
                             margins_name='Total')
    LOG.table(table=a,header=a.columns)

    a = expenses.pivot_table(index="category", columns="year_month",
                             values='amount', aggfunc='sum', margins=True,
                             margins_name='Total')
    LOG.table(table=a, header=a.columns)

    LOG.info(message="Ended")

if __name__ == '__main__':
    main()
