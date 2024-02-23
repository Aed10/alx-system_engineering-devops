# Create a file in /tmp using puppet
file {'/tmp/school':
  content => 'I love Puppet',
  owner   => 'www-data',
  group   => 'www-data',

}
