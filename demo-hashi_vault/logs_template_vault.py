vault_group_creation_log = {
  "type": "hashi_vault",
  "_source": {
    "request": {
      "client_token": "s.Ubtbu3BkWLROmnZ8lGwdAXKn",
      "client_token_accessor": "noCiri5z03Mja0daCI2xRvD4",
      "namespace": {
        "id": "root"
      },
      "path": "identity/group", # the path for the created group (groups will be created only under this path
      "data": {
        "name": "Smadi_Group", # the requested name for the created group
        "type": "internal"  # the type of the created group - can be onlhy internal or external for the puprose of the story its better that some of the malicious activity will create external groups as well
      },
      "remote_address": "127.0.0.1",
      "id": "54e75929-b59c-7349-076b-4869c16eb430",
      "operation": "update"
    },
    "log": {
      "offset": 15548,
      "file": {}
    },
    "auth": {
      "client_token": "s.Ubtbu3BkWLROmnZ8lGwdAXKn",
      "accessor": "noCiri5z03Mja0daCI2xRvD4",
      "display_name": "root", #the name of the user that created the group ( the same one as in the request filed)
      "policies": [ # the policies that are assigned to user that created the group.
        "root"
      ],
      "token_policies": [
        "root"
      ],
      "token_type": "service"
    },
    "@metadata": {
      "beat": "filebeat",
      "type": "_doc",
      "version": "7.3.0"
    },
    "source": "/home/ubuntu/Desktop/vault_audit_smadi.log",
    "type": "hashi_vault",
    "hashi_type": "response",
    "tags": [
      "beats-5015"
    ],
    "input": {
      "type": "log"
    },
    "@timestamp": "2019-09-03T14:55:16.384Z",
    "ecs": {
      "version": "1.0.1"
    },
    "response": {
      "data": {
        "id": "be6c8687-718e-1e26-52d7-0ed32cb08e35",
        "name": "Smadi_Group" # the name of the created group
      }
    },
    "beat_agent": {
      "ephemeral_id": "5e5f1cc7-19c7-4338-94bb-9e39ec596514",
      "hostname": "ubuntu-doris",
      "id": "107284ef-95c7-4b82-a2e9-cdddcb3a7e02",
      "version": "7.3.0",
      "type": "filebeat"
    },
    "time": "2019-09-03T14:55:09.672901495Z"
  },
  "fields": {
    "@timestamp": [
      1567522516384
    ]
  },
  "highlight": {
    "source": [
      "@kibana-highlighted-field@/home/ubuntu/Desktop/vault_audit_smadi.log@/kibana-highlighted-field@"
    ],
    "type": [
      "@kibana-highlighted-field@hashi_vault@/kibana-highlighted-field@"
    ]
  }
}

vault_permission_denied_log = {
  "type": "hashi_vault",
  "_source": {
    "request": {
      "id": "99b19dbd-5487-c617-0e2f-247329ff400b",
      "operation": "update",
      "client_token": "s.vIzyj9PSjdQ5NvZ9P0MsLV10",
      "client_token_accessor": "nPsUoFJT4GhCOAae5rALcC9X",
      "namespace": {
        "id": "root"
      },
      "path": "sys/mounts/ssh", # the path of the secret that the user tried to enable
      "data": {
        "path": "ssh", # the name of the secret
        "type": "ssh", # the type of the secret
        "config": {},
        "generate_signing_key": 1
      },
      "remote_address": "127.0.0.1" # the remote address from where the user connected
    },
    "log": {
      "file": {},
      "offset": 121828
    },
    "auth": {
      "entity_id": "85c0d553-2047-c3ed-259f-5ef8218e2144",
      "token_type": "service",
      "client_token": "s.vIzyj9PSjdQ5NvZ9P0MsLV10", # the users token
      "accessor": "nPsUoFJT4GhCOAae5rALcC9X",
      "display_name": "userpass-smadi_a", # the user that tried to perform the action (the methon of authentiocation will always be before the username)
      "policies": [ # the policies that the user have
        "default"
      ],
      "token_policies": [
        "default"
      ],
      "metadata": {
        "username": "smadi_a"
      }
    },
    "@metadata": {
      "beat": "filebeat",
      "type": "_doc",
      "version": "7.3.0"
    },
    "source": "/home/ubuntu/Desktop/vault_audit_smadi.log",
    "type": "hashi_vault",
    "error": "1 error occurred:\n\t* permission denied\n\n", # the permission denied action aka unauthorised action error
    "hashi_type": "response",
    "tags": [
      "beats-5015"
    ],
    "input": {
      "type": "log"
    },
    "@timestamp": "2019-09-03T15:51:16.247Z",
    "ecs": {
      "version": "1.0.1"
    },
    "response": {
      "data": {
        "error": "1 error occurred:\n\t* permission denied\n\n" # the permission denied action aka unauthorised action error
      }
    },
    "beat_agent": {
      "type": "filebeat",
      "ephemeral_id": "5e5f1cc7-19c7-4338-94bb-9e39ec596514",
      "hostname": "ubuntu-doris",
      "id": "107284ef-95c7-4b82-a2e9-cdddcb3a7e02",
      "version": "7.3.0"
    },
    "time": "2019-09-03T15:51:08.575945808Z"
  },
  "fields": {
    "@timestamp": [
      1567525876247
    ]
  },
  "highlight": {
    "source": [
      "@kibana-highlighted-field@/home/ubuntu/Desktop/vault_audit_smadi.log@/kibana-highlighted-field@"
    ],
    "type": [
      "@kibana-highlighted-field@hashi_vault@/kibana-highlighted-field@"
    ],
    "error": [
      "@kibana-highlighted-field@1 error occurred:\n\t* permission denied\n\n@/kibana-highlighted-field@"
    ],
    "hashi_type": [
      "@kibana-highlighted-field@response@/kibana-highlighted-field@"
    ]
  },
  "sort": [
    1567525876247
  ]
}

vault_alias_assigned_log = {
  "type": "hashi_vault",
  "_source": {
    "request": {
      "path": "identity/entity-alias", # the alias path ( will always be the same when creating an alias)
      "data": {
        "canonical_id": "13125336-1248-0612-5815-363a7811d286", # the id of the user that the alias was assigned to
        "mount_accessor": "auth_token_b91c1c68",
        "name": "Smadi_A" # the name of the created alias
      },
      "remote_address": "127.0.0.1", # the remote address from where the user created the alias
      "id": "8133a80b-d519-3f38-31e7-ac7b1cd5e7ca",
      "operation": "update",
      "client_token": "s.Ubtbu3BkWLROmnZ8lGwdAXKn",
      "client_token_accessor": "noCiri5z03Mja0daCI2xRvD4",
      "namespace": {
        "id": "root"
      }
    },
    "log": {
      "file": {},
      "offset": 70420
    },
    "auth": {
      "token_type": "service",
      "client_token": "s.Ubtbu3BkWLROmnZ8lGwdAXKn",
      "accessor": "noCiri5z03Mja0daCI2xRvD4",
      "display_name": "root", # the name of the user that created the alias
      "policies": [ # the policies that the user have
        "root"
      ],
      "token_policies": [
        "root"
      ]
    },
    "@metadata": {
      "beat": "filebeat",
      "type": "_doc",
      "version": "7.3.0"
    },
    "source": "/home/ubuntu/Desktop/vault_audit_smadi.log",
    "type": "hashi_vault",
    "hashi_type": "response",
    "tags": [
      "beats-5015"
    ],
    "input": {
      "type": "log"
    },
    "@timestamp": "2019-09-03T15:07:15.451Z",
    "ecs": {
      "version": "1.0.1"
    },
    "response": {
      "data": {
        "canonical_id": "13125336-1248-0612-5815-363a7811d286",
        "id": "b1d0d5e3-9656-f634-47d8-ff0a1cfab7e5"
      }
    },
    "beat_agent": {
      "id": "107284ef-95c7-4b82-a2e9-cdddcb3a7e02",
      "version": "7.3.0",
      "type": "filebeat",
      "ephemeral_id": "5e5f1cc7-19c7-4338-94bb-9e39ec596514",
      "hostname": "ubuntu-doris"
    },
    "time": "2019-09-03T15:07:11.974635314Z"
  },
  "fields": {
    "@timestamp": [
      1567523235451
    ]
  },
  "highlight": {
    "source": [
      "@kibana-highlighted-field@/home/ubuntu/Desktop/vault_audit_smadi.log@/kibana-highlighted-field@"
    ],
    "type": [
      "@kibana-highlighted-field@hashi_vault@/kibana-highlighted-field@"
    ],
    "request.path": [
      "@kibana-highlighted-field@identity/entity-alias@/kibana-highlighted-field@"
    ],
    "hashi_type": [
      "@kibana-highlighted-field@response@/kibana-highlighted-field@"
    ]
  },
  "sort": [
    1567523235451
  ]
}

vault_entity_creation_log = {
  "type": "hashi_vault",
  "_source": {
    "request": {
      "client_token_accessor": "noCiri5z03Mja0daCI2xRvD4",
      "namespace": {
        "id": "root"
      },
      "path": "identity/entity", # path for the entity creation
      "data": {
        "disabled": 0,
        "name": "Smadi" # name of the created entity
      },
      "remote_address": "127.0.0.1", # the remote address from where the user created the entity ( forgot to mention in the last 2 logs)
      "id": "2c1cbed3-65f1-40a4-e90f-9a1ad46f39ed",
      "operation": "update", # in entity creation the operation will always be update
      "client_token": "s.Ubtbu3BkWLROmnZ8lGwdAXKn"
    },
    "auth": {
      "accessor": "noCiri5z03Mja0daCI2xRvD4",
      "display_name": "root", # the name of the user that created the entity
      "policies": [ # the policies that are assigned to the user
        "root"
      ],
      "token_policies": [
        "root"
      ],
      "token_type": "service",
      "client_token": "s.Ubtbu3BkWLROmnZ8lGwdAXKn"
    },
    "log": {
      "file": {},
      "offset": 63506
    },
    "@metadata": {
      "beat": "filebeat",
      "type": "_doc",
      "version": "7.3.0"
    },
    "source": "/home/ubuntu/Desktop/vault_audit_smadi.log",
    "type": "hashi_vault",
    "hashi_type": "response",
    "tags": [
      "beats-5015"
    ],
    "input": {
      "type": "log"
    },
    "@timestamp": "2019-09-03T15:07:00.448Z",
    "ecs": {
      "version": "1.0.1"
    },
    "response": {
      "data": {
        "id": "13125336-1248-0612-5815-363a7811d286",
        "name": "Smadi"
      }
    },
    "beat_agent": {
      "type": "filebeat",
      "ephemeral_id": "5e5f1cc7-19c7-4338-94bb-9e39ec596514",
      "hostname": "ubuntu-doris",
      "id": "107284ef-95c7-4b82-a2e9-cdddcb3a7e02",
      "version": "7.3.0"
    },
    "time": "2019-09-03T15:06:57.073589473Z"
  },
  "fields": {
    "@timestamp": [
      1567523220448
    ]
  },
  "highlight": {
    "source": [
      "@kibana-highlighted-field@/home/ubuntu/Desktop/vault_audit_smadi.log@/kibana-highlighted-field@"
    ],
    "type": [
      "@kibana-highlighted-field@hashi_vault@/kibana-highlighted-field@"
    ],
    "request.path": [
      "@kibana-highlighted-field@identity/entity@/kibana-highlighted-field@"
    ]
  },
  "sort": [
    1567523220448
  ]
}

vault_wrong_authentication_method_log = {
    "type": "hashi_vault",
    "_source": {
        "request": {
            "id": "99b19dbd-5487-c617-0e2f-247329ff400b",
            "operation": "update",
            "client_token": "s.vIzyj9PSjdQ5NvZ9P0MsLV10",
            "client_token_accessor": "nPsUoFJT4GhCOAae5rALcC9X",
            "namespace": {
                "id": "root"
            },
            "path": "sys/mounts/ssh",  # the path of the secret that the user tried to enable
            "data": {
                "path": "ssh",  # the name of the secret
                "type": "ssh",  # the type of the secret
                "config": {},
                "generate_signing_key": 1
            },
            "remote_address": "127.0.0.1"  # the remote address from where the user connected
        },
        "log": {
            "file": {},
            "offset": 121828
        },
        "auth": {
            "entity_id": "85c0d553-2047-c3ed-259f-5ef8218e2144",
            "token_type": "service",
            "client_token": "s.vIzyj9PSjdQ5NvZ9P0MsLV10",  # the users token
            "accessor": "nPsUoFJT4GhCOAae5rALcC9X",
            "display_name": "userpass-smadi_a",
            # the user that tried to perform the action (the methon of authentiocation will always be before the username)
            "policies": [  # the policies that the user have
                "default"
            ],
            "token_policies": [
                "default"
            ],
            "metadata": {
                "username": "smadi_a"
            }
        },
        "@metadata": {
            "beat": "filebeat",
            "type": "_doc",
            "version": "7.3.0"
        },
        "source": "/home/ubuntu/Desktop/vault_audit_smadi.log",
        "type": "hashi_vault",
        "error": "1 error occurred:\n\t* permission denied\n\n",
        # the permission denied action aka unauthorised action error
        "hashi_type": "response",
        "tags": [
            "beats-5015"
        ],
        "input": {
            "type": "log"
        },
        "@timestamp": "2019-09-03T15:51:16.247Z",
        "ecs": {
            "version": "1.0.1"
        },
        "response": {
            "data": {
                "error": "1 error occurred:\n\t* permission denied\n\n"
                # the permission denied action aka unauthorised action error
            }
        },
        "beat_agent": {
            "type": "filebeat",
            "ephemeral_id": "5e5f1cc7-19c7-4338-94bb-9e39ec596514",
            "hostname": "ubuntu-doris",
            "id": "107284ef-95c7-4b82-a2e9-cdddcb3a7e02",
            "version": "7.3.0"
        },
        "time": "2019-09-03T15:51:08.575945808Z"
    },
    "fields": {
        "@timestamp": [
            1567525876247
        ]
    },
    "highlight": {
        "source": [
            "@kibana-highlighted-field@/home/ubuntu/Desktop/vault_audit_smadi.log@/kibana-highlighted-field@"
        ],
        "type": [
            "@kibana-highlighted-field@hashi_vault@/kibana-highlighted-field@"
        ],
        "error": [
            "@kibana-highlighted-field@1 error occurred:\n\t* permission denied\n\n@/kibana-highlighted-field@"
        ],
        "hashi_type": [
            "@kibana-highlighted-field@response@/kibana-highlighted-field@"
        ]
    },
    "sort": [
        1567525876247
    ]
}

vault_failed_authentication_log = {
  "type": "hashi_vault",
  "_source": {
    "request": {
      "id": "591f8427-723f-2051-1f7d-436f3e129642",
      "operation": "update", # the operation will always be update in this senario
      "namespace": {
        "id": "root"
      },
      "path": "auth/userpass/login/Smadi_A", # the user that tried to login
      "data": {
        "password": "123"
      },
      "remote_address": "127.0.0.1" # the address from where the user tried to authinticate
    },
    "log": {
      "offset": 106566,
      "file": {}
    },
    "auth": {
      "token_type": "default"
    },
    "@metadata": {
      "beat": "filebeat",
      "type": "_doc",
      "version": "7.3.0"
    },
    "source": "/home/ubuntu/Desktop/vault_audit.log",
    "type": "hashi_vault",
    "hashi_type": "response",
    "tags": [
      "beats-5015"
    ],
    "input": {
      "type": "log"
    },
    "@timestamp": "2019-09-03T15:47:14.201Z",
    "ecs": {
      "version": "1.0.1"
    },
    "response": {
      "data": {
        "error": "invalid username or password" # the failed authentication error
      }
    },
    "beat_agent": {
      "type": "filebeat",
      "ephemeral_id": "5e5f1cc7-19c7-4338-94bb-9e39ec596514",
      "hostname": "ubuntu-org",
      "id": "107284ef-95c7-4b82-a2e9-cdddcb3a7e02",
      "version": "7.3.0"
    },
    "time": "2019-09-03T15:47:07.367542041Z"
  },
  "fields": {
    "@timestamp": [
      1567525634201
    ]
  },
  "highlight": {
    "source": [
      "@kibana-highlighted-field@/home/ubuntu/Desktop/vault_audit.log@/kibana-highlighted-field@"
    ],
    "type": [
      "@kibana-highlighted-field@hashi_vault@/kibana-highlighted-field@"
    ],
    "response.data.error": [
      "@kibana-highlighted-field@invalid username or password@/kibana-highlighted-field@"
    ],
    "hashi_type": [
      "@kibana-highlighted-field@response@/kibana-highlighted-field@"
    ]
  },
  "sort": [
    1567525634201
  ]
}