import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')

user = 'consul_user'
group = 'consul_group'
dir = 'consul_dir'
ex_file = 'bin/consul'
cfg = 'consul_config'
cfg_file = 'config.json'
service_name = 'consul'

@pytest.fixture(scope='module')
def ans_var(host):
  return host.ansible(
    'include_vars', '../../defaults/main.yml'
  )['ansible_facts']


def test_group(host, ans_var):
    test_group = host.group(ans_var[group])
    assert test_group.exists


def test_user(host, ans_var):
    test_user = host.user(ans_var[user])
    assert test_user.exists


def test_directory(host, ans_var):
    test_dir = host.file(ans_var[dir])
    assert test_dir.exists
    assert test_dir.is_directory


def test_file_installed(host, ans_var):
    test_file = host.file(ans_var[dir] + '/' + ex_file)
    assert test_file.exists
    assert test_file.user == ans_var[user]
    assert test_file.group == ans_var[group]


def test_template(host, ans_var):
    test_cfg = host.file(ans_var[cfg] + '/' + cfg_file)
    assert test_cfg.exists
    assert test_cfg.is_file


def test_consul_service(host):
    service = host.service(service_name)
    assert service.is_running
    assert service.is_enabled
