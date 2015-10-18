from mmse15project.model.DBConnectionSQLite import DBConnectionSQLite
from mmse15project.model.AccountDBInterface            import AccountDBInterface
from mmse15project.model.ClientDBInterface             import ClientDBInterface
from mmse15project.model.FinancialRequestDBInterface   import FinancialRequestDBInterface
from mmse15project.model.RecruitmentRequestDBInterface import RecruitmentRequestDBInterface
from mmse15project.model.RequestDBInterface            import RequestDBInterface
from mmse15project.model.RequestDetailsDBInterface     import RequestDetailsDBInterface
from mmse15project.model.DiscountDBInterface           import DiscountDBinterface
from mmse15project.model.TaskDBInterface               import TaskDBInterface
from mmse15project.model.ClientMeetingDBInterface      import ClientMeetingDBInterface
from mmse15project.model.ScheduleDBInterface           import ScheduleDBInterface
class Model:
    def __init__(self):
        database = DBConnectionSQLite("SEP.db")
        self.account_db             = AccountDBInterface(database)
        self.client_db              = ClientDBInterface(database)
        self.financial_request_db   = FinancialRequestDBInterface(database)
        self.recruitment_request_db = RecruitmentRequestDBInterface(database)
        self.request_db             = RequestDBInterface(database)
        self.request_details_db     = RequestDetailsDBInterface(database)
        self.discount_db            = DiscountDBinterface(database)
        self.task_db                = TaskDBInterface(database)
        self.client_meeting_db      = ClientMeetingDBInterface(database)
        self.schedule_db            = ScheduleDBInterface(database)
