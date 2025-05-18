import json
import os

from app.config.config_loader.models.exceptions import MissingEnvVarError


class ConfigLoader:
    def __init__(self, filename='config.json', base_dir='app/resources'):
        self.config = {}
        self.load_config(os.path.join(base_dir, filename))

    def load_config(self, path):
        if not os.path.exists(path):
            raise FileNotFoundError(f"No se encontró el archivo de configuración en: {path}")

        with open(path, 'r', encoding='utf-8') as f:
            raw_config = json.load(f)

        self.config = self._resolve_env_vars(raw_config)

    def _resolve_env_vars(self, config_dict):
        resolved = {}
        for key, value in config_dict.items():
            if isinstance(value, str) and value.startswith('$'):
                env_var = value[1:]
                env_value = os.getenv(env_var)
                if env_value is None:
                    raise MissingEnvVarError(env_var)
                resolved[key] = env_value
            else:
                resolved[key] = value
        return resolved

    def get(self, key, default=None):
        return self.config.get(key, default)