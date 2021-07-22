import os

# Kivy settings, mocking environment variables to enforce desired parameters
os.environ['KCFG_GRAPHICS_MAXFPS'] = '30'
os.environ['KCFG_GRAPHICS_ALLOW_SCREENSAVER'] = '0'
os.environ['KCFG_GRAPHICS_SHOW_CURSOR'] = '0'
os.environ['KCFG_GRAPHICS_FULLSCREEN'] = 'auto'
os.environ['KCFG_GRAPHICS_BORDERLESS'] = '1'

# TODO: See if we can use egl rpi driver, might perform better than the sdl2 for rpi3
# os.environ['KIVY_WINDOW'] = 'egl_rpi'
# os.environ['KIVY_GL_BACKEND'] = 'gl'

REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 0


def read_settings(settings_file_path: str = "settings.yaml"):
    pass


def write_settings(settings_file_path: str = "settings.yaml"):
    from lib.model import settings_schema, Tool, Origin, Settings, AxisConfiguration
    import yaml

    settings = Settings(
        axis_configurations=[
            AxisConfiguration(
                label="X",
                direction=+1,
                decimal_places=3,
                increment_per_step=0.05
            ),
            AxisConfiguration(
                label="Y",
                direction=+1,
                decimal_places=1,
                increment_per_step=0.05
            ),
            AxisConfiguration(
                label="Z",
                direction=+1,
                decimal_places=2,
                increment_per_step=0.05
            ),
            AxisConfiguration(
                label="A",
                direction=-1,
                decimal_places=2,
                increment_per_step=0.05
            )
        ],
        origins=[
            Origin("Base", offset=[0, 0, 0, 0])
        ],
        tools=[
            Tool(1, "Empty Tool", icon="", offset=[0, 0, 0, 0],
                 diameter=0)
        ],
        current_tool=0,
        current_origin=0
    )

    settings_dict = settings_schema.dump(settings)
    with open(settings_file_path, "w") as yaml_file:
        yaml_file.write(yaml.safe_dump(settings_dict))


write_settings(settings_file_path="test.yaml")
