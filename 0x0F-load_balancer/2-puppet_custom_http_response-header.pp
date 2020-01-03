# Set header with puppet

package { 'nginx':
  provider => 'gem',
}

file_line { 'Set header':
  path    => '/etc/nginx/sites-available/default',
  match   => 'location \/ {',
  line    => 'location \/ {\n\t\tadd_header X-Served-By \$hostname;\n',
  replace => 'true',
}

exec { 'service nginx restart':
  command => 'service nginx restart',
  path    => '/usr/bin/',
}
