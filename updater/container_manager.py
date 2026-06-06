import docker
import logging

client = docker.from_env()


class ContainerManager:

    def __init__(
        self,
        image_name,
        container_name,
        ports
    ):
        self.image_name = image_name
        self.container_name = container_name
        self.ports = ports

    def stop_container(self):

        try:

            container = client.containers.get(
                self.container_name
            )

            logging.info(
                f"Parando {self.container_name}"
            )

            container.stop()

            return True

        except docker.errors.NotFound:

            logging.warning(
                "Container não encontrado"
            )

            return False

    def remove_container(self):

        try:

            container = client.containers.get(
                self.container_name
            )

            logging.info(
                f"Removendo {self.container_name}"
            )

            container.remove()

            return True

        except docker.errors.NotFound:

            return False

    def create_container(self):

        try:

            port_mapping = {}

            for host_port, container_port in self.ports.items():

                port_mapping[
                    f"{container_port}/tcp"
                ] = int(host_port)

            container = client.containers.run(
                self.image_name,
                name=self.container_name,
                detach=True,
                ports=port_mapping,
                restart_policy={
                    "Name": "always"
                }
            )

            logging.info(
                "Novo container criado"
            )

            return container

        except Exception as e:

            logging.error(
                f"Erro ao criar container: {e}"
            )

            return None
