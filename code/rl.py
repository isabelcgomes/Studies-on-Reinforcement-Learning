import gym
import time #lib, leiam a documentação
env = gym.make('CartPole-v0')
env.reset() #para garantir que as variáveis estão resetadas
print(env.action_space)
done = False
t = 0 
while not done:
    t += 1
    env.render()
    observation, reward, done, info = env.step(env.action_space.sample()) # take a random action
    print(observation) #estado do ambiente
    print(reward)
    time.sleep(0.1)
steps = t + 1
print(f'Enviroment finished after {steps}')
env.close()