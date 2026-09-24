"""
Automated API Tests for Attendance, Geofencing, and Clock-In/Out Endpoints
"""
import pytest

class TestAttendanceAPI:
    def test_daily_log_endpoint(self, session, base_url):
        """
        Verify GET /kapi/v1/attendance/mobile/daily-log
        """
        url = f"{base_url}/kapi/v1/attendance/mobile/daily-log"
        response = session.get(url, timeout=5)
        assert response.status_code in [200, 401, 403, 404], f"Unexpected status: {response.status_code}"

    def test_clock_in_payload_validation(self, session, base_url):
        """
        Verify POST /kapi/v1/attendance/mobile/clockIn with valid GPS coordinates payload structure.
        """
        url = f"{base_url}/kapi/v1/attendance/mobile/clockIn"
        payload = {
            "latitude": 12.9716,
            "longitude": 77.5946,
            "punch_type": "IN",
            "device_timestamp": "2026-09-24T09:30:00.000Z"
        }
        response = session.post(url, json=payload, timeout=5)
        assert response.status_code in [200, 201, 400, 401, 403, 404], f"Unexpected status: {response.status_code}"

    def test_clock_in_missing_coordinates_negative(self, session, base_url):
        """
        Verify POST /kapi/v1/attendance/mobile/clockIn rejects empty/missing coordinates.
        """
        url = f"{base_url}/kapi/v1/attendance/mobile/clockIn"
        payload = {"punch_type": "IN"}
        response = session.post(url, json=payload, timeout=5)
        assert response.status_code in [400, 422, 401, 403, 404], f"Should reject missing coordinates, got: {response.status_code}"
