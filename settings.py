from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    os_auth_url: str
    os_username: str
    os_password: str

    os_project_name: str
    os_user_domain_name: str
    os_project_domain_name: str
    os_region_name: str

    os_image_id: str
    os_flavor_id: str
    os_network_id: str

    model_config = SettingsConfigDict(
        env_file="openstack.env",
        env_file_encoding="utf-8",
        case_sensitive=False
    )


settings = Settings()