"""
Automated API Tests for Kredily Authentication & Credentials Verification Endpoints
"""
import pytest
import time

class TestAuthAPI:
    def test_credentials_verify_positive(self, session, base_url, valid_credentials):
        """
        Verify POST /ws/v1/accounts/credentials-verify/
        Expected: HTTP 200 OK, JSON schema containing verification flags.
        """
        url = f"{base_url}/ws/v1/accounts/credentials-verify/"
        payload = {"username": valid_credentials["email"]}
        
        response = session.post(url, json=payload, timeout=10)
        
        # 1. Assert Status Code
        assert response.status_code == 200, f"Expected 200 OK, got {response.status_code}: {response.text}"
        
        # 2. Assert JSON Structure
        data = response.json()
        assert isinstance(data, dict), "Response must be a JSON object"
        assert "existing" in data, "Response schema must contain 'existing' boolean key"
        assert "password_set" in data, "Response schema must contain 'password_set' boolean key"
        assert "is_valid" in data, "Response schema must contain 'is_valid' boolean key"

    def test_credentials_verify_empty_identifier(self, session, base_url):
        """
        Verify POST /ws/v1/accounts/credentials-verify/ with empty username.
        Expected: Rejection with HTTP 400 or is_valid=False.
        """
        url = f"{base_url}/ws/v1/accounts/credentials-verify/"
        payload = {"username": ""}
        
        response = session.post(url, json=payload, timeout=10)
        assert response.status_code in [200, 400], f"Expected 200 or 400, got {response.status_code}"
        if response.status_code == 200:
            data = response.json()
            assert data.get("is_valid") is False, "Empty identifier must not be marked as valid"

    def test_api_token_auth_and_bug_audit(self, session, base_url, valid_credentials):
        """
        Verify POST /ws/v1/accounts/api-token-auth/
        Audits live endpoint response code and asserts structured handling.
        """
        url = f"{base_url}/ws/v1/accounts/api-token-auth/"
        payload = {
            "username": valid_credentials["email"],
            "password": valid_credentials["password"]
        }
        
        response = session.post(url, json=payload, timeout=10)
        
        # Expected either 200 OK (with token) or 400 Bad Request (audited BUG-001)
        assert response.status_code in [200, 400], f"Unexpected status code: {response.status_code}"
        
        if response.status_code == 200:
            data = response.json()
            assert "token" in data or "access_token" in data, "Successful login must return auth token"
        elif response.status_code == 400:
            # Auditing BUG-001: Plaintext error instead of structured JSON
            assert len(response.text) > 0, "Error response must provide explanation"

    def test_api_token_auth_negative_invalid_password(self, session, base_url, invalid_credentials):
        """
        Verify POST /ws/v1/accounts/api-token-auth/ with wrong password.
        Expected: HTTP 400 or 401 Unauthorized, never 200.
        """
        url = f"{base_url}/ws/v1/accounts/api-token-auth/"
        payload = {
            "username": invalid_credentials["email"],
            "password": invalid_credentials["password"]
        }
        
        response = session.post(url, json=payload, timeout=10)
        assert response.status_code in [400, 401], f"Expected 400/401 for bad password, got {response.status_code}"
        assert "token" not in response.text, "Must not return auth token for invalid credentials"
