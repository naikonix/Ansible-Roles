backend "file" {
        path = "{{ vault_data }}"
}

listener "tcp" {
        tls_disable = 0
        tls_cert_file = "/etc/letsencrypt/live/example.com/fullchain.pem"
        tls_key_file = "/etc/letsencrypt/live/example.com/privkey.pem"

}
