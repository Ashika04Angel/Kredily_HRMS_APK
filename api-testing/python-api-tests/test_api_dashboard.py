"""
Automated API Tests for Dashboard, Announcements, and Company Banners Endpoints
"""
import pytest

class TestDashboardAPI:
    def test_dashboard_endpoint(self, session, base_url):
        """
        Verify GET /ws/v2/company/dashboard
        """
        url = f"{base_url}/ws/v2/company/dashboard"
        response = session.get(url, timeout=10)
        assert response.status_code in [200, 401, 403], f"Unexpected status: {response.status_code}"

    def test_announcements_and_wishes_endpoint(self, session, base_url):
        """
        Verify GET /ws/v2/company/get-announcements-and-wishes
        """
        url = f"{base_url}/ws/v2/company/get-announcements-and-wishes"
        response = session.get(url, timeout=10)
        assert response.status_code in [200, 401, 403], f"Unexpected status: {response.status_code}"

    def test_company_banners_endpoint(self, session, base_url):
        """
        Verify GET /ws/v2/company/get_banners
        """
        url = f"{base_url}/ws/v2/company/get_banners"
        response = session.get(url, timeout=10)
        assert response.status_code in [200, 401, 403], f"Unexpected status: {response.status_code}"
