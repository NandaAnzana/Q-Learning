<h1>Q-Learning<h1>

<p>Q-learning is a model-free reinforcement learning algorithm to learn a policy telling an agent what action to take under what circumstances. It does not require a model (hence the connotation "model-free") of the environment, and it can handle problems with stochastic transitions and rewards, without requiring adaptations.<br>
A model-free algorithm is an algorithm that estimates the optimal policy without using or estimating the dynamics (transition and reward functions) of the environment. Whereas, a model-based algorithm is an algorithm that uses the transition function (and the reward function) in order to estimate the optimal policy.</p>
<h2>Q-Learning Steps<h2>

<p><ol>
<li>Create a q-table that follows the shape of [state, action] and we initialize the q-table with random values.</li>
<li>The agent select an action, it can select action from q-table which contain the highest q-value for a state, or select a random action and discover new states.
<li>The agent interact with the environment and make updates to the state action pairs in our q-table Q[state, action] with formula:</li>
<img src="images/formula.png" alt="q-learning formula" />
<li> Loop for large amount of episodes so eventually it will converge to optimal q-value</li>