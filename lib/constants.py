kong = dict(
    name = "API Gateway",
    req_per_minute = "How many requests per minute are allowed? [{}]: ",
    req_per_hour = "How many requests per hour are allowed? [{}]: ",
    pg_user = "{} postgres username [{}]: ",
    pg_password = "{} postgres password [{}]: "
)

devm = dict(
    name = "Device Manager",
    pg_user = "Device Manager postgres username [{}]: ",
    pg_password = "Device Manager postgres password [{}]: "
)

auth = dict(
    name = "Authentication System",
    replicas = "How many replicas would you like for Authentication System? [{}]: ",
    pg_user = "Authentication System postgres username [{}]: ",
    pg_password = "Authentication System postgres password [{}]: ",
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
    super_user = "Super PostgreSQL username [{}]: ",
    super_password = "Super PostgreSQL password [{}]: ",
    use_persistent_volume = "Do you want to use persistent volumes for PostgreSQL?: (y/n) [n]: ",
    volume_size = "What is the volume size in GB for PostgreSQL? [{}]: "
)

mongo = dict(
    name = "MongoDB",
    super_user = "Super MongoDB username [{}]: ",
    super_password = "Super MongoDB password [{}]: ",
    persistence_time = "How many hours would you like the data to be kept in MongoDB (0 for indeterminate) ? [{}]: ",
    use_persistent_volume = "Do you want to use persistent volumes for MongoDB?: (y/n) [n]: ",
    volume_size = "What is the volume size in GB for MongoDB? [{}]: "
)
