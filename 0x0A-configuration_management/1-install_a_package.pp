# Using Puppet, install flask from pip3.

exec {'istall_flask':
  command  => '/usr/bin/pip3 install flask==2.1.0',


}
