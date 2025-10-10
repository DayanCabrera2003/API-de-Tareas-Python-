from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Final

class Settings(BaseSettings):
    """
    Define el esquema de configuración de la aplicación.
    Pydantic carga automáticamente estas variables desde el archivo .env
    o las variables de entorno del sistema (con mayor prioridad).
    """
    model_config=SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf_8'
    )
    
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_DB: str
    
    ENVIRONMENT: str = 'development'
    
    @property
    def DATABASE_URL(self) -> str:
        """
        Construye la URL de conexión a la base de datos PostgreSQL.
        """
        return (
            f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@"
            f"{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )
    
    
