# puppet to fix bug

exec { 'Replace String':
  command => 'sudo sed -i "s/class-wp-locale.phpp/class-wp-locale.php/g" /var/www/html/wp-settings.php',
}
