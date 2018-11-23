import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

register(
	id='Continuous_CartpoleEnv-v0',
	entry_point='cp_cont.envs:Continuous_CartpoleEnv',
    timestep_limit=500,
    reward_threshold=250.0,
)
