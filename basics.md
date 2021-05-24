# What is Reinforcement Learning

An area of Machine Learning concerned with how intelligent agents ougth to take actions in order to maximize the notion of cumulative reward.

[Reinforcement Learning](https://en.wikipedia.org/wiki/Reinforcement_learning#:~:text=Reinforcement%20learning%20(RL)%20is%20an,supervised%20learning%20and%20unsupervised%20learning.)

## Keys
- Cumulative Reward
  - Enviroments provide a bunch of situations wich agents need to solve in order to recieve rewards
  - Those rewards may (exponentially or not) grow
  - According to the rewards the enviroment may provide to the agent, this may chose a different action and learn trough reward.
    - The reward will reinforce that acion or set of actions
    - the set of actions will be taken more than once
    - the agent learned trough reinforce

![schema](esquema.png)

Note that the agent recieve two inputs per action:
- The reward
- The information about it's state after proceruring the action

Those informations are important to solve the Q-Learn equation:

![q-learning equation](https://wikimedia.org/api/rest_v1/media/math/render/svg/678cb558a9d59c33ef4810c9618baf34a9577686)

### **_More explanations_** about the equation variables and about the Q-learn algorithm may be found at: [Q-Learning](https://en.wikipedia.org/wiki/Q-learning)
### Nonetheless, the Q-Learning algorithm is a technique wich creates a table (Q-Table) with all the results of a [Markov Decision Process](https://en.wikipedia.org/wiki/Markov_decision_process).

![Markov's Equation](https://wikimedia.org/api/rest_v1/media/math/render/svg/63b502aafbe6ea1585231222ea3783f40f0808a9)

### The key of Reinforcement Learning is to solve a Markov Decision Process without the specification of the transition probabilities.

## How does it work?

- Maximize the reward function.
  - The entire goal of an agent is to maximize the reward function of an enviroment or, to be more precise, of an enviroment interpreter.

![second schema](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/Reinforcement_learning_diagram.svg/375px-Reinforcement_learning_diagram.svg.png)

