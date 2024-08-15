# Fixed bad "phpp" extensions to "php" in the file name

exec { 'fix_using_strace':
  command => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
  path    => '/usr/local/bin:/bin/',
}
