from logs_template_ad import ad_4624_logon_success_log, ad_4625_logon_failed_log, ad_4720_account_created_log, ad_4722_account_enabled_log, ad_4724_reset_password_log, \
    ad_4725_account_disabled_log, ad_4726_account_deleted_log, ad_4740_account_was_locked_out_log
import log_data_ad

###################################################################################################################
# User Scenario
#
# 3 admins are managing the AD
# They create & delete, enable & disable  accounts
# Admin resets the password when requested, user forgot passwd or security incident
##
# Story 5 - daily activity - 24 hours scenario - Orel
# ===================================================
# In thus story over 24 we will see:
#        Login successful -  from benign users
#        Login Failed  -  from benign users
#        Login Failed - from malicious users
#
# 08:00 - 09:00 -  3 begnin administrators "Create Users"  - log 4720
# 08:30 - 08:31 -  1 malicious administrator called Administrator "Create User" - log 4720
# 09:31 - 09:32 -  after 1 hour - 1 malicious administrator called Administrator "Delete User" - log 4726
#
# 10:00 - 11:00 -  3 begnin administrators "Enable Users" - freelancers - log 4722
# 09:00 - 17:00 -  Once an hour 2 begnin users fail authentication - log 4625
# 09:00 - 17:00 -  Every 6 hours 4 benign users fail authentication - log 4625
# 09:00 - 17:00 -  3 benign administrators fail authentication - log 4625 statuscode 0x6A
# 17:00 - 17:00 -  2 accounts are disabled following too many auth failures
# 17:00 - 17:00 -  2 accounts are locked out following being disabled - 4740
# 09:00 - 08:59 -  5 accounts have Password Resets by Admin - benign admin - over 24 hours - 4724
#
#ad_4624_logon_success_log
#ad_4625_logon_failed_log
#ad_4720_account_created_log
#ad_4722_account_enabled_log
#ad_4724_reset_password_log
#ad_4725_account_disabled_log
#ad_4726_account_deleted_log
#ad_4740_account_was_locked_out_log
###################################################################################################################

logs_program_ad2 = [

    ###################################################################################################################
    # Story 5 - daily activity - 24 hours scenario - Orel
    # ===================================================
    # In thus story over 24 we will see:
    #        Login successful -  from benign users
    #        Login Failed  -  from benign users
    #        Login Failed - from malicious users
    #
    # ok 10:00 - 17:00    8 users login every 3 minutes successfully   4624
    # ok 08:00 - 09:00 -  every 15 minutes one of 4 begnin administrators "Create Users"  - log 4720
    # ok 08:30 - 08:31 -  1 malicious administrator called Administrator "Create User" - log 4720
    # ok 09:31 - 09:32 -  after 1 hour - 1 malicious administrator called Administrator "Delete User" - log 4726
    #
    # ok 10:00 - 11:00 -  every 15 minutes 1 begnin administrators "Enable Users" - freelancers - total 4 logs -  log 4722
    # ok 09:00 - 17:00 -  Once every 30 min.  1 begnin user fail authentication - log 4625
    # ok 09:00 - 17:00 -  Once every 2 hours 1 benign users fail authentication - log 4625
    # ok 09:00 - 17:00 -  3 benign administrators fail authentication - log 4625 statuscode 0x6A

    # ok 17:00 - 17:00 -  2 accounts are disabled following too many auth failures 4725
    # ok 17:00 - 17:00 -  2 accounts are locked out following being disabled - 4740
    # ok 09:00 - 08:59 -  2 accounts have Password Resets by Admin - benign admin - over 24 hours 4724
    ###################################################################################################################

    {"log_type": ad_4624_logon_success_log, "from_time": "10:00:00", "to_time": "17:00:00", "every": 180,
     "cross_fields": False, "rolling_values": 1,
     "add_logzio_security": True, "ip_field": 'event_data|IpAddress',
     "fields": [
         {"field_name": 'event_data|IpAddress', "values": log_data_ad.IpAddress},
         {"field_name": 'event_data|TargetUserName', "values": log_data_ad.TargetUserName}
     ]
     },
    {"log_type": ad_4720_account_created_log, "from_time": "08:00:00", "to_time": "09:00:00", "every": 900,
     "cross_fields": False, "rolling_values": 1,
     "add_logzio_security": False,
     "fields": [
         # created user
         {"field_name": 'event_data|DisplayName', "values": log_data_ad.DisplayNameAccountCreated2},
         {"field_name": 'event_data|TargetUserName', "values": log_data_ad.TargetUserNameCreated2},
         {"field_name": 'event_data|SamAccountName', "values": log_data_ad.TargetUserNameCreated2},
         # admin
         {"field_name": 'event_data|SubjectUserName', "values": log_data_ad.SubjectAdminName},
     ]
     },
    {"log_type": ad_4720_account_created_log, "from_time": "08:30:00", "to_time": "08:31:00", "every": 60,
     "cross_fields": False,
     "add_logzio_security": False,
     "fields": [
         {"field_name": 'event_data|DisplayName', "values": log_data_ad.DisplayNameBadAdmin},
         {"field_name": 'event_data|TargetUserName', "values": log_data_ad.TargetUserNamebadadmin},
         {"field_name": 'event_data|SamAccountName', "values": log_data_ad.TargetUserNamebadadmin},
         {"field_name": 'event_data|SubjectUserName', "values": ["Administrator"]},
     ]
     },
    {"log_type": ad_4726_account_deleted_log, "from_time": "09:31:00", "to_time": "09:32:00", "every": 60,
     "cross_fields": False,
     "add_logzio_security": False,
     "fields": [
         {"field_name": 'event_data|TargetUserName', "values": ["JohnDoe"]},
         {"field_name": 'event_data|SubjectUserName', "values": ["Administrator"]},
     ]
     },
    {"log_type": ad_4722_account_enabled_log, "from_time": "10:00:00", "to_time": "11:0:00", "every": 900,
     "cross_fields": False, "rolling_values": 1,
     "add_logzio_security": False,
     "fields": [
         {"field_name": 'event_data|TargetUserName', "values": log_data_ad.TargetUserNameFreelance},
         {"field_name": 'event_data|SubjectUserName', "values": log_data_ad.SubjectAdminName},
     ]
     },
    # AD Login failed
    {"log_type": ad_4625_logon_failed_log, "from_time": "09:00:00", "to_time": "17:00:00", "every": 1800,
     "cross_fields": False, "rolling_values": 1,
     "add_logzio_security": False,
     "fields": [
         {"field_name": 'event_data|IpAddress', "values": log_data_ad.BenignIpAddress2},
         {"field_name": 'event_data|TargetUserName', "values": log_data_ad.BenignUserName2}
     ]
     },
    # AD Login failed
    {"log_type": ad_4625_logon_failed_log, "from_time": "09:00:00", "to_time": "17:00:00", "every": 7200,
     "cross_fields": False, "rolling_values": 1,
     "add_logzio_security": False,
     "fields": [
         {"field_name": 'event_data|IpAddress', "values": log_data_ad.BenignIpAddress},
         {"field_name": 'event_data|TargetUserName', "values": log_data_ad.BenignUserName}
     ]
     },
    # AD Login failed
    # 09:00 - 17:00 -  4 benign administrators fail authentication - log 4625 statuscode 0x6A
    {"log_type": ad_4625_logon_failed_log, "from_time": "09:00:00", "to_time": "17:00:00", "every": 7200,
     "cross_fields": False, "rolling_values": 1,
     "add_logzio_security": False,
     "fields": [
         {"field_name": 'event_data|IpAddress', "values": log_data_ad.BenignAdminIpAddress},
         {"field_name": 'event_data|TargetUserName', "values": log_data_ad.SubjectAdminName},
         {"field_name": 'event_data|Status', "values": ["0xc000006a"]}
     ]
     },
    # 17:00 - 17:02 -  2 accounts are disabled following too many auth failures 4725
    {"log_type": ad_4725_account_disabled_log, "from_time": "17:00:00", "to_time": "17:02:00", "every": 60,
     "cross_fields": False, "rolling_values": 1,
     "add_logzio_security": False,
     "fields": [
         {"field_name": 'event_data|TargetUserName', "values": log_data_ad.BenignUserName2},
         {"field_name": 'event_data|SubjectUserName', "values": log_data_ad.SubjectAdminName}
     ]
     },
    {"log_type": ad_4740_account_was_locked_out_log, "from_time": "17:00:00", "to_time": "17:02:00", "every": 60,
     "cross_fields": False, "rolling_values": 1,
     "add_logzio_security": False,
     "fields": [
         {"field_name": 'event_data|TargetUserName', "values": log_data_ad.BenignUserName2}
     ]
     },
    {"log_type": ad_4724_reset_password_log, "from_time": "18:00:00", "to_time": "19:00:00", "every": 1800,
     "cross_fields": False, "rolling_values": 1,
     "add_logzio_security": False,
     "fields": [
         {"field_name": 'event_data|TargetUserName', "values": log_data_ad.BenignUserName2},
         {"field_name": 'event_data|SubjectUserName', "values": log_data_ad.SubjectAdminName}
     ]
     }
]