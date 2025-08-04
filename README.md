# Autonomous-Drone-Path-Planning-Using-Deep-Learning

This project demonstrates a 3D autonomous drone navigation system that leverages **deep learning**, **reinforcement learning**, and **heuristic search** to plan optimal flight paths while avoiding obstacles. It combines AI-powered decision-making with real-time visualization and user-friendly interfaces like a Telegram bot.


Objective

The goal of this project is to design a drone path planner that can:
- Automatically compute safe, efficient paths in 3D space
- Avoid static and dynamic obstacles
- Adapt to real-time environmental changes using AI
- Provide visualization and path analysis for verification

Project Highlights

- ✅ Real-time 3D obstacle avoidance
- ✅ Path analysis: efficiency, length, safety
- ✅ AI-based movement prediction using the Sequential_9 model
- ✅ Custom Python environment for path planning
- ✅ Telegram bot for input/output & video generation

Technologies & Tools

| Category                 | Tools Used                                                                                            |
|--------------------------|------------------------------------------------------------------------------------------------------ |
| Language                 | Python 3.10                                                                                           |
| Libraries                | NumPy,Matplotlib,TensorFlow,SciPy,PriorityQueue,python-telegram-bot                                   |
| AI Techniques            | Deep Learning(Sequential Model),Reinforcement Learning(DQN), Heuristics                               |
| Visualization            | 3D Plotting with Matplotlib                                                                           |
| User Interface           | Telegram Bot Integration                                                                              |
| Deployment               | Local Python environment                                                                              |


Folder Structure

drone-path-planning/

├── drone_path_planner.py          # 3D environment and BFS path planner

├── environment.py                 # Obstacle setup & collision detection

├── model_training.py              # Deep learning model training

├── telegram_bot.py                # Telegram bot for interactive input

├── visualize.py                   # Path visualization

├── final.pdf                      # Project documentation

├── drone_path.mp4                 # Demo video



Installation & Setup

Requirements:   Python 3.10+

Install dependencies :   pip install numpy matplotlib tensorflow python-telegram-bot nest_asyncio

Run the simulation :    python drone_path_planner.py

Start Telegram Bot 

Edit telegram_bot.py and replace:    TOKEN = "YOUR_BOT_TOKEN"

Then run:     python telegram_bot.py


Algorithms Used
1. Sequential_9 Model : A deep neural network trained to predict movement directions using environmental states.
   
2. Features include:
           3 hidden layers with ReLU
           Dropout for regularization
           Tanh activation for normalized direction vector output

3. Priority Queue + Heuristic Search
            Used for path planning with direction prioritization based on distance to goal.

4. Deep Q-Network (DQN)
            Reinforcement learning model integrated for continuous learning and improvement in   obstacle avoidance.

5. Obstacle Collision Detection
            Calculates minimum distance to all known obstacles in 3D using Euclidean distance.

6. Path Analysis
    Path length vs. straight-line distance
    Path efficiency
    Obstacle clearance


Testing the Planner

1. Set up obstacle coordinates manually or allow random generation.
   
2. Run the planner script.
   
3. The system checks for collisions and computes an optimal route.
   
4. The drone's trajectory is visualized in a 3D plot.
   
5. Telegram bot allows interactive command like:
     /start_goal 0,0,0 49,49,29


📊 Sample Output

Path Analysis : 

    Total path length: 75.18 units
    
    Straight-line distance: 75.12 units
    
    Path efficiency: 99.92%
    
    Minimum distance to obstacles: 9.16 units


🧭 Project Flow Diagram

You can upload these in /images/ folder and reference here:

    Architecture Diagram: images/architecture.png
    
    Sequence Diagram: images/sequence.png
    
    Use Case: images/usecase.png



👥 Team Members

Batta Layasri

Sommisetti Leelavathi

Sriram V V V N S M Praneeta

Kavitha Mamidala

Mannem Sudheshna



Institution

St. Ann’s College of Engineering & Technology

CSE - Artificial Intelligence & Machine Learning

JNTU Kakinada | Batch 2021–2025



Future Work 

Improve dynamic obstacle prediction using LSTM

Implement energy-aware planning (battery-aware routing)

Swarm drone coordination via multi-agent RL

ROS and AirSim integration for real-time deployment
