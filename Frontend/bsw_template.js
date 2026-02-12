const BSW_CONFIG_TEMPLATE = {
    "input_info": [
        {
            "input_id": 1,
            "redis": {
                "hostname": "redis",
                "port": 6379,
                "channelData": "data-plc-destacker-500",
                "username": null,
                "password": null,
                "db": 0,
                "keyStatus": "status-plc-destacker-500",
                "sleeping_time": 0.1,
                "output_status": {
                    "kind": "print",
                    "topic": null,
                    "hostname": null,
                    "port": null,
                    "username": null,
                    "password": null
                }
            }
        },
        {
            "input_id": 2,
            "redis": {
                "hostname": "redis",
                "port": 6379,
                "channelData": "data-plc-destacker-150",
                "username": null,
                "password": null,
                "db": 0,
                "keyStatus": "status-plc-destacker-150",
                "sleeping_time": 0.1,
                "output_status": {
                    "kind": "print",
                    "topic": null,
                    "hostname": null,
                    "port": null,
                    "username": null,
                    "password": null
                }
            }
        }
    ],
    "output_info": [
        {
            "influxdb": {
                "tags": [
                    "historyAlarm.aggr0",
                    "historyAlarm.code",
                    "historyAlarm.isFirst"
                ],
                "use_asp_name": false,
                "host": "influxdb",
                "port": 8086,
                "username": "40f",
                "password": "fCLgYTRSJHF4LjGedrHcl85x6",
                "ssl": false,
                "database": "MCC0f0bf29f3628469184e4e817319cc402",
                "measurement": "historyAlarm",
                "retention_policy": {
                    "name": "retention_prod",
                    "days": 900
                },
                "aspects_to_write": [
                    "historyAlarm"
                ]
            }
        },
        {
            "influxdb": {
                "tags": [
                    "stateTransition.aggr0"
                ],
                "use_asp_name": false,
                "host": "influxdb",
                "port": 8086,
                "username": "40f",
                "password": "fCLgYTRSJHF4LjGedrHcl85x6",
                "ssl": false,
                "database": "MCC0f0bf29f3628469184e4e817319cc402",
                "measurement": "stateTransition",
                "retention_policy": {
                    "name": "retention_prod",
                    "days": 900
                },
                "aspects_to_write": [
                    "stateTransition"
                ]
            }
        },
        {
            "influxdb": {
                "tags": [
                    "aggrData.aggr0"
                ],
                "use_asp_name": false,
                "host": "influxdb",
                "port": 8086,
                "username": "40f",
                "password": "fCLgYTRSJHF4LjGedrHcl85x6",
                "ssl": false,
                "database": "MCC0f0bf29f3628469184e4e817319cc402",
                "measurement": "aggrData",
                "retention_policy": {
                    "name": "retention_prod",
                    "days": 900
                },
                "aspects_to_write": [
                    "aggrData"
                ]
            }
        },
        {
            "influxdb": {
                "tags": [],
                "use_asp_name": false,
                "host": "influxdb",
                "port": 8086,
                "username": "40f",
                "password": "fCLgYTRSJHF4LjGedrHcl85x6",
                "ssl": false,
                "database": "MCC0f0bf29f3628469184e4e817319cc402",
                "measurement": "rawDataParams",
                "retention_policy": {
                    "name": "retention_raw",
                    "days": 365
                },
                "aspects_to_write": [
                    "rawDataParams"
                ]
            }
        },
        {
            "influxdb": {
                "tags": [],
                "use_asp_name": false,
                "host": "influxdb",
                "port": 8086,
                "username": "40f",
                "password": "fCLgYTRSJHF4LjGedrHcl85x6",
                "ssl": false,
                "database": "MCC0f0bf29f3628469184e4e817319cc402",
                "measurement": "rawData500",
                "retention_policy": {
                    "name": "retention_raw",
                    "days": 365
                },
                "aspects_to_write": [
                    "rawData500"
                ]
            }
        },
        {
            "influxdb": {
                "tags": [],
                "use_asp_name": false,
                "host": "influxdb",
                "port": 8086,
                "username": "40f",
                "password": "fCLgYTRSJHF4LjGedrHcl85x6",
                "ssl": false,
                "database": "MCC0f0bf29f3628469184e4e817319cc402",
                "measurement": "rawData150",
                "retention_policy": {
                    "name": "retention_raw",
                    "days": 365
                },
                "aspects_to_write": [
                    "rawData150"
                ]
            }
        },
        {
            "influxdb": {
                "tags": [
                    "historyCycle.aggr0"
                ],
                "use_asp_name": false,
                "host": "influxdb",
                "port": 8086,
                "username": "40f",
                "password": "fCLgYTRSJHF4LjGedrHcl85x6",
                "ssl": false,
                "database": "MCC0f0bf29f3628469184e4e817319cc402",
                "measurement": "historyCycle",
                "retention_policy": {
                    "name": "retention_prod",
                    "days": 900
                },
                "aspects_to_write": [
                    "historyCycle"
                ]
            }
        },
        {
            "influxdb": {
                "tags": [
                    "historyParams.aggr0",
                    "historyParams.code"
                ],
                "use_asp_name": false,
                "host": "influxdb",
                "port": 8086,
                "username": "40f",
                "password": "fCLgYTRSJHF4LjGedrHcl85x6",
                "ssl": false,
                "database": "MCC0f0bf29f3628469184e4e817319cc402",
                "measurement": "historyParams",
                "retention_policy": {
                    "name": "retention_prod",
                    "days": 900
                },
                "aspects_to_write": [
                    "historyParams"
                ]
            }
        },
        {
            "json": {
                "use_asp_name": true,
                "snapshot": true,
                "file_path": "mind",
                "snapshot_name": "rawData500",
                "aspects_to_write": [
                    "rawData500"
                ]
            }
        },
        {
            "json": {
                "use_asp_name": true,
                "snapshot": true,
                "file_path": "mind",
                "snapshot_name": "rawData150",
                "aspects_to_write": [
                    "rawData150"
                ]
            }
        },
        {
            "json": {
                "use_asp_name": true,
                "snapshot": true,
                "file_path": "mind",
                "snapshot_name": "stateTransition",
                "aspects_to_write": [
                    "stateTransition"
                ]
            }
        }
    ],
    "aspects": [
        {
            "input_id": 1,
            "name": "aggrData",
            "mapping_file": null,
            "first_write": false,
            "update": 300,
            "breakers": [],
            "datapoint": []
        },
        {
            "input_id": 1,
            "name": "stateTransition",
            "mapping_file": null,
            "first_write": false,
            "update": 60,
            "breakers": [],
            "datapoint": []
        },
        {
            "input_id": 1,
            "name": "historyCycle",
            "mapping_file": null,
            "first_write": false,
            "update": "never",
            "breakers": [],
            "datapoint": []
        },
        {
            "input_id": 1,
            "name": "historyParams",
            "mapping_file": null,
            "first_write": false,
            "update": {
                "write_if_up": {
                    "update_kind": 0,
                    "bool_name": "activeParams.paramsResume"
                }
            },
            "breakers": [],
            "datapoint": []
        },
        {
            "input_id": 1,
            "name": "activeParams",
            "mapping_file": null,
            "first_write": true,
            "update": "on_var",
            "breakers": [],
            "datapoint": []
        },
        {
            "input_id": 1,
            "name": "rawDataParams",
            "mapping_file": null,
            "first_write": true,
            "update": "never",
            "breakers": [],
            "datapoint": [
                {
                    "name": "param_0",
                    "type": "double",
                    "input_data": { "var": "Press_Set_Billet_Length" },
                    "used_func": "doNothing"
                },
                {
                    "name": "param_1",
                    "type": "double",
                    "input_data": { "var": "Set_ButtEnd_Length" },
                    "used_func": "doNothing"
                },
                {
                    "name": "param_2",
                    "type": "double",
                    "input_data": { "var": "Set_Extrusion_Speed" },
                    "used_func": "doNothing"
                }
            ]
        },
        {
            "input_id": 1,
            "name": "historyAlarm",
            "mapping_file": null,
            "first_write": false,
            "update": {
                "write_if_up": {
                    "update_kind": 0,
                    "bool_name": "activeAlarms.alarmsResume"
                }
            },
            "breakers": [],
            "datapoint": []
        }
    ],
    "general_param": {
        "output_frequency": 5,
        "init_string": "",
        "generate_number_mapping": false,
        "truncate_len": 56,
        "log_info": "info",
        "verbose": true,
        "equalizer": false,
        "dummyPickle": {
            "active": false,
            "destination": "mind/rawPickles/",
            "hourPeriod": 24
        },
        "persistence": {
            "active": false,
            "period": 120,
            "folder_path": "persistence",
            "time_tollerance": 7200
        }
    }
};
