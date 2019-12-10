kong = dict(
    name = "API Gateway",
    req_per_minute = "\n\nHow many requests per minute are allowed? [{}]: ",
    req_per_hour = "How many requests per hour are allowed? [{}]: ",
    pg_user = "{} postgres username [{}]: ",
    pg_password = "{} postgres password [{}]: "
)

devm = dict(
    name = "Device Manager",
    pg_user = "\n\n{} postgres username [{}]: ",
    pg_password = "{} postgres password [{}]: "
)

auth = dict(
    name = "Authentication System",
    replicas = "\n\nHow many replicas would you like for Authentication System? [{}]: ",
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
    use = "\n\nWould you like to add {} ? (y/n) [n]: "
)

gui = dict(
    name = "GUI",
    use = "\n\nWould you like to add {} ? (y/n) [n]: "
)
