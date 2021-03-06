<h1>Q-Learning</h1>

<p>Q-learning is a model-free reinforcement learning algorithm to learn a policy telling an agent what action to take under what circumstances. It does not require a model (hence the connotation "model-free") of the environment, and it can handle problems with stochastic transitions and rewards, without requiring adaptations<br>
<br>
A model-free algorithm is an algorithm that estimates the optimal policy without using or estimating the dynamics (transition and reward functions) of the environment. Whereas, a model-based algorithm is an algorithm that uses the transition function (and the reward function) in order to estimate the optimal policy.</p>


<h2>Q-Learning Steps</h2>

<p><ol>
<li>Create a q-table that follows the shape of [state, action] and we initialize the q-table with random values.</li>
<li>The agent select an action, it can select action from q-table which contain the highest q-value for a state, or select a random action and discover new states.</li>
<li>The agent interact with the environment and make updates to the state action pairs in our q-table Q[state, action] with formula:</li>
<img src="images/Formula.png" alt="q-learning formula"/>
<li> Loop for large amount of episodes so eventually it will converge to optimal q-value</li></ol></p>
<p>For further read about q-learning, you can read this superb <a href="https://link.springer.com/content/pdf/10.1007/BF00992698.pdf">technical note </a>from <a href="http://www.cs.rhul.ac.uk/~chrisw/">Chris Watkins</a> and <a href="https://www.ed.ac.uk/profile/peter-dayan">Peter Dayan</a>.</p>

<h2>Q-Learning for Taxi problem from Openai gym</h2>

<p> The Taxi Problem<br>
    <br>
    from "Hierarchical Reinforcement Learning with the MAXQ Value Function Decomposition"<br>
    by <a href="https://eecs.oregonstate.edu/people/dietterich-thomas">Tom Dietterich</a><br>
    <br>
    Description:<br>
    There are four designated locations in the grid world indicated by R(ed), G(reen), Y(ellow), and B(lue). When the episode starts, the taxi starts off at a random square and the passenger is at a random location. The taxi drives to the passenger's location, picks up the passenger, drives to the passenger's destination (another one of the four specified locations), and then drops off the passenger. Once the passenger is dropped off, the episode ends.<br>
    <br>
    Observations: <br>
    There are 500 discrete states since there are 25 taxi positions, 5 possible locations of the passenger (including the case when the passenger is in the taxi), and 4 destination locations. 
    
    Passenger locations:
    - 0: R(ed)
    - 1: G(reen)
    - 2: Y(ellow)
    - 3: B(lue)
    - 4: in taxi
    
    Destinations:
    - 0: R(ed)
    - 1: G(reen)
    - 2: Y(ellow)
    - 3: B(lue)
        
    Actions:
    There are 6 discrete deterministic actions:
    - 0: move south
    - 1: move north
    - 2: move east 
    - 3: move west 
    - 4: pickup passenger
    - 5: dropoff passenger
    
    Rewards: 
    There is a default per-step reward of -1,
    except for delivering the passenger, which is +20,
    or executing "pickup" and "drop-off" actions illegally, which is -10.
    
    Rendering:
    - blue: passenger
    - magenta: destination
    - yellow: empty taxi
    - green: full taxi
    - other letters (R, G, Y and B): locations for passengers and destinations
    
    state space is represented by:
    (taxi_row, taxi_col, passenger_location, destination)
</p>
<img src="images/q-learning.gif">

<h2>References</h2>

<p><ul>
<li>Youtube:<ul>
<li><a href="https://www.youtube.com/watch?v=wN3rxIKmMgE" title="TheComputerScientist">An Introduction to Q-learning </a>by TheComputerScientist</li>
<li><a href="https://www.youtube.com/playlist?list=PLQVvvaa0QuDezJFIOU5wDdfy4e9vdnx-7" title="RL by Sentdex">Reinforcement Learning playlist </a>by Sentdex</li>
<li><a href="https://www.youtube.com/watch?v=FgzM3zpZ55o" title="RL by standfordonline">Stanford CS234: Reinforcement Learning</a></li></ul>
</li>
<li>Article:<ul>
<li><a href="https://towardsdatascience.com/introduction-to-q-learning-88d1c4f2b49c" title="Introduction to Q-Learning">Introduction to Q-Learning</a> by Aneek Das</li>
<li><a href="https://medium.com/@fin.techology/reinforcement-learning-introduction-to-q-learning-444c951e292c" title="Reinforcement Learning: Introduction to Q Learning">Reinforcement Learning: Introduction to Q Learning</a> by J Li</li>
<li><a href="https://www.freecodecamp.org/news/an-introduction-to-q-learning-reinforcement-learning-14ac0b4493cc/" title="An introduction to Q-Learning: reinforcement learning">An introduction to Q-Learning: reinforcement learning</a> by ADL</li></ul>
</li></ul>


That's all. Keep learning!</p>