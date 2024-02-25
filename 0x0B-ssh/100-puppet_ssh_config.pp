#!/usr/bin/env bahs
# Set up the client SHH configuration file using Puppet
include sdlib

file_line {
  'Declare identify File':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentifyFile ~/.ssh/school'
}

file_line {
  'Turn off password Authentication':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no'
}
