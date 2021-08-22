import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_serf_is_installed(host):
    assert host.exists('serf')


def test_serf_running_and_enabled(host):
    service = host.service('serf')
    assert service.is_running
    assert service.is_enabled


def test_serf_is_listen(host):
    assert host.socket('tcp://127.0.0.1:7373').is_listening
#    assert host.socket('tcp://127.0.0.1:7946').is_listening
