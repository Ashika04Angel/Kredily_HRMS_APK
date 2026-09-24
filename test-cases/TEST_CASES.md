# Kredily HRMS Android Mobile App – Master Test Cases Suite

**Document Version:** 1.0.0  
**Application:** Kredily HRMS Android APK (`kredily-mobile-v2.apk`)  
**Package Name:** `com.kredily.mobile`  
**Target Environment:** Android 10 - 15 (Emulators & Physical Devices)  
**Test Author:** Intern QA Engineer  
**Date:** September 2026  

---

## 📊 Test Case Summary Matrix

| Module | Positive Cases | Negative Cases | Edge / Boundary Cases | Total |
|---|:---:|:---:|:---:|:---:|
| **1. Authentication & Onboarding** | 2 | 2 | 1 | 5 |
| **2. Dashboard & Navigation** | 2 | 1 | 1 | 4 |
| **3. Attendance & Check-in / Geofencing** | 2 | 2 | 2 | 6 |
| **4. Leave Management & Approvals** | 2 | 1 | 1 | 4 |
| **5. Payroll & Payslips** | 1 | 1 | 1 | 3 |
| **6. Profile & KYC Records** | 1 | 0 | 1 | 2 |
| **TOTAL** | **10** | **7** | **7** | **24** |

---

## 📋 Detailed Test Specifications

### Module 1: Authentication & Onboarding

#### `TC-AUTH-001`
* **Test Title:** Verify successful login with valid registered email and password
* **Type:** Positive | **Priority:** P1 (Critical) | **Execution Type:** Automated / Manual
* **Preconditions:**
  1. Kredily mobile app is installed and launched on Android device.
  2. Active employee account exists (`peoplekredily1@yopmail.com` / `Pass@9865`).
  3. Device has active internet connectivity.
* **Test Steps:**
  1. Open Kredily app.
  2. In the identifier screen, enter email: `peoplekredily1@yopmail.com`.
  3. Click "Continue" / "Next".
  4. In the password screen, enter password: `Pass@9865`.
  5. Tap the "Sign In" button.
* **Test Data:** Email: `peoplekredily1@yopmail.com`, Password: `Pass@9865`
* **Expected Result:** App authenticates successfully, stores auth token securely, and redirects user to HRMS Dashboard displaying the employee profile header.
* **Actual Result:** Authenticates and navigates to Dashboard home screen.
* **Status:** `PASS`

---

#### `TC-AUTH-002`
* **Test Title:** Verify login error handling with invalid password
* **Type:** Negative | **Priority:** P1 (High) | **Execution Type:** Automated / Manual
* **Preconditions:** App is on password input screen for a valid identifier.
* **Test Steps:**
  1. Enter valid email: `peoplekredily1@yopmail.com`.
  2. Click "Continue".
  3. Enter invalid password: `WrongPassword@123`.
  4. Tap "Sign In".
* **Test Data:** Email: `peoplekredily1@yopmail.com`, Password: `WrongPassword@123`
* **Expected Result:** App displays inline error alert or toast: "Invalid credentials / Incorrect password" without crashing or revealing sensitive backend error traces. Password field remains editable.
* **Actual Result:** Error message displayed; user remains on password screen.
* **Status:** `PASS`

---

#### `TC-AUTH-003`
* **Test Title:** Verify validation on malformed email address and blank identifier
* **Type:** Negative | **Priority:** P2 (Medium) | **Execution Type:** Automated / Manual
* **Preconditions:** App is on identifier screen.
* **Test Steps:**
  1. Leave identifier input blank and tap "Continue".
  2. Enter invalid email format: `invalid_user@@domain..com` and tap "Continue".
  3. Enter numeric string with invalid length: `12345`.
* **Test Data:** `""`, `invalid_user@@domain..com`, `12345`
* **Expected Result:** Client-side validation triggers immediately with "Please enter a valid email address or phone number" without sending unnecessary network requests.
* **Actual Result:** Client-side validation prevents submission and highlights error state on input.
* **Status:** `PASS`

---

#### `TC-AUTH-004`
* **Test Title:** Verify "Forgot Password" OTP request and reset workflow
* **Type:** Positive | **Priority:** P2 (Medium) | **Execution Type:** Manual / API
* **Preconditions:** Employee email is registered on Kredily HRMS.
* **Test Steps:**
  1. On login screen, tap "Forgot Password?".
  2. Enter registered email `peoplekredily1@yopmail.com`.
  3. Tap "Send OTP" / "Reset Link".
  4. Verify network call to `/ws/v1/accounts/send-reset-otp/` or `/auth/otp/request`.
* **Test Data:** Email: `peoplekredily1@yopmail.com`
* **Expected Result:** Success message "OTP sent to your registered email" is displayed, and screen transitions to OTP verification input.
* **Actual Result:** OTP request screen triggers verification workflow.
* **Status:** `PASS`

---

#### `TC-AUTH-005`
* **Test Title:** Verify login behavior with trailing whitespace and mixed-case email (Edge Case)
* **Type:** Edge Case | **Priority:** P2 (Medium) | **Execution Type:** Automated / Manual
* **Preconditions:** App is launched on identifier screen.
* **Test Steps:**
  1. Enter email with leading/trailing whitespace and uppercase characters: `  PeOpLeKrEdIlY1@YoPmAil.CoM   `.
  2. Tap "Continue".
  3. Enter password `Pass@9865` and submit.
* **Test Data:** `  PeOpLeKrEdIlY1@YoPmAil.CoM   `
* **Expected Result:** App trims whitespace and normalizes email casing to lowercase before API authentication, allowing successful login.
* **Actual Result:** Trim & lowercase sanitization succeeds; user navigates to dashboard.
* **Status:** `PASS`

---

### Module 2: Dashboard & Quick Actions

#### `TC-DASH-001`
* **Test Title:** Verify Dashboard widgets and employee summary loading
* **Type:** Positive | **Priority:** P1 (High) | **Execution Type:** Automated / Manual
* **Preconditions:** User is logged into Kredily Mobile App.
* **Test Steps:**
  1. Observe Dashboard loading sequence.
  2. Verify presence of:
     - Employee Name & Greeting Header
     - Attendance Clock In / Clock Out Dashlet
     - Leave Balances Summary Card (Casual / Sick / Earned)
     - Quick Action Tiles (Apply Leave, View Payslip, Regularize, Directory)
     - Company Announcements / Wishes Banner
* **Test Data:** Logged in user session.
* **Expected Result:** All dashboard dashlets render within 2 seconds without blank placeholders or broken SVG icons.
* **Actual Result:** Dashboard renders header, clocking dashlet, leave cards, and banners accurately.
* **Status:** `PASS`

---

#### `TC-DASH-002`
* **Test Title:** Verify pull-to-refresh on Dashboard updates real-time attendance & leaves
* **Type:** Positive | **Priority:** P2 (Medium) | **Execution Type:** Manual / Automation
* **Preconditions:** User is on Dashboard screen.
* **Test Steps:**
  1. Drag down from the top of the dashboard to trigger pull-to-refresh indicator.
  2. Verify network triggers for `/ws/v2/company/dashboard` and `/mapi/v1/leave/balances/me`.
  3. Release and observe UI refresh completion.
* **Test Data:** N/A
* **Expected Result:** Refresh spinner animates smoothly, syncs latest data from backend, and auto-dismisses upon response.
* **Actual Result:** Dashboard refreshes data successfully.
* **Status:** `PASS`

---

#### `TC-DASH-003`
* **Test Title:** Verify dashboard behavior when company announcements list is empty (Edge Case)
* **Type:** Edge Case | **Priority:** P3 (Low) | **Execution Type:** Manual / API
* **Preconditions:** API `/ws/v2/company/get-announcements-and-wishes` returns empty array `[]`.
* **Test Steps:**
  1. Open dashboard with empty announcements payload.
  2. Observe announcements section.
* **Test Data:** API mock `{ "announcements": [], "wishes": [] }`
* **Expected Result:** Dashboard gracefully hides the announcements carousel or displays a clean empty state card ("No new announcements") without rendering layout artifacts.
* **Actual Result:** Section collapses gracefully.
* **Status:** `PASS`

---

#### `TC-DASH-004`
* **Test Title:** Verify quick navigation and back-stack handling across all bottom navigation tabs
* **Type:** Negative / Edge | **Priority:** P2 (Medium) | **Execution Type:** Automated / Manual
* **Preconditions:** User is on Dashboard home tab.
* **Test Steps:**
  1. Tap "Attendance" bottom tab -> verify route `/attendance`.
  2. Tap "Leave" bottom tab -> verify route `/leave`.
  3. Tap "Payroll" bottom tab -> verify route `/payroll`.
  4. Tap Android hardware Back button from deep sub-screen.
* **Test Data:** Tab routes
* **Expected Result:** Navigation transitions without screen flickering; back button returns to previous screen in stack without unintended app termination.
* **Actual Result:** Navigation stack preserved correctly.
* **Status:** `PASS`

---

### Module 3: Attendance & Check-In / Geofencing

#### `TC-ATT-001`
* **Test Title:** Verify successful Clock-In punch with GPS location within office geofence
* **Type:** Positive | **Priority:** P1 (Critical) | **Execution Type:** Automated / Manual
* **Preconditions:**
  1. Employee is logged in and assigned an active office location/shift.
  2. Device Location (GPS) permission is granted (`ACCESS_FINE_LOCATION`).
  3. Mock GPS coordinates are set within authorized office geofence radius (< 100m).
* **Test Steps:**
  1. Navigate to Attendance / Clock-In screen.
  2. Verify map/address displays current location accurately.
  3. Tap "Clock In" button.
  4. If selfie verification is enabled, capture face selfie.
  5. Tap "Confirm Punch".
* **Test Data:** Lat: `12.9716`, Long: `77.5946` (Office Geofence)
* **Expected Result:** Clock-in succeeds, toast "Clocked in successfully at HH:MM AM" appears, button state toggles to "Clock Out", and daily log list updates with In-Punch entry.
* **Actual Result:** Punch recorded successfully; state changes to Clock Out.
* **Status:** `PASS`

---

#### `TC-ATT-002`
* **Test Title:** Verify Clock-In rejection when GPS location is outside geofenced radius
* **Type:** Negative | **Priority:** P1 (High) | **Execution Type:** Automated / Manual
* **Preconditions:** Location permission granted; device coordinates set 50km outside office perimeter.
* **Test Steps:**
  1. Open Attendance punch screen with outside coordinates.
  2. Tap "Clock In".
* **Test Data:** Lat: `13.3400`, Long: `77.1000` (Outside Perimeter)
* **Expected Result:** App prevents punch submission and displays alert: "You are outside the designated office premises (Current distance: 50.2 km). Punch cannot be recorded."
* **Actual Result:** Alert displayed; punch blocked by geofence validation.
* **Status:** `PASS`

---

#### `TC-ATT-003`
* **Test Title:** Verify Clock-In prompt when Location Permission is denied by user
* **Type:** Negative | **Priority:** P2 (High) | **Execution Type:** Manual / Automated
* **Preconditions:** App location permission is set to "Don't allow" / Denied in Android OS settings.
* **Test Steps:**
  1. Launch Kredily app.
  2. Tap "Clock In" on dashboard.
* **Test Data:** Location permission = `DENIED`
* **Expected Result:** App displays rationale modal explaining why location is required for attendance, with a direct CTA "Open App Settings". App must not crash with `SecurityException`.
* **Actual Result:** Permission prompt / settings dialog displayed safely.
* **Status:** `PASS`

---

#### `TC-ATT-004`
* **Test Title:** Verify Attendance behavior on Network Drop / Airplane Mode during punch (Edge Case)
* **Type:** Edge Case | **Priority:** P1 (High) | **Execution Type:** Manual / Bug Verification
* **Preconditions:** User is on punch confirmation modal.
* **Test Steps:**
  1. Tap "Clock In".
  2. Immediately switch device to Airplane Mode / disconnect Wi-Fi.
  3. Observe app handling of pending HTTP request.
* **Test Data:** Network disconnected mid-request.
* **Expected Result:** App detects network timeout within 10 seconds, displays "Network connection lost. Please check your connection and retry", and provides a "Retry" button. Local punch state does not get corrupted.
* **Actual Result:** Found bug (BUG-05): Infinite spinner / unhandled promise rejection without retry button.
* **Status:** `FAIL (Bug Documented)`

---

#### `TC-ATT-005`
* **Test Title:** Verify Mock Location / Fake GPS detection during attendance punch (Security Edge Case)
* **Type:** Edge Case / Security | **Priority:** P1 (Critical) | **Execution Type:** Manual / Automated
* **Preconditions:** Android Developer Options enabled; Mock Location app selected.
* **Test Steps:**
  1. Enable mock GPS provider to spoof coordinates into office geofence.
  2. Open Kredily app and attempt "Clock In".
* **Test Data:** Spoofed GPS provider active (`isFromMockProvider == true`).
* **Expected Result:** App detects mock location flag via Android Location API and rejects punch with warning: "Mock location detected. Please disable location spoofing apps to record attendance."
* **Actual Result:** Found security vulnerability (BUG-02): Punch passes through without mock provider check.
* **Status:** `FAIL (Bug Documented)`

---

#### `TC-ATT-006`
* **Test Title:** Verify rapid multi-tap / double-click prevention on Clock-In CTA (Edge Case)
* **Type:** Edge Case | **Priority:** P2 (Medium) | **Execution Type:** Automated / Manual
* **Preconditions:** User is on Clock-In screen on a 3G / slow network connection.
* **Test Steps:**
  1. Rapidly tap the "Clock In" button 5 times within 1 second.
* **Test Data:** 5 simultaneous click events.
* **Expected Result:** Button disables immediately on first tap (`isSubmitting = true`), debouncing subsequent taps and sending only 1 API request to prevent duplicate punch logs.
* **Actual Result:** Button debounce works; single request dispatched.
* **Status:** `PASS`

---

### Module 4: Leave Management & Balance Tracking

#### `TC-LEV-001`
* **Test Title:** Verify successful leave application within available leave balance
* **Type:** Positive | **Priority:** P1 (High) | **Execution Type:** Automated / Manual
* **Preconditions:**
  1. Employee has available Casual Leave balance (e.g. 8 days).
  2. Navigated to Leave Application screen (`/leave`).
* **Test Steps:**
  1. Tap "Apply Leave".
  2. Select Leave Type: "Casual Leave".
  3. Select Start Date: Tomorrow, End Date: Tomorrow (1 Day).
  4. Enter Reason: "Personal family commitment".
  5. Tap "Submit Leave Request".
* **Test Data:** Leave Type: `Casual Leave`, Duration: `1 day`, Reason: `Personal family commitment`
* **Expected Result:** Application submitted successfully, confirmation toast shown, status set to "Pending Approval", and Casual Leave balance deducted or marked as provisional.
* **Actual Result:** Leave application submitted and displayed in leave log.
* **Status:** `PASS`

---

#### `TC-LEV-002`
* **Test Title:** Verify validation error when requesting leave exceeding available balance
* **Type:** Negative | **Priority:** P1 (High) | **Execution Type:** Automated / Manual
* **Preconditions:** Sick Leave balance is 2 days.
* **Test Steps:**
  1. Open Apply Leave form.
  2. Select Leave Type: "Sick Leave".
  3. Select Date Range of 5 working days.
  4. Enter Reason: "Medical treatment".
  5. Tap "Submit".
* **Test Data:** Requested: 5 days, Balance: 2 days.
* **Expected Result:** App displays validation message: "Requested days (5) exceed your available Sick Leave balance (2). Please adjust duration or apply as Loss of Pay (LOP)." Form submission is blocked.
* **Actual Result:** Validation triggers and blocks submission.
* **Status:** `PASS`

---

#### `TC-LEV-003`
* **Test Title:** Verify Leave Date Picker validation when End Date is before Start Date (Edge Case)
* **Type:** Negative / Edge | **Priority:** P1 (High) | **Execution Type:** Automated / Manual
* **Preconditions:** Leave application form open.
* **Test Steps:**
  1. Select Start Date: `28-Sep-2026`.
  2. Select End Date: `20-Sep-2026` (Past date relative to Start Date).
  3. Tap "Submit".
* **Test Data:** Start: `28-Sep-2026`, End: `20-Sep-2026`
* **Expected Result:** Date picker disallows selecting an End Date prior to Start Date (greyed out), or form displays inline error: "End Date cannot be earlier than Start Date."
* **Actual Result:** Found UI bug (BUG-03): Date picker allows inverted dates and submits malformed payload to server.
* **Status:** `FAIL (Bug Documented)`

---

#### `TC-LEV-004`
* **Test Title:** Verify leave application spanning across public holidays and weekends (Boundary Case)
* **Type:** Boundary / Edge | **Priority:** P2 (Medium) | **Execution Type:** Manual / API
* **Preconditions:** Company holiday calendar configured with Saturday/Sunday off and National Holiday on Monday.
* **Test Steps:**
  1. Apply leave from Friday to Tuesday (5 calendar days).
  2. Check calculated leave duration in summary view.
* **Test Data:** Friday to Tuesday with weekend + 1 public holiday.
* **Expected Result:** App calculates net working leave days as 2 days (Friday + Tuesday), excluding weekend and public holiday according to company leave policy rules.
* **Actual Result:** Working day deduction calculated accurately as 2 days.
* **Status:** `PASS`

---

### Module 5: Payroll & Payslip Access

#### `TC-PAY-001`
* **Test Title:** Verify viewing monthly payslip breakdown and downloading PDF
* **Type:** Positive | **Priority:** P2 (Medium) | **Execution Type:** Automated / Manual
* **Preconditions:** Employee has processed payroll records for the previous month.
* **Test Steps:**
  1. Navigate to "Payroll" tab (`/payroll`).
  2. Select Month: "August 2026".
  3. Verify display of Earnings (Basic, HRA, Allowances) and Deductions (PF, Professional Tax, TDS).
  4. Tap "Download Payslip PDF".
* **Test Data:** Month: `August 2026`
* **Expected Result:** Salary breakdown values match total Net Pay; PDF downloads to device storage and displays success notification.
* **Actual Result:** Payslip breakdown rendered and PDF download initiated.
* **Status:** `PASS`

---

#### `TC-PAY-002`
* **Test Title:** Verify payslip screen display when payroll has not been generated for the selected cycle
* **Type:** Negative / Boundary | **Priority:** P3 (Low) | **Execution Type:** Manual
* **Preconditions:** Selected month is the current ongoing month where payroll is unprocessed.
* **Test Steps:**
  1. Open Payroll screen.
  2. Select current month.
* **Test Data:** Ongoing Month
* **Expected Result:** Screen shows informative placeholder: "Payslip for this month is currently being processed by HR/Payroll team" with download button disabled.
* **Actual Result:** Informative message displayed; download CTA disabled.
* **Status:** `PASS`

---

#### `TC-PAY-003`
* **Test Title:** Verify masked CTC / salary figures when privacy toggle is enabled (Edge Case)
* **Type:** Edge Case / Security | **Priority:** P2 (Medium) | **Execution Type:** Manual
* **Preconditions:** User is on Payroll / Profile compensation screen.
* **Test Steps:**
  1. Tap the "Eye / Privacy Toggle" icon next to Net Salary figures.
  2. Verify all numerical currency values are masked with `••••••`.
  3. Tap toggle again to unmask.
* **Test Data:** Privacy toggle toggle state.
* **Expected Result:** Numbers toggle between masked and plaintext smoothly without clipping text layout.
* **Actual Result:** Privacy masking works as expected.
* **Status:** `PASS`

---

### Module 6: Profile & Employee KYC Records

#### `TC-PROF-001`
* **Test Title:** Verify employee personal and work information display
* **Type:** Positive | **Priority:** P2 (Medium) | **Execution Type:** Automated / Manual
* **Preconditions:** User is logged in and navigates to Profile tab.
* **Test Steps:**
  1. Open Profile tab.
  2. Inspect sections: Personal Info (Email, Phone, Blood Group), Work Info (Designation, Department, Manager, Date of Joining), Bank & UAN Details.
* **Test Data:** Logged in user profile data.
* **Expected Result:** All employee records match backend database entries without missing fields or placeholder `null` strings.
* **Actual Result:** Profile sections render data accurately.
* **Status:** `PASS`

---

#### `TC-PROF-002`
* **Test Title:** Verify profile image upload with oversized file and invalid format (Edge Case)
* **Type:** Edge Case / Negative | **Priority:** P3 (Low) | **Execution Type:** Manual
* **Preconditions:** User is on Profile Edit screen.
* **Test Steps:**
  1. Tap "Change Profile Photo".
  2. Select non-image file (e.g. `.pdf` or `.docx`) or an image > 15MB.
* **Test Data:** File: `test_document.pdf` (16 MB)
* **Expected Result:** App shows validation error: "Please upload a valid image file (JPG/PNG) under 5MB" and prevents upload.
* **Actual Result:** File picker limits to image types and enforces size constraint.
* **Status:** `PASS`

---

## 📈 Test Execution Results Summary

| Status | Count | Percentage |
|---|:---:|:---:|
| **Passed (`PASS`)** | 21 | 87.5% |
| **Failed (`FAIL`) - Bugs Documented** | 3 | 12.5% |
| **Blocked (`BLOCKED`)** | 0 | 0.0% |
| **Total Test Cases** | **24** | **100.0%** |
