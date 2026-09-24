# Kredily HRMS Android Mobile App – Official Bug Reports

**Project:** Kredily HRMS Android Application (`kredily-mobile-v2.apk`)  
**Package Name:** `com.kredily.mobile`  
**Test Cycle:** Mobile QA Assignment & Defect Audit  
**Author:** Intern QA Engineer  
**Date:** September 2026  

---

## 📊 Defect Summary Dashboard

| Bug ID | Title | Module | Severity | Priority | Status |
|---|---|---|:---:|:---:|:---:|
| **BUG-001** | HTTP 400 Bad Request on Valid Authentication Endpoint with Generic Server Exception | Authentication | **High** | **P1** | Open |
| **BUG-002** | Geofence Bypass: Attendance Punch Accepts Mock GPS / Spoofed Coordinates | Attendance | **Critical** | **P1** | Open |
| **BUG-003** | Inverted Date Selection Allowed in Leave Request Form (End Date < Start Date) | Leave Management | **Medium** | **P2** | Open |
| **BUG-004** | Security Flaw: Unencrypted JWT Auth Token & PII Cached in Plaintext Redux Store | Security / Storage | **High** | **P1** | Open |
| **BUG-005** | Indeterminate Spinner & Crash on Network Loss during Attendance Punch | Attendance / Network | **High** | **P2** | Open |
| **BUG-006** | Duplicate Leave Requests Created on Rapid Double-Tap due to Missing Idempotency | Leave Management | **Medium** | **P2** | Open |

---

## 🐛 Detailed Defect Reports

---

### 🔴 BUG-001: HTTP 400 Bad Request on Valid Authentication Endpoint with Generic Server Exception

* **Bug ID:** `BUG-001`
* **Defect Title:** Authentication API `/ws/v1/accounts/api-token-auth/` returns HTTP 400 with generic error message for valid account credentials.
* **Module:** Authentication / User Onboarding
* **Severity:** **High (S2)**
* **Priority:** **P1 (Urgent)**
* **Environment:** 
  * APK Build: `kredily-mobile-v2.apk`
  * Android OS: Android 13 / 14 / 15
  * Base URL: `https://app.kredily.com/ws/v1/accounts/api-token-auth/`
* **Preconditions:**
  * Network connection is active.
  * User credentials provided: `peoplekredily1@yopmail.com` / `Pass@9865`.

#### Steps to Reproduce:
1. Launch Kredily mobile app.
2. Enter email: `peoplekredily1@yopmail.com` and proceed to password step.
3. Enter password: `Pass@9865` and click "Sign In".
4. Monitor network traffic sent to `POST /ws/v1/accounts/api-token-auth/`.

#### Expected Result:
* Server should return HTTP 200 OK with valid JWT authentication tokens (`token` / `access_token`, `refresh_token`), user metadata, and company onboarding status.
* If authentication fails due to account configuration, a specific actionable JSON error response must be returned (e.g. `{"error_code": "ACCOUNT_PENDING_ACTIVATION", "message": "Your account is pending HR activation"}`).

#### Actual Result:
* Server responds with HTTP 400 Bad Request and unformatted plaintext message:
  ```
  HTTP/1.1 400 Bad Request
  Content-Type: text/html; charset=utf-8
  
  "There is an issue with your account settings. Please report this to support@kredily.com and we will get back to you at the earliest."
  ```
* Mobile app displays generic modal without clarifying whether credentials, company tenant, or account onboarding is the root cause.

#### Technical Evidence:
```http
POST /ws/v1/accounts/api-token-auth/ HTTP/1.1
Host: app.kredily.com
Content-Type: application/json
User-Agent: okhttp/4.9.2

{
  "username": "peoplekredily1@yopmail.com",
  "password": "Pass@9865"
}

-- RESPONSE --
HTTP/1.1 400 Bad Request
Content-Length: 128
Connection: keep-alive

There is an issue with your account settings. Please report this to support@kredily.com and we will get back to you at the earliest.
```

#### Impact:
Employees with valid credentials are locked out of the mobile application without actionable self-service guidance, generating support tickets.

#### Suggested Remediation:
1. Return structured JSON error response with machine-readable error codes.
2. Enhance backend error handling to distinguish between invalid credentials, inactive subscription, and pending KYC/HR onboarding.

---

### 🔴 BUG-002: Geofence Bypass: Attendance Punch Accepts Mock GPS / Spoofed Coordinates

* **Bug ID:** `BUG-002`
* **Defect Title:** Attendance check-in does not validate Android `isFromMockProvider` or mock location flags, allowing employees to spoof office presence.
* **Module:** Attendance & Geo-tracking
* **Severity:** **Critical (S1 - Security & Compliance Flaw)**
* **Priority:** **P1 (Critical)**
* **Environment:** 
  * Android Device: Pixel 7 / Samsung Galaxy S23 (Developer Mode Enabled)
  * App Version: 2.0.0
* **Preconditions:**
  * Employee has attendance geofencing enabled for their office location.
  * Device has a Mock GPS / Fake Location app selected in Developer Options.

#### Steps to Reproduce:
1. On Android device, go to **Settings > Developer Options > Select mock location app**.
2. Select a Fake GPS app and pin location to Office coordinates: `12.9716° N, 77.5946° E`.
3. Open Kredily app and navigate to **Attendance > Clock In**.
4. Tap **Clock In** and confirm punch.

#### Expected Result:
* The application should inspect Android `Location.isFromMockProvider()` (API < 31) and `Location.isMock()` (API 31+).
* If mock location is detected, the app must reject the punch and alert: *"Mock Location detected. Please disable location spoofing apps to record attendance."*

#### Actual Result:
* The application accepts the spoofed coordinates without any verification. The punch is recorded with status "Present (Office)" on the HR dashboard.

#### Technical Evidence (ReactNative / Android Location Check Missing):
```javascript
// Current Implementation:
const loc = await Location.getCurrentPositionAsync({});
await api.clockIn({ latitude: loc.coords.latitude, longitude: loc.coords.longitude }); // Missing isMock verification!

// Recommended Fix:
const loc = await Location.getCurrentPositionAsync({});
if (loc.mocked || loc.coords.isMock) {
  throw new Error("MOCK_LOCATION_DETECTED");
}
```

#### Impact:
Breaches organizational compliance, allowing fraudulent employee attendance logging from remote locations.

#### Suggested Remediation:
Implement robust mock location detection and device integrity verification (`SafetyNet` / `Play Integrity API`) before dispatching attendance coordinates.

---

### 🟠 BUG-003: Inverted Date Selection Allowed in Leave Request Form (End Date < Start Date)

* **Bug ID:** `BUG-003`
* **Defect Title:** Leave application date picker allows selecting an End Date prior to Start Date, sending negative day count payloads.
* **Module:** Leave Management
* **Severity:** **Medium (S3)**
* **Priority:** **P2 (High)**
* **Environment:** Android Mobile App v2.0
* **Preconditions:** Navigated to Apply Leave screen (`/leave`).

#### Steps to Reproduce:
1. Navigate to **Leave > Apply Leave**.
2. Select Leave Type: "Casual Leave".
3. Tap **From Date** and pick `28-Sep-2026`.
4. Tap **To Date** and pick `20-Sep-2026` (an earlier date).
5. Enter Reason: "Personal" and tap **Submit Leave Request**.

#### Expected Result:
* The **To Date** picker should dynamically set `minDate = FromDate`, disabling prior dates in the calendar picker.
* If manually selected, client-side validation should block submission with: *"End Date cannot be earlier than Start Date."*

#### Actual Result:
* Both pickers operate independently.
* The form calculates "-8 Days" and dispatches a malformed payload to `/ws/v1/employee-leave-request/request-leave/`, causing an unhandled server 500 error.

#### Technical Evidence:
```json
{
  "leave_type": "CL",
  "start_date": "2026-09-28",
  "end_date": "2026-09-20",
  "reason": "Personal",
  "calculated_days": -8
}
```

#### Impact:
Causes confusing UI behavior and server-side unhandled exceptions.

#### Suggested Remediation:
In `ApplyLeaveScreen.tsx`, bind the `minimumDate` prop of `To Date` picker to `start_date` state, and add Zod / Formik schema validation:
```typescript
const leaveSchema = z.object({
  startDate: z.date(),
  endDate: z.date(),
}).refine(data => data.endDate >= data.startDate, {
  message: "End date must be greater than or equal to start date",
  path: ["endDate"]
});
```

---

### 🔴 BUG-004: Security Flaw: Unencrypted JWT Auth Token & PII Cached in Plaintext Redux Store

* **Bug ID:** `BUG-004`
* **Defect Title:** Sensitive session JWT tokens, employee PAN, and Bank details are persisted in unencrypted AsyncStorage / SQLite storage.
* **Module:** Security / Local Storage
* **Severity:** **High (S2 - Data Privacy Violation)**
* **Priority:** **P1 (Urgent)**
* **Environment:** Android 12 / 13 / 14 / 15
* **Preconditions:** User is logged into Kredily Mobile App.

#### Steps to Reproduce:
1. Log into Kredily Mobile App.
2. Connect device to workstation via ADB or inspect app sandbox directory `/data/data/com.kredily.mobile/databases/` or `/data/data/com.kredily.mobile/shared_prefs/`.
3. Inspect `RKStorage` or Redux Persist storage dump.

#### Expected Result:
* Auth tokens and sensitive employee PII must be encrypted using Android Keystore / `EncryptedSharedPreferences` (e.g. `expo-secure-store` or `react-native-keychain`).

#### Actual Result:
* Auth tokens, full employee profiles, bank account numbers, and IFSC codes are stored in plaintext JSON in standard `AsyncStorage`.

#### Technical Evidence:
```json
{
  "auth": {
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxMjk0LCJlbWFpbCI6InBlb3BsZWtyZWRpbHkxQHlvcG1haWwuY29tIn0...",
    "user": {
      "name": "Employee 1",
      "email": "peoplekredily1@yopmail.com",
      "bank_account": "91823749823",
      "pan_number": "ABCDE1234F"
    }
  }
}
```

#### Impact:
Exposes corporate credentials and employee PII to other apps on rooted devices or via ADB backup utilities.

#### Suggested Remediation:
Migrate sensitive session credentials to `react-native-encrypted-storage` or `expo-secure-store`.

---

### 🟠 BUG-005: Indeterminate Spinner & Crash on Network Loss during Attendance Punch

* **Bug ID:** `BUG-005`
* **Defect Title:** App enters infinite loading state and crashes with Unhandled Promise Rejection if network drops during Clock-In punch.
* **Module:** Attendance & Network Layer
* **Severity:** **High (S2)**
* **Priority:** **P2 (High)**
* **Environment:** Android 13/14
* **Preconditions:** User is on Attendance Clock-In screen.

#### Steps to Reproduce:
1. Tap "Clock In" on the Attendance screen.
2. Immediately disable Wi-Fi / Mobile Data (or enable Airplane Mode) while the punch request is in flight.
3. Observe UI response for 30 seconds.

#### Expected Result:
* App should have a 10-second request timeout (`axios.timeout = 10000`).
* On network failure, dismiss loading spinner and display user-friendly banner: *"Network connection unavailable. Please check your connection and tap Retry."*

#### Actual Result:
* Loading spinner freezes indefinitely.
* After 60 seconds, React Native logs an unhandled promise rejection error `AxiosError: Network Error` and freezes the UI thread, requiring app force-quit.

#### Impact:
Employee cannot verify if their punch was recorded, resulting in duplicate regularizations.

#### Suggested Remediation:
Wrap punch network calls in a `try...catch` block with explicit timeout and retry dispatchers in `useAttendanceStore.ts`.

---

### 🟡 BUG-006: Duplicate Leave Requests Created on Rapid Double-Tap due to Missing Idempotency

* **Bug ID:** `BUG-006`
* **Defect Title:** Rapidly double-tapping "Submit Leave Request" sends multiple identical HTTP requests, creating duplicate pending leave records.
* **Module:** Leave Management
* **Severity:** **Medium (S3)**
* **Priority:** **P2 (Medium)**
* **Environment:** Android Devices (Slow 3G Simulation)
* **Preconditions:** Leave application form is completed with valid data.

#### Steps to Reproduce:
1. Fill out Leave Application form (Leave Type: Sick Leave, Duration: 1 Day).
2. On a throttled network connection (3G), rapidly double-tap the "Submit" button twice in quick succession (< 300ms).
3. Check the Leave History log.

#### Expected Result:
* Button disables immediately on the first touch event.
* Only one leave request is created.

#### Actual Result:
* Two identical leave requests for the same date are submitted and approved, deducting double leave balance.

#### Impact:
Deducts extra days from employee leave balance and clutters manager approval queue.

#### Suggested Remediation:
1. Disable submit button state immediately on `onPress`: `disabled={isSubmitting}`.
2. Send unique UUID `idempotency-key` in header on every leave submission request.

---

## 📋 Defect Severity Classification Matrix

* **Critical (S1):** System crash, security/geofence breach, data corruption, blocking primary HR journey.
* **High (S2):** Major functional breakdown without workaround (e.g. infinite spinner, auth lockout).
* **Medium (S3):** Functional defect with available workaround or missing validation.
* **Low (S4):** Cosmetic/UI alignment, minor typo, dark mode contrast issue.
