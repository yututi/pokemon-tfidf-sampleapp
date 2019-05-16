## Start of configuration add by letsencrypt container
location ^~ /.well-known/acme-challenge/ {
    auth_basic off;
    allow all;
    root /usr/share/nginx/html;
    try_files $uri =404;
    break;
}
## End of configuration add by letsencrypt container

gzip on;
gzip_types  image/png image/gif image/jpeg text/javascript text/css;
gzip_min_length 1000;

location /assets/ {
    alias /app/static/;
}