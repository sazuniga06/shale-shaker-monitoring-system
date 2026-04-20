# SCADA Integration and Monitoring Logic

The system is designed to integrate with industrial SCADA platforms using the following supervisory logic:

## Supervisory Tags
| Tag Name | Description | Data Type |
| :--- | :--- | :--- |
| RMS_WINDOW | Real-time RMS acceleration value | Float |
| BASELINE | Established reference value | Float |
| DELTA_PERCENT | Relative shift vs baseline | Float |
| ALARM_STATUS | Binary fault indicator | Boolean |

## Monitoring Rule
The SCADA system triggers a high-priority alarm on the HMI if `DELTA_PERCENT` exceeds 5% for a continuous duration of 15 seconds (equivalent to 3 consecutive 5-second analytical windows). This prevents false triggers from transient mechanical shocks during drilling operations.
