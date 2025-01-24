# Copy and paste your OpenAI API Key
#route to OpenRouter
openai_base_url = "https://openrouter.ai/api/v1"
#OpenRouter API Key
openai_api_key = "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"
#OpenAI API key for calling embedding model
openai_embedding_key =  "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"
# Put your name
key_owner = "ducva4"

maze_assets_loc = "../../environment/frontend_server/static_dirs/assets"
env_matrix = f"{maze_assets_loc}/the_ville/matrix"
env_visuals = f"{maze_assets_loc}/the_ville/visuals"

fs_storage = "../../environment/frontend_server/storage"
fs_temp_storage = "../../environment/frontend_server/temp_storage"

collision_block_id = "32125"

# Verbose 
debug = True

wake_up_hour_param = {"engine": "qwen/qwq-32b-preview", "max_tokens": 5, 
             "temperature": 0.8, "top_p": 1, "stream": False,
             "frequency_penalty": 0, "presence_penalty": 0, "stop": ["\n"]}

daily_plan_param = {"engine": "meta-llama/llama-3.3-70b-instruct", "max_tokens": 300, 
               "temperature": 0.4, "top_p": 1, "stream": False,
               "frequency_penalty": 0, "presence_penalty": 0, "stop": None}
hourly_schedule_param = {"engine": "nousresearch/hermes-3-llama-3.1-405b", "max_tokens": 1000, 
             "temperature": 0, "top_p": 1, "stream": False,
             "frequency_penalty": 0, "presence_penalty": 0, "stop":None }
task_decomp_param = {"engine": "nousresearch/hermes-3-llama-3.1-405b", "max_tokens": 1000, 
             "temperature": 0, "top_p": 1, "stream": False,
             "frequency_penalty": 0, "presence_penalty": 0, "stop": ["---"]}
action_sector_param = {"engine": "qwen/qwq-32b-preview", "max_tokens": 15, 
               "temperature": 0, "top_p": 1, "stream": False,
               "frequency_penalty": 0, "presence_penalty": 0, "stop": None}

action_arena_param = {"engine": "meta-llama/llama-3.3-70b-instruct", "max_tokens": 15, 
               "temperature": 0, "top_p": 1, "stream": False,
               "frequency_penalty": 0, "presence_penalty": 0, "stop": None}

action_game_object_param = {"engine": "meta-llama/llama-3.3-70b-instruct", "max_tokens": 15, 
               "temperature": 0, "top_p": 1, "stream": False,
               "frequency_penalty": 0, "presence_penalty": 0, "stop": None}
#ChatGPT
pronunciatio_param = {"engine": "meta-llama/llama-3.3-70b-instruct", "max_tokens": 15, 
               "temperature": 0, "top_p": 1, "stream": False,
               "frequency_penalty": 0, "presence_penalty": 0, "stop": None}

event_triple_param = {"engine": "qwen/qwq-32b-preview", "max_tokens": 30, 
               "temperature": 0, "top_p": 0.1, "stream": False,
               "frequency_penalty": 0, "presence_penalty": 0, "stop": ["\n"]}
#ChatGPT
act_obj_desc_param = {"engine": "meta-llama/llama-3.3-70b-instruct", "max_tokens": 15, 
               "temperature": 0, "top_p": 1, "stream": False,
               "frequency_penalty": 0, "presence_penalty": 0, "stop": None}

act_obj_event_triple_param = {"engine": "qwen/qwq-32b-preview", "max_tokens": 30, 
               "temperature": 0, "top_p": 1, "stream": False,
               "frequency_penalty": 0, "presence_penalty": 0, "stop": ["\n"]}

new_decomp_schedule_param = {"engine": "meta-llama/llama-3.3-70b-instruct", "max_tokens": 500, 
               "temperature": 0, "top_p": 1, "stream": False,
               "frequency_penalty": 0, "presence_penalty": 0, "stop": None}

decide_to_talk_param = {"engine": "meta-llama/llama-3.3-70b-instruct", "max_tokens": 150,
               "temperature": 0, "top_p": 1, "stream": False,
               "frequency_penalty": 0, "presence_penalty": 0, "stop": None}

decide_to_react_param = {"engine": "google/gemma-2-27b-it", "max_tokens": 150,
               "temperature": 0, "top_p": 1, "stream": False,
               "frequency_penalty": 0, "presence_penalty": 0, "stop": None}

create_conversation_param = {"engine": "meta-llama/llama-3.3-70b-instruct", "max_tokens": 1000, 
               "temperature": 0.7, "top_p": 1, "stream": False,
               "frequency_penalty": 0, "presence_penalty": 0, "stop": None}
#ChatGPT
summarize_conversation_param = {"engine": "nousresearch/hermes-3-llama-3.1-405b", "max_tokens": 15, 
               "temperature": 0, "top_p": 1, "stream": False,
               "frequency_penalty": 0, "presence_penalty": 0, "stop": None}

extract_keywords_param = {"engine": "meta-llama/llama-3.3-70b-instruct", "max_tokens": 50, 
               "temperature": 0, "top_p": 1, "stream": False,
               "frequency_penalty": 0, "presence_penalty": 0, "stop": None}

keyword_to_thoughts_param = {"engine": "meta-llama/llama-3.3-70b-instruct", "max_tokens": 40, 
               "temperature": 0.7, "top_p": 1, "stream": False,
               "frequency_penalty": 0, "presence_penalty": 0, "stop": None}

convo_to_thoughts_param = {"engine": "nousresearch/hermes-3-llama-3.1-405b", "max_tokens": 40, 
               "temperature": 0.7, "top_p": 1, "stream": False,
               "frequency_penalty": 0, "presence_penalty": 0, "stop": None}
#ChatGPT
event_poignancy_param = {"engine": "meta-llama/llama-3.3-70b-instruct", "max_tokens": 15, 
               "temperature": 0, "top_p": 1, "stream": False,
               "frequency_penalty": 0, "presence_penalty": 0, "stop": None}
#ChatGPT
thought_poignancy_param = {"engine": "meta-llama/llama-3.3-70b-instruct", "max_tokens": 15, 
               "temperature": 0, "top_p": 1, "stream": False,
               "frequency_penalty": 0, "presence_penalty": 0, "stop": None}
#ChatGPT
chat_poignancy_param = {"engine": "meta-llama/llama-3.3-70b-instruct", "max_tokens": 15, 
               "temperature": 0, "top_p": 1, "stream": False,
               "frequency_penalty": 0, "presence_penalty": 0, "stop": None}
#ChatGPT
focal_pt_param = {"engine": "meta-llama/llama-3.3-70b-instruct", "max_tokens": 500,
               "temperature": 0, "top_p": 1, "stream": False,
               "frequency_penalty": 0, "presence_penalty": 0, "stop": None}

insight_and_guidance_param = {"engine":"meta-llama/llama-3.3-70b-instruct", "max_tokens": 150,
               "temperature": 0.5, "top_p": 1, "stream": False,
               "frequency_penalty": 0, "presence_penalty": 0, "stop": None}
#ChatGPT
chat_summarize_ideas_param = {"engine": "nousresearch/hermes-3-llama-3.1-405b", "max_tokens": 15, 
               "temperature": 0, "top_p": 1, "stream": False,
               "frequency_penalty": 0, "presence_penalty": 0, "stop": None}
#ChatGPT
agent_chat_summarize_relationship_param = {"engine": "meta-llama/llama-3.3-70b-instruct", "max_tokens": 15, 
               "temperature": 0.2, "top_p": 1, "stream": False,
               "frequency_penalty": 0, "presence_penalty": 0, "stop": None}
#ChatGPT
agent_chat_param = {"engine": "meta-llama/llama-3.3-70b-instruct", "max_tokens": 15, 
               "temperature": 0, "top_p": 1, "stream": False,
               "frequency_penalty": 0, "presence_penalty": 0, "stop": None}
#ChatGPT
summarize_ideas_param = {"engine": "meta-llama/llama-3.3-70b-instruct", "max_tokens": 15, 
               "temperature": 0, "top_p": 1, "stream": False,
               "frequency_penalty": 0, "presence_penalty": 0, "stop": None}

generate_next_convo_line_param = {"engine": "nousresearch/hermes-3-llama-3.1-405b", "max_tokens": 250, 
               "temperature": 0.6, "top_p": 1, "stream": False,
               "frequency_penalty": 0, "presence_penalty": 0, "stop": None}

generate_whisper_inner_thought_param = {"engine": "meta-llama/llama-3.3-70b-instruct", "max_tokens": 50, 
               "temperature": 0, "top_p": 1, "stream": False,
               "frequency_penalty": 0, "presence_penalty": 0, "stop": None}
relationship_status_by_whisper_param = {"engine": "meta-llama/llama-3.3-70b-instruct", "max_tokens": 100,
               "temperature": 0, "top_p": 1, "stream": False,
               "frequency_penalty": 0, "presence_penalty": 0, "stop": None}
planning_thought_on_convo_param = {"engine": "meta-llama/llama-3.3-70b-instruct", "max_tokens": 50, 
               "temperature": 0, "top_p": 1, "stream": False,
               "frequency_penalty": 0, "presence_penalty": 0, "stop": None}

memo_on_convo_param = {"engine": "qwen/qwq-32b-preview", "max_tokens": 100,
               "temperature": 0, "top_p": 1, "stream": False,
               "frequency_penalty": 0, "presence_penalty": 0, "stop": None}
#ChatGPT
generate_safety_score_param = {"engine": "meta-llama/llama-3.3-70b-instruct", "max_tokens": 50, 
               "temperature": 0, "top_p": 1, "stream": False,
               "frequency_penalty": 0, "presence_penalty": 0, "stop": None}
#ChatGPT
generate_iterative_chat_utt_param = {"engine": "sao10k/l3.3-euryale-70b", "max_tokens": 150,
               "temperature": 0.3, "top_p": 0.1, "stream": False,
               "frequency_penalty": 0.3, "presence_penalty": 0, "stop": None}
