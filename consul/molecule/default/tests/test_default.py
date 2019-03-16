import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_host('vagrant')


def test_consul_is_installed(File):
    consul = File("/usr/local/bin/consul")
    assert consul.exists


def test_consul_template(File):
    f = File("/etc/consul.d/config.json")
    assert f.exists
    assert f.is_file


def test_consul_directory(File):
    f = File("/tmp/consul")
    assert f.exists
    assert f.is_directory
