from typing import Any, Tuple

import numpy as np

from .done_tracker import DoneTrackerEnv


class SingleProcessEnv(DoneTrackerEnv):
    def __init__(self, env_fn):
        super().__init__(num_envs=1)
        self.env = env_fn()
        self.dim_actions = self.env.action_space.shape[0]

    def should_reset(self) -> bool:
        return self.num_envs_done == 1

    def reset(self) -> np.ndarray:
        self.reset_done_tracker()
        obs = self.env.reset()
        obs = self.env.sim.render(*(64, 64), mode="offscreen", camera_name="corner3")
        return obs[None, ...]

    def step(self, action) -> Tuple[np.ndarray, np.ndarray, np.ndarray, Any]:
        obs, reward, done, info = self.env.step(
            action[0]
        )  # action is supposed to be ndarray (1,)
        obs = self.env.sim.render(*(64, 64), mode="offscreen", camera_name="corner3")
        done = np.array([done])
        self.update_done_tracker(done)
        return obs[None, ...], np.array([reward]), done, None

    def render(self) -> None:
        self.env.render()

    def close(self) -> None:
        self.env.close()
