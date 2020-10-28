ad_4624_logon_success_log = {
	"process_id": 596,
	"logzio_codec": "plain",
	"event_data": {
		"TransmittedServices": "-",
		"SubjectLogonId": "0x3e7",
		"SubjectDomainName": "ORGANIZATION",
		"TargetUserName": "RANDOMIZE",
		"LogonGuid": "{088F0999-4C49-4C79-ADF1-F2840EF7B1CE}",
		"IpPort": "0",
		"ElevatedToken": "%%1822",
		"VirtualAccount": "%%1822",
		"IpAddress": "RANDOMIZE",
		"SubjectUserName": "EC2AMAZ-AEGIACD$",
		"ImpersonationLevel": "%%1823",
		"TargetOutboundDomainName": "-",
		"TargetUserSid": "S-1-5-21-1282426543-1088070111-3804447329-1106",
		"KeyLength": "0",
		"LmPackageName": "-",
		"TargetOutboundUserName": "-",
		"ProcessName": "C:\\Windows\\System32\\svchost.exe",
		"LogonProcessName": "User32 ",
		"WorkstationName": "EC2AMAZ-AEGIACD",
		"TargetLogonId": "0x9e8c4c7",
		"LogonType": "10",
		"ProcessId": "0x48",
		"SubjectUserSid": "S-1-5-19",
		"TargetLinkedLogonId": "0x9e7c4d8",
		"AuthenticationPackageName": "Negotiate",
		"TargetDomainName": "ORGANIZATION",
		"RestrictedAdminMode": "%%1843"
	},
	"type": "wineventlog",
	"opcode": "Info",
	"thread_id": 6776,
	"provider_guid": "{54849625-5478-4994-A5BA-3E3B0328C30D}",
	"beat": {
		"hostname": "EC2AMAZ-AEGIACD",
		"version": "6.5.4",
		"name": "EC2AMAZ-AEGIACD"
	},
	"activity_id": "{175BA43A-D733-0000-48A4-5B1733D7D401}",
	"source_name": "Microsoft-Windows-Security-Auditing",
	"computer_name": "EC2AMAZ - AEGIACD.organization.internal",
	"log_name": "Security",
	"level": "Information",
	"@metadata": {
		"beat": "winlogbeat",
		"type": "doc",
		"version": "6.5.4"
	},
	"event_id_description": "An account was successfully logged on",
	"event_id": 4624,
	"task": "Logon",
	"meta": {
		"cloud": {
			"instance_id": "i-06fb7554bfff258bd",
			"machine_type": "t3.medium",
			"region": "us-east-2",
			"availability_zone": "us-east-2a",
			"provider": "ec2"
		}
	}
}

#
#   event_id: 4625
#
#   Status and SubStatus
#            for example:
#                          "SubStatus": "0xc000006a"
#                          Description is: "user name is correct but the password is wrong"
#
#  0xC0000064	user name does not exist
#  0xC000006A	user name is correct but the password is wrong
#  0xC0000234	user is currently locked out
#  0xC0000072	account is currently disabled
#  0xC000006F	user tried to logon outside his day of week or time of day restrictions
#  0xC0000070	workstation restriction, or Authentication Policy Silo violation (look for event ID 4820 on domain controller)
#  0xC0000193	account expiration
#  0xC0000071	expired password
#  0xC0000133	clocks between DC and other computer too far out of sync
#  0xC0000224	user is required to change password at next logon
#  0xC0000225	evidently a bug in Windows and not a risk
#  0xc000015b	The user has not been granted
#
ad_4625_logon_failed_log = {
	"process_id": "596",
	"keywords": [
		"Audit Failure"
	],
	"logzio_codec": "plain",
	"record_number": "970554",
	"event_data": {
		"ProcessName": "-",
		"LmPackageName": "-",
		"KeyLength": "0",
		"ProcessId": "0x0",
		"SubjectLogonId": "0x0",
		"TargetUserSid": "S-1-0-0",
		"IpPort": "0",
		"TargetDomainName": "organization",
		"Status": "0xc000006d",
		"SubjectUserSid": "S-1-0-0",
		"IpAddress": "1.1.1.1",
		"LogonType": "3",
		"AuthenticationPackageName": "NTLM",
		"WorkstationName": "ec2-54-144-39-189.compute-1.amazonaws.com",
		"LogonProcessName": "NtLmSsp ",
		"TargetUserName": "RANDOMIZE",
		"FailureReason": "%%2313",
		"SubjectUserName": "-",
		"SubjectDomainName": "-",
		"SubStatus": "0xc000006a",
		"TransmittedServices": "-"
	},
	"opcode": "Info",
	"type": "wineventlog",
	"thread_id": 6320,
	"provider_guid": "{54849625-5478-4994-A5BA-3E3B0328C30D}",
	"beat": {
		"hostname": "EC2AMAZ-AEGIACD",
		"version": "6.5.4",
		"name": "EC2AMAZ-AEGIACD"
	},
	"source_name": "Microsoft-Windows-Security-Auditing",
	"computer_name": "EC2AMAZ-AEGIACD.organization.internal",
	"log_name": "Security",
	"level": "Information",
	"@metadata": {
		"beat": "winlogbeat",
		"type": "doc",
		"version": "6.5.4"
	},
	"tags": [
		"beats-5015"
	],
	"event_id": 4625,
	"task": "Logon",
	"meta": {
		"cloud": {
			"availability_zone": "eu-west-2b",
			"provider": "ec2",
			"instance_id": "i-06fb7554bfff258bd",
			"machine_type": "t3.medium",
			"region": "eu-west-2b"
		}
	}
}

ad_4720_account_created_log = {
	"process_id": 596,
	"keywords": [
		"Audit Success"
	],
	"logzio_codec": "plain",
	"event_data": {
		"AccountExpires": "%%1794",
		"PrivilegeList": "-",
		"AllowedToDelegateTo": "-",
		"UserWorkstations": "-",
		"SidHistory": "-",
		"LogonHours": "%%1793",
		"HomePath": "-",
		"PrimaryGroupId": "513",
		"UserAccountControl": "\n\t\t%%2080\n\t\t%%2084",
		"SubjectLogonId": "0x1b2f3af",
		"HomeDirectory": "-",
		"NewUacValue": "0x11",
		"SubjectDomainName": "organization",
		"DisplayName": "RANDOMIZE",
		"OldUacValue": "0x0",
		"SubjectUserSid": "S-1-5-21-1282426543-1088070111-3805647329-1104",
		"UserParameters": "-",
		"TargetUserName": "RANDOMIZE",
		"UserPrincipalName": "-",
		"PasswordLastSet": "%%1794",
		"SubjectUserName": "RANDOMIZE / administrator",
		"TargetSid": "S-1-5-21-1282426543-1088070111-3805647329-1135",
		"SamAccountName": "RANDOMIZE(same as TargetUserName)",
		"ScriptPath": "-",
		"TargetDomainName": "organization",
		"ProfilePath": "-"
	},
	"opcode": "Info",
	"type": "wineventlog",
	"thread_id": 6468,
	"provider_guid": "{54849625-5478-4994-A5BA-3E3B0328C30D}",
	"beat": {
		"version": "6.5.4",
		"name": "EC2AMAZ-AEGIACD",
		"hostname": "EC2AMAZ-AEGIACD"
	},
	"source_name": "Microsoft-Windows-Security-Auditing",
	"computer_name": "EC2AMAZ - AEGIACD.organization.internal",
	"log_name": "Security",
	"level": "Information",
	"@metadata": {
		"beat": "winlogbeat",
		"type": "doc",
		"version": "6.5.4"
	},
	"event_id": 4720,
	"task": "User Account Management",
	"meta": {
		"cloud": {
			"instance_id": "i-06fb7554bfff258bd",
			"machine_type": "t3.medium",
			"region": "us-east-2",
			"availability_zone": "us-east-2a",
			"provider": "ec2"
		}
	}
}

ad_4722_account_enabled_log = {
	"process_id": 596,
	"keywords": [
		"Audit Success"
	],
	"logzio_codec": "plain",
	"event_data": {
		"SubjectDomainName": "organization",
		"SubjectLogonId": "0x1b2f3af",
		"TargetUserName": "RANDOMIZER",
		"TargetDomainName": "organization",
		"TargetSid": "S-1-5-21-1282426543-1088070111-3805647329-1125",
		"SubjectUserSid": "S-1-5-21-1282426543-1088070111-3805647329-1104",
		"SubjectUserName": "RANDOMIZE / administrator"
	},
	"opcode": "Info",
	"type": "wineventlog",
	"thread_id": 1900,
	"provider_guid": "{54849625-5478-4994-A5BA-3E3B0328C30D}",
	"beat": {
		"name": "EC2AMAZ-AEGIACD",
		"hostname": "EC2AMAZ-AEGIACD",
		"version": "6.5.4"
	},
	"source_name": "Microsoft-Windows-Security-Auditing",
	"computer_name": "EC2AMAZ - AEGIACD.organization.internal",
	"level": "Information",
	"log_name": "Security",
	"@metadata": {
		"beat": "winlogbeat",
		"type": "doc",
		"version": "6.5.4"
	},
	"task": "User Account Management",
	"event_id": 4722,
	"meta": {
		"cloud": {
			"instance_id": "i-06fb7554bfff258bd",
			"machine_type": "t3.medium",
			"region": "us-east-2",
			"availability_zone": "us-east-2a",
			"provider": "ec2"
		}
	}
}

ad_4725_account_disabled_log = {
	"process_id": 596,
	"logzio_codec": "plain",
	"keywords": [
		"Audit Success"
	],
	"event_data": {
		"TargetUserName": "RANDOMIZE",
		"TargetDomainName": "organization",
		"TargetSid": "S-1-5-21-1282426543-1088070111-3805647329-1125",
		"SubjectUserSid": "S-1-5-21-1282426543-1088070111-3805647329-1104",
		"SubjectUserName": "RANDOMIZE / administrator",
		"SubjectDomainName": "organization",
		"SubjectLogonId": "0x1b2f3af"
	},
	"type": "wineventlog",
	"opcode": "Info",
	"thread_id": 6468,
	"provider_guid": "{54849625-5478-4994-A5BA-3E3B0328C30D}",
	"beat": {
		"version": "6.5.4",
		"name": "EC2AMAZ-AEGIACD",
		"hostname": "EC2AMAZ-AEGIACD"
	},
	"source_name": "Microsoft-Windows-Security-Auditing",
	"computer_name": "EC2AMAZ - AEGIACD.organization.internal",
	"level": "Information",
	"log_name": "Security",
	"@metadata": {
		"beat": "winlogbeat",
		"type": "doc",
		"version": "6.5.4"
	},
	"task": "User Account Management",
	"event_id": 4725,
	"meta": {
		"cloud": {
			"instance_id": "i-06fb7554bfff258bd",
			"machine_type": "t3.medium",
			"region": "us-east-2",
			"availability_zone": "us-east-2a",
			"provider": "ec2"
		}
	}
}

ad_4724_reset_password_log = {
	"process_id": 596,
	"logzio_codec": "plain",
	"keywords": [
		"Audit Success"
	],
	"event_data": {
		"TargetUserName": "RANDOMIZE",
		"TargetDomainName": "organization",
		"TargetSid": "S-1-5-21-1282426543-1088070111-3805647329-1123",
		"SubjectUserSid": "S-1-5-21-1282426543-1088070111-3805647329-1104",
		"SubjectUserName": "RANDOMIZE / administrator",
		"SubjectDomainName": "organization",
		"SubjectLogonId": "0x1b2f3af"
	},
	"opcode": "Info",
	"type": "wineventlog",
	"thread_id": 1900,
	"provider_guid": "{54849625-5478-4994-A5BA-3E3B0328C30D}",
	"beat": {
		"name": "EC2AMAZ-AEGIACD",
		"hostname": "EC2AMAZ-AEGIACD",
		"version": "6.5.4"
	},
	"source_name": "Microsoft-Windows-Security-Auditing",
	"computer_name": "EC2AMAZ - AEGIACD.organization.internal",
	"level": "Information",
	"log_name": "Security",
	"@metadata": {
		"beat": "winlogbeat",
		"type": "doc",
		"version": "6.5.4"
	},
	"task": "User Account Management",
	"event_id": 4724,
	"meta": {
		"cloud": {
			"region": "us-east-2",
			"availability_zone": "us - east - 2 a ",
			"provider": "ec2",
			"instance_id": "i-06fb7554bfff258bd",
			"machine_type": "t3.medium"
		}
	}
}

ad_4726_account_deleted_log = {
	"process_id": 596,
	"keywords": [
		"Audit Success"
	],
	"logzio_codec": "plain",
	"event_data": {
		"TargetDomainName": "organization",
		"TargetSid": "S-1-5-21-1282426543-1088070111-3805647329-1134",
		"SubjectUserSid": "S-1-5-21-1282426543-1088070111-3805647329-1104",
		"SubjectUserName": "RANDOMIZE / administrator",
		"SubjectDomainName": "organization",
		"SubjectLogonId": "0x1b2f3af",
		"PrivilegeList": "-",
		"TargetUserName": "RANDOMIZE"
	},
	"type": "wineventlog",
	"opcode": "Info",
	"thread_id": 1900,
	"provider_guid": "{54849625-5478-4994-A5BA-3E3B0328C30D}",
	"beat": {
		"version": "6.5.4",
		"name": "EC2AMAZ-AEGIACD",
		"hostname": "EC2AMAZ-AEGIACD"
	},
	"source_name": "Microsoft-Windows-Security-Auditing",
	"computer_name": "EC2AMAZ - AEGIACD.organization.internal",
	"log_name": "Security",
	"level": "Information",
	"@metadata": {
		"beat": "winlogbeat",
		"type": "doc",
		"version": "6.5.4"
	},
	"event_id": 4726,
	"task": "User Account Management",
	"meta": {
		"cloud": {
			"instance_id": "i-06fb7554bfff258bd",
			"machine_type": "t3.medium",
			"region": "us-east-2",
			"availability_zone": "us-east-2a",
			"provider": "ec2"
		}
	}
}

# override - like 4625
ad_4740_account_was_locked_out_log = {
	"process_id": "596",
	"keywords": [
		"Audit Failure"
	],
	"logzio_codec": "plain",
	"record_number": "970554",
	"event_data": {
		"ProcessName": "-",
		"LmPackageName": "-",
		"KeyLength": "0",
		"ProcessId": "0x0",
		"SubjectLogonId": "0x0",
		"TargetUserSid": "S-1-0-0",
		"IpPort": "0",
		"TargetDomainName": "organization",
		"SubjectUserSid": "S-1-0-0",
		"IpAddress": "1.1.1.1",
		"LogonType": "3",
		"WorkstationName": "ec2-54-144-39-189.compute-1.amazonaws.com",
		"TargetUserName": "RANDOMIZE",
		"SubjectUserName": "-",
		"SubjectDomainName": "-",
		"TransmittedServices": "-"
	},
	"opcode": "Info",
	"type": "wineventlog",
	"thread_id": 6320,
	"provider_guid": "{54849625-5478-4994-A5BA-3E3B0328C30D}",
	"beat": {
		"hostname": "EC2AMAZ-AEGIACD",
		"version": "6.5.4",
		"name": "EC2AMAZ-AEGIACD"
	},
	"source_name": "Microsoft-Windows-Security-Auditing",
	"computer_name": "EC2AMAZ-AEGIACD.organization.internal",
	"log_name": "Security",
	"level": "Information",
	"@metadata": {
		"beat": "winlogbeat",
		"type": "doc",
		"version": "6.5.4"
	},
	"tags": [
		"beats-5015"
	],
	"event_id": 4740,
	"task": "Logon",
	"meta": {
		"cloud": {
			"availability_zone": "eu-west-2b",
			"provider": "ec2",
			"instance_id": "i-06fb7554bfff258bd",
			"machine_type": "t3.medium",
			"region": "eu-west-2b"
		}
	}
}
