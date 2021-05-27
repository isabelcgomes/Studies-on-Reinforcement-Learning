# What is Reinforcement Learning

An area of Machine Learning concerned with how intelligent agents ougth to take actions in order to maximize the notion of cumulative reward. 

[Reinforcement Learning](https://en.wikipedia.org/wiki/Reinforcement_learning#:~:text=Reinforcement%20learning%20(RL)%20is%20an,supervised%20learning%20and%20unsupervised%20learning.)

The model recieves each reward for each action taken but does not gets any clue on how to solve the environment

At the begining the actions are random, that explains why every experiment has a different result if the number of steps are sufficiently low.

## Keys
- Reward
  - A number that may be positive (reward) or negative (penalty) that the agent aims to increase and maximize in the long term.
  - The reward and all the actions are loaded in the Q-Table
- Cumulative Reward
  - Environments provide a bunch of situations wich agents need to solve in order to recieve rewards
  - Those rewards may (exponentially or not) grow
  - According to the rewards the environment may provide to the agent, this may chose a different action and learn trough reward.
    - The reward will reinforce that acion or set of actions
    - the set of actions will be taken more than once
    - the agent learned trough reinforce
  - This is why it's possible for the model to maximize the reward in the long term

Note that the agent recieve two inputs per action:
- The reward
- The information about it's state after proceruring the action

  ![schema](images\esquema.png)

Those informations are important to solve the Q-Learn equation:

![q-learning equation](https://wikimedia.org/api/rest_v1/media/math/render/svg/678cb558a9d59c33ef4810c9618baf34a9577686)

### **_More explanations_** about the equation variables and about the Q-learn algorithm may be found at: [Q-Learning](https://en.wikipedia.org/wiki/Q-learning)
### Nonetheless, the Q-Learning algorithm is a technique wich creates a table (Q-Table) with all the results of a [Markov Decision Process](https://en.wikipedia.org/wiki/Markov_decision_process).

- Q-Table
  - A set of all the states, rewards, actions and parameters taken from the begining of the experiment
  - Works as a log, a register of everything that has already happened to the environment
  - Every action generates a new line to the Q-table and sets a new state do the agent and to the environment.

  ![Markov's Equation](https://wikimedia.org/api/rest_v1/media/math/render/svg/63b502aafbe6ea1585231222ea3783f40f0808a9)

### The key of Reinforcement Learning is to solve a Markov Decision Process without the specification of the transition probabilities.
- The data scientist sets the rewards but the model finds out how to solve the environment

## How does it work?

- Maximize the reward function.
  - The entire goal of an agent is to maximize the reward function of an environment or, to be more precise, of an environment interpreter.

  ![second schema](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Reinforcement_learning_diagram.svg/375px-Reinforcement_learning_diagram.svg.png)

  - the reward is maximized at a long term. 


## References
1. [Geeks for geeks](https://www.geeksforgeeks.org/what-is-reinforcement-learning/)
2. [O que é Aprendizado por Reforço?](https://www.deeplearningbook.com.br/o-que-e-aprendizagem-por-reforco/)
3. [Reinforcement Learning - Wikipédia](https://en.wikipedia.org/wiki/Reinforcement_learning)
4. [Q-Learning - Wikipédia](https://en.wikipedia.org/wiki/Q-learning)
5. [Markov Decision Process](https://en.wikipedia.org/wiki/Markov_decision_process)