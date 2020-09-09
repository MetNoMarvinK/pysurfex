import unittest
import surfex
import os
import toml
import json
from datetime import datetime


class TestSubmit(unittest.TestCase):
    exp = "EXP"
    hm_wd = "/tmp/host0/hm_wd/" + exp
    os.makedirs(hm_wd, exist_ok=True)
    hm_rev = os.getcwd()
    # env_system = hm_wd + "/Env_system"

    oper_version = "test"
    domain = None
    levels = None
    host = "pc4384-test"

    ecf_port = "44855"
    ecf_logport = "44855"
    hm_conf = hm_rev

    env_submit_file = hm_conf + "/config/submit/" + host + ".json"

    # Set progress
    dtg = datetime(2020, 6, 9, 9)
    progress = {"DTG": dtg.strftime("%Y%m%d%H")}
    progress_pp = {"DTGPP": dtg.strftime("%Y%m%d%H")}
    progress = surfex.Progress(progress, progress_pp)

    env_system = hm_conf + "/config/system/" + host + ".toml"
    system = surfex.SystemFromFile(env_system, exp)

    experiment_is_locked = False
    sfx_exp = surfex.Exp(exp, hm_wd, hm_rev, hm_conf, experiment_is_locked, env_submit=env_submit_file,
                         progress=progress, system=system)

    stream = None
    all_merged_settings = sfx_exp.merge_toml_env_from_config_dicts()
    merged_config, member_merged_config = sfx_exp.process_merged_settings(all_merged_settings, "0")
    config = surfex.Configuration(system, merged_config, member_merged_config,
                                  config_dir=hm_conf, stream=stream)

    ecf_name = "/" + exp + "/Forecasting/Forecast"
    ecf_tryno = "1"
    ecf_pass = "dummy_password"
    ecf_rid = "12345"

    submission_defs = hm_conf + "/config/submit/" + host + ".json"
    submission_defs = json.load(open(submission_defs, "r"))
    # submit = surfex.EcflowSubmitTask(config, ecf_name, ecf_tryno, ecf_pass, ecf_rid, dtg, submission_defs,
    #                                 ensmbr=None, complete=None)
    ### submit.write_job()
