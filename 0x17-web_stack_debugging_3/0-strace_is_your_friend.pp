# puppet to fix bug

exec { 'Replace String':
  command => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
}
