import docker
import logging

client = docker.from_env()


class ImageChecker:

    def __init__(self, image_name):
        self.image_name = image_name

    def get_local_image_id(self):
        try:
            image = client.images.get(self.image_name)
            return image.id
        except Exception:
            return None

    def pull_image(self):
        try:
            logging.info(
                f"Baixando imagem {self.image_name}"
            )

            image = client.images.pull(
                self.image_name
            )

            return image.id

        except Exception as e:
            logging.error(
                f"Erro ao baixar imagem: {e}"
            )
            return None

    def has_update(self):

        old_id = self.get_local_image_id()

        new_id = self.pull_image()

        if old_id is None:
            return True

        return old_id != new_id
