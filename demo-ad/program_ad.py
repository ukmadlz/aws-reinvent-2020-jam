from logs_template_ad import ad_4624_logon_success_log, ad_4625_logon_failed_log, ad_4720_account_created_log, ad_4722_account_enabled_log, ad_4724_reset_password_log, \
    ad_4725_account_disabled_log, ad_4726_account_deleted_log
import log_data_ad

###################################################################################################################
# User Scenario
#
# 3 admins are managing the AD
# They create & delete, enable & disable  accounts
# Admin resets the password when requested, user forgot passwd or security incident
#
# Story #1
# ========
# Malicious hacker is using fake user names to login/logout repeatedly into the organization
# Admin disable this account and verifies such a user left the company
# Admin deletes the account
#
# Story #2
# ========
# Malicious hacker uses an IP to login to the organization, multiple fails + success, using an exsiting user's account
# After 10 minutes the admin disables the account
# Adter 20 minutes the admin resets the password and enables the account
#
# Story #3 - daily activity benign
# ================================
# 11:00 - 11:30 3 admins create new accounts every 10 minutes - total of 9 new accounts
# 09:00 - 10:00 8 users login every minute  ad_4624_logon_success_log
# 10:00 - 17:00 8 users login every 1 hour   ad_4624_logon_success_log
#  9:00 - 17:00 1 user failure every 1 hour ad_4625_logon_failed_log
#
# Story #4 - AD Dashboard
# =======================
# 15:00 - 15:10 - Malicious hacker uses a malicious IP to login to the organization existing user, multiple fails
# 15:11 - 15:12 - Success login, using an existing user's account
# 15:30 - the admin gets an alert and disables the account
# 15:31 - the admin resets the password
# 15:32 - the admin enables the account
# 15:40 -  Existing user logs in from a benign IP
#
#ad_4624_logon_success_log
#ad_4625_logon_failed_log
#ad_4720_account_created_log
#ad_4722_account_enabled_log
#ad_4724_reset_password_log
#ad_4725_account_disabled_log
#ad_4726_account_deleted_log
###################################################################################################################


logs_program_ad = [

    ###################################################################################################################
    # Story #1
    # ========
    # 03:00 -  04:00  A malicious hacker is using a fake user name to login repeatedly into the organization - failed
    # 04:00 - 04:01 login succeeded
    # 09:00 -  Admin disables this account and verifies such a user left the company
    # 09:30 -  Admin deletes the account
    #
    ###################################################################################################################
    {"log_type": ad_4625_logon_failed_log, "from_time": "03:00:00", "to_time": "04:00:00", "every": 5,
     "cross_fields": False,
     "add_logzio_security": True, "ip_field": 'event_data|IpAddress',
     "fields": [
         {"field_name": 'event_data|IpAddress', "values": log_data_ad.MaliciousIpAddress},
         {"field_name": 'event_data|TargetUserName', "values": log_data_ad.TargetUserNameOld}
     ]
     },

    {"log_type": ad_4624_logon_success_log, "from_time": "04:00:00", "to_time": "04:01:00", "every": 60,
     "cross_fields": False, "rolling_values": 1,
     "add_logzio_security": True, "ip_field": 'event_data|IpAddress',
     "fields": [
         {"field_name": 'event_data|IpAddress', "values": log_data_ad.MaliciousIpAddress},
         {"field_name": 'event_data|TargetUserName', "values": log_data_ad.TargetUserNameOld}
     ]
     },

    {"log_type": ad_4725_account_disabled_log, "from_time": "09:00:00", "to_time": "09:01:00", "every": 60,
     "cross_fields": False, "rolling_values": 1,
     "add_logzio_security": False,
     "fields": [
         {"field_name": 'event_data|TargetUserName', "values": log_data_ad.TargetUserNameOld},
         {"field_name": 'event_data|SubjectAdminUserName', "values": log_data_ad.SubjectAdminName},
     ]
     },

    {"log_type": ad_4726_account_deleted_log, "from_time": "09:00:00", "to_time": "09:01:00", "every": 60,
     "cross_fields": False, "rolling_values": 1,
     "add_logzio_security": False,
     "fields": [
         {"field_name": 'event_data|TargetUserName', "values": log_data_ad.TargetUserNameOld},
         {"field_name": 'event_data|SubjectAdminUserName', "values": log_data_ad.SubjectAdminName},
     ]
     },

    ###################################################################################################################
    # Story #2
    # ========
    # 15:00 - 15:10 - Malicious hacker uses a malicious IP to login to the organization existing user, multiple fails
    # 15:11 - 15:12 - Success login, using an existing user's account
    # 15:30 - the admin gets an alert and disables the account
    # 15:31 - the admin resets the password
    # 15:32 - the admin enables the account
    # 15:40 -  Existing user logs in from a benign IP
    ###################################################################################################################
    {"log_type": ad_4625_logon_failed_log, "from_time": "15:00:00", "to_time": "15:10:00", "every": 5,
     "cross_fields": False,
     "add_logzio_security": True, "ip_field": 'event_data|IpAddress',
     "fields": [
         {"field_name": 'event_data|IpAddress', "values": log_data_ad.MaliciousIpAddress},
         {"field_name": 'event_data|TargetUserName', "values": log_data_ad.TargetUserNameExists}
     ]
     },
     {"log_type": ad_4624_logon_success_log, "from_time": "15:11:00", "to_time": "15:12:00", "every": 60,
     "cross_fields": False,
     "add_logzio_security": True, "ip_field": 'event_data|IpAddress',
     "fields": [
         {"field_name": 'event_data|IpAddress', "values": log_data_ad.MaliciousIpAddress},
         {"field_name": 'event_data|TargetUserName', "values": log_data_ad.TargetUserNameExists}
     ]
     },
     {"log_type": ad_4725_account_disabled_log, "from_time": "15:30:00", "to_time": "15:31:00", "every": 60,
     "cross_fields": False,
     "add_logzio_security": False,
     "fields": [
         {"field_name": 'event_data|TargetUserName', "values": log_data_ad.TargetUserNameExists},
         {"field_name": 'event_data|SubjectAdminUserName', "values": log_data_ad.SubjectAdminName},
     ]
     },
     {"log_type": ad_4724_reset_password_log, "from_time": "15:31:00", "to_time": "15:32:00", "every": 60,
     "cross_fields": False,
     "add_logzio_security": False,
     "fields": [
         {"field_name": 'event_data|TargetUserName', "values": log_data_ad.TargetUserNameExists},
         {"field_name": 'event_data|SubjectAdminUserName', "values": log_data_ad.SubjectAdminName},
     ]
     },
     {"log_type": ad_4722_account_enabled_log, "from_time": "15:32:00", "to_time": "15:33:00", "every": 60,
     "cross_fields": False,
     "add_logzio_security": False,
     "fields": [
         {"field_name": 'event_data|TargetUserName', "values": log_data_ad.TargetUserNameExists},
         {"field_name": 'event_data|SubjectAdminUserName', "values": log_data_ad.SubjectAdminName},
     ]
     },
     {"log_type": ad_4624_logon_success_log, "from_time": "15:40:00", "to_time": "15:41:00", "every": 60,
     "cross_fields": False,
     "add_logzio_security": True, "ip_field": 'event_data|IpAddress',
     "fields": [
         {"field_name": 'event_data|IpAddress', "values": log_data_ad.IpAddress},
         {"field_name": 'event_data|TargetUserName', "values": log_data_ad.TargetUserNameExists}
     ]
     },
    ###################################################################################################################
    # Story #3 - daily activity benign
    # ================================
    # 11:00 - 11:30 3 admins create new accounts every 10 minutes - total of 9 new accounts
    # 09:00 - 10:00 8 users login every minute  ad_4624_logon_success_log
    # 10:00 - 17:00 8 users login every 1 hour   ad_4624_logon_success_log
    #  9:00 - 17:00 1 user failure every 1 hour ad_4625_logon_failed_log
    ###################################################################################################################
    {"log_type": ad_4720_account_created_log, "from_time": "11:00:00", "to_time": "11:30:00", "every": 600,
     "cross_fields": True,
     "add_logzio_security": False,
     "fields": [
         {"field_name": 'event_data|DisplayName', "values": log_data_ad.DisplayNameAccountCreated},
         {"field_name": 'event_data|TargetUserName', "values": log_data_ad.TargetUserNameCreated},
         {"field_name": 'event_data|SamAccountName', "values": log_data_ad.TargetUserNameCreated},
         {"field_name": 'event_data|SubjectAdminUserName', "values": log_data_ad.SubjectAdminName},
     ]
     },
    # AD Login succeeded
    {"log_type": ad_4624_logon_success_log, "from_time": "09:00:00", "to_time": "10:00:00", "every": 60,
     "cross_fields": True,
     "add_logzio_security": True, "ip_field": 'event_data|IpAddress',
     "fields": [
         {"field_name": 'event_data|IpAddress', "values": log_data_ad.IpAddress},
         {"field_name": 'event_data|TargetUserName', "values": log_data_ad.TargetUserName}
     ]
     },

    {"log_type": ad_4624_logon_success_log, "from_time": "10:00:00", "to_time": "17:00:00", "every": 180,
     "cross_fields": False, "rolling_values": 1,
     "add_logzio_security": True, "ip_field": 'event_data|IpAddress',
     "fields": [
         {"field_name": 'event_data|IpAddress', "values": log_data_ad.IpAddress},
         {"field_name": 'event_data|TargetUserName', "values": log_data_ad.TargetUserName}
     ]
     },
    # AD Login failed
    {"log_type": ad_4625_logon_failed_log, "from_time": "09:00:00", "to_time": "17:00:00", "every": 60,
     "cross_fields": False,
     "add_logzio_security": True, "ip_field": 'event_data|IpAddress',
     "fields": [
         {"field_name": 'event_data|IpAddress', "values": log_data_ad.IpAddress},
         {"field_name": 'event_data|TargetUserName', "values": log_data_ad.TargetUserName}
     ]
     },

    ###################################################################################################################
    # Story #4 - AD Dashboard
    # =======================
    # 15:00 - 15:10 - Malicious hacker uses a malicious IP to login to the organization existing user, multiple fails
    # 15:11 - 15:12 - Success login, using an existing user's account
    # 15:30 - the admin gets an alert and disables the account
    # 15:31 - the admin resets the password
    # 15:32 - the admin enables the account
    # 15:40 -  Existing user logs in from a benign IP
    ###################################################################################################################

    {"log_type": ad_4624_logon_success_log, "from_time": "15:11:00", "to_time": "15:12:00", "every": 60,
     "cross_fields": False,
     "add_logzio_security": True, "ip_field": 'event_data|IpAddress',
     "fields": [
         {"field_name": 'event_data|IpAddress', "values": log_data_ad.MaliciousIpAddress},
         {"field_name": 'event_data|TargetUserName', "values": log_data_ad.TargetUserNameExists}
     ]
     },
    {"log_type": ad_4725_account_disabled_log, "from_time": "15:30:00", "to_time": "15:31:00", "every": 60,
     "cross_fields": False,
     "add_logzio_security": False,
     "fields": [
         {"field_name": 'event_data|TargetUserName', "values": log_data_ad.TargetUserNameExists},
         {"field_name": 'event_data|SubjectAdminUserName', "values": log_data_ad.SubjectAdminName},
     ]
     },
    {"log_type": ad_4724_reset_password_log, "from_time": "15:31:00", "to_time": "15:32:00", "every": 60,
     "cross_fields": False,
     "add_logzio_security": False,
     "fields": [
         {"field_name": 'event_data|TargetUserName', "values": log_data_ad.TargetUserNameExists},
         {"field_name": 'event_data|SubjectAdminUserName', "values": log_data_ad.SubjectAdminName},
     ]
     },
    {"log_type": ad_4722_account_enabled_log, "from_time": "15:32:00", "to_time": "15:33:00", "every": 60,
     "cross_fields": False,
     "add_logzio_security": False,
     "fields": [
         {"field_name": 'event_data|TargetUserName', "values": log_data_ad.TargetUserNameExists},
         {"field_name": 'event_data|SubjectAdminUserName', "values": log_data_ad.SubjectAdminName},
     ]
     },
    {"log_type": ad_4624_logon_success_log, "from_time": "15:40:00", "to_time": "15:41:00", "every": 60,
     "cross_fields": False,
     "add_logzio_security": True, "ip_field": 'event_data|IpAddress',
     "fields": [
         {"field_name": 'event_data|IpAddress', "values": log_data_ad.IpAddress},
         {"field_name": 'event_data|TargetUserName', "values": log_data_ad.TargetUserNameExists}
     ]
     }
 ]
