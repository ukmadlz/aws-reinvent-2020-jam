suricata_log = {
    "src_ip": "61.178.18.190",
    "alert": {"rev": 3, "action": "allowed", "gid": 1, "signature_id": 2009582,
              "signature": "ET SCAN NMAP -sS window 1024",
              "category": "Attempted Information Leak", "severity": 3},
    "t-pot_hostname": "faintgarbage",
    "dest_ip": "172.31.16.206", "stream": 0, "@version": "1",
    "ip_rep": "known attacker", "proto": "TCP", "host": "d46d1eaa028c",
    "in_iface": "eth0",
    "t-pot_ip_ext": "52.23.224.247", "type": "Suricata", "src_port": 19645,
    "path": "/data/suricata/log/eve.json", "payload_printable": "", "dest_port": 445,
    "t-pot_ip_int": "172.31.16.206"
}

logzio_security = {
    "origin_feeds": [
        "dan.me.uk - Tor tracker"
    ],
    "origin_feeds_num": 1,
    "context": [
        "Malicious IP"
    ],
    "severity": 5,
    "ioc": {
        "malicious_ip": "69.146.146.75"
    }
}

aws_login_log = {
    "eventVersion": "1.05",
    "userIdentity": {
        "type": "IAMUser",
        "principalId": "AIDAIJXPRREIRI4XUSYAY",
        "arn": "arn:aws:iam::486140753397:user/maria.p",
        "accountId": "486140753397",
        "userName": "maria.p"
    },
    "type": "cloudtrail",
    "eventTime": "2019-01-30T12:23:07Z",
    "eventSource": "signin.amazonaws.com",
    "eventName": "ConsoleLogin",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "199.203.204.57",
    "userAgent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
    "responseElements": {
        "ConsoleLogin": "Success"
    },
    "additionalEventData": {
        "LoginTo": "https://console.aws.amazon.com/console/home?nc2=h_ct&src=header-signin&state=hashArgs%23&isauthcode=true",
        "MobileVersion": "No",
        "MFAUsed": "No"
    },
    "eventID": "06011b28-7eb8-4c51-a188-9c749f61169b",
    "eventType": "AwsConsoleSignIn",
    "recipientAccountId": "486140753397"
}
{"process":{"pid":"9414","exe":"/usr/sbin/sshd"},"logzio_codec":"json","@metadata":{"beat":"auditbeat","type":"doc","version":"6.6.1"},"source":{"ip":"199.203.204.57"},"auditd":{"sequence":106,"result":"success","session":"324","data":{"terminal":"ssh","hostname":"199.203.204.57","acct":"ubuntu","op":"PAM:session_open"},"summary":{"object":{"secondary":"199.203.204.57","type":"user-session","primary":"ssh"},"how":"/usr/sbin/sshd","actor":{"primary":"ubuntu","secondary":"ubuntu"}}},"type":"ec2audit","network":{"direction":"incoming"},"tags":["beats-5015","_logzio_codec_json"],"@timestamp":"2019-02-27T08:41:16.138Z","meta":{"cloud":{"availability_zone":"us-east-1b","provider":"ec2","instance_id":"i-0fb1ea7286e0283a9","machine_type":"t2.medium","region":"us-east-1"}},"beat":{"version":"6.6.1","name":"ip-172-31-92-79","hostname":"ip-172-31-92-79"},"event":{"module":"auditd","category":"user-login","type":"user_start","action":"started-session"},"user":{"uid":"0","name_map":{"auid":"ubuntu","uid":"root"},"auid":"1000"}}

ec2ssh_login_log = {
    "type":"ec2ssh",
    "process":{
        "pid":"9408",
        "exe":"/usr/sbin/sshd"
    },
    "logzio_codec":"json",
    "@metadata":{
        "beat":"auditbeat",
        "type":"doc","version":"6.6.1"
    },
    "source_ip":"199.203.204.57",
    "auditd":{
           "session":"unset",
            "data":{
               "hostname":"199.203.204.57",
               "op":"PAM:bad_ident",
               "terminal":"ssh"
           },
           "summary":{
               "actor":{
                   "primary":"unset","secondary":"root"
                },
                "object":{
                    "primary":"ssh",
                    "secondary":"199.203.204.57",
                    "type":"user-session"
                },
                "how":"/usr/sbin/sshd"
           },
           "sequence":96,
           "result":"fail"
    },
    "network":{
        "direction":"incoming"
    },
    "tags":["beats-5015","_logzio_codec_json"],
    "meta":{
        "cloud":{
            "machine_type":"t2.medium",
            "region":"us-east-1",
            "availability_zone":"us-east-1b",
            "provider":"ec2",
            "instance_id":"i-0fb1eaaa86e0283a9"
        }
    },
    "beat":{
        "name":"ip-172-31-92-88",
        "hostname":"ip-172-31-92-88",
        "version":"6.6.1"
    },
    "event":{
        "category":"user-login",
        "type":"user_err",
        "action":"error",
        "module":"auditd"
    },
    "user":{
        "name_map":{
            "uid":"root"
        },
        "uid":"0",
        "auid":"unset"
    }
}

s3_get_object_log = {
    "eventVersion": "1.05",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AROAI57PZC54LOHRAY7QC:test1",
        "arn": "arn:aws:sts::891625686292:assumed-role/test1-roles/test1",
        "accountId": "891625686292",
        "accessKeyId": "ASIA47GIIIUKNFMTL6SC",
        "userName": "test1-roles",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AROAI57PZC54LOHRAY7QC",
                "arn": "arn:aws:iam::891625686292:role/service-role/test1-roles",
                "accountId": "891625686292"
            },
            "attributes": {
                "creationDate": "2019-02-13T09:08:06Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "type": "cloudtrail",
    "eventTime": "2019-02-13T09:09:34Z",
    "eventSource": "s3.amazonaws.com",
    "eventName": "GetObject",
    "awsRegion": "us-east-2",
    "sourceIPAddress": "194.29.32.132",
    "userAgent": "[PostmanRuntime/7.6.0]",
    "requestParameters": {
        "bucketName": "daniel-bucket-123",
        "Host": "daniel-bucket-123.s3.amazonaws.com",
        "key": "my_file.txt"
    },
    "additionalEventData": {
        "SignatureVersion": "SigV4",
        "CipherSuite": "ECDHE-RSA-AES128-GCM-SHA256",
        "AuthenticationMethod": "AuthHeader",
        "x-amz-id-2": "kdZAMiv+ESzVBoKy9dB9mjduh3AakME28YL1OSBKtZ04TLmJ0EQMwEntVqp1FvFlZiZ0qmV2nl8="
    },
    "requestID": "59A83704DBA0D728",
    "eventID": "996ef836-acfb-4459-b055-08b1c1a74376",
    "readOnly": True,
    "resources":
        {
            "type": "AWS::S3::Object",
            "ARN": "arn:aws:s3:::daniel-bucket-123/my_file.txt"
        },
    "eventType": "AwsApiCall",
    "recipientAccountId": "891625686292"
}

s3_delete_object_log = {
    "eventVersion": "1.05",
    "userIdentity": {
        "type": "AssumedRole",
        "principalId": "AROAI57PZC54LOHRAY7QC:test1",
        "arn": "arn:aws:sts::891625686292:assumed-role/test1-roles/test1",
        "accountId": "891625686292",
        "accessKeyId": "ASIA48GIIIUKNFMTL6SC",
        "userName": "test1-roles",
        "sessionContext": {
            "sessionIssuer": {
                "type": "Role",
                "principalId": "AROAI57PZC54LOHRAY7QC",
                "arn": "arn:aws:iam::891625686292:role/service-role/test1-roles",
                "accountId": "891625686292"
            },
            "attributes": {
                "creationDate": "2019-02-13T09:08:06Z",
                "mfaAuthenticated": "false"
            }
        }
    },
    "type": "cloudtrail",
    "eventTime": "2019-02-13T09:09:48Z",
    "eventSource": "s3.amazonaws.com",
    "eventName": "DeleteObject",
    "awsRegion": "us-east-2",
    "sourceIPAddress": "81.29.32.132",
    "userAgent": "[PostmanRuntime/7.6.0]",
    "requestParameters": {
        "bucketName": "daniel-bucket-123",
        "Host": "daniel-bucket-123.s3.amazonaws.com",
        "key": "my_file.txt"
    },
    "additionalEventData": {
        "SignatureVersion": "SigV4",
        "CipherSuite": "ECDHE-RSA-AES128-GCM-SHA256",
        "AuthenticationMethod": "AuthHeader",
        "x-amz-id-2": "9vQ/IzaajwtVmBN62ZATwOMc1065ak48lW9gTcZLi6J1jkzJ6hTRcgdTpsIVMZFWJCteYQScVE0="
    },
    "requestID": "10B77555108D4B70",
    "eventID": "e17ea85b-888d-4df3-9a19-c45846598a72",
    "readOnly": False,
    "resources": [
        {
            "type": "AWS::S3::Object",
            "ARN": "arn:aws:s3:::daniel-bucket-123/my_file.txt"
        },
        {
            "accountId": "891625686292",
            "type": "AWS::S3::Bucket",
            "ARN": "arn:aws:s3:::daniel-bucket-123"
        }
    ],
    "eventType": "AwsApiCall",
    "recipientAccountId": "8916256862.92"
}

s3_delete_bucket_log = {
    "eventVersion": "1.05",
    "userIdentity": {
        "type": "IAMUser",
        "principalId": "AIDAIJXPRREIRI4XUSYAY",
        "arn": "arn:aws:iam::486140753397:user/maria.p",
        "accountId": "486140753397",
        "accessKeyId": "ASIAXCMB7GX2RRPWFJDO",
        "userName": "maria.p",
        "sessionContext": {
            "attributes": {
                "mfaAuthenticated": "false",
                "creationDate": "2019-02-12T07:50:48Z"
            }
        },
        "invokedBy": "signin.amazonaws.com"
    },
    "type": "cloudtrail",
    "eventTime": "2019-02-12T09:45:46Z",
    "eventSource": "s3.amazonaws.com",
    "eventName": "DeleteBucket",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "199.203.204.57",
    "userAgent": "signin.amazonaws.com",
    "requestParameters": {
        "host": [
            "s3.amazonaws.com"
        ],
        "bucketName": "s3testdeletebucket"
    },
    "additionalEventData": {
        "SignatureVersion": "SigV4",
        "CipherSuite": "ECDHE-RSA-AES128-SHA",
        "AuthenticationMethod": "AuthHeader",
        "vpcEndpointId": "vpce-38d25651"
    },
    "requestID": "5D9B06FB06D414A1",
    "eventID": "f0473ac5-6463-4963-8c9f-caf96e5c5410",
    "eventType": "AwsApiCall",
    "recipientAccountId": "486140753397",
    "vpcEndpointId": "vpce-38d25651"
}

s3_delete_security_group_log = {
    "eventVersion": "1.05",
    "userIdentity": {
        "type": "IAMUser",
        "principalId": "AIDAIJXPRREIRI4XUSYAY",
        "arn": "arn:aws:iam::486140753397:user/marian.t",
        "accountId": "486140222397",
        "accessKeyId": "ASIAXCMB7GX2RRPWFJWW",
        "userName": "mariana.t",
        "sessionContext": {
            "attributes": {
                "mfaAuthenticated": "false",
                "creationDate": "2019-02-12T07:50:48Z"
            }
        },
        "invokedBy": "signin.amazonaws.com"
    },
    "type": "cloudtrail",
    "eventTime": "2019-02-12T09:45:46Z",
    "eventSource": "s3.amazonaws.com",
    "eventName": "DeleteSecurityGroup",
    "awsRegion": "us-east-1",
    "sourceIPAddress": "199.203.204.57",
    "userAgent": "signin.amazonaws.com",
    "requestParameters": {
        "host": [
            "s3.amazonaws.com"
        ],
    },
    "additionalEventData": {
        "SignatureVersion": "SigV4",
        "CipherSuite": "ECDHE-RSA-AES128-SHA",
        "AuthenticationMethod": "AuthHeader",
        "vpcEndpointId": "vpce-38d25651"
    },
    "requestID": "5D9B06FB06D414A1",
    "eventID": "f0473ac5-6463-4963-8c9f-caf96e5c5410",
    "eventType": "AwsApiCall",
    "recipientAccountId": "486140222397",
    "vpcEndpointId": "vpce-38d25651"
}

AD_winevenlog_login_success_log = {
    "process_id": 600,
    "keywords": [
        "Audit Success"
    ],
    "logzio_codec": "plain",
    "record_number": "411284",
    "event_data": {
        "TargetLinkedLogonId": "0x0",
        "LmPackageName": "-",
        "ImpersonationLevel": "%%1833",
        "ProcessId": "0x0",
        "SubjectUserSid": "S-1-0-0",
        "TargetLogonId": "0x1bc9951",
        "TargetOutboundUserName": "-",
        "WorkstationName": "-",
        "LogonType": "3",
        "RestrictedAdminMode": "-",
        "TransmittedServices": "-",
        "LogonProcessName": "Kerberos",
        "LogonGuid": "{738130F9-860F-CCCC-A775-2BD0BFC2DB14}",
        "SubjectDomainName": "-",
        "TargetUserName": "EC2AMAZ-FNVOMDK$",
        "TargetDomainName": "LOGZIO.INTERNAL",
        "IpPort": "54064",
        "VirtualAccount": "%%1843",
        "SubjectUserName": "-",
        "ElevatedToken": "%%1842",
        "TargetOutboundDomainName": "-",
        "ProcessName": "-",
        "AuthenticationPackageName": "Kerberos",
        "KeyLength": "0",
        "SubjectLogonId": "0x0",
        "IpAddress": "::1",
        "TargetUserSid": "S-1-5-18"
    },
    "opcode": "Info",
    "type": "wineventlog",
    "thread_id": 4092,
    "provider_guid": "{54849625-5478-4994-A5BA-3E3B0328C30D}",
    "beat": {
        "hostname": "EC2AMAZ-FNVOMDK",
        "version": "6.5.4",
        "name": "EC2AMAZ-FNVOMDK"
    },
    "_logzio_insights": [
        "2385c2b3c9361e6480e2ad8cb2c129e8ab82b241"
    ],
    "source_name": "Microsoft-Windows-Security-Auditing",
    "computer_name": "EC2AMAZ-FNVOMDK.logzio.internal",
    "level": "Information",
    "log_name": "Security",
    "@metadata": {
        "beat": "winlogbeat",
        "type": "doc",
        "version": "6.5.4"
    },
    "message": "An account was successfully logged on.\n\nSubject:\n\tSecurity ID:\t\tS-1-0-0\n\tAccount Name:\t\t-\n\tAccount Domain:\t\t-\n\tLogon ID:\t\t0x0\n\nLogon Information:\n\tLogon Type:\t\t3\n\tRestricted Admin Mode:\t-\n\tVirtual Account:\t\tNo\n\tElevated Token:\t\tYes\n\nImpersonation Level:\t\tImpersonation\n\nNew Logon:\n\tSecurity ID:\t\tS-1-5-18\n\tAccount Name:\t\tEC2AMAZ-FNVOMDK$\n\tAccount Domain:\t\tLOGZIO.INTERNAL\n\tLogon ID:\t\t0x1BC9951\n\tLinked Logon ID:\t\t0x0\n\tNetwork Account Name:\t-\n\tNetwork Account Domain:\t-\n\tLogon GUID:\t\t{738130F9-860F-CDA9-A775-2BD0BFC2DB14}\n\nProcess Information:\n\tProcess ID:\t\t0x0\n\tProcess Name:\t\t-\n\nNetwork Information:\n\tWorkstation Name:\t-\n\tSource Network Address:\t::1\n\tSource Port:\t\t54064\n\nDetailed Authentication Information:\n\tLogon Process:\t\tKerberos\n\tAuthentication Package:\tKerberos\n\tTransited Services:\t-\n\tPackage Name (NTLM only):\t-\n\tKey Length:\t\t0\n\nThis event is generated when a logon session is created. It is generated on the computer that was accessed.\n\nThe subject fields indicate the account on the local system which requested the logon. This is most commonly a service such as the Server service, or a local process such as Winlogon.exe or Services.exe.\n\nThe logon type field indicates the kind of logon that occurred. The most common types are 2 (interactive) and 3 (network).\n\nThe New Logon fields indicate the account for whom the new logon was created, i.e. the account that was logged on.\n\nThe network fields indicate where a remote logon request originated. Workstation name is not always available and may be left blank in some cases.\n\nThe impersonation level field indicates the extent to which a process in the logon session can impersonate.\n\nThe authentication information fields provide detailed information about this specific logon request.\n\t- Logon GUID is a unique identifier that can be used to correlate this event with a KDC event.\n\t- Transited services indicate which intermediate services have participated in this logon request.\n\t- Package name indicates which sub-protocol was used among the NTLM protocols.\n\t- Key length indicates the length of the generated session key. This will be 0 if no session key was requested.",
    "version": 2,
    "tags": [
        "beats-5015"
    ],
    "event_id": 4624,
    "task": "Logon",
    "meta": {
        "cloud": {
            "instance_id": "i-06fb7554bfff258bd",
            "machine_type": "t3.medium",
            "region": "us-east-1",
            "availability_zone": "us-east-1a",
            "provider": "ec2"
        }
    }
}

AD_winevenlog_login_fail_log = {
    "process_id": 536,
    "keywords": [
        "Audit Failure"
    ],
    "logzio_codec": "json",
    "record_number": "599142",
    "event_data": {
        "TargetUserSid": "S-1-0-0",
        "LogonType": "3",
        "ProcessId": "0x0",
        "FailureReason": "%%2313",
        "LogonProcessName": "NtLmSsp ",
        "AuthenticationPackageName": "NTLM",
        "TransmittedServices": "-",
        "KeyLength": "0",
        "SubjectDomainName": "-",
        "IpPort": "-",
        "LmPackageName": "-",
        "IpAddress": "-",
        "ProcessName": "-",
        "SubStatus": "0xc0000064",
        "SubjectUserName": "-",
        "TargetUserName": "ADMIN",
        "Status": "0xc000006d",
        "SubjectUserSid": "S-1-0-0",
        "SubjectLogonId": "0x0",
        "WorkstationName": "-"
    },
    "type": "wineventlog",
    "opcode": "Info",
    "thread_id": 1448,
    "provider_guid": "{54849625-5478-4994-A5BA-3E3B0328C30D}",
    "beat": {
        "name": "logzdemowin1",
        "hostname": "logzdemowin1",
        "version": "6.6.0"
    },
    "source_name": "Microsoft-Windows-Security-Auditing",
    "computer_name": "logzdemowin1",
    "log_name": "Security",
    "level": "Information",
    "@metadata": {
        "beat": "winlogbeat",
        "type": "doc",
        "version": "6.6.0"
    },
    "message": "An account failed to log on.\n\nSubject:\n\tSecurity ID:\t\tS-1-0-0\n\tAccount Name:\t\t-\n\tAccount Domain:\t\t-\n\tLogon ID:\t\t0x0\n\nLogon Type:\t\t\t3\n\nAccount For Which Logon Failed:\n\tSecurity ID:\t\tS-1-0-0\n\tAccount Name:\t\tADMIN\n\tAccount Domain:\t\t\n\nFailure Information:\n\tFailure Reason:\t\tUnknown user name or bad password.\n\tStatus:\t\t\t0xC000006D\n\tSub Status:\t\t0xC0000064\n\nProcess Information:\n\tCaller Process ID:\t0x0\n\tCaller Process Name:\t-\n\nNetwork Information:\n\tWorkstation Name:\t-\n\tSource Network Address:\t-\n\tSource Port:\t\t-\n\nDetailed Authentication Information:\n\tLogon Process:\t\tNtLmSsp \n\tAuthentication Package:\tNTLM\n\tTransited Services:\t-\n\tPackage Name (NTLM only):\t-\n\tKey Length:\t\t0\n\nThis event is generated when a logon request fails. It is generated on the computer where access was attempted.\n\nThe Subject fields indicate the account on the local system which requested the logon. This is most commonly a service such as the Server service, or a local process such as Winlogon.exe or Services.exe.\n\nThe Logon Type field indicates the kind of logon that was requested. The most common types are 2 (interactive) and 3 (network).\n\nThe Process Information fields indicate which account and process on the system requested the logon.\n\nThe Network Information fields indicate where a remote logon request originated. Workstation name is not always available and may be left blank in some cases.\n\nThe authentication information fields provide detailed information about this specific logon request.\n\t- Transited services indicate which intermediate services have participated in this logon request.\n\t- Package name indicates which sub-protocol was used among the NTLM protocols.\n\t- Key length indicates the length of the generated session key. This will be 0 if no session key was requested.",
    "tags": [
        "beats-5015",
        "_logzio_codec_json",
        "_jsonparsefailure"
    ],
    "task": "Logon",
    "event_id": 4625,
    "_logzio_pattern": 154764,
    "meta": {
        "cloud": {
            "instance_id": "53fbae52-4325-4a85-80e3-cb82c4d684be",
            "instance_name": "logzdemowin1",
            "machine_type": "Standard_DS1_v2",
            "region": "westus",
            "provider": "az"
        }
    }
}

wazuh_bf_log = {
    "predecoder": {
        "hostname": "ip-172-31-61-49",
        "program_name": "sshd",
    },
    "agent": {
        "ip": "1.1.1.1",
        "name": "ip-172-31-61-49",
        "id": "010"
    },
    "previous_output": "Feb 16 03:42:57 ip-172-31-61-49 sshd[24401]: Invalid user deploy from 54.39.146.94\nFeb 16 03:42:54 ip-172-31-61-49 sshd[24399]: Invalid user zabbix from 54.39.146.94\nFeb 16 03:42:52 ip-172-31-61-49 sshd[24385]: Invalid user zabbix from 54.39.146.94\nFeb 16 03:42:49 ip-172-31-61-49 sshd[24383]: Invalid user app from 54.39.146.94\nFeb 16 03:42:47 ip-172-31-61-49 sshd[24381]: Invalid user app from 54.39.146.94\nFeb 16 03:42:44 ip-172-31-61-49 sshd[24379]: Invalid user jenkins from 54.39.146.94\nFeb 16 03:42:42 ip-172-31-61-49 sshd[24377]: Invalid user jenkins from 54.39.146.94",
    "data": {
        "srcuser": "john.doe",
        "srcip": "1.1.1.1"
    },
    "logzio_codec": "json",
    "manager": {
        "name": "ip-172-31-21-163"
    },
    "log": "",
    "@metadata": {
        "beat": "filebeat",
        "type": "doc",
        "version": "6.5.0"
    },
    "rule": {
        "firedtimes": 11,
        "mail": False,
        "level": 10,
        "pci_dss": [
            "11.4",
            "10.2.4",
            "10.2.5"
        ],
        "groups": [
            "syslog",
            "sshd",
            "authentication_failures"
        ],
        "description": "sshd: brute force trying to get access to the system.",
        "id": "5712",
        "frequency": 6,
        "gdpr": [
            "IV_35.7.d",
            "IV_32.2"
        ]
    },
    "prospector": {
        "type": "log"
    },
    "source": "/var/ossec/logs/alerts/alerts.json",
    "decoder": {
        "parent": "sshd",
        "name": "sshd"
    },
    "type": "wazuh",
    "full_log": "Feb 16 03:43:00 ip-172-31-61-49 sshd[24403]: Invalid user  from srcip",
    "tags": [
        "beats-5015",
        "_logzio_codec_json"
    ],
    "input": {
        "type": "log"
    },
    "beat": {
        "hostname": "ip-172-31-21-163",
        "name": "ip-172-31-21-163",
        "version": "6.5.0"
    },
    "location": "/var/log/auth.log",
    "id": "1550288580.344433"
}

#
# Logs for PerimeterX Scenarion
#

# 83.149.9.216 - - [17/May/2015:10:05:03 +0000] "GET /product/12345 HTTP/1.1" 200 203023 "https://www.buymyproducts.com/search" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36"
# 68.56.222.154 - - [21/Feb/2019:07:30:51 +0000] "POST /api/signin HTTP/1.1" 200 203023 "https://www.buymyproducts.com/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"    
apache_get_log = {
        "uri": "https://www.buymyproducts.com/search",
        "referrer": "/product/12345 HTTP/1.1",
        "http_method": "GET",
        "status_code": "200",
        "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36",
        "ip": "83.149.9.216",
        "event_type": "apache",
        "type": "apache_access"
}

apache_post_log = {
        "uri": "https://www.buymyproducts.com/",
        "referrer": "/api/signin HTTP/1.1",
        "http_method": "POST",
        "status_code": "200",
        "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36",
        "ip": "83.149.9.216",
        "event_type": "apache",
        "type": "apache_access"
}

px_block_log = {
        "event_type": "px_block",
        "block_score": 100,
        "true_ip": "103.3.77.99",
        "client_ip": "103.3.77.99",
        "domain": "www.buymyproducts.com",
        "path": "/api/signin",
        "user_agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36",
        "px_vid": "", "px_client_uuid": "0f5b3321-63ce-40f7-a853-fdf9b3ced9cb",
        "type": "PerimeterX"
}
