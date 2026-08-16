# BPMN Process Modeling - Comprehensive Process Report

This document provides a detailed breakdown of the business logic, control flow, decision gates, and BPMN 2.0 element mappings for each modeled scenario.

---

## Scenario 1: Employee Leave Approval

### 1. Process Overview & Business Objective
The Employee Leave Approval workflow manages internal time-off requests submitted through the enterprise HR system[cite: 1]. The objective is to automate balance validation, route valid requests to management for authorization, update system balances upon approval, and provide clear notifications across all outcomes[cite: 1].

### 2. Step-by-Step Execution Logic
1. **Trigger:** The workflow is initiated when an employee submits a leave request through the HR portal[cite: 1].
2. **Automated Verification:** The HR system queries the employee's record to check their current leave balance against the requested duration[cite: 1].
3. **Balance Decision Gateway (XOR 1):**
   - **Insufficient Balance (Default/Exception Path):** If the balance is insufficient, the system generates and sends an insufficient-balance notification to the employee[cite: 1]. The process terminates immediately[cite: 1].
   - **Sufficient Balance (Happy Path):** If sufficient balance is confirmed, the request is forwarded to the employee's manager for review[cite: 1].
4. **Manager Approval Gateway (XOR 2):**
   - **Rejected Path:** If the manager rejects the request, the system sends a rejection notification to the employee[cite: 1]. The process ends[cite: 1].
   - **Approved Path:** If the manager approves the request, the system deducts the approved days from the employee's leave balance and dispatches an approval notification[cite: 1]. The process terminates successfully[cite: 1].

### 3. BPMN 2.0 Element Mapping
- **Start Event:** `Leave Request Submitted` (Unspecified Start Event)[cite: 1].
- **Tasks:**
  - `Check Leave Balance` (Service/Automated Task)[cite: 1]
  - `Send Request to Manager for Approval` (User/Manual Task)[cite: 1]
  - `Update Leave Balance` (Service Task)[cite: 1]
  - `Send Approval Notification` (Send Task)[cite: 1]
  - `Send Rejection Notification` (Send Task)[cite: 1]
  - `Send Insufficient-Balance Notification` (Send Task)[cite: 1]
- **Exclusive Gateways (XOR):**
  - `Sufficient Balance?` (Evaluates leave balance availability)[cite: 1]
  - `Manager Approved?` (Evaluates managerial decision)[cite: 1]
- **End Events:**
  - `Request Terminated` (End state for insufficient balance)[cite: 1]
  - `Request Rejected` (End state for manager rejection)[cite: 1]
  - `Leave Approved` (Successful completion end state)[cite: 1]

---

## Scenario 2: Online Purchase Order Processing

### 1. Process Overview & Business Objective
The Online Purchase Order Processing workflow governs e-commerce customer transactions[cite: 1]. It coordinates real-time inventory validation, payment gateway authorization, product packing, carrier fulfillment, and customer tracking updates[cite: 1].

### 2. Step-by-Step Execution Logic
1. **Trigger:** The process begins when a customer places an online order[cite: 1].
2. **Inventory Verification:** The inventory module checks product availability in the warehouse[cite: 1].
3. **Availability Gateway (XOR 1):**
   - **Out of Stock:** If the item is unavailable, the system notifies the customer that the product is out of stock[cite: 1]. The process terminates[cite: 1].
   - **In Stock:** If available, the transaction proceeds to payment processing[cite: 1].
4. **Payment Processing & Gateway (XOR 2):**
   - **Payment Failure:** If the payment fails or is declined, a payment failure notification is sent to the customer[cite: 1]. The process terminates[cite: 1].
   - **Payment Success:** If payment succeeds, the system confirms the order, schedules warehouse fulfillment, prepares the item for shipment, hands it to logistics for shipping, and sends a shipping confirmation email to the customer[cite: 1]. The order process completes successfully[cite: 1].

### 3. BPMN 2.0 Element Mapping
- **Start Event:** `Order Placed` (Message/Start Event)[cite: 1].
- **Tasks:**
  - `Check Product Availability` (Service Task)[cite: 1]
  - `Notify Customer (Out of Stock)` (Send Task)[cite: 1]
  - `Process Payment` (Service Task)[cite: 1]
  - `Notify Customer (Payment Failed)` (Send Task)[cite: 1]
  - `Confirm Order` (Service Task)[cite: 1]
  - `Prepare Product for Shipment` (User/Manual Task)[cite: 1]
  - `Ship Order` (Service/Manual Task)[cite: 1]
  - `Send Shipping Confirmation` (Send Task)[cite: 1]
- **Exclusive Gateways (XOR):**
  - `Product Available?` (Branches based on stock count)[cite: 1]
  - `Payment Successful?` (Branches based on transaction status)[cite: 1]
- **End Events:**
  - `Order Terminated` (Cancelled due to inventory unavailability)[cite: 1]
  - `Order Cancelled` (Cancelled due to failed transaction)[cite: 1]
  - `Order Fulfilled` (Successful fulfillment and dispatch)[cite: 1]

---

## Scenario 3: IT Service Request

### 1. Process Overview & Business Objective
The IT Service Request workflow models technical issue triage, prioritization, tier-based assignment, diagnosis, troubleshooting, escalation, and ticket resolution within an organization[cite: 1].

### 2. Step-by-Step Execution Logic
1. **Trigger & Intake:** The workflow triggers when an employee reports an IT problem and submits a support request[cite: 1].
2. **Registration & Classification:** The IT help desk logs the ticket and evaluates problem severity[cite: 1].
3. **Severity Routing (Diverging XOR 1):**
   - **Low Severity:** Routed to a standard Support Technician[cite: 1].
   - **High Severity:** Routed directly to a Senior Technician[cite: 1].
4. **Converging Gateway (Merge 1):** Both assignment paths merge into a shared investigation phase where the designated technician diagnoses the root cause[cite: 1].
5. **Resolution Assessment (Diverging XOR 2):**
   - **Internal Resolution:** If the problem can be resolved internally, the technician applies the fix directly[cite: 1].
   - **External Escalation:** If the issue cannot be resolved internally, the technician escalates it to an external service provider for remediation[cite: 1].
6. **Converging Gateway (Merge 2):** Both remediation paths merge into status reconciliation[cite: 1].
7. **Closure & Notification:** The help desk updates the ticket status to resolved, sends a resolution confirmation notification to the employee, and closes the ticket[cite: 1].

### 3. BPMN 2.0 Element Mapping
- **Start Event:** `IT Problem Reported`[cite: 1]
- **Tasks:**
  - `Register IT Support Request` (User Task)[cite: 1]
  - `Check Problem Severity` (Business Rule / User Task)[cite: 1]
  - `Assign to Support Technician` (Service Task)[cite: 1]
  - `Assign to Senior Technician` (Service Task)[cite: 1]
  - `Investigate Problem` (User Task)[cite: 1]
  - `Fix Problem` (User Task)[cite: 1]
  - `Escalate to External Service Provider` (User/Send Task)[cite: 1]
  - `Update Request Status` (Service Task)[cite: 1]
  - `Send Resolution Notification to Employee` (Send Task)[cite: 1]
- **Exclusive Gateways (XOR):**
  - `Severity Level?` (Diverging XOR)[cite: 1]
  - `Severity Merge` (Converging XOR)
  - `Resolved Internally?` (Diverging XOR)[cite: 1]
  - `Resolution Merge` (Converging XOR)
- **End Event:** `Request Closed` (Terminal State)[cite: 1]