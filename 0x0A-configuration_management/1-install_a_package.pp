# installing puppet link
package { 'install flask':
    ensure   => '2.1.0',
    name     => 'flask',
    provider => 'pip3',
}
