from collections import deque
import random
class Buffer:

    def __init__(self, max_size):
        self.max_size = max_size
        self.buffer = deque(maxlen=max_size)
        self.jump_buffer = deque(maxlen=max_size)

    def push(self, state, action, reward, next_state, next_action, done):
        experience = (state, action, reward, next_state, next_action, done)
        if action:
            self.jump_buffer.append(experience)
        else:
            self.buffer.append(experience)


    def sample(self, batch_size):
        state_batch = []
        action_batch = []
        reward_batch = []
        next_state_batch = []
        next_action_batch = []
        done_batch = []

        if (batch_size >= len(self.buffer)) or (batch_size >= len(self.jump_buffer)):
            batch_size = min(len(self.buffer), len(self.jump_buffer))
        if batch_size < 1000:
            batch = self.jump_buffer + self.buffer
        else:
            batch = random.sample(self.buffer, batch_size) + random.sample(self.jump_buffer, batch_size) 

        for experience in batch:
            state, action, reward, next_state, next_action, done = experience
            state_batch.append(state)
            action_batch.append(action)
            reward_batch.append(reward)
            next_state_batch.append(next_state)
            next_action_batch.append(next_action)
            done_batch.append(done)

        return (state_batch, action_batch, reward_batch, next_state_batch, next_action_batch,done_batch)

    def __len__(self):
        return len(self.jump_buffer)