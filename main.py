import sys
from lib import Installer, Kafka, Gui, Cron, Kong, DeviceManager, Auth, Postgres


installer = Installer(sys.argv)

if installer.is_for_configuration():

    try:

        installer.say_wellcome()
        installer.clone_repository()

        kafka = Kafka() \
            .ask_persistence_time() \
            .ask_persistence_volume() \
            .ask_volume_size()

        kong = Kong() \
            .ask_req_per_minute() \
            .ask_req_per_hour() \
            .ask_pg_username() \
            .ask_pg_password()

        devm = DeviceManager() \
            .ask_pg_username() \
            .ask_pg_password()

        auth = Auth() \
            .ask_how_many_replicas() \
            .and_pg_username() \
            .and_pg_password() \
            .ask_if_should_send_mail() \
            .and_smtp_host() \
            .and_smtp_username() \
            .and_smtp_password() \
            .and_password_reset_link()
    
        postgres = Postgres() \
            .ask_super_username() \
            .and_super_password() \
            .and_if_use_persistent_volume() \
            .and_volume_size()

        cron = Cron() \
            .ask_use() \
            .ask_replicas()

        gui = Gui() \
            .ask_use() \
            .ask_replicas()


        installer \
            .create_vars_file_for( \
                [kafka, kong, cron, gui, devm, auth, postgres] \
            ) \
            .call_ansible()

        installer.say_thanks()

    except KeyboardInterrupt:
        installer.say_thanks()

