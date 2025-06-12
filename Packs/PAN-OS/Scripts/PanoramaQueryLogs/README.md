To query logs in Panorama.

## Script Data

---

| **Name** | **Description** |
| --- | --- |
| Script Type | python3 |
| Tags | Utilities |
| Cortex XSOAR Version | 6.1.0 |

## Inputs

---

| **Argument Name** | **Description** |
| --- | --- |
| log-type | The log type. Can be: threat, traffic, wildfire, url, data, corr, system, decryption. |
| query | The query string by which to match criteria for the logs. This is similar to the query provided in the web interface under the Monitor tab when viewing the logs. Do not use the query argument in combination with the following arguments: time-generated, time-generated-after, addr-src, addr-dst, zone-src, zone-dst, action, port-dst, rule, url, filedigest. |
| time-generated | The time the log was generated from the timestamp and prior to it. For example "2019/08/11 01:10:44, will get logs before the specified date. |
| time-generated-after | The time the log was generated from the timestamp and prior to it. For example "2019/08/11 01:10:44", will get logs after the specified date. |
| addr-src | The source IP address. |
| addr-dst | The destination IP address. |
| ip | The source or destination IP address. |
| zone-src | The source zone. |
| zone-dst | The destination source. |
| action | The rule action. |
| port-dst | The destination port. |
| rule | The rule name, for example "Allow all outbound". |
| url | The URL, for example "safebrowsing.googleapis.com". |
| filedigest | The file hash (for WildFire logs only). |
| number_of_logs | The maximum number of logs to retrieve. If empty, the default is 100. The maximum is 5,000. |
| polling | Whether to use polling. Default is 'false'. |
| timeout | The timeout (in seconds) when polling. Default is 120. |
| interval_in_seconds | The interval (in seconds) when polling. Default is 10. |
| show-detail | Whether to show only `after-change-preview`, and `before-change-preview`, or get full data for it. The full data are under the fields `after-change-detail`, and `before-change-detail`. Default is 'no'. |

## Outputs

---

| **Path** | **Description** | **Type** |
| --- | --- | --- |
| Panorama.Monitor.JobID | The job ID of the logs query. | String |
| Panorama.Monitor.Status | The status of the logs query. | String |
| Panorama.Monitor.Message | The message of the logs query. | String |
| Panorama.Monitor.Logs.Action | The action taken for the session. Can be "alert", "allow", "deny", "drop", "drop-all-packets", "reset-client", "reset-server", "reset-both", or "block-url". | String |
| Panorama.Monitor.Logs.Application | The application associated with the session. | String |
| Panorama.Monitor.Logs.Category | The URL category of the URL subtype. For WildFire subtype, it is the verdict on the file, and can be either "malicious", "phishing", "grayware", or "benign". For other subtypes, the value is "any". | String |
| Panorama.Monitor.Logs.DeviceName | The hostname of the firewall on which the session was logged. | String |
| Panorama.Monitor.Logs.DestinationAddress | The original session destination IP address. | String |
| Panorama.Monitor.Logs.DestinationUser | The username of the user to which the session was destined. | String |
| Panorama.Monitor.Logs.DestinationCountry | The destination country or internal region for private addresses. Maximum length is 32 bytes. | String |
| Panorama.Monitor.Logs.DestinationPort | The destination port utilized by the session. | String |
| Panorama.Monitor.Logs.FileDigest | Only for the WildFire subtype, all other types do not use this field. The filedigest string shows the binary hash of the file sent to be analyzed by the WildFire service. | String |
| Panorama.Monitor.Logs.FileName | File name or file type when the subtype is file. File name when the subtype is virus. File name when the subtype is wildfire-virus. File name when the subtype is wildfire. | String |
| Panorama.Monitor.Logs.FileType | Only for the WildFire subtype, all other types do not use this field. Specifies the type of file that the firewall forwarded for WildFire analysis. | String |
| Panorama.Monitor.Logs.FromZone | The zone from which the session was sourced. | String |
| Panorama.Monitor.Logs.URLOrFilename | The actual URL when the subtype is url. The file name or file type when the subtype is file. The file name when the subtype is virus. The file name when the subtype is wildfire-virus. The file name when the subtype is wildfire. The URL or file name when the subtype is vulnerability (if applicable). | String |
| Panorama.Monitor.Logs.NATDestinationIP | The post-NAT destination IP address if destination NAT was performed. | String |
| Panorama.Monitor.Logs.NATDestinationPort | The post-NAT destination port. | String |
| Panorama.Monitor.Logs.NATSourceIP | The post-NAT source IP address if source NAT was performed. | String |
| Panorama.Monitor.Logs.NATSourcePort | The post-NAT source port. | String |
| Panorama.Monitor.Logs.PCAPid | The packet capture (pcap) ID is a 64 bit unsigned integral denoting an ID to correlate threat pcap files with extended pcaps taken as a part of that flow. All threat logs will contain either a pcap_id of 0 (no associated pcap), or an ID referencing the extended pcap file. | String |
| Panorama.Monitor.Logs.IPProt | The IP protocol associated with the session. | String |