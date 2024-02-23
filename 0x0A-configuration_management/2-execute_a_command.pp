# Using Puppet, create a manifest that kills a process named killmenow.
exec {
  'killmenow':
    command => '/bin/pkill -n killmenow',
    path    => ['/bin','/usr/bin'],

}
