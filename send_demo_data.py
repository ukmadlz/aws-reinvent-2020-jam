import requests
import json
import time
import copy
import sys
import os
import datetime
import logging
sys.path.insert(0, 'demo-ad')
# sys.path.insert(0, 'demo-ssh')
sys.path.insert(0, 'demo-nginx')
sys.path.insert(0, 'demo-hashi_vault')
from logs_template import logzio_security
from program import logs_program
from program_ad import logs_program_ad
# from program_ad2 import logs_program_ad2
# from program_nginx import logs_program_nginx
from program_vault import logs_program_vault

whole_seconds = 1

def send_logs(logs):
    if len(logs) == 0:
        return
    url = sys.argv[1]
    logztoken = sys.argv[2]
    logging.info(str(datetime.datetime.now()) + " sending " + str(len(logs)) + " logs size: " + str(sys.getsizeof(logs)))
    data_to_send = ""
    for msg in logs:
        data_to_send += "\n" + json.dumps(msg)
    try:
        result = requests.post(url, data=data_to_send, params={"token": logztoken})
        if result.status_code == 200:
            logging.info(str(datetime.datetime.now().time()) + " Successfully sent " + str(len(logs)) + " logs")
        else:
            logging.error(str(datetime.datetime.now().time()) + " error " + str(result.status_code) + ", couldn't send " + str(len(logs)) + " logs")
    except:
        logging.error(str(datetime.datetime.now().time()) + " error sending logs: " + str(logs))


def get_logs_for_program(prog):
    if prog['cross_fields']:
        temp_logs = [copy.deepcopy(prog['log_type'])]
        for field in prog['fields']:
            concat_logs = []
            for value in field['values']:
                for log in temp_logs:
                    new_log = copy.deepcopy(log)
                    write_to_nested_dict(new_log, field['field_name'], value)
                    concat_logs.append(new_log)
            temp_logs = concat_logs
    else:
        temp_logs = []
        values_count = min([len(field['values']) for field in prog['fields']])

        rolling_values = prog.get('rolling_values', values_count)
        if 'rolling_offset' in prog and prog['rolling_offset'] > 0:
            prog['rolling_offset'] += 1
        else:
            prog['rolling_offset'] = 0
        offset = prog['rolling_offset'] % values_count
        for i in range(rolling_values):
            new_log = copy.deepcopy(prog['log_type'])
            for field in prog['fields']:
                write_to_nested_dict(new_log, field['field_name'], field['values'][i + offset])
            temp_logs.append(new_log)
    return temp_logs

def get_logs_for_time():
    result_logs = []
    # Select the user story as follows:
    #        SSH demo - logs_program
    #         AD demo - logs_program_ad
    #         AD2 demo #2 - logs_program_ad2
    # example:  for AD demo only
    #             for prog in logs_program_ad:
    #             for prog in logs_program + logs_program_ad:
    for prog in logs_program_vault + logs_program + logs_program_ad:
        from_time = datetime.time(int(prog['from_time'].split(":")[0]), int(prog['from_time'].split(":")[1]), int(prog['from_time'].split(":")[2]))
        to_time = datetime.time(int(prog['to_time'].split(":")[0]), int(prog['to_time'].split(":")[1]), int(prog['to_time'].split(":")[2]))
        every = prog['every']
        simulate_time = datetime.datetime.now() + delta_time
        if to_time > from_time:
            generate = from_time <= simulate_time.time() < to_time
        else:
            generate = simulate_time.time() >= from_time or simulate_time.time() < to_time
        generate = generate and whole_seconds % every == 0
        if generate:
            result_logs += get_logs_for_program(prog)
    return result_logs


def write_to_nested_dict(dictionary, key, value):
    try:
        keys = key.split("|")
        for inner_key in range(len(keys) - 1):
            dictionary = dictionary[keys[inner_key]]
        dictionary[keys[len(keys) - 1]] = value
    except:
        logging.error("cant find key " + key + " in dictionary")


def read_from_nested_dict(dictionary, key):
    keys = key.split("|")
    for inner_key in range(len(keys) - 1):
        dictionary = dictionary[keys[inner_key]]
    return dictionary[keys[len(keys) - 1]]


def write_logs_to_file(logs):
    with open("app.log", "a") as myfile:
        for log in logs:
            log_line = "{}\n".format(json.dumps(log))
            myfile.write(log_line)


if not os.path.exists('logger'):
    os.makedirs('logger')
delta_time = (datetime.datetime.strptime(sys.argv[1], '%H:%M:%S') if len(sys.argv) > 1 else datetime.datetime.now()) - datetime.datetime.now()

logging.basicConfig(filename='logger/events.log', level=logging.DEBUG)
while True:
    logs_to_send = get_logs_for_time()
    write_logs_to_file(logs_to_send)
    for log in logs_to_send:
        logging.info(log)
    time.sleep(1)
    whole_seconds += 1
