kong = dict(
    name = "API Gateway",
    req_per_minute = "How many requests per minute are allowed? [{}]: ",
    req_per_hour = "How many requests per hour are allowed? [{}]: ",
    pg_user = "{} postgres username [{}]: ",
    pg_password = "{} postgres password [{}]: "
)

devm = dict(
    name = "Device Manager",
    pg_user = "{} postgres username [{}]: ",
    pg_password = "{} postgres password [{}]: "
)

auth = dict(
    name = "Authentication System",
    replicas = "How many replicas would you like for Authentication System? [{}]: ",
    pg_user = "{} postgres username [{}]: ",
    pg_password = "{} postgres password [{}]: ",
    send_mail = "Would you like that Auth sends mail for user registration or reset password? (y/n) [y]: ",
    smtp_host = "Auth SMTP host: ",
    smtp_user = "Auth SMTP user: ",
    smtp_password = "Auth SMTP password: ",
    password_reset_link = "Auth password reset link: ",
)

cron = dict(
    name = "Cron",
    use = "Would you like to add {} ? (y/n) [n]: "
)

gui = dict(
    name = "GUI",
    use = "Would you like to add {} ? (y/n) [n]: "
)

postgres = dict(
    name = "PostgreSQL",
    super_user = "Super {} username [{}]: ",
    super_password = "Super {} password [{}]: ",
    use_persistent_volume = "Do you want to use persistent volumes for {}?: (y/n) [n]: ",
    volume_size = "What is the volume size in GB for {}? [{}]: "
)
