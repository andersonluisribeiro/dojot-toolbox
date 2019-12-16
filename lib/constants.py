
repository = dict(
    use_existent_repository = "\nYou already have a ansible-dojot repository. Do you want to use that? (y/n) [n]: ",
    delete_repository = "\nSo delete ansible-dojot folder or change the current directory before use \"dojot configure\"\n\nThanks!\n",
    clonning_repository = "Clonning dojot repository for configuration ",
    cant_clone = "\nCan't clone dojot repository. Verify your internet connection, please.\n",
    repo_dir = "ansible-dojot",
    repository_url = "https://github.com/dojot/ansible-dojot.git",
    current_branch = "release/v0.4.1"
)

kafka = dict(
    name = "Apache Kafka",
    persistence_time = "How many hours would you like the data to be kept in Apache Kafka (0 for indeterminate)? [{}]: ",
    use_persistent_volume = "Do you want to use persistent volumes for Apache Kafka: (y/n) [n]: ",
    volume_size = "What is the volume size in GB for Apache Kafka? [{}]: "
)

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

iotagent_mqtt = dict(
    name = "IoT Agent MQTT",
    use = "Would you like to add IoT Agent MQTT? (y/n) [y]: ",
    use_insecure_mqtt = "Do you want to enable insecure mode for IoT Agent MQTT? (y/n) [n]: ",
    replicas = "How many instances would you like for IoT Agent MQTT? [{}]: "
)

iotagent_lwm2m = dict(
    name = "IoT Agent LWM2M",
    use = "Would you like to add IoT Agent LWM2M? (y/n) [y]: "
)