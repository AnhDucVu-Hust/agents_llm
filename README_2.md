<p align="center" width="100%">
<img src="cover.png" alt="Smallville" style="width: 80%; min-width: 300px; display: block; margin: auto;">
</p>
# Nectar AI: Online Dating Simulation

## Overview

This assesment adapts the architecture of generative agents for an online dating simulation. Inspired by the Smallville paper and the `generative_agents` repository, the simulation involves six characters interacting in a fictional dating show setting. OpenAI API calls were replaced with open-source models to create a customizable and open-source solution.

## Features

- Simulates interaction between generative agents with distinct personality traits. .
- Customizable for Dating Show Simulation
- Open-source model integration for efficient resource usage.

---

## Project Approach Plan

1. **Understand the Framework**  
   Reviewed both the Smallville paper and source code to learn how LLMs control agents’ interactions, memory, and decision-making. Key components include:
   - Interaction loop for steps.
   - Personality configuration.
   - LLM API call structure.

2. **Run and Observe a Basic Simulation**  
   - Configured a basic simulation where agents interact in default config by author.  
   - Observed how agents planned their day and broke it into 5–15 minute chunks also the way agents interact with each other and environment.   
   - Explored the concept of a memory stream as a list of ConceptNodes representing events and thoughts.

3. **Configure New Context: Dating Show**  
   - Developed a new context where all agents interact in the same location.  
   - Added descriptions of a love game show for realistic agent interactions.

4. **Replace API Calls with Open-Source Models**  
   - Replaced OpenAI API calls with open-source models like LLaMa, Qwen, DeepSeek, Mistral, and Command R.
   - Ensured optimal model selection based on task complexity and domain requirements.
   - Improved configuration management by centralizing parameters in `utils.py`.

5. **Enhance Interactions with Memory Integration**  
   - Introduced memory augmentation to guide agent interactions dynamically.  
   - Enhanced realism by allowing agents to reflect and adapt based on their memory streams.

---

## Simulation Workflow

1. **Agent Behavior Loop**  
   Each agent follows these steps for interaction:
   - **Perceive:** Identify surroundings, events, and objects, adding new observations to memory.
   - **Retrieve:** Fetch relevant events or thoughts based on recency, importance, and relevance.
   - **Plan:** Decide actions based on retrieved information and the daily schedule.
   - **Reflect:** Organize the memory stream by synthesizing high-level statements about observations and thoughts.

2. **Key Simulation Functions**  
   - Found in `reverie.py`, including functions for event analysis, schedule management, and insights extraction.

3. **Open-Source Model Replacement**  
   - API calling logic is located in:
     - `reverie/backend_server/persona/prompt_template/`
       - `gpt_structure.py`
       - `run_gpt_prompt.py`
   - Configuration centralized in `utils.py` for seamless model swapping.
   - Challenges:
     - Different models have different output format. Need larger model for better context handle. 
     - Fix the postprocessing the generated text from LLM function.
     - There's a lot of different functions need to be observed.

---

## Technical Details

### Module Usage and Observations
- **Wake up hour:** Models like Qwen perform better for generating wake-up hours.
- **Focal Points Question, Insight and Guidance:** These fuction are used for generating high-level information from the Memory Stream. Deepseek and LlaMa perform well in this module. Adjusted output handling for consistency.
- **Schedules:** Use for generate long-term schedule based on agent's characteristic. Using DeepSeek for better reasoning. Customized post-processing functions to fix formatting issues. 
- **Object description, Exact information from conversation,:** Refined prompts for clarity and conciseness.
- **Poignancy:** Generate the importance of each event or thought of agent or conversation. LLaMa 70B is good enough.
- **Conversation** Using roleplay model for generating lines of each agent. Command-R is in trending.
- **Decide** Base on what agent can see, these function is used for agent to decide to keep doing what is in the schedule, or doing another thing. I use Qwen 32B.
- **Summary Conversation Idea and Relationship, Statements of Agent** Generating high-level statement and thought of agent. Make the characteristic deeper and more unique. Using DeepSeek for the best performance.
### Engineering details
- Centralized API parameters for easy configuration.
- Save the log for review and optimize iteratively
- Added timeouts to improve simulation speed and handle API delays.

## Further Improvement

