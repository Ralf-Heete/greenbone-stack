FROM nginx:latest

# Kopieren der SSL/TLS-Zertifikate
COPY ./cert.crt /etc/nginx/cert.crt
COPY ./cert.key /etc/nginx/cert.key

# Ersetzen der Standard-Nginx-Konfigurationsdatei
COPY ./ngnix.conf /etc/nginx/nginx.conf

EXPOSE 443

CMD ["nginx", "-g", "daemon off;"]

