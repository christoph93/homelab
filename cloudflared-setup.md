https://www.sakowi.cz/blog/cloudflared-docker-compose-tutorial



    ---
    version: "3.1"
    services:
        cloudflared:
            image: cloudflare/cloudflared:latest
            user: "0:0"
            volumes:
            - ./config:/root/.cloudflared
            #command: tunnel login
            #command: tunnel create my_tunnel
            #command: tunnel --no-autoupdate run


config.yml

    tunnel: 22df2ed6-1e93-4138-9464-95ea98ad5527


    ingress:
    - hostname: vaultwarden.ccalifice.com
        service: http://192.168.1.202:8080
    - service: http_status:404



Create CNAME DNS record with subdomain pointing to \<UUID>.cfargotunnel.com