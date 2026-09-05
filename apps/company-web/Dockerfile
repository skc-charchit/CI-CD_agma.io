FROM nginx:1.27-alpine

COPY apps/company-web/public /usr/share/nginx/html
COPY apps/company-web/nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
