from logs_template import suricata_log, px_block_log, aws_login_log, s3_get_object_log, s3_delete_object_log, \
    s3_delete_bucket_log, wazuh_bf_log, apache_get_log, apache_post_log, s3_delete_security_group_log, ec2ssh_login_log
import log_data

logs_program = [

    # One time only - will generate alert mail once a day 
    # IAM malicious 
    # {"log_type": aws_login_log, "from_time": "11:15:00", "to_time": "11:20:00", "every": 60*1, "cross_fields": False, "add_logzio_security": True, "ip_field": 'sourceIPAddress',
    # "fields": [
    #    {"field_name": 'sourceIPAddress', "values": log_data.iam_attackers},
    #    {"field_name": 'userIdentity|userName', "values": log_data.iam_attacker_names},
    #     {"field_name": 'userIdentity|arn', "values": log_data.iam_attacker_arn},
    #    {"field_name": 'responseElements|ConsoleLogin', "values": ["Failure"]*len(log_data.iam_attacker_names)}
    # ]
    # },

    ##################################################################################### 
    # Wazuh alert logs - for the Summary Dashboard - 04:00 - 05:00
    #
    # 5 endpoints/attackers
    # Over 5 logs in 30 minutes 
    # 22:00 - 23:00  attackers send log every 5 minutes
    #####################################################################################
    {"log_type": wazuh_bf_log, "from_time": "04:00:00", "to_time": "05:00:00", "every": 60 * 5, "cross_fields": False,
     "add_logzio_security": True, "ip_field": 'data|srcip',
     "fields": [
         {"field_name": 'agent|ip', "values": log_data.wazuh_attackers},
         {"field_name": 'data|srcuser', "values": log_data.wazuh_attacker_names},
         {"field_name": 'data|srcip', "values": log_data.wazuh_attackers},
     ]
     },

    ##################################################################################### 
    # Audit alerts - for the Summary Dashboard - 04:00 - 05:00
    #
    # 5 endpoints/attackers
    # Over 5 logs in 30 minutes 
    # 22:00 - 23:00  attackers send log every 5 minutes
    #####################################################################################
    {"log_type": s3_delete_security_group_log, "from_time": "04:00:00", "to_time": "05:00:00", "every": 60 * 30,
     "cross_fields": False, "add_logzio_security": True, "ip_field": 'sourceIPAddress',
     "fields": [
         {"field_name": 'eventName', "values": ["DeleteSecurityGroup"]},
     ]
     },

    ##################################################################################### 
    # User Story #2 - Benign . 10:00-17:00 
    #                   Attack is t 2:00 - 02:30
    #
    # 22:00 - 23:00  attackers send MMAP (Suricata) every 5 mintues to multiple destinations/ports
    # all day long -  every 5 hours NMAP begnin logs - by non malicious IPs
    #
    # 22:55 1 time IAM Login Failed by attackers -  to create a nice line
    # 23:00 - 2:00 IAM login Failed by attackers every minute
    # 02:30 1 time IAM Login Failed by attackers -  to create a nice line
    # 2:01 - 2:02 - one time Login Success
    #
    # 2:03 - 2:06 - every minute GetObject - 2 sensitive buckets and 3 benign buckets 
    # 2:07 - 2:08 - once delete object - 2 sensitive buckets
    # 2:09 - 2:10 - once delete bucket - 2 sensitive buckets
    #
    # 10:00 - 17:00 - every 50 minutes Login Success of benign users 
    # 10:02 - 17:00 - every 100 minutes naive Get Object
    ##################################################################################### 

    # Suricata NMAP attacks
    {"log_type": suricata_log, "from_time": "22:00:00", "to_time": "23:00:00", "every": 60 * 5, "cross_fields": True,
     "add_logzio_security": True, "ip_field": 'src_ip',
     "fields": [
         {"field_name": 'src_ip', "values": log_data.nmap_attackers},
         {"field_name": 'dest_ip', "values": log_data.nmap_destinations},
         {"field_name": 'dest_port', "values": log_data.nmap_ports}
     ]
     },

    # Suricata NMAP benigns
    {"log_type": suricata_log, "from_time": "00:00:00", "to_time": "23:59:00", "every": 60 * 60 * 5,
     "cross_fields": False, "add_logzio_security": False,
     "fields": [
         {"field_name": 'src_ip', "values": log_data.nmap_benigns},
         {"field_name": 'dest_ip', "values": log_data.nmap_dest_benigns},
         {"field_name": 'dest_port', "values": log_data.nmap_ports_benigns}
     ]
     },

    # SSH malicious START - failure
    {"log_type": ec2ssh_login_log, "from_time": "22:55:00", "to_time": "22:56:00", "every": 60 * 1,
     "cross_fields": False,
     "add_logzio_security": True, "ip_field": 'source_ip',
     "fields": [
         {"field_name": 'source_ip', "values": log_data.ssh_attackers},
         {"field_name": 'auditd|data|hostname', "values": log_data.ssh_attackers},
         {"field_name": 'auditd|data|op', "values": ["PAM:bad_ident"]*5},
         {"field_name": 'auditd|summary|object|secondary', "values": log_data.ssh_attackers},
         {"field_name": 'auditd|result', "values": ["fail"]*5},
         {"field_name": 'event|type', "values": ["user_err"]*5},
         {"field_name": 'event|action', "values": ["error"]*5},
         {"field_name": 'user|name_map|uid', "values": ["root"]*5},
         {"field_name": 'meta|cloud|instance_id', "values": log_data.ssh_instance_id}     
     ]
     },

    # IAM malicious START - failure
    # {"log_type": aws_login_log, "from_time": "22:55:00", "to_time": "22:56:00", "every": 60 * 1, "cross_fields": False,
    # "add_logzio_security": True, "ip_field": 'sourceIPAddress',
    # "fields": [
    #  {"field_name": 'sourceIPAddress', "values": log_data.iam_attackers},
    # {"field_name": 'userIdentity|userName', "values": log_data.iam_attacker_names},
    #  {"field_name": 'userIdentity|arn', "values": log_data.iam_attacker_arn},
    #  {"field_name": 'responseElements|ConsoleLogin', "values": ["Failure"] * len(log_data.iam_attacker_names)}
    # ]
    #  },

    # IAM malicious - 3 hours of failure
    #   {"log_type": aws_login_log, "from_time": "23:00:00", "to_time": "02:00:00", "every": 60 * 1, "cross_fields": False,
    #   "add_logzio_security": True, "ip_field": 'sourceIPAddress',
    #   "fields": [
    #       {"field_name": 'sourceIPAddress', "values": log_data.iam_attackers},
    #       {"field_name": 'userIdentity|userName', "values": log_data.iam_attacker_names},
    #       {"field_name": 'userIdentity|arn', "values": log_data.iam_attacker_arn},
    #        {"field_name": 'responseElements|ConsoleLogin', "values": ["Failure"] * len(log_data.iam_attacker_names)}
    #   ]
    #    },

    {"log_type": ec2ssh_login_log, "from_time": "23:00:00", "to_time": "02:00:00", "every": 60 * 1,
     "cross_fields": False,
     "add_logzio_security": True, "ip_field": 'source_ip',
     "fields": [
         {"field_name": 'source_ip', "values": log_data.ssh_attackers},
         {"field_name": 'auditd|data|hostname', "values": log_data.ssh_attackers},
         {"field_name": 'auditd|data|op', "values": ["PAM:bad_ident"]*5},
         {"field_name": 'auditd|summary|object|secondary', "values": log_data.ssh_attackers},
         {"field_name": 'auditd|result', "values": ["fail"]*5},
         {"field_name": 'event|type', "values": ["user_err"]*5},
         {"field_name": 'event|action', "values": ["error"]*5},
         {"field_name": 'user|name_map|uid', "values": ["root"]*5},
         {"field_name": 'meta|cloud|instance_id', "values": log_data.ssh_instance_id}     
     ]
     },

    # SSH malicious END - failure
    {"log_type": ec2ssh_login_log, "from_time": "02:30:00", "to_time": "02:31:00", "every": 60 * 1,
     "cross_fields": False,
     "add_logzio_security": True, "ip_field": 'source_ip',
     "fields": [
         {"field_name": 'source_ip', "values": log_data.ssh_attackers},
         {"field_name": 'auditd|data|hostname', "values": log_data.ssh_attackers},
         {"field_name": 'auditd|data|op', "values": ["PAM:bad_ident"]*5},
         {"field_name": 'auditd|summary|object|secondary', "values": log_data.ssh_attackers},
         {"field_name": 'auditd|result', "values": ["fail"]*5},
         {"field_name": 'event|type', "values": ["user_err"]*5},
         {"field_name": 'event|action', "values": ["error"]*5},
         {"field_name": 'user|name_map|uid', "values": ["root"]*5},
         {"field_name": 'meta|cloud|instance_id', "values": log_data.ssh_instance_id}     
     ]
     },

    # IAM malicious END - failure
    #
    #  {"log_type": aws_login_log, "from_time": "02:30:00", "to_time": "02:31:00", "every": 60 * 1, "cross_fields": False,
    #   "add_logzio_security": True, "ip_field": 'sourceIPAddress',
    #   "fields": [
    #       {"field_name": 'sourceIPAddress', "values": log_data.iam_attackers},
    #       {"field_name": 'userIdentity|userName', "values": log_data.iam_attacker_names},
    #       {"field_name": 'userIdentity|arn', "values": log_data.iam_attacker_arn},
    #       {"field_name": 'responseElements|ConsoleLogin', "values": ["Failure"] * len(log_data.iam_attacker_names)}
    #   ]
    #   },

    # IAM malicious - success login
    #  {"log_type": aws_login_log, "from_time": "02:01:00", "to_time": "02:02:00", "every": 60 * 1, "cross_fields": False,
    #   "add_logzio_security": True, "ip_field": 'sourceIPAddress',
    #   "fields": [
    #       {"field_name": 'sourceIPAddress', "values": log_data.iam_attackers},
    #      {"field_name": 'userIdentity|userName', "values": log_data.iam_attacker_names},
    #        {"field_name": 'userIdentity|arn', "values": log_data.iam_attacker_arn},
    #       {"field_name": 'responseElements|ConsoleLogin', "values": ["Success"] * len(log_data.iam_attacker_names)}
    #   ]
    #   },

    # SSH malicious  - Success Login
    {"log_type": ec2ssh_login_log, "from_time": "02:01:00", "to_time": "02:02:00", "every": 60 * 1,
     "cross_fields": False,
     "add_logzio_security": True, "ip_field": 'source_ip',
     "fields": [
         {"field_name": 'source_ip', "values": log_data.ssh_attackers},
         {"field_name": 'auditd|data|hostname', "values": log_data.ssh_attackers},
         {"field_name": 'auditd|data|op', "values": ["PAM:session_open"]*5},
         {"field_name": 'auditd|summary|object|secondary', "values": log_data.ssh_attackers},
         {"field_name": 'auditd|result', "values": ["success"]*5},
         {"field_name": 'event|type', "values": ["user_start"]*5},
         {"field_name": 'event|action', "values": ["started"]*5},
         {"field_name": 'user|name_map|uid', "values": ["root"]*5},
         {"field_name": 'meta|cloud|instance_id', "values": log_data.ssh_instance_id}     
     ]
     },

    # aws s3 malicious - get bucket
    {"log_type": s3_get_object_log, "from_time": "02:03:00", "to_time": "02:06:00", "every": 60 * 1,
     "cross_fields": False, "add_logzio_security": True, "ip_field": 'sourceIPAddress',
     "fields": [
         {"field_name": 'sourceIPAddress', "values": log_data.iam_attackers},
         {"field_name": 'requestParameters|bucketName', "values": log_data.s3_bucket_sensitive},
         {"field_name": 'requestParameters|key', "values": log_data.s3_files_sensitive},
         {"field_name": 'requestParameters|Host', "values": log_data.s3_bucket_host_sensitive},
         {"field_name": 'resources|ARN', "values": log_data.s3_bucket_arn_sensitive},
         {"field_name": 'userIdentity|userName', "values": log_data.iam_attacker_names}
     ]
     },

    # aws attackers on s3 benign - get bucket
    {"log_type": s3_get_object_log, "from_time": "02:03:00", "to_time": "02:06:00", "every": 60 * 1,
     "cross_fields": False, "add_logzio_security": True, "ip_field": 'sourceIPAddress',
     "fields": [
         {"field_name": 'sourceIPAddress', "values": log_data.iam_benigns},
         {"field_name": 'requestParameters|bucketName', "values": log_data.s3_bucket_benign},
         {"field_name": 'requestParameters|key', "values": log_data.s3_files_benign},
         {"field_name": 'requestParameters|Host', "values": log_data.s3_bucket_host_benign},
         {"field_name": 'resources|ARN', "values": log_data.s3_bucket_arn_benign},
         {"field_name": 'userIdentity|userName', "values": log_data.iam_benigns_names}
     ]
     },

    # aws s3 malicious - delete object
    {"log_type": s3_delete_object_log, "from_time": "02:07:00", "to_time": "02:08:00", "every": 60 * 1,
     "cross_fields": False, "add_logzio_security": True, "ip_field": 'sourceIPAddress',
     "fields": [
         {"field_name": 'sourceIPAddress', "values": log_data.iam_attackers},
         {"field_name": 'requestParameters|bucketName', "values": log_data.s3_bucket_sensitive},
         {"field_name": 'requestParameters|key', "values": log_data.s3_files_sensitive},
         {"field_name": 'requestParameters|Host', "values": log_data.s3_bucket_host_sensitive},
         {"field_name": 'resources|ARN', "values": log_data.s3_bucket_arn_sensitive},
         {"field_name": 'userIdentity|userName', "values": log_data.iam_attacker_names}
     ]
     },

    # aws s3 malicious - delete bucket
    {"log_type": s3_delete_bucket_log, "from_time": "02:09:00", "to_time": "02:10:00", "every": 60 * 1,
     "cross_fields": False, "add_logzio_security": True, "ip_field": 'sourceIPAddress',
     "fields": [
         {"field_name": 'sourceIPAddress', "values": log_data.iam_attackers},
         {"field_name": 'userIdentity|userName', "values": log_data.iam_attacker_names},
         {"field_name": 'userIdentity|arn', "values": log_data.iam_attacker_arn},
         {"field_name": 'requestParameters|bucketName', "values": log_data.s3_bucket_sensitive},
     ]
     },

    # IAM benigns
    #  {"log_type": aws_login_log, "from_time": "10:00:00", "to_time": "17:00:00", "every": 60 * 50, "cross_fields": False,
    #   "add_logzio_security": False,
    #   "fields": [
    #       {"field_name": 'sourceIPAddress', "values": log_data.nmap_benigns},
    #       {"field_name": 'userIdentity|userName', "values": log_data.iam_benigns_names},
    #        {"field_name": 'userIdentity|arn', "values": log_data.iam_benigns_arn},
    #       {"field_name": 'responseElements|ConsoleLogin', "values": ["Success"] * len(log_data.iam_benigns_names)}
    #    ]
    #    },

    # SSH benigns
    {"log_type": ec2ssh_login_log, "from_time": "10:00:00", "to_time": "17:00:00", "every": 60 * 50,
     "cross_fields": False,
     "add_logzio_security": False,
     "fields": [
         {"field_name": 'source_ip', "values": log_data.iam_benigns},
         {"field_name": 'auditd|data|hostname', "values": log_data.ssh_user},
         {"field_name": 'auditd|data|op', "values": ["PAM:session_open"]*5},
         {"field_name": 'auditd|summary|object|secondary', "values": log_data.ssh_user},
         {"field_name": 'auditd|result', "values": ["success"]*5},
         {"field_name": 'event|type', "values": ["user_start"]*5},
         {"field_name": 'event|action', "values": ["started"]*5},
         {"field_name": 'user|name_map|uid', "values": log_data.ssh_user},
         {"field_name": 'meta|cloud|instance_id', "values": log_data.ssh_instance_id}        
     ]
     },

    # aws s3 naive - get bucket
    {"log_type": s3_get_object_log, "from_time": "10:02:00", "to_time": "17:00:00", "every": 60 * 100,
     "cross_fields": False, "add_logzio_security": False,
     "fields": [
         {"field_name": 'sourceIPAddress', "values": log_data.nmap_benigns},
         {"field_name": 'requestParameters|bucketName', "values": log_data.s3_bucket_benign},
         {"field_name": 'requestParameters|key', "values": log_data.s3_files_benign},
         {"field_name": 'requestParameters|Host', "values": log_data.s3_bucket_host_benign},
         {"field_name": 'resources|ARN', "values": log_data.s3_bucket_arn_benign},
         {"field_name": 'userIdentity|userName', "values": log_data.iam_benigns_names}
     ]
     },

    ###################################################################################################################
    # User Scenario #1 - 06:00 - 07:00
    #
    # 06:00 - 06:30 Apache web logs come in showing normal traffic of both logins and product views - naive source IPs
    #           Get - 5 per second
    #           Post - 5 per minute 
    # 06:10 - 06:30   An attack 2 types of logs - every 1 second
    #         1. Apache login with status code of 403
    #         2. PerimeterX block log . - every 1 second from 1 malicious IP
    # 06:31  - 07:00 Successful apache logs for login and product. Same as 06:00 - 06:30
    # 06:41  - 07:00  An attack 2 types of logs - every 1 second
    #         1. Apache login with status code of 403
    #         2. PerimeterX block log . - every 1 second from 1 malicious IP
    ###################################################################################################################   
    # Apache naive logs - GET POST
    {"log_type": apache_get_log, "from_time": "06:00:00", "to_time": "6:30:00", "every": 1, "cross_fields": False,
     "add_logzio_security": False,
     "fields": [
         {"field_name": 'ip', "values": log_data.apache_benigns},
     ]
     },

    {"log_type": apache_post_log, "from_time": "06:00:00", "to_time": "06:30:00", "every": 60, "cross_fields": False,
     "add_logzio_security": False,
     "fields": [
         {"field_name": 'ip', "values": log_data.apache_benigns},
     ]
     },

    # Apache attack - 3 malicious IPs - 1 per second or like before 
    {"log_type": apache_post_log, "from_time": "06:10:00", "to_time": "06:30:00", "every": 1, "cross_fields": False,
     "add_logzio_security": True, "ip_field": 'ip',
     "fields": [
         {"field_name": 'ip', "values": log_data.apache_attacker},
         {"field_name": 'user_agent', "values": log_data.apache_user_agent},
         {"field_name": 'status_code', "values": ["403"]*3}
     ]
     },

    # PX - blocking the attackers' POST 
    {"log_type": px_block_log, "from_time": "06:10:00", "to_time": "06:30:00", "every": 1, "cross_fields": False,
     "add_logzio_security": True, "ip_field": 'true_ip',
     "fields": [
         {"field_name": 'true_ip', "values": log_data.apache_attacker},
         {"field_name": 'client_ip', "values": log_data.apache_attacker},
         {"field_name": 'user_agent', "values": log_data.apache_user_agent}
     ]
     },

    # Repeat same scenario -  Apache naive logs - GET POST
    {"log_type": apache_get_log, "from_time": "06:31:00", "to_time": "7:00:00", "every": 1, "cross_fields": False,
     "add_logzio_security": False,
     "fields": [
         {"field_name": 'ip', "values": log_data.apache_benigns}
     ]
     },

    {"log_type": apache_post_log, "from_time": "06:31:00", "to_time": "07:00:00", "every": 60, "cross_fields": False,
     "add_logzio_security": False,
     "fields": [
         {"field_name": 'ip', "values": log_data.apache_benigns},
     ]
     },

    # Apache attack - single malicious IP - 1 per second or like before 
    {"log_type": apache_post_log, "from_time": "06:40:00", "to_time": "07:00:00", "every": 1, "cross_fields": False,
     "add_logzio_security": True, "ip_field": 'ip',
     "fields": [
         {"field_name": 'ip', "values": log_data.apache_attacker},
         {"field_name": 'user_agent', "values": log_data.apache_user_agent},
         {"field_name": 'status_code', "values": ["403"]*3}
     ]
     },

    # pX blocked
    {"log_type": px_block_log, "from_time": "06:40:00", "to_time": "07:00:00", "every": 1, "cross_fields": False,
     "add_logzio_security": True, "ip_field": 'true_ip',
     "fields": [
         {"field_name": 'true_ip', "values": log_data.apache_attacker},
         {"field_name": 'client_ip', "values": log_data.apache_attacker},
         {"field_name": 'user_agent', "values": log_data.apache_user_agent}
     ]
     }
]
