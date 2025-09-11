import os
from dotenv import load_dotenv


load_dotenv()

def get_env_variable(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise ValueError(f"Environment variable '{name}' is not set")
    return value


def get_initials(username: str) -> str:
    initials = str(username.split()[0]).capitalize()[0] + str(username.split()[1]).capitalize()[0]
    return initials


def check_tag(rq_tags: list, rs_tags: list, creator_id: str) -> bool:
    flag = None
    for i in rs_tags:
        if i['name'] in rq_tags and i['creator'] == int(creator_id):
            flag = True
        else: flag = False
    return flag


CLICKUP_API_KEY = get_env_variable("CLICKUP_API_KEY")
CLICKUP_EMAIL = get_env_variable("CLICKUP_EMAIL")
CLICKUP_PASSWORD = get_env_variable("CLICKUP_PASSWORD")
MY_ID = get_env_variable("MY_ID")
TEAM_ID = get_env_variable("TEAM_ID")
BOARD_ID = get_env_variable("BOARD_ID")
USERNAME = get_env_variable("USERNAME")



