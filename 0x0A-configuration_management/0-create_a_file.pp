# Create a file in /tmp using puppet
file {'school':
ensure    => 'present',
  content => 'I love Puppet',
  owner   => 'www-data',
  group   => 'www-data',
  path    => '/tmp/school',
  mode    => '0744',
}
