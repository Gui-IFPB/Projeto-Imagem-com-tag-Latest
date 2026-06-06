import yaml
import logging

from scheduler.scheduler import run_scheduler

from updater.image_checker import (
    ImageChecker
)

from updater.container_manager import (
    ContainerManager
)

from updater.rollback import (
    RollbackManager
)


logging.basicConfig(
    filename="logs/updater.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


with open(
    "config/config.yaml",
    "r"
) as file:

    config = yaml.safe_load(file)


IMAGE = config["image"]

CONTAINER_NAME = config["container_name"]

INTERVAL = config["interval"]

PORTS = config["ports"]


def monitor():

    checker = ImageChecker(IMAGE)

    updated = checker.has_update()

    if not updated:

        logging.info(
            "Nenhuma atualização encontrada"
        )

        return

    logging.info(
        "Nova imagem detectada"
    )

    manager = ContainerManager(
        IMAGE,
        CONTAINER_NAME,
        PORTS
    )

    manager.stop_container()

    manager.remove_container()

    container = manager.create_container()

    if container:

        logging.info(
            "Container atualizado com sucesso"
        )

    else:

        RollbackManager.execute()


if __name__ == "__main__":

    logging.info(
        "Docker Auto Updater iniciado"
    )

    run_scheduler(
        INTERVAL,
        monitor
    )
