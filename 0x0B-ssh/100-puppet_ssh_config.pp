# Set up the client SSH configuration file using Puppet
include stdlib

file_line { 'Declare identity file':  # Added comment
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/school'
}

file_line { 'Turn off password authentication': # Added comment
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no'
}
