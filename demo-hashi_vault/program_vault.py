from logs_template_vault import vault_alias_assigned_log, vault_group_creation_log, vault_entity_creation_log, vault_failed_authentication_log, vault_wrong_authentication_method_log, vault_permission_denied_log
import log_data_vault

logs_program_vault = [

    ##################################################################################### 
    # User Story
    #
    # Benign activities     10:00-17:00
    # Malicious activities  3:00 - 5:00
    #
    #  10:00 - 10:30     Created 3 groups
    #                   Created 3 policies
    #                   Each policy was assigned to 1 group
    #  10:45 - 11:15     3 new entities were created
    #                   3 new aliases were created
    #
    #   3:00 - 3:30       Authentication attempts from malicious IPs,  every minute 5 different IPs
    #  10:00 - 17:00      Authentication attempts from benign IPs -  every 30 minutes one IP is authenticated - total 20 IPs
    #   3:00 - 3:30       Failed authentication from malicious IPs,  every minute 5 different IPs
    #  10:00 - 17:00      Failed authentication  from benign IPs -  every 30 minutes one IP is authenticated - total 20 IPs
    #   3:00 - 3:10       A single user tries to login and Fails - it can be by a tool (so every 5 seconds) or manual (every 2 minutes) ???
    #   4:00 - 4:30       Unauthorized action,  at least 3 different actions,  every 5 minutes 1 action
    #
    # List of logs:
    #         vault_group_creation_log
    #         vault_permission_denied_log
    #         vault_alias_assigned_log
    #         vault_entity_creation_log
    #         vault_wrong_authentication_method_log
    #         vault_failed_authentication_log
    ##################################################################################### 

    #
    {"log_type": vault_failed_authentication_log, "from_time": "03:00:00", "to_time": "03:30:00", "every": 60*1, "cross_fields": False,
     "add_logzio_security": True, "ip_field": '_source|request|remote_address',
     "fields": [
         {"field_name": '_source|request|path', "values": log_data_vault.vault_attacker_user},
         {"field_name": '_source|request|remote_address', "values": log_data_vault.vault_attackers}
     ]
     }
]
