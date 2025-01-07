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
hourly_schedule_param = {"engine": "deepseek/deepseek-chat", "max_tokens": 1000, 
             "temperature": 0, "top_p": 1, "stream": False,
             "frequency_penalty": 0, "presence_penalty": 0, "stop":None }
task_decomp_param = {"engine": "deepseek/deepseek-chat", "max_tokens": 1000, 
             "temperature": 0, "top_p": 1, "stream": False,
             "frequency_penalty": 0, "presence_penalty": 0, "stop": ["---"]}
action_sector_param = {"engine": "qwen/qwq-32b-preview", "max_tokens": 15, 
               "temperature": 0, "top_p": 1, "stream": False,
               "frequency_penalty": 0, "presence_penalty": 0, "stop": None}

action_arena_param = {"engine": "qwen/qwq-32b-preview", "max_tokens": 15, 
               "temperature": 0, "top_p": 1, "stream": False,
               "frequency_penalty": 0, "presence_penalty": 0, "stop": None}

action_game_object_param = {"engine": "qwen/qwq-32b-preview", "max_tokens": 15, 
               "temperature": 0, "top_p": 1, "stream": False,
               "frequency_penalty": 0, "presence_penalty": 0, "stop": None}
#ChatGPT
pronunciatio_param = {"engine": "meta-llama/llama-3.3-70b-instruct", "max_tokens": 15, 
               "temperature": 0, "top_p": 1, "stream": False,
               "frequency_penalty": 0, "presence_penalty": 0, "stop": None}

event_triple_param = {"engine": "qwen/qwq-32b-preview", "max_tokens": 30, 
               "temperature": 0, "top_p": 1, "stream": False,
               "frequency_penalty": 0, "presence_penalty": 0, "stop": ["\n"]}
#ChatGPT
act_obj_desc_param = {"engine": "meta-llama/llama-3.3-70b-instruct", "max_tokens": 15, 
               "temperature": 0, "top_p": 1, "stream": False,
               "frequency_penalty": 0, "presence_penalty": 0, "stop": None}

act_obj_event_triple_param = {"engine": "qwen/qwq-32b-preview", "max_tokens": 30, 
               "temperature": 0, "top_p": 1, "stream": False,
               "frequency_penalty": 0, "presence_penalty": 0, "stop": ["\n"]}

new_decomp_schedule_param = {"engine": "deepseek/deepseek-chat", "max_tokens": 1000, 
               "temperature": 0, "top_p": 1, "stream": False,
               "frequency_penalty": 0, "presence_penalty": 0, "stop": None}

decide_to_talk_param = {"engine": "qwen/qwq-32b-preview", "max_tokens": 50,
               "temperature": 0, "top_p": 1, "stream": False,
               "frequency_penalty": 0, "presence_penalty": 0, "stop": None}

decide_to_react_param = {"engine": "qwen/qwq-32b-preview", "max_tokens": 20, 
               "temperature": 0, "top_p": 1, "stream": False,
               "frequency_penalty": 0, "presence_penalty": 0, "stop": None}

create_conversation_param = {"engine": "meta-llama/llama-3.3-70b-instruct", "max_tokens": 1000, 
               "temperature": 0.7, "top_p": 1, "stream": False,
               "frequency_penalty": 0, "presence_penalty": 0, "stop": None}
#ChatGPT
summarize_conversation_param = {"engine": "deepseek/deepseek-chat", "max_tokens": 15, 
               "temperature": 0, "top_p": 1, "stream": False,
               "frequency_penalty": 0, "presence_penalty": 0, "stop": None}

extract_keywords_param = {"engine": "meta-llama/llama-3.3-70b-instruct", "max_tokens": 50, 
               "temperature": 0, "top_p": 1, "stream": False,
               "frequency_penalty": 0, "presence_penalty": 0, "stop": None}

keyword_to_thoughts_param = {"engine": "meta-llama/llama-3.3-70b-instruct", "max_tokens": 40, 
               "temperature": 0.7, "top_p": 1, "stream": False,
               "frequency_penalty": 0, "presence_penalty": 0, "stop": None}

convo_to_thoughts_param = {"engine": "deepseek/deepseek-chat", "max_tokens": 40, 
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
chat_summarize_ideas_param = {"engine": "deepseek/deepseek-chat", "max_tokens": 15, 
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
summarize_ideas_param = {"engine": "deepseek/deepseek-chat", "max_tokens": 15, 
               "temperature": 0, "top_p": 1, "stream": False,
               "frequency_penalty": 0, "presence_penalty": 0, "stop": None}

generate_next_convo_line_param = {"engine": "deepseek/deepseek-chat", "max_tokens": 250, 
               "temperature": 1, "top_p": 1, "stream": False,
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
generate_iterative_chat_utt_param = {"engine": "microsoft/wizardlm-2-8x22b", "max_tokens": 100,
               "temperature": 0, "top_p": 1, "stream": False,
               "frequency_penalty": 0, "presence_penalty": 0, "stop": None}
