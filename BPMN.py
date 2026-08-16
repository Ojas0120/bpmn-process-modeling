import os

scenarios = {
    "diagrams/scenario-1-leave-approval.bpmn": """<?xml version="1.0" encoding="UTF-8"?>
<bpmn:definitions xmlns:bpmn="http://www.omg.org/spec/BPMN/20100524/MODEL"
                  xmlns:bpmndi="http://www.omg.org/spec/BPMN/20100524/DI"
                  xmlns:dc="http://www.omg.org/spec/DD/20100524/DC"
                  xmlns:di="http://www.omg.org/spec/DD/20100524/DI"
                  id="Definitions_1"
                  targetNamespace="http://bpmn.io/schema/bpmn">
  <bpmn:process id="Process_LeaveApproval" isExecutable="false">
    <bpmn:startEvent id="Start_1" name="Leave Request Submitted">
      <bpmn:outgoing>f1</bpmn:outgoing>
    </bpmn:startEvent>
    <bpmn:task id="Task_1" name="Check Leave Balance">
      <bpmn:incoming>f1</bpmn:incoming>
      <bpmn:outgoing>f2</bpmn:outgoing>
    </bpmn:task>
    <bpmn:exclusiveGateway id="XOR_1" name="Sufficient Balance?">
      <bpmn:incoming>f2</bpmn:incoming>
      <bpmn:outgoing>f3</bpmn:outgoing>
      <bpmn:outgoing>f5</bpmn:outgoing>
    </bpmn:exclusiveGateway>
    <bpmn:task id="Task_NoBal" name="Send Insufficient-Balance Notification">
      <bpmn:incoming>f3</bpmn:incoming>
      <bpmn:outgoing>f4</bpmn:outgoing>
    </bpmn:task>
    <bpmn:endEvent id="End_NoBal" name="Request Terminated">
      <bpmn:incoming>f4</bpmn:incoming>
    </bpmn:endEvent>
    <bpmn:task id="Task_SendMgr" name="Send Request to Manager for Approval">
      <bpmn:incoming>f5</bpmn:incoming>
      <bpmn:outgoing>f6</bpmn:outgoing>
    </bpmn:task>
    <bpmn:exclusiveGateway id="XOR_2" name="Manager Approved?">
      <bpmn:incoming>f6</bpmn:incoming>
      <bpmn:outgoing>f7</bpmn:outgoing>
      <bpmn:outgoing>f9</bpmn:outgoing>
    </bpmn:exclusiveGateway>
    <bpmn:task id="Task_Reject" name="Send Rejection Notification">
      <bpmn:incoming>f7</bpmn:incoming>
      <bpmn:outgoing>f8</bpmn:outgoing>
    </bpmn:task>
    <bpmn:endEvent id="End_Reject" name="Request Rejected">
      <bpmn:incoming>f8</bpmn:incoming>
    </bpmn:endEvent>
    <bpmn:task id="Task_UpdateBal" name="Update Leave Balance">
      <bpmn:incoming>f9</bpmn:incoming>
      <bpmn:outgoing>f10</bpmn:outgoing>
    </bpmn:task>
    <bpmn:task id="Task_ApproveNotif" name="Send Approval Notification">
      <bpmn:incoming>f10</bpmn:incoming>
      <bpmn:outgoing>f11</bpmn:outgoing>
    </bpmn:task>
    <bpmn:endEvent id="End_Approved" name="Leave Approved">
      <bpmn:incoming>f11</bpmn:incoming>
    </bpmn:endEvent>
    <bpmn:sequenceFlow id="f1" sourceRef="Start_1" targetRef="Task_1" />
    <bpmn:sequenceFlow id="f2" sourceRef="Task_1" targetRef="XOR_1" />
    <bpmn:sequenceFlow id="f3" name="No" sourceRef="XOR_1" targetRef="Task_NoBal" />
    <bpmn:sequenceFlow id="f4" sourceRef="Task_NoBal" targetRef="End_NoBal" />
    <bpmn:sequenceFlow id="f5" name="Yes" sourceRef="XOR_1" targetRef="Task_SendMgr" />
    <bpmn:sequenceFlow id="f6" sourceRef="Task_SendMgr" targetRef="XOR_2" />
    <bpmn:sequenceFlow id="f7" name="No" sourceRef="XOR_2" targetRef="Task_Reject" />
    <bpmn:sequenceFlow id="f8" sourceRef="Task_Reject" targetRef="End_Reject" />
    <bpmn:sequenceFlow id="f9" name="Yes" sourceRef="XOR_2" targetRef="Task_UpdateBal" />
    <bpmn:sequenceFlow id="f10" sourceRef="Task_UpdateBal" targetRef="Task_ApproveNotif" />
    <bpmn:sequenceFlow id="f11" sourceRef="Task_ApproveNotif" targetRef="End_Approved" />
  </bpmn:process>
  <bpmndi:BPMNDiagram id="BPMNDiagram_1">
    <bpmndi:BPMNPlane id="BPMNPlane_1" bpmnElement="Process_LeaveApproval">
      <bpmndi:BPMNShape id="Start_1_di" bpmnElement="Start_1">
        <dc:Bounds x="160" y="102" width="36" height="36" />
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="Task_1_di" bpmnElement="Task_1">
        <dc:Bounds x="250" y="80" width="110" height="80" />
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="XOR_1_di" bpmnElement="XOR_1" isMarkerVisible="true">
        <dc:Bounds x="415" y="95" width="50" height="50" />
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="Task_NoBal_di" bpmnElement="Task_NoBal">
        <dc:Bounds x="520" y="200" width="120" height="80" />
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="End_NoBal_di" bpmnElement="End_NoBal">
        <dc:Bounds x="692" y="222" width="36" height="36" />
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="Task_SendMgr_di" bpmnElement="Task_SendMgr">
        <dc:Bounds x="520" y="80" width="120" height="80" />
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="XOR_2_di" bpmnElement="XOR_2" isMarkerVisible="true">
        <dc:Bounds x="695" y="95" width="50" height="50" />
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="Task_Reject_di" bpmnElement="Task_Reject">
        <dc:Bounds x="800" y="200" width="120" height="80" />
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="End_Reject_di" bpmnElement="End_Reject">
        <dc:Bounds x="972" y="222" width="36" height="36" />
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="Task_UpdateBal_di" bpmnElement="Task_UpdateBal">
        <dc:Bounds x="800" y="80" width="110" height="80" />
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="Task_ApproveNotif_di" bpmnElement="Task_ApproveNotif">
        <dc:Bounds x="960" y="80" width="110" height="80" />
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="End_Approved_di" bpmnElement="End_Approved">
        <dc:Bounds x="1122" y="102" width="36" height="36" />
      </bpmndi:BPMNShape>
      <bpmndi:BPMNEdge id="f1_di" bpmnElement="f1">
        <di:waypoint x="196" y="120" />
        <di:waypoint x="250" y="120" />
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNEdge id="f2_di" bpmnElement="f2">
        <di:waypoint x="360" y="120" />
        <di:waypoint x="415" y="120" />
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNEdge id="f3_di" bpmnElement="f3">
        <di:waypoint x="440" y="145" />
        <di:waypoint x="440" y="240" />
        <di:waypoint x="520" y="240" />
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNEdge id="f4_di" bpmnElement="f4">
        <di:waypoint x="640" y="240" />
        <di:waypoint x="692" y="240" />
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNEdge id="f5_di" bpmnElement="f5">
        <di:waypoint x="465" y="120" />
        <di:waypoint x="520" y="120" />
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNEdge id="f6_di" bpmnElement="f6">
        <di:waypoint x="640" y="120" />
        <di:waypoint x="695" y="120" />
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNEdge id="f7_di" bpmnElement="f7">
        <di:waypoint x="720" y="145" />
        <di:waypoint x="720" y="240" />
        <di:waypoint x="800" y="240" />
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNEdge id="f8_di" bpmnElement="f8">
        <di:waypoint x="920" y="240" />
        <di:waypoint x="972" y="240" />
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNEdge id="f9_di" bpmnElement="f9">
        <di:waypoint x="745" y="120" />
        <di:waypoint x="800" y="120" />
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNEdge id="f10_di" bpmnElement="f10">
        <di:waypoint x="910" y="120" />
        <di:waypoint x="960" y="120" />
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNEdge id="f11_di" bpmnElement="f11">
        <di:waypoint x="1070" y="120" />
        <di:waypoint x="1122" y="120" />
      </bpmndi:BPMNEdge>
    </bpmndi:BPMNPlane>
  </bpmndi:BPMNDiagram>
</bpmn:definitions>""",

    "diagrams/scenario-2-purchase-order.bpmn": """<?xml version="1.0" encoding="UTF-8"?>
<bpmn:definitions xmlns:bpmn="http://www.omg.org/spec/BPMN/20100524/MODEL"
                  xmlns:bpmndi="http://www.omg.org/spec/BPMN/20100524/DI"
                  xmlns:dc="http://www.omg.org/spec/DD/20100524/DC"
                  xmlns:di="http://www.omg.org/spec/DD/20100524/DI"
                  id="Definitions_2"
                  targetNamespace="http://bpmn.io/schema/bpmn">
  <bpmn:process id="Process_PurchaseOrder" isExecutable="false">
    <bpmn:startEvent id="Start_2" name="Order Placed">
      <bpmn:outgoing>sf1</bpmn:outgoing>
    </bpmn:startEvent>
    <bpmn:task id="Task_CheckStock" name="Check Product Availability">
      <bpmn:incoming>sf1</bpmn:incoming>
      <bpmn:outgoing>sf2</bpmn:outgoing>
    </bpmn:task>
    <bpmn:exclusiveGateway id="XOR_Stock" name="Product Available?">
      <bpmn:incoming>sf2</bpmn:incoming>
      <bpmn:outgoing>sf3</bpmn:outgoing>
      <bpmn:outgoing>sf5</bpmn:outgoing>
    </bpmn:exclusiveGateway>
    <bpmn:task id="Task_OOS" name="Notify Customer (Out of Stock)">
      <bpmn:incoming>sf3</bpmn:incoming>
      <bpmn:outgoing>sf4</bpmn:outgoing>
    </bpmn:task>
    <bpmn:endEvent id="End_OOS" name="Order Terminated">
      <bpmn:incoming>sf4</bpmn:incoming>
    </bpmn:endEvent>
    <bpmn:task id="Task_Payment" name="Process Payment">
      <bpmn:incoming>sf5</bpmn:incoming>
      <bpmn:outgoing>sf6</bpmn:outgoing>
    </bpmn:task>
    <bpmn:exclusiveGateway id="XOR_Payment" name="Payment Successful?">
      <bpmn:incoming>sf6</bpmn:incoming>
      <bpmn:outgoing>sf7</bpmn:outgoing>
      <bpmn:outgoing>sf9</bpmn:outgoing>
    </bpmn:exclusiveGateway>
    <bpmn:task id="Task_PayFail" name="Notify Customer (Payment Failed)">
      <bpmn:incoming>sf7</bpmn:incoming>
      <bpmn:outgoing>sf8</bpmn:outgoing>
    </bpmn:task>
    <bpmn:endEvent id="End_PayFail" name="Order Cancelled">
      <bpmn:incoming>sf8</bpmn:incoming>
    </bpmn:endEvent>
    <bpmn:task id="Task_Confirm" name="Confirm Order">
      <bpmn:incoming>sf9</bpmn:incoming>
      <bpmn:outgoing>sf10</bpmn:outgoing>
    </bpmn:task>
    <bpmn:task id="Task_Prep" name="Prepare Product for Shipment">
      <bpmn:incoming>sf10</bpmn:incoming>
      <bpmn:outgoing>sf11</bpmn:outgoing>
    </bpmn:task>
    <bpmn:task id="Task_Ship" name="Ship Order">
      <bpmn:incoming>sf11</bpmn:incoming>
      <bpmn:outgoing>sf12</bpmn:outgoing>
    </bpmn:task>
    <bpmn:task id="Task_ShipConf" name="Send Shipping Confirmation">
      <bpmn:incoming>sf12</bpmn:incoming>
      <bpmn:outgoing>sf13</bpmn:outgoing>
    </bpmn:task>
    <bpmn:endEvent id="End_OrderComplete" name="Order Fulfilled">
      <bpmn:incoming>sf13</bpmn:incoming>
    </bpmn:endEvent>
    <bpmn:sequenceFlow id="sf1" sourceRef="Start_2" targetRef="Task_CheckStock" />
    <bpmn:sequenceFlow id="sf2" sourceRef="Task_CheckStock" targetRef="XOR_Stock" />
    <bpmn:sequenceFlow id="sf3" name="No" sourceRef="XOR_Stock" targetRef="Task_OOS" />
    <bpmn:sequenceFlow id="sf4" sourceRef="Task_OOS" targetRef="End_OOS" />
    <bpmn:sequenceFlow id="sf5" name="Yes" sourceRef="XOR_Stock" targetRef="Task_Payment" />
    <bpmn:sequenceFlow id="sf6" sourceRef="Task_Payment" targetRef="XOR_Payment" />
    <bpmn:sequenceFlow id="sf7" name="No" sourceRef="XOR_Payment" targetRef="Task_PayFail" />
    <bpmn:sequenceFlow id="sf8" sourceRef="Task_PayFail" targetRef="End_PayFail" />
    <bpmn:sequenceFlow id="sf9" name="Yes" sourceRef="XOR_Payment" targetRef="Task_Confirm" />
    <bpmn:sequenceFlow id="sf10" sourceRef="Task_Confirm" targetRef="Task_Prep" />
    <bpmn:sequenceFlow id="sf11" sourceRef="Task_Prep" targetRef="Task_Ship" />
    <bpmn:sequenceFlow id="sf12" sourceRef="Task_Ship" targetRef="Task_ShipConf" />
    <bpmn:sequenceFlow id="sf13" sourceRef="Task_ShipConf" targetRef="End_OrderComplete" />
  </bpmn:process>
  <bpmndi:BPMNDiagram id="BPMNDiagram_2">
    <bpmndi:BPMNPlane id="BPMNPlane_2" bpmnElement="Process_PurchaseOrder">
      <bpmndi:BPMNShape id="Start_2_di" bpmnElement="Start_2">
        <dc:Bounds x="160" y="102" width="36" height="36" />
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="Task_CheckStock_di" bpmnElement="Task_CheckStock">
        <dc:Bounds x="250" y="80" width="110" height="80" />
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="XOR_Stock_di" bpmnElement="XOR_Stock" isMarkerVisible="true">
        <dc:Bounds x="415" y="95" width="50" height="50" />
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="Task_OOS_di" bpmnElement="Task_OOS">
        <dc:Bounds x="520" y="200" width="110" height="80" />
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="End_OOS_di" bpmnElement="End_OOS">
        <dc:Bounds x="692" y="222" width="36" height="36" />
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="Task_Payment_di" bpmnElement="Task_Payment">
        <dc:Bounds x="520" y="80" width="110" height="80" />
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="XOR_Payment_di" bpmnElement="XOR_Payment" isMarkerVisible="true">
        <dc:Bounds x="685" y="95" width="50" height="50" />
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="Task_PayFail_di" bpmnElement="Task_PayFail">
        <dc:Bounds x="790" y="200" width="110" height="80" />
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="End_PayFail_di" bpmnElement="End_PayFail">
        <dc:Bounds x="962" y="222" width="36" height="36" />
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="Task_Confirm_di" bpmnElement="Task_Confirm">
        <dc:Bounds x="790" y="80" width="110" height="80" />
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="Task_Prep_di" bpmnElement="Task_Prep">
        <dc:Bounds x="950" y="80" width="110" height="80" />
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="Task_Ship_di" bpmnElement="Task_Ship">
        <dc:Bounds x="1110" y="80" width="100" height="80" />
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="Task_ShipConf_di" bpmnElement="Task_ShipConf">
        <dc:Bounds x="1260" y="80" width="110" height="80" />
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="End_OrderComplete_di" bpmnElement="End_OrderComplete">
        <dc:Bounds x="1432" y="102" width="36" height="36" />
      </bpmndi:BPMNShape>
      <bpmndi:BPMNEdge id="sf1_di" bpmnElement="sf1">
        <di:waypoint x="196" y="120" />
        <di:waypoint x="250" y="120" />
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNEdge id="sf2_di" bpmnElement="sf2">
        <di:waypoint x="360" y="120" />
        <di:waypoint x="415" y="120" />
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNEdge id="sf3_di" bpmnElement="sf3">
        <di:waypoint x="440" y="145" />
        <di:waypoint x="440" y="240" />
        <di:waypoint x="520" y="240" />
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNEdge id="sf4_di" bpmnElement="sf4">
        <di:waypoint x="630" y="240" />
        <di:waypoint x="692" y="240" />
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNEdge id="sf5_di" bpmnElement="sf5">
        <di:waypoint x="465" y="120" />
        <di:waypoint x="520" y="120" />
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNEdge id="sf6_di" bpmnElement="sf6">
        <di:waypoint x="630" y="120" />
        <di:waypoint x="685" y="120" />
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNEdge id="sf7_di" bpmnElement="sf7">
        <di:waypoint x="710" y="145" />
        <di:waypoint x="710" y="240" />
        <di:waypoint x="790" y="240" />
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNEdge id="sf8_di" bpmnElement="sf8">
        <di:waypoint x="900" y="240" />
        <di:waypoint x="962" y="240" />
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNEdge id="sf9_di" bpmnElement="sf9">
        <di:waypoint x="735" y="120" />
        <di:waypoint x="790" y="120" />
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNEdge id="sf10_di" bpmnElement="sf10">
        <di:waypoint x="900" y="120" />
        <di:waypoint x="950" y="120" />
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNEdge id="sf11_di" bpmnElement="sf11">
        <di:waypoint x="1060" y="120" />
        <di:waypoint x="1110" y="120" />
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNEdge id="sf12_di" bpmnElement="sf12">
        <di:waypoint x="1210" y="120" />
        <di:waypoint x="1260" y="120" />
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNEdge id="sf13_di" bpmnElement="sf13">
        <di:waypoint x="1370" y="120" />
        <di:waypoint x="1432" y="120" />
      </bpmndi:BPMNEdge>
    </bpmndi:BPMNPlane>
  </bpmndi:BPMNDiagram>
</bpmn:definitions>""",

    "diagrams/scenario-3-it-service-request.bpmn": """<?xml version="1.0" encoding="UTF-8"?>
<bpmn:definitions xmlns:bpmn="http://www.omg.org/spec/BPMN/20100524/MODEL"
                  xmlns:bpmndi="http://www.omg.org/spec/BPMN/20100524/DI"
                  xmlns:dc="http://www.omg.org/spec/DD/20100524/DC"
                  xmlns:di="http://www.omg.org/spec/DD/20100524/DI"
                  id="Definitions_3"
                  targetNamespace="http://bpmn.io/schema/bpmn">
  <bpmn:process id="Process_ITService" isExecutable="false">
    <bpmn:startEvent id="Start_3" name="IT Problem Reported">
      <bpmn:outgoing>s1</bpmn:outgoing>
    </bpmn:startEvent>
    <bpmn:task id="Task_Reg" name="Register IT Support Request">
      <bpmn:incoming>s1</bpmn:incoming>
      <bpmn:outgoing>s2</bpmn:outgoing>
    </bpmn:task>
    <bpmn:task id="Task_Sev" name="Check Problem Severity">
      <bpmn:incoming>s2</bpmn:incoming>
      <bpmn:outgoing>s3</bpmn:outgoing>
    </bpmn:task>
    <bpmn:exclusiveGateway id="XOR_Sev" name="Severity Level?">
      <bpmn:incoming>s3</bpmn:incoming>
      <bpmn:outgoing>s4</bpmn:outgoing>
      <bpmn:outgoing>s5</bpmn:outgoing>
    </bpmn:exclusiveGateway>
    <bpmn:task id="Task_SuppTech" name="Assign to Support Technician">
      <bpmn:incoming>s4</bpmn:incoming>
      <bpmn:outgoing>s6</bpmn:outgoing>
    </bpmn:task>
    <bpmn:task id="Task_SrTech" name="Assign to Senior Technician">
      <bpmn:incoming>s5</bpmn:incoming>
      <bpmn:outgoing>s7</bpmn:outgoing>
    </bpmn:task>
    <bpmn:exclusiveGateway id="XOR_Merge1">
      <bpmn:incoming>s6</bpmn:incoming>
      <bpmn:incoming>s7</bpmn:incoming>
      <bpmn:outgoing>s8</bpmn:outgoing>
    </bpmn:exclusiveGateway>
    <bpmn:task id="Task_Investigate" name="Investigate Problem">
      <bpmn:incoming>s8</bpmn:incoming>
      <bpmn:outgoing>s9</bpmn:outgoing>
    </bpmn:task>
    <bpmn:exclusiveGateway id="XOR_Res" name="Resolved Internally?">
      <bpmn:incoming>s9</bpmn:incoming>
      <bpmn:outgoing>s10</bpmn:outgoing>
      <bpmn:outgoing>s11</bpmn:outgoing>
    </bpmn:exclusiveGateway>
    <bpmn:task id="Task_Fix" name="Fix Problem">
      <bpmn:incoming>s10</bpmn:incoming>
      <bpmn:outgoing>s12</bpmn:outgoing>
    </bpmn:task>
    <bpmn:task id="Task_Escalate" name="Escalate to External Service Provider">
      <bpmn:incoming>s11</bpmn:incoming>
      <bpmn:outgoing>s13</bpmn:outgoing>
    </bpmn:task>
    <bpmn:exclusiveGateway id="XOR_Merge2">
      <bpmn:incoming>s12</bpmn:incoming>
      <bpmn:incoming>s13</bpmn:incoming>
      <bpmn:outgoing>s14</bpmn:outgoing>
    </bpmn:exclusiveGateway>
    <bpmn:task id="Task_Status" name="Update Request Status">
      <bpmn:incoming>s14</bpmn:incoming>
      <bpmn:outgoing>s15</bpmn:outgoing>
    </bpmn:task>
    <bpmn:task id="Task_NotifyEmp" name="Send Resolution Notification">
      <bpmn:incoming>s15</bpmn:incoming>
      <bpmn:outgoing>s16</bpmn:outgoing>
    </bpmn:task>
    <bpmn:endEvent id="End_IT" name="Request Closed">
      <bpmn:incoming>s16</bpmn:incoming>
    </bpmn:endEvent>
    <bpmn:sequenceFlow id="s1" sourceRef="Start_3" targetRef="Task_Reg" />
    <bpmn:sequenceFlow id="s2" sourceRef="Task_Reg" targetRef="Task_Sev" />
    <bpmn:sequenceFlow id="s3" sourceRef="Task_Sev" targetRef="XOR_Sev" />
    <bpmn:sequenceFlow id="s4" name="Low" sourceRef="XOR_Sev" targetRef="Task_SuppTech" />
    <bpmn:sequenceFlow id="s5" name="High" sourceRef="XOR_Sev" targetRef="Task_SrTech" />
    <bpmn:sequenceFlow id="s6" sourceRef="Task_SuppTech" targetRef="XOR_Merge1" />
    <bpmn:sequenceFlow id="s7" sourceRef="Task_SrTech" targetRef="XOR_Merge1" />
    <bpmn:sequenceFlow id="s8" sourceRef="XOR_Merge1" targetRef="Task_Investigate" />
    <bpmn:sequenceFlow id="s9" sourceRef="Task_Investigate" targetRef="XOR_Res" />
    <bpmn:sequenceFlow id="s10" name="Yes" sourceRef="XOR_Res" targetRef="Task_Fix" />
    <bpmn:sequenceFlow id="s11" name="No" sourceRef="XOR_Res" targetRef="Task_Escalate" />
    <bpmn:sequenceFlow id="s12" sourceRef="Task_Fix" targetRef="XOR_Merge2" />
    <bpmn:sequenceFlow id="s13" sourceRef="Task_Escalate" targetRef="XOR_Merge2" />
    <bpmn:sequenceFlow id="s14" sourceRef="XOR_Merge2" targetRef="Task_Status" />
    <bpmn:sequenceFlow id="s15" sourceRef="Task_Status" targetRef="Task_NotifyEmp" />
    <bpmn:sequenceFlow id="s16" sourceRef="Task_NotifyEmp" targetRef="End_IT" />
  </bpmn:process>
  <bpmndi:BPMNDiagram id="BPMNDiagram_3">
    <bpmndi:BPMNPlane id="BPMNPlane_3" bpmnElement="Process_ITService">
      <bpmndi:BPMNShape id="Start_3_di" bpmnElement="Start_3">
        <dc:Bounds x="152" y="132" width="36" height="36" />
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="Task_Reg_di" bpmnElement="Task_Reg">
        <dc:Bounds x="230" y="110" width="110" height="80" />
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="Task_Sev_di" bpmnElement="Task_Sev">
        <dc:Bounds x="380" y="110" width="110" height="80" />
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="XOR_Sev_di" bpmnElement="XOR_Sev" isMarkerVisible="true">
        <dc:Bounds x="535" y="125" width="50" height="50" />
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="Task_SuppTech_di" bpmnElement="Task_SuppTech">
        <dc:Bounds x="630" y="40" width="120" height="80" />
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="Task_SrTech_di" bpmnElement="Task_SrTech">
        <dc:Bounds x="630" y="180" width="120" height="80" />
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="XOR_Merge1_di" bpmnElement="XOR_Merge1" isMarkerVisible="true">
        <dc:Bounds x="795" y="125" width="50" height="50" />
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="Task_Investigate_di" bpmnElement="Task_Investigate">
        <dc:Bounds x="890" y="110" width="110" height="80" />
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="XOR_Res_di" bpmnElement="XOR_Res" isMarkerVisible="true">
        <dc:Bounds x="1045" y="125" width="50" height="50" />
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="Task_Fix_di" bpmnElement="Task_Fix">
        <dc:Bounds x="1140" y="40" width="110" height="80" />
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="Task_Escalate_di" bpmnElement="Task_Escalate">
        <dc:Bounds x="1140" y="180" width="120" height="80" />
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="XOR_Merge2_di" bpmnElement="XOR_Merge2" isMarkerVisible="true">
        <dc:Bounds x="1305" y="125" width="50" height="50" />
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="Task_Status_di" bpmnElement="Task_Status">
        <dc:Bounds x="1400" y="110" width="110" height="80" />
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="Task_NotifyEmp_di" bpmnElement="Task_NotifyEmp">
        <dc:Bounds x="1550" y="110" width="120" height="80" />
      </bpmndi:BPMNShape>
      <bpmndi:BPMNShape id="End_IT_di" bpmnElement="End_IT">
        <dc:Bounds x="1712" y="132" width="36" height="36" />
      </bpmndi:BPMNShape>
      <bpmndi:BPMNEdge id="s1_di" bpmnElement="s1">
        <di:waypoint x="188" y="150" />
        <di:waypoint x="230" y="150" />
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNEdge id="s2_di" bpmnElement="s2">
        <di:waypoint x="340" y="150" />
        <di:waypoint x="380" y="150" />
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNEdge id="s3_di" bpmnElement="s3">
        <di:waypoint x="490" y="150" />
        <di:waypoint x="535" y="150" />
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNEdge id="s4_di" bpmnElement="s4">
        <di:waypoint x="560" y="125" />
        <di:waypoint x="560" y="80" />
        <di:waypoint x="630" y="80" />
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNEdge id="s5_di" bpmnElement="s5">
        <di:waypoint x="560" y="175" />
        <di:waypoint x="560" y="220" />
        <di:waypoint x="630" y="220" />
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNEdge id="s6_di" bpmnElement="s6">
        <di:waypoint x="750" y="80" />
        <di:waypoint x="820" y="80" />
        <di:waypoint x="820" y="125" />
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNEdge id="s7_di" bpmnElement="s7">
        <di:waypoint x="750" y="220" />
        <di:waypoint x="820" y="220" />
        <di:waypoint x="820" y="175" />
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNEdge id="s8_di" bpmnElement="s8">
        <di:waypoint x="845" y="150" />
        <di:waypoint x="890" y="150" />
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNEdge id="s9_di" bpmnElement="s9">
        <di:waypoint x="1000" y="150" />
        <di:waypoint x="1045" y="150" />
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNEdge id="s10_di" bpmnElement="s10">
        <di:waypoint x="1070" y="125" />
        <di:waypoint x="1070" y="80" />
        <di:waypoint x="1140" y="80" />
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNEdge id="s11_di" bpmnElement="s11">
        <di:waypoint x="1070" y="175" />
        <di:waypoint x="1070" y="220" />
        <di:waypoint x="1140" y="220" />
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNEdge id="s12_di" bpmnElement="s12">
        <di:waypoint x="1250" y="80" />
        <di:waypoint x="1330" y="80" />
        <di:waypoint x="1330" y="125" />
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNEdge id="s13_di" bpmnElement="s13">
        <di:waypoint x="1260" y="220" />
        <di:waypoint x="1330" y="220" />
        <di:waypoint x="1330" y="175" />
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNEdge id="s14_di" bpmnElement="s14">
        <di:waypoint x="1355" y="150" />
        <di:waypoint x="1400" y="150" />
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNEdge id="s15_di" bpmnElement="s15">
        <di:waypoint x="1510" y="150" />
        <di:waypoint x="1550" y="150" />
      </bpmndi:BPMNEdge>
      <bpmndi:BPMNEdge id="s16_di" bpmnElement="s16">
        <di:waypoint x="1670" y="150" />
        <di:waypoint x="1712" y="150" />
      </bpmndi:BPMNEdge>
    </bpmndi:BPMNPlane>
  </bpmndi:BPMNDiagram>
</bpmn:definitions>"""
}

os.makedirs("diagrams", exist_ok=True)
for path, content in scenarios.items():
    with open(path, "w", encoding="utf-8") as f:
        f.write(content.strip())
    print(f"Generated {path}")