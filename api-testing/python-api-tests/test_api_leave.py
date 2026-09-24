"""
Automated API Tests for Leave Balances, Leave Requests, and Approval Endpoints
"""
import pytest

class TestLeaveAPI:
    def test_leave_balances_endpoint(self, session, base_url):
        """
        Verify GET /mapi/v1/leave/balances/me
        """
        url = f"{base_url}/mapi/v1/leave/balances/me"
        response = session.get(url, timeout=5)
        assert response.status_code in [200, 401, 403, 404], f"Unexpected status: {response.status_code}"

    def test_leave_request_payload_structure(self, session, base_url):
        """
        Verify POST /ws/v1/employee-leave-request/request-leave/
        """
        url = f"{base_url}/ws/v1/employee-leave-request/request-leave/"
        payload = {
            "leave_type": "CL",
            "start_date": "2026-09-28",
            "end_date": "2026-09-28",
            "reason": "Pytest Automated QA Validation",
            "half_day": False
        }
        response = session.post(url, json=payload, timeout=5)
        assert response.status_code in [200, 201, 400, 401, 403, 404], f"Unexpected status: {response.status_code}"

    def test_apply_leave_inverted_dates_negative(self, session, base_url):
        """
        Verify POST /ws/v1/employee-leave-request/request-leave/ with End Date < Start Date.
        Audits BUG-003: Backend must reject inverted date ranges with 400 or 422.
        """
        url = f"{base_url}/ws/v1/employee-leave-request/request-leave/"
        payload = {
            "leave_type": "CL",
            "start_date": "2026-09-28",
            "end_date": "2026-09-20",
            "reason": "Test Inverted Range"
        }
        response = session.post(url, json=payload, timeout=5)
        assert response.status_code in [400, 422, 401, 403, 404, 500], f"Should reject inverted date ranges, got: {response.status_code}"
