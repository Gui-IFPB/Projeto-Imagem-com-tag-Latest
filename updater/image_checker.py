import docker
import logging

client = docker.from_env()


class ImageChecker:

    def __init__(self, image_name):
        self.image_name = image_name

    def get_local_image_id(self):
        try:
            image = client.images.get(
                self.image_name
            )
            return image.id

        except Exception:
            return None

    def has_update(self):

        old_id = self.get_local_image_id()

        logging.info(
            f"Imagem atual: {old_id}"
        )

        try:

            logging.info(
                f"Verificando atualizações para {self.image_name}"
            )

            image = client.images.pull(
                self.image_name
            )

            new_id = image.id

            logging.info(
                f"Imagem após pull: {new_id}"
            )

            if old_id is None:

                logging.info(
                    "Imagem não encontrada localmente"
                )

                return True

            if old_id != new_id:

                logging.info(
                    "Nova versão detectada"
                )

                return True

            logging.info(
                "Nenhuma alteração detectada"
            )

            return False

        except Exception as e:

            logging.error(
                f"Erro ao verificar atualização: {e}"
            )

            return False
