from mmse15project.model.DBConnectionSQLite import DBConnectionSQLite
from mmse15project.model.AccountDBInterface            import AccountDBInterface
from mmse15project.model.ClientDBInterface             import ClientDBInterface
from mmse15project.model.FinancialRequestDBInterface   import FinancialRequestDBInterface
from mmse15project.model.RecruitmentRequestDBInterface import RecruitmentRequestDBInterface
from mmse15project.model.RequestDBInterface            import RequestDBInterface
from mmse15project.model.RequestDetailsDBInterface     import RequestDetailsDBInterface


class Model:
    def __init__(self):
        database = DBConnectionSQLite("SEP.db")
        self.account_db             = AccountDBInterface(database)
        self.client_db              = ClientDBInterface(database)
        self.financial_request_db   = FinancialRequestDBInterface(database)
        self.recruitment_request_db = RecruitmentRequestDBInterface(database)
        self.request_db             = RequestDBInterface(database)
        self.request_details_db     = RequestDetailsDBInterface(database)
