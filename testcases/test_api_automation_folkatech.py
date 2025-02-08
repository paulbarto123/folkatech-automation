import pytest
import requests
import json
import urllib.parse

class TestAPIFolkatech():
    # Base URL dari Collection API
    BASE_URL = "https://lapor.folkatech.com/api/"  # Ganti dengan URL yang benar jika berbeda
    # Request Headers
    HEADERS = {
        "Accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    def get_auth_token(self):
        """Logs in to the API and returns the authentication token."""
        # Login Data
        PAYLOAD = {
            "email": "rhmtsaepuloh@gmail.com",
            "password": "password",
            "reg_id": "12345"
        }
        encoded_payload = urllib.parse.urlencode(PAYLOAD)  # Explicit encoding

        # Send POST request
        try:
            response = requests.post(url=f"{self.BASE_URL}login", headers=self.HEADERS, data=encoded_payload)

            if response.status_code == 200:
                response_json = response.json()
                self.token = response_json.get("data").get("token")
                if self.token:
                    return self.token
                else:
                    raise ValueError("❌ Token not found in response!")

            elif response.status_code == 404:
                error_data = response.json()
                exception = error_data.get("exception", "Unknown Exception")
                return f"❌ API Not Found! Exception: {exception}"

            else:
                return f"❌ Error: {response.status_code} - {response.text}"

        except requests.exceptions.RequestException as e:
            return f"❌ Request failed: {str(e)}"

    # Positive Scenario: Kirim laporan dengan data valid
    def test_create_report_valid(self):
        payload = {
            "report_category_id": "3",
            "fullname": "Rahmat Saefulloh",
            "gender": "l",
            "province_id": "1",
            "tipe_korban": "php",
            "description": "Tes",
            "lat": "1",
            "lng": "1",
            "address_location": "Cimahi",
            "urgency": "rendah"
        }

        # Authentication Token (Replace with dynamic retrieval if needed)
        auth_token = self.get_auth_token()
        # File Path (Ensure this path is correct)
        file_path = "/Users/rhmtsaepuloh/Downloads/gamaharsaasia.png"

        # File Upload
        FILES = {
            "userfile": open(file_path, "rb")  # Open image file in binary mode
        }

        """Sends a valid report request and checks the response."""
        try:
            response = requests.post(f"{self.BASE_URL}report", headers=self.HEADERS, data=payload, files=FILES)
            FILES["userfile"].close()  # Close file after sending request

            # Check response status
            if response.status_code == 201:
                response_json = response.json()
                print("✅ Report successfully created!")
                print("Response:", response_json)
                return response_json
            else:
                print(f"❌ Failed to create report! Status Code: {response.status_code}")
                print("Response:", response.text)
                return None

        except requests.exceptions.RequestException as e:
            print(f"❌ Request failed: {str(e)}")
            return None


    # Negative Scenario: Kirim laporan dengan data tidak lengkap
    def test_create_report_invalid(self):
        payload = {
            "title": "Laporan Kebersihan",  # Missing required fields
        }

        response = requests.post(f"{self.BASE_URL}/report", headers=self.HEADERS, data=json.dumps(payload))
        assert response.status_code == 400, f"Expected 400, but got {response.status_code}"
        response_json = response.json()
        assert "error" in response_json, "Expected error message in response JSON"
        print("✅ Negative Test Passed: Proper error message received!")
