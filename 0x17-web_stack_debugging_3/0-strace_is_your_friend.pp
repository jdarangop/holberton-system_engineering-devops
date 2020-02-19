# puppet to fix bug

file_line { 'Replace line broken':
  path    => '/var/www/html/wp-settings.php',
  match   => 'phpp',
  line    => 'php',
  replace => 'true',
}
