"""
Tests for the Reports API class.
"""
import datetime
import unittest
import mws
from .utils import CommonRequestTestTools


class ReportsTestCase(unittest.TestCase, CommonRequestTestTools):
    """
    Test cases for Reports.
    """
    # TODO: Add remaining methods for Reports
    def setUp(self):
        self.api = mws.Reports(
            self.CREDENTIAL_ACCESS,
            self.CREDENTIAL_SECRET,
            self.CREDENTIAL_ACCOUNT,
            auth_token=self.CREDENTIAL_TOKEN
        )
        self.api._test_request_params = True

    def test_request_report(self):
        """
        RequestReport operation.
        """
        report_type = '_GET_FLAT_FILE_OPEN_LISTINGS_DATA_'
        start_date = datetime.datetime.utcnow()
        end_date = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        marketplace_ids = [
            'iQzBCmf1y3',
            'wH9q0CiEMp',
        ]
        params = self.api.request_report(
            report_type=report_type,
            start_date=start_date,
            end_date=end_date,
            marketplace_ids=marketplace_ids,
        )
        self.assert_common_params(params)
        self.assertEqual(params['Action'], 'RequestReport')
        self.assertEqual(params['ReportType'], report_type)
        self.assertEqual(params['StartDate'], start_date.isoformat())
        self.assertEqual(params['EndDate'], end_date.isoformat())
        self.assertEqual(params['MarketplaceIdList.Id.1'], marketplace_ids[0])
        self.assertEqual(params['MarketplaceIdList.Id.2'], marketplace_ids[1])

    def test_get_report_request_list(self):
        """
        GetReportRequestList operation.
        """
        request_ids = [
            'rPlSxpfnR7',
            'qRrkqv03qh',
        ]
        report_types = [
            '_GET_MFN_PAN_EU_OFFER_STATUS_',
            '_GET_FLAT_FILE_ORDERS_DATA_',
        ]
        processing_statuses = [
            '_SUBMITTED_',
            '_DONE_NO_DATA_',
        ]
        max_count = 987
        from_date = datetime.datetime.utcnow()
        to_date = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        params = self.api.get_report_request_list(
            request_ids=request_ids,
            report_types=report_types,
            processing_statuses=processing_statuses,
            max_count=max_count,
            from_date=from_date,
            to_date=to_date,
        )
        self.assert_common_params(params)
        self.assertEqual(params['Action'], 'GetReportRequestList')
        self.assertEqual(params['MaxCount'], max_count)
        self.assertEqual(params['RequestedFromDate'], from_date.isoformat())
        self.assertEqual(params['RequestedToDate'], to_date.isoformat())
        self.assertEqual(params['ReportRequestIdList.Id.1'], request_ids[0])
        self.assertEqual(params['ReportRequestIdList.Id.2'], request_ids[1])
        self.assertEqual(params['ReportTypeList.Type.1'], report_types[0])
        self.assertEqual(params['ReportTypeList.Type.2'], report_types[1])
        self.assertEqual(params['ReportProcessingStatusList.Status.1'], processing_statuses[0])
        self.assertEqual(params['ReportProcessingStatusList.Status.2'], processing_statuses[1])

    def test_get_report_request_list_by_next_token(self):
        """
        GetReportRequestListByNextToken operation, via method decorator.
        """
        next_token = 'RXmLZ2bEgE'
        params = self.api.get_report_request_list(next_token=next_token)
        self.assert_common_params(params)
        self.assertEqual(params['Action'], 'GetReportRequestListByNextToken')
        self.assertEqual(params['NextToken'], next_token)

    def test_get_report_request_list_by_next_token_alias(self):
        """
        GetReportRequestListByNextToken operation, via alias method.
        """
        next_token = '0hytxbkaOb'
        params = self.api.get_report_request_list_by_next_token(next_token)
        self.assert_common_params(params)
        self.assertEqual(params['Action'], 'GetReportRequestListByNextToken')
        self.assertEqual(params['NextToken'], next_token)

    def test_get_report_request_count(self):
        """
        GetReportRequestCount operation.
        """
        report_types = [
            '_GET_XML_ALL_ORDERS_DATA_BY_LAST_UPDATE_',
            '_GET_FLAT_FILE_ALL_ORDERS_DATA_BY_ORDER_DATE_',
        ]
        processing_statuses = [
            '_CANCELLED_',
            '_IN_PROGRESS_',
        ]
        from_date = datetime.datetime.utcnow()
        to_date = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        params = self.api.get_report_request_count(
            report_types=report_types,
            processing_statuses=processing_statuses,
            from_date=from_date,
            to_date=to_date,
        )
        self.assert_common_params(params)
        self.assertEqual(params['Action'], 'GetReportRequestCount')
        self.assertEqual(params['RequestedFromDate'], from_date.isoformat())
        self.assertEqual(params['RequestedToDate'], to_date.isoformat())
        self.assertEqual(params['ReportTypeList.Type.1'], report_types[0])
        self.assertEqual(params['ReportTypeList.Type.2'], report_types[1])
        self.assertEqual(params['ReportProcessingStatusList.Status.1'], processing_statuses[0])
        self.assertEqual(params['ReportProcessingStatusList.Status.2'], processing_statuses[1])

    def test_get_report_list(self):
        """
        GetReportList operation.
        """
        request_ids = [
            'c4eik8sxXC',
            'NIVgnbHXe0',
        ]
        report_types = [
            '_GET_V1_SELLER_PERFORMANCE_REPORT_',
            '_GET_SELLER_FEEDBACK_DATA_',
        ]
        max_count = 564
        acknowledged = True
        from_date = datetime.datetime.utcnow()
        to_date = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        params = self.api.get_report_list(
            request_ids=request_ids,
            max_count=max_count,
            report_types=report_types,
            acknowledged=acknowledged,
            from_date=from_date,
            to_date=to_date,
        )
        self.assert_common_params(params)
        self.assertEqual(params['Action'], 'GetReportList')
        self.assertEqual(params['Acknowledged'], acknowledged)
        self.assertEqual(params['AvailableFromDate'], from_date.isoformat())
        self.assertEqual(params['AvailableToDate'], to_date.isoformat())
        self.assertEqual(params['MaxCount'], max_count)
        self.assertEqual(params['ReportRequestIdList.Id.1'], request_ids[0])
        self.assertEqual(params['ReportRequestIdList.Id.2'], request_ids[1])
        self.assertEqual(params['ReportTypeList.Type.1'], report_types[0])
        self.assertEqual(params['ReportTypeList.Type.2'], report_types[1])

    def test_get_report_list_by_next_token(self):
        """
        GetReportListByNextToken operation, via method decorator.
        """
        next_token = '5u6Of2fS8B'
        params = self.api.get_report_list(next_token=next_token)
        self.assert_common_params(params)
        self.assertEqual(params['Action'], 'GetReportListByNextToken')
        self.assertEqual(params['NextToken'], next_token)

    def test_get_report_list_by_next_token_alias(self):
        """
        GetReportListByNextToken operation, via alias method.
        """
        next_token = '3TczcliCkb'
        params = self.api.get_report_list_by_next_token(next_token)
        self.assert_common_params(params)
        self.assertEqual(params['Action'], 'GetReportListByNextToken')
        self.assertEqual(params['NextToken'], next_token)

    def test_get_report_count(self):
        """
        GetReportCount operation.
        """
        pass

    def test_get_report(self):
        """
        GetReport operation.
        """
        pass

    def test_get_report_schedule_list(self):
        """
        GetReportScheduleList operation.
        """
        pass

    def test_get_report_schedule_list_by_next_token(self):
        """
        GetReportScheduleListByNextToken operation, via method decorator.
        """
        next_token = 'Yj3hOfPcIE'
        params = self.api.get_report_schedule_list(next_token=next_token)
        self.assert_common_params(params)
        self.assertEqual(params['Action'], 'GetReportScheduleListByNextToken')
        self.assertEqual(params['NextToken'], next_token)

    def test_get_report_schedule_list_by_next_token_alias(self):
        """
        GetReportScheduleListByNextToken operation, via alias method.
        """
        next_token = 'SAlt4JwJGv'
        params = self.api.get_report_schedule_list_by_next_token(next_token)
        self.assert_common_params(params)
        self.assertEqual(params['Action'], 'GetReportScheduleListByNextToken')
        self.assertEqual(params['NextToken'], next_token)

    def test_get_report_schedule_count(self):
        """
        GetReportScheduleCount operation.
        """
        pass

    # # TODO Complete when method is available in Reports
    # def test_update_report_acknowledgements(self):
    #     """
    #     UpdateReportAcknowledgements operation.
    #     """
    #     pass
